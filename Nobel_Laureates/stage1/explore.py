import pandas as pd
import os
import requests

# write your code here


if __name__ == '__main__':
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if 'Nobel_laureates.json' not in os.listdir('../Data'):
        print('Nobel_laureates.json')
        url = "https://www.dropbox.com/s/m6ld4vaq2sz3ovd/nobel_laureates.json?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/Nobel_laureates.json', 'wb').write(r.content)
        print('Loaded.')
    df = pd.read_json('../Data/Nobel_laureates.json')
    #print(df.axes)
    #print(df.info())
    print(any(df.duplicated()))
    df = df.dropna(subset=['gender'])
    df = df.reset_index(drop=True)
    print(df[0:20][['country', 'name']].to_dict())
