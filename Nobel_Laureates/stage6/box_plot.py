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
    data_chem = df.loc[df['category'] == 'Chemistry', 'age_of_winning'].to_list()
    data_econom = df.loc[df['category'] == 'Economics', 'age_of_winning'].to_list()
    data_lit = df.loc[df['category'] == 'Literature', 'age_of_winning'].to_list()
    data_peace = df.loc[df['category'] == 'Peace', 'age_of_winning'].to_list()
    data_phys = df.loc[df['category'] == 'Physics', 'age_of_winning'].to_list()
    data_med = df.loc[df['category'] == 'Physiology or Medicine', 'age_of_winning'].to_list()
    data_all = df['age_of_winning'].to_list()
    cat = ['Physiology or Medicine', 'Literature', 'Chemistry', 'Peace',
           'Physics', 'Economics', 'All categories']
    data = [data_med, data_lit, data_chem, data_peace, data_phys, data_econom, data_all]
    plt.figure(figsize=(10, 10))
    plt.boxplot(data, labels=cat, showmeans=True)
    plt.xlabel('Category', fontsize=14)
    plt.ylabel('Age of obtaining the Nobel Prize', fontsize=14)
    plt.title('The total count of male and female Nobel Prize winners in each category', fontsize=20)
    plt.show()



