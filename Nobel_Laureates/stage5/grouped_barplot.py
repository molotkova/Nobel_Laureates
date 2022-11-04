import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# write your code here

def f(x):
    if x:
        if len(x.split(',')) < 2:
            return None
        else:
            return x.split(',')[-1].strip()
    else:
        return None


if __name__ == '__main__':

    df = pd.read_json('../Data/Nobel_laureates.json')
    df = df.dropna(subset=['gender'])
    df = df.reset_index(drop=True)
    df['place_of_birth'] = df['place_of_birth'].apply(f)
    df.loc[df['born_in'] == '', 'born_in'] = None
    df['born_in'] = df['born_in'].fillna(df['place_of_birth'])
    df = df.dropna(subset=['born_in'])
    df = df.reset_index(drop=True)
    df.loc[df['born_in'] == 'U.S.', 'born_in'] = 'USA'
    df.loc[df['born_in'] == 'United States', 'born_in'] = 'USA'
    df.loc[df['born_in'] == 'US', 'born_in'] = 'USA'
    df.loc[df['born_in'] == 'United Kingdom', 'born_in'] = 'UK'
    df['year_born'] = [x.split(' ')[-1] if len(x.split(' ')) > 1 else x.split('-')[0] for x in
                       df['date_of_birth'].values]
    df['year_born'] = df['year_born'].astype(int)
    df['age_of_winning'] = df['year'] - df['year_born']
    df.loc[df['category'] == '', 'category'] = None
    male_cat = df.loc[df['gender'] == 'male', 'category'].value_counts().sort_index()
    female_cat = df.loc[df['gender'] == 'female', 'category'].value_counts().sort_index()
    x_axis = np.arange(len(df['category'].unique()) - 1)
    y_axis = np.arange(0, 225, 25)
    plt.figure(figsize=(10, 10))
    plt.bar(x_axis - 0.2, male_cat.values, width=0.4, label='Males')
    plt.bar(x_axis + 0.2, female_cat.values, width=0.4, label='Females')
    plt.xticks(x_axis, male_cat.index)
    plt.yticks(y_axis)
    plt.xlabel('Category', fontsize=14)
    plt.ylabel('Nobel Laureates Count', fontsize=14)
    plt.title('The total count of male and female Nobel Prize winners in each category', fontsize=20)
    plt.legend(['Males', 'Females'])
    plt.show()



