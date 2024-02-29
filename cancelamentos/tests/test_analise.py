import pandas as pd

# Lê o arquivo CSV e ignora linhas com erros
tabela = pd.read_csv("cancelamentos.csv", on_bad_lines='skip')

# Remove a coluna "CustomerId" (verifique se o nome da coluna está correto)
tabela = tabela.drop("CustomerID", axis=1)

# Exibe apenas a primeira linha
print(tabela.head(1))
