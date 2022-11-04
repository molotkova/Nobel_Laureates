import pandas as pd


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
    print(df['born_in'].to_list())
