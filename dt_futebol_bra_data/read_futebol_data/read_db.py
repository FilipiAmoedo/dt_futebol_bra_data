import sqlite3
import pandas as pd
from os import path

DB_FUTEBOL_DATA = path.join(path.expanduser('~'), 'Documents', 'databases')


def read_futebol_data_db():
    db_path = path.join(DB_FUTEBOL_DATA, 'scc_futebol_data', 'futebol_bra.db')
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query('SELECT * FROM futebol_data', conn)
    conn.close()
    return df


# if __name__ == '__main__':
#     print(read_futebol_data_db())


def futebol_data_wo():
    df = read_futebol_data_db()
    df['WO'] = (df['Home'] == 'Chapecoense-SC') & (df['Away'] == 'Atletico-MG')
    df.loc[df['WO'], ['HG', 'AG', 'Res']] = ['0', '0', 'D']
    return df

if __name__ == '__main__':
    print(futebol_data_wo().to_string())