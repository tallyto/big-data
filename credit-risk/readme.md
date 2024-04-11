# Análise de Risco de Crédito

Este projeto consiste em uma análise exploratória de um conjunto de dados relacionado ao risco de crédito. O objetivo é entender as características dos clientes e seu impacto no status de pagamento de empréstimos.

## Conjunto de Dados

O conjunto de dados foi obtido do Kaggle e contém informações sobre clientes, incluindo idade, renda, valor do empréstimo e status de pagamento. O arquivo CSV utilizado pode ser encontrado [aqui](https://www.kaggle.com/datasets/laotse/credit-risk-dataset).

## Passos do Projeto

O projeto segue os seguintes passos:

1. **Carregamento e Exploração Inicial dos Dados**: Os dados são carregados em um DataFrame pandas e os primeiros registros são visualizados para entender sua estrutura.

2. **Limpeza de Dados**: São identificados e removidos registros com dados inconsistentes, como idades negativas ou superiores a 100 anos.

3. **Análise Estatística Descritiva**: São calculadas estatísticas descritivas básicas para as variáveis numéricas do conjunto de dados, como idade, renda e valor do empréstimo.

4. **Visualização das Variáveis**: São criados histogramas para visualizar a distribuição das variáveis de interesse e uma matriz de dispersão para investigar os relacionamentos entre as variáveis.

5. **Verificação de Valores Ausentes**: É verificada a presença de valores ausentes no conjunto de dados e medidas são tomadas para lidar com eles, se necessário.

6. **Preparação dos Dados para Modelagem**: As variáveis preditoras são selecionadas e padronizadas para garantir que estejam na mesma escala para modelagem de machine learning.

## Bibliotecas Utilizadas

- pandas
- numpy
- seaborn
- matplotlib
- plotly.express

## Como Executar o Código

1. Clone o repositório em sua máquina local.
2. Certifique-se de ter as bibliotecas mencionadas instaladas em seu ambiente Python.
3. Execute o arquivo Python `analise_risco_credito.py` para reproduzir a análise.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com sugestões de melhorias.

