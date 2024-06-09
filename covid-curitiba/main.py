import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV para um dataframe
file_path = "data/curitiba_covid.csv"

data = pd.read_csv(file_path, delimiter=";")

# Exibir as primeiras linhas do dataframe
print(data.head())

# Verificar dados faltantes e tipos de dados
missing_data = data.isnull().sum()
print(missing_data)

data_info = data.info()
print(data_info)

# Converter colunas de datas para o formato datetime
data["DATA INCLUSÃO/ NOTIFICAÇÃO"] = pd.to_datetime(
    data["DATA INCLUSÃO/ NOTIFICAÇÃO"], format="%d/%m/%Y"
)
data["DATA COLETA EXAME"] = pd.to_datetime(data["DATA COLETA EXAME"], format="%d/%m/%Y")
data["DATA ÓBITO"] = pd.to_datetime(data["DATA ÓBITO"], format="%d/%m/%Y")

# Verificar a consistência dos dados categóricos
unique_values = {
    "CLASSIFICAÇÃO FINAL": data["CLASSIFICAÇÃO FINAL"].unique(),
    "SEXO": data["SEXO"].unique(),
    "INTERNADO (SIM/NÃO)": data["INTERNADO (SIM/NÃO)"].unique(),
    "ENCERRAMENTO": data["ENCERRAMENTO"].unique(),
}
print(unique_values)

# Uniformizar os valores de "SEXO"
data["SEXO"] = data["SEXO"].str.upper()

# Uniformizar os valores de "INTERNADO (SIM/NÃO)"
data["INTERNADO (SIM/NÃO)"] = data["INTERNADO (SIM/NÃO)"].str.upper()
data["INTERNADO (SIM/NÃO)"] = data["INTERNADO (SIM/NÃO)"].replace(
    {"SIM": "SIM", "NÃO": "NÃO", "NÃO": "NÃO", "SIM": "SIM"}
)

# Verificar novamente os valores únicos após a correção
unique_values_corrected = {
    "SEXO": data["SEXO"].unique(),
    "INTERNADO (SIM/NÃO)": data["INTERNADO (SIM/NÃO)"].unique(),
}
print(unique_values_corrected)

# Distribuição de casos por sexo
sex_distribution = data["SEXO"].value_counts()
print(sex_distribution)

# Distribuição de casos por faixa etária
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = [
    "0-10",
    "11-20",
    "21-30",
    "31-40",
    "41-50",
    "51-60",
    "61-70",
    "71-80",
    "81-90",
    "91-100",
]
data["Faixa Etária"] = pd.cut(
    data["IDADE (anos)"], bins=bins, labels=labels, right=False
)
age_distribution = data["Faixa Etária"].value_counts().sort_index()
print(age_distribution)

# Distribuição de casos por bairro
neighborhood_distribution = data["BAIRRO"].value_counts().head(10)
print(neighborhood_distribution)

# Contar os casos internados e não internados
interned_distribution = data["INTERNADO (SIM/NÃO)"].value_counts()
print(interned_distribution)

# Distribuição dos casos por situação de encerramento
encerramento = data["ENCERRAMENTO"].value_counts()
print(encerramento)

# Distribuição dos casos por faixa etária e sexo
faixa_etaria_sexo = data.groupby("Faixa Etária")["SEXO"].value_counts().unstack()
print(faixa_etaria_sexo)

# Distribuição dos casos por faixa etária e situação de encerramento
faixa_etaria_situacao = (
    data.groupby("Faixa Etária")["ENCERRAMENTO"].value_counts().unstack()
)
print(faixa_etaria_situacao)

# Distribuição dos casos por ano de inclusão
data_inclusao = (
    data["DATA INCLUSÃO/ NOTIFICAÇÃO"]
    .groupby(data["DATA INCLUSÃO/ NOTIFICAÇÃO"].dt.year)
    .count()
)
print(data_inclusao)

# Adicionar coluna de ano ao dataframe
data["ANO"] = data["DATA INCLUSÃO/ NOTIFICAÇÃO"].dt.year

# Distribuição dos casos por ano e situação de encerramento
situacao_por_ano = (
    data.groupby(["ANO", "ENCERRAMENTO"])["ENCERRAMENTO"]
    .count()
    .unstack()
    .reset_index()
)
print(situacao_por_ano)
