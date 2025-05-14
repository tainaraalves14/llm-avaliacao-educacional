import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('avaliacao_llm.db')

# Consultar todas as questões e respostas
questoes_df = pd.read_sql_query("SELECT * FROM questoes", conn)
respostas_modelos_df = pd.read_sql_query("SELECT * FROM respostas_modelos", conn)

# Exibir os dados
print("Questões:")
print(questoes_df)
print("\nRespostas dos Modelos:")
print(respostas_modelos_df)

# Fechar a conexão
conn.close()
