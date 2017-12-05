import pandas as pd


def load_data():
    path = 'files/olympics.csv'
    df = pd.read_csv(path,skiprows=1)
    df.columns = ['Country','# Summer','Gold','Silver','Bronze','Total','# Winter','Gold','Silver','Bronze','Total','# Games','Gold','Silver','Bronze','Combined total']
    new_col = df.Country.str.split('(').str.get(1).str.translate(None, ",!.; -@!%^&*)(").str.split('[').str.get(0)
    df.insert(loc=0, column='Code', value=new_col)
    df.index = df.Country.str.split('(').str.get(0)
    del df['Country']
    del df['Total']
    return df


def first_country(df):
    return df.iloc[0]


def gold_medal(df):
    return df['Gold'].iloc[:-1,0].idxmax()


def biggest_difference_in_gold_medal(df):
    diff = df['Gold'].iloc[:-1,0] - df['Gold'].iloc[:-1,1]
    return diff.idxmax()

def get_points(df):
    gold_points =  df['Gold'].iloc[:-1,2]*3
    silver_points =  df['Silver'].iloc[:-1,2]*2
    bronze_points =  df['Bronze'].iloc[:-1,2]*1
    total_points = gold_points + silver_points +bronze_points
    df['Points'] = total_points
    return total_points


df = load_data()
print(first_country(df)["# Summer"])
print(gold_medal(df))
print(biggest_difference_in_gold_medal(df))
print(get_points(df))
