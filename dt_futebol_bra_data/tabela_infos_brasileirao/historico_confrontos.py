import pandas as pd
from dt_futebol_bra_data.read_futebol_data.read_db import futebol_data_wo


def df_historico_times(end_year: str, start_year: str = '2012'):
    df = futebol_data_wo()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[(df['Season'] >= start_year) & (df['Season'] <= end_year)]
    df['HG'] = pd.to_numeric(df['HG'])
    df['AG'] = pd.to_numeric(df['AG'])
    return df

# if __name__ == '__main__':
#     print(df_historico_times(end_year='2024'))


def historico_confrontros(team_1: str, team_2: str, end_year: str, start_year: str = '2012'):
    df = df_historico_times(end_year, start_year)
    df[['Home', 'Away']] = df[['Home', 'Away']].replace({'Flamengo RJ': 'Flamengo', 'Botafogo RJ': 'Botafogo'})
    jogos_vitorias = df[((df['Home'] == team_1) & (df['Res'] == 'H') & (df['Away'] == team_2)) | ((df['Away'] == team_1)
                        & (df['Res'] == 'A') & (df['Home'] == team_2))].shape[0]
    jogos_derrota = df[((df['Home'] == team_2) & (df['Res'] == 'H') & (df['Away'] == team_1)) | ((df['Away'] == team_2)
                        & (df['Res'] == 'A') & (df['Home'] == team_1))].shape[0]
    jogos_empate = df[((df['Home'] == team_1) & (df['Res'] == 'D') & (df['Away'] == team_2)) | ((df['Away'] == team_1)
                        & (df['Res'] == 'D') & (df['Home'] == team_2))].shape[0]
    total_confrontos = jogos_vitorias + jogos_derrota + jogos_empate
    data_confronto = {'Vitorias': [jogos_vitorias], 'Derrotas': [jogos_derrota], 'Empates': [jogos_empate], 'Total_jogos': [total_confrontos]}
    df_confronto = pd.DataFrame(data=data_confronto, index=[f'{team_1} x {team_2}'])
    return df_confronto
if __name__ == '__main__':
    print(historico_confrontros('Flamengo', 'Vasco', '2024', '2012'))
