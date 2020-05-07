from sklearn.preprocessing import OrdinalEncoder
import datetime as dt

class preprocess():

    def provinceNan(df):
        # vymazem null hodnoty z provincii
        df.Province_State.fillna('NaN', inplace=True)
        oe = OrdinalEncoder()
        df[['Province_State', 'Country_Region', 'Continent']] = oe.fit_transform(
            df.loc[:, ['Province_State', 'Country_Region', 'Continent']])
        return df

    # z datumov ziskam dalsie informacie pre lepsie vizualne spracovanie
    def date_formatting(df):
        df['day'] = df['Date'].dt.day
        df['month'] = df['Date'].dt.month
        df['dayofweek'] = df['Date'].dt.dayofweek
        df['dayofyear'] = df['Date'].dt.dayofyear
        df['quarter'] = df['Date'].dt.quarter
        df['weekofyear'] = df['Date'].dt.weekofyear
        return df

    # rozdelim trenovaciu mnozinu
    def train_split(df, days):
        date = df['Date'].max() - dt.timedelta(days=days)
        return df[df['Date'] <= date], df[df['Date'] > date]

    # Aby sa zabranilo preteceniu udajov, prekrujem datumy v trenovacej a v testovacej mnozine
    # Preto odstranim udaje, ktore uz existuju v testovacej mnozine
    def avoid_data_leakage(df, date_min):
        # date_min je minimalny datum z testovacej mnoziny
        return df[df['Date'] < date_min]