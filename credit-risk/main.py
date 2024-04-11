# Dataset
# https://www.kaggle.com/datasets/laotse/credit-risk-dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('data/credit_risk_dataset.csv')

# Visualiza os 5 primeiros registros
base_credit.head()

# Visualiza os últimos registros
base_credit.tail()



# Exibe informações da tabela como número de linhas, número de colunas, tipo de dados e etc.
base_credit.info()

# Pessoas com idade negativa
base_credit.loc[base_credit['person_age'] < 0]

# Pessoas com mais de 100
base_credit.loc[base_credit['person_age'] > 100]


# Apagar somente os registros com valores inconsistentes

base_credit = base_credit.drop(base_credit[base_credit['person_age'] > 100].index)


# Visualiza algumas estatísticas
base_credit.describe()

# Visualizar a pessoa que recebeu mais

base_credit[base_credit['person_income'] <= 2.039784e+06]

# Visualizar a pessoa que tem a menor divida

base_credit[base_credit['loan_amnt'] <= 500.000000	]

# contagem de registros em cada uma das classes

np.unique(base_credit['loan_status'], return_counts=True)

# Empréstimos 
sns.countplot(x= base_credit['loan_status']);

# 0 é não inadimplente e 1 é inadimplente

# 25468 pagos e 7108 não pagos

plt.hist(x= base_credit['person_age'], bins=30);
plt.title('Age Distribution');
plt.xlabel('Age');

# Renda

plt.hist(x = base_credit['person_income'], bins=30);
plt.title('Distribuição de Renda')

# divida
plt.hist(x = base_credit['loan_amnt'], bins = 20);
plt.title('Divida');


grafico = px.scatter_matrix(base_credit, dimensions=['person_age', 'person_income', 'loan_amnt'], color='loan_status')
grafico.show()

#Verifica valores faltantes
base_credit.isnull().sum()

# Previsores

credit = base_credit[['person_age', 'person_income', 'loan_amnt', 'loan_status']]
x_credit = credit.iloc[:, 0:3].values

x_credit

# verificar tipo
type(x_credit)

y_credit = credit.iloc[:, 3].values

y_credit

# verificar tipo
type(y_credit)


# pessoa mais nova e pessoa mais velha
 
x_credit[:,0].min() , x_credit[:,0].max()

# R = (20, 94)


# menor e maior renda
x_credit[:,1].min(), x_credit[:,1].max()

# R = (4000, 2039784)


# menor divida e maior divida
x_credit[:,2].min() , x_credit[:,2].max()

# R = (500, 35000


# Existe uma grande diferença na escala desses valores tanto se compararmos a idade com a divida quando se compararmos a idade com a renda assim nos temos uma diferença grande na renda para a divida e isso pode ser um problema para os algorítimos de machine learning principalmente algorítimos baseados em distancia como por exemplo o algoritmo knn e redes neurais artificiais por tanto precisamos aplicar uma formula para a padronização desses valores para que eles acabem ficando na mesma escala outro problema que pode acontecer com alguns algoritmos e que como os valores da renda são muito maiores do que os valores da idade o algorítimo pode considerar que a renda é muito mais importante que a idade ou que a divida é mais importante que a idade pois esses valores são muito maiores 


# Padronização (Standardization)

"""
x = (x - x.mean()) / x.std()

x é igual a x menos a média de x e dividido pela desvio padrão de x.

"""


# Normalização (Normalization)

"""
x = (x - min(x)) / (max(x) - min(x))

x é igual a x menos o menor valor de x e dividido pelo maior valor menos o menor valor de x.
"""

# Valores mínimos 
x_credit[:,0].min() , x_credit[:,1].min() , x_credit[:,2].min() 

# Valores sem escala

# R = (20, 4000, 500)

# Valores maximos 
x_credit[:,0].max() , x_credit[:,1].max() , x_credit[:,2].max() 

# Valores sem escala

# R = (94, 2039784, 35000)

from sklearn.preprocessing import StandardScaler

scaler_credit = StandardScaler()

x_credit = scaler_credit.fit_transform(x_credit)

# Valores mínimos 
x_credit[:,0].min() , x_credit[:,1].min() , x_credit[:,2].min() 

# Valores na mesma escala

# R = (-1.2438638905517996, -1.1779405316576799, -1.4377443770407878)


# Valores maximos 
x_credit[:,0].max() , x_credit[:,1].max() , x_credit[:,2].max() 

# Valores na mesma escala

# R = (10.682205511601307, 37.573667575291424, 4.019570880913998)

# Valores escalonados

x_credit