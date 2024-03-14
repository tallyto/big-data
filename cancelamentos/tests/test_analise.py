import pandas as pd
import plotly.express as px

# Lê o arquivo CSV e ignora linhas com erros
tabela = pd.read_csv("../data/cancelamentos.csv", on_bad_lines="skip")

tabela = tabela.drop("CustomerID", axis=1)

# Exibe informações sobre o DataFrame
print(tabela.info())

# Remove linhas com valores nulos
tabela = tabela.dropna()


def calcularCancelamentos(tabela: pd.DataFrame):
    # Calcula a quantidade de pessoas que cancelaram e não cancelaram
    cancelou_counts = tabela["cancelou"].value_counts()

    # Calcula a porcentagem de pessoas que cancelaram e não cancelaram
    cancelou_percent = tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format)

    # Cria um DataFrame com as informações
    resultado = pd.DataFrame({"Cancelou": cancelou_counts, "Porcentagem": cancelou_percent})

    return resultado

print(calcularCancelamentos(tabela))

def calcularDuracaoContrato(tabela: pd.DataFrame):
    # Calcula a quantidade de pessoas que cancelaram e não cancelaram
    duracao_contrato_counts = tabela["duracao_contrato"].value_counts()

    # Calcula a porcentagem de pessoas que cancelaram e não cancelaram
    duracao_contrato_percent = tabela["duracao_contrato"].value_counts(normalize=True).map("{:.2%}".format)

    # Cria um DataFrame com as informações
    resultado = pd.DataFrame({"Duração do Contrato": duracao_contrato_counts, "Porcentagem": duracao_contrato_percent})

    return resultado

print(calcularDuracaoContrato(tabela))

# Analizando o contrato mensal

print(tabela.groupby("duracao_contrato").mean(numeric_only=True))


def calcularCancelamentoPorPeriodo(tabela: pd.DataFrame, periodo: str):
    # Filtra as linhas com o periodo especificado
    tabela_periodo = tabela[tabela["duracao_contrato"] == periodo]

    # Calcula a quantidade de pessoas que cancelaram e não cancelaram
    cancelou_counts = tabela_periodo["cancelou"].value_counts()

    # Calcula a porcentagem de pessoas que cancelaram e não cancelaram
    cancelou_percent = tabela_periodo["cancelou"].value_counts(normalize=True).map("{:.2%}".format)

    # Cria um DataFrame com as informações
    resultado = pd.DataFrame({"Cancelou": cancelou_counts, "Porcentagem": cancelou_percent})

    return resultado


print(calcularCancelamentoPorPeriodo(tabela, "Monthly"))
print(calcularCancelamentoPorPeriodo(tabela, "Quarterly"))
print(calcularCancelamentoPorPeriodo(tabela, "Annual"))


print(tabela["assinatura"].value_counts(normalize=True))
print(tabela.groupby("assinatura").mean(numeric_only=True))


#Clientes que cancelaram com menos de 4 ligações

condicao = tabela["ligacoes_callcenter"] <= 4

tabela = tabela[condicao]

print(tabela["cancelou"].value_counts())

print(tabela["cancelou"].value_counts(normalize=True))

# com menos de 20 dias de atraso

condicao = tabela["dias_atraso"] <= 20

tabela = tabela[condicao]

print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True))

# Visualização

grafico_idade = px.histogram(tabela, x="idade", color="cancelou", 
                             title="Histograma da Idade dos Clientes",
                             labels={"idade": "Idade", "cancelou": "Cancelou"})
grafico_idade.update_layout(
    font=dict(size=14),
    xaxis_title="Idade",
    yaxis_title="Número de Clientes",
)

grafico_idade.show()
