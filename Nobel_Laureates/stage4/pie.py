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


def my_fmt(x):
    return '{:.2f}%\n({:.0f})'.format(x, total * x / 100)


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
    birthplace_dict = df['born_in'].value_counts().to_dict()
    df['born_in_corrected'] = [key if birthplace_dict[key] >= 25 else 'Other countries' for key in df['born_in'].values]
    data_to_pie = df['born_in_corrected'].value_counts()
    colors = ['blue', 'orange', 'red', 'yellow', 'green', 'pink', 'brown',
              'cyan', 'purple']
    explode = [0.0, 0.0, 0.0, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]
    plt.figure(figsize=(12, 12))
    total = sum(data_to_pie)
    plt.pie(data_to_pie,
            labels=data_to_pie.index,
            colors=colors,
            explode=explode,
            autopct=my_fmt)
    plt.show()
