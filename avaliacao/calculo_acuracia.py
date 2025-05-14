import pandas as pd
from sklearn.metrics import accuracy_score

# Carregar os dados das respostas
questoes_df = pd.read_csv('../dados/questoes.csv')
respostas_modelos_df = pd.read_csv('../dados/respostas_modelos.csv')

# Exemplo de como comparar respostas objetivas
# Suponhamos que as questões tenham uma coluna 'resposta_correta' e o modelo tenha 'resposta_modelo'
def calcular_acuracia_respostas_objetivas():
    # Comparar respostas do modelo com as corretas
    acuracia = accuracy_score(questoes_df['resposta_correta'], respostas_modelos_df['resposta_modelo'])
    print(f"Acurácia das respostas objetivas: {acuracia * 100:.2f}%")
    return acuracia

# Exemplo de como calcular a acurácia para respostas dissertativas
def comparar_respostas_dissertativas(resposta_modelo, resposta_correta):
    # Usaremos uma comparação simples de similaridade de texto (ou outro critério)
    # Aqui você pode implementar algoritmos mais complexos para comparar a qualidade das respostas dissertativas
    return resposta_modelo.lower() == resposta_correta.lower()

def calcular_acuracia_dissertativas():
    acertos = 0
    for index, row in questoes_df.iterrows():
        if comparar_respostas_dissertativas(respostas_modelos_df.iloc[index]['resposta_modelo'], row['resposta_correta']):
            acertos += 1
    acuracia_dissertativa = acertos / len(questoes_df)
    print(f"Acurácia das respostas dissertativas: {acuracia_dissertativa * 100:.2f}%")
    return acuracia_dissertativa

# Calcular acurácia para respostas objetivas
acuracia_objetiva = calcular_acuracia_respostas_objetivas()

# Calcular acurácia para respostas dissertativas
acuracia_dissertativa = calcular_acuracia_dissertativas()
