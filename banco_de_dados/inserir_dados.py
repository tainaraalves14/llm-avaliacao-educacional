import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('avaliacao_llm.db')
cursor = conn.cursor()

# Carregar os dados dos CSVs
questoes_df = pd.read_csv('../dados/questoes.csv')
respostas_modelos_df = pd.read_csv('../dados/respostas_modelos.csv')

# Inserir questões no banco de dados
for index, row in questoes_df.iterrows():
    cursor.execute("INSERT INTO questoes (enunciado, resposta_correta) VALUES (?, ?)",
                   (row['enunciado'], row['resposta_correta']))

# Inserir respostas dos modelos no banco de dados
for index, row in respostas_modelos_df.iterrows():
    cursor.execute("INSERT INTO respostas_modelos (id_questao, resposta_modelo) VALUES (?, ?)",
                   (row['id_questao'], row['resposta_modelo']))

# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso no banco de dados!")
