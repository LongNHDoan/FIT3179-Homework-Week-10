"""
Extracting co2-emission data for industries
"""
import pandas as pd


def main():
    # Extract data
    df = pd.read_csv('owid-co2-data.csv')
    df = df[
        ['coal_co2', 'cement_co2', 'flaring_co2', 'gas_co2', 'oil_co2', 'other_industry_co2', 'year']].fillna(0)
    df['other_industry_co2'] += df['flaring_co2'] + df['cement_co2']
    df.drop(['cement_co2', 'flaring_co2'], axis=1, inplace=True)
    df.rename(columns={'coal_co2': 'Coal', 'gas_co2': 'Gas', 'oil_co2': 'Oil',
                       'other_industry_co2': 'Other Industries'}, inplace=True)
    # Convert to long format
    df = df.melt(id_vars=['year'], var_name='Type', value_name='Co2 Emission')
    fun = {'Co2 Emission': 'sum'}
    df = df.groupby(['year', 'Type']).agg(fun)
    df.to_csv('IndustryCo2.csv')
    return None


if __name__ == "__main__":
    main()
