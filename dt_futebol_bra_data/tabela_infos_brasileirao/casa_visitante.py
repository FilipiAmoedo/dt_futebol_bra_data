import pandas as pd
from dt_futebol_bra_data.read_futebol_data.read_db import read_futebol_data_db



def read_bd_year(start_year:str):
    df = read_futebol_data_db()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[(df['Date'].dt.year == int(start_year))]
    df['HG'] = pd.to_numeric(df['HG'])
    df['AG'] = pd.to_numeric(df['AG'])
    return df

# if __name__ == '__main__':
#     print(read_bd_year(2023, 2024).to_string())


def victory_home_and_out(df):
    df_times = pd.DataFrame({'Time': df['Home'].unique()})
    df_times['Vitoria_Casa'] = df_times['Time'].apply(lambda time: ((df['Home'] == time) & (df['Res'] == 'H')).sum()).astype(int)
    df_times['Vitoria_fora'] = df_times['Time'].apply(lambda time: ((df['Away'] == time) & (df['Res'] == 'A')).sum()).astype(int)
    df_times.sort_values(by=['Vitoria_Casa', 'Vitoria_fora'], ascending=False, inplace=True)
    df_times['Time'] = df_times['Time'].replace({'Flamengo RJ': 'Flamengo', 'Botafogo RJ': 'Botafogo'})
    return df_times.set_index('Time')





if __name__ == '__main__':
    df = read_bd_year('2024')
    print(victory_home_and_out(df).to_string())