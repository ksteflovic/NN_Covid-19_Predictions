from sklearn.preprocessing import OrdinalEncoder

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

