from sklearn.preprocessing import OrdinalEncoder

class preprocess():

    def categoricalToInteger(df):
        # vymazem null hodnoty z provincii
        df.Province_State.fillna('NaN', inplace=True)
        oe = OrdinalEncoder()
        df[['Province_State', 'Country_Region', 'Continent']] = oe.fit_transform(
            df.loc[:, ['Province_State', 'Country_Region', 'Continent']])
        return df


