import pandas as pd

# Carregar dados
df = pd.read_csv("funcionarios.csv")

# Exibir as 5 primeiras linhas
print(df.head())

# Média salarial por setor
media_setor = df.groupby("setor")["salario"].mean().sort_values(ascending=False)
print("Média salarial por setor:\n", media_setor)
