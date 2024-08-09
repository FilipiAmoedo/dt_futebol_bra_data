import pandas as pd
from dt_futebol_bra_data.tabela_infos_brasileirao.classificacao import ano_liga


def media_gols(year: str):
    df = ano_liga(year)
    df_times = pd.DataFrame({f'Times{year}': df['Home'].unique()})
    df_times['gols_casa'] = df_times[f'Times{year}'].apply(lambda time: (df[df['Home'] == time]['HG'].sum()))
    df_times['gols_fora'] = df_times[f'Times{year}'].apply(lambda time: (df[df['Away'] == time]['AG'].sum()))
    df_times[f'Times{year}'] = df_times[f'Times{year}'].replace({'Flamengo RJ': 'Flamengo', 'Botafogo RJ': 'Botafogo'})
    df_times.sort_values(by=['gols_casa', 'gols_fora'], ascending=False, inplace=True)
    df_times.set_index(f'Times{year}', inplace=True)
    df_times.index.name = None
    return df_times.astype(int)


if __name__ == '__main__':
    print(media_gols('2016'))