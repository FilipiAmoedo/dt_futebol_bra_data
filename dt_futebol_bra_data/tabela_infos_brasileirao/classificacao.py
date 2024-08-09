import pandas as pd
from dt_futebol_bra_data.read_futebol_data.read_db import futebol_data_wo


def ano_liga(year: str):
    df = futebol_data_wo()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Date'].dt.year == int(year)]
    df['HG'] = pd.to_numeric(df['HG'])
    df['AG'] = pd.to_numeric(df['AG'])
    return df

# if __name__ == '__main__':
#     print(df_year('2023').to_string())


def tabela_liga(df):
    classificacao = pd.DataFrame({'Time': df['Home'].unique()})
    classificacao['Jogos'] = classificacao['Time'].apply(lambda time: ((df['Home'] == time) | (df['Away'] == time)).sum())
    classificacao['Vitorias'] = classificacao['Time'].apply(
        lambda time: (((df['Home'] == time) & (df['Res'] == 'H')) | ((df['Away'] == time) & (df['Res'] == 'A'))).sum())
    classificacao['Derrotas'] = classificacao['Time'].apply(
        lambda time: (((df['Home'] == time) & (df['Res'] == 'A')) | ((df['Away'] == time) & (df['Res'] == 'H'))).sum())
    classificacao['Empate'] = classificacao['Time'].apply(lambda time: (((df['Home'] == time) | (df['Away'] == time)) & (df['Res'] == 'D')).sum())
    classificacao['Gols Marcados'] = classificacao['Time'].apply(lambda time: (df[df['Home'] == time]['HG'].sum() + df[df['Away'] == time]['AG'].sum())).astype(int)
    classificacao['Gols Sofridos'] = classificacao['Time'].apply(
        lambda time: (df[df['Home'] == time]['AG'].sum() + df[df['Away'] == time]['HG'].sum())).astype(int)
    classificacao['Saldo de Gols'] = classificacao['Gols Marcados'] - classificacao['Gols Sofridos'].astype(int)
    classificacao['Pontos'] = classificacao['Vitorias'] * 3 + classificacao['Empate']
    times_wo = df.loc[df['WO'], ['Home', 'Away']]
    for _, row in times_wo.iterrows():
        classificacao.loc[classificacao['Time'] == row['Home'], ['Pontos', 'Empate']] -= 1
        classificacao.loc[classificacao['Time'] == row['Away'], ['Pontos', 'Empate']] -= 1
        classificacao.loc[classificacao['Time'] == row['Home'], 'Derrotas'] += 1
        classificacao.loc[classificacao['Time'] == row['Away'], 'Derrotas'] += 1
    classificacao = classificacao.sort_values(by=['Pontos', 'Vitorias', 'Saldo de Gols'], ascending=False).reset_index(
        drop=True)
    classificacao['Time'] = classificacao['Time'].replace({'Flamengo RJ': 'Flamengo', 'Botafogo RJ': 'Botafogo'})
    colunas_ordem = ['Time', 'Pontos', 'Jogos', 'Vitorias', 'Empate', 'Derrotas', 'Gols Marcados', 'Gols Sofridos', 'Saldo de Gols']
    classificacao = classificacao[colunas_ordem].set_index('Time')
    classificacao.index.name = None
    return classificacao

if __name__ == '__main__':
    year = '2016'
    df = ano_liga(year)
    print(tabela_liga(df).to_string())