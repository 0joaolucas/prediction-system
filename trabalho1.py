# -*- coding: utf-8 -*-
"""Trabalho1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A1uI92Px3gWiU1VAAoM1BUVJQWtMgtHz

#Regressão Linear Multipla no Python

https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9
"""

import pandas as pd 
import numpy as np 
import seaborn as sns

############## Importando o banco de dados HousingData.csv

#dataset = pd.read_csv('Dados_compra.csv')
url='https://github.com/gustavowillam/ML/blob/main/trabalhos/Trab1/StudentsPerformance_train.csv?raw=true'
df = pd.read_csv(url, sep=";")

url='https://github.com/gustavowillam/ML/blob/main/trabalhos/Trab1/StudentsPerformance_test.csv?raw=true'
df2 = pd.read_csv(url, sep=";")

print(df.head(10)) #obtendo os primeiros registros do dataframe

print(df2.head(10))

df.info()  #obtendo informações do dataframe

df["gender"] = df["gender"].astype('category')
df['gender'] = df['gender'].cat.codes

df["lunch"] = df["lunch"].astype('category')
df['lunch'] = df['lunch'].cat.codes

df["test preparation course"] = df["test preparation course"].astype('category')
df['test preparation course'] = df['test preparation course'].cat.codes

df2["gender"] = df2["gender"].astype('category')
df2['gender'] = df2['gender'].cat.codes

df2["lunch"] = df2["lunch"].astype('category')
df2['lunch'] = df2['lunch'].cat.codes

df2["test preparation course"] = df2["test preparation course"].astype('category')
df2['test preparation course'] = df2['test preparation course'].cat.codes

df = pd.get_dummies(df, columns=['gender'])
df = pd.get_dummies(df, columns=['lunch'])
df = pd.get_dummies(df, columns=['test preparation course'])
df = pd.get_dummies(df, columns=['reading score'])
df = pd.get_dummies(df, columns=['writing score'])
df = pd.get_dummies(df, columns=['race/ethnicity_group A'])
df = pd.get_dummies(df, columns=['race/ethnicity_group B'])
df = pd.get_dummies(df, columns=['race/ethnicity_group C'])
df = pd.get_dummies(df, columns=['race/ethnicity_group D'])
df = pd.get_dummies(df, columns=['race/ethnicity_group E'])
df = pd.get_dummies(df, columns=["parental level of education_associate's degree"])
df = pd.get_dummies(df, columns=["parental level of education_bachelor's degree"])
df = pd.get_dummies(df, columns=["parental level of education_high school"])
df = pd.get_dummies(df, columns=["parental level of education_master's degree"])
df = pd.get_dummies(df, columns=["parental level of education_some college"])
df = pd.get_dummies(df, columns=["parental level of education_some high school"])






df.info()

df2.isnull().sum()

df.shape  #Número de linhas e colunas

df.corr()

sns.lmplot(x="reading score", y="math score", data=df);

#### Matriz de correlação dos dados

import seaborn as sns
corr = df.corr()  
sns.heatmap(corr)

"""#Utilizando todas as colunas do dataframe para ser X"""

cols = df.columns
print(cols)

cols2 = df2.columns
print(cols2)

"""#Criar as variáveis X e y e separar o conjunto de Trein e Teste  """

############## Cria as variáveis independentes e dependente

### Separar dados de treinamento e dados de teste.
X_train = df[cols] #slice no dataframe e retorna dataframe
X_train  = X_train.drop(['math score'], axis=1) #remove a variável dependente do X
y_train = df[['math score']]

print(X_train)

print(y_train)

X_test = df2[cols] #slice no dataframe e retorna dataframe
X_test  = X_test.drop(['math score'], axis=1) #remove a variável dependente do X
y_test = df2[['math score']]

print(X_test) #Imprime o conjunto de teste da variáveis independentes

print(y_test) #Imprime o conjunto de teste da variável dependente

"""#Regressão Linear LinearRegression"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression() #esse método já considera a constante

## ajustando o modelo de regressão
regressor.fit(X_train, y_train)

#fazer a predição
y_pred = regressor.predict(X_train)

### Criando Dataframe com os valores observados e preditos, para avaliar a qualidade das previsões do modelo

resultado = pd.DataFrame()
resultado["math_OBS"] = y_train.reset_index(drop = True)
resultado["math_PRED"] = y_pred

print(resultado)

### gráfico de dispersão dos valores observados ("math_OBS") versus os valores preditos ("math_PRED") pelo modelo de regressão.

import matplotlib.pyplot as plt

plt.scatter(resultado["math_OBS"], resultado["math_PRED"]) ## valores observados no eixo x e os preditos no eixo y

plt.xlabel("Valor real")

plt.ylabel("Valor predito")

plt.show()

## os pontos juntos em uma diagonal indica boa relação entre os valores observados e preditos

from sklearn.metrics import mean_absolute_error  #EAM
from sklearn.metrics import mean_squared_error   #RMSE
from sklearn.metrics import r2_score             #R2

## Calculando erro médio absoluto

EAM = mean_absolute_error(resultado["math_OBS"], resultado["math_PRED"])
print(EAM)

## desempenho bom do modelo na previsão dos valores da variável dependente.

## Calculando a raiz quadrada da média dos erros quadráticos

RMSE = np.sqrt(mean_squared_error(resultado["math_OBS"], resultado["math_PRED"]))
print(RMSE)

##por ser relativamente baixo também indica desempenho bom do modelo na previsão dos valores da variável dependente.

### Calculando coeficiente de determinação

R2 = r2_score(resultado["math_OBS"], resultado["math_PRED"])
print(R2)

### valor mais próximo de 1 indica um modelo de regressão mais preciso.

import joblib

filename = 'modelo.pkl'
joblib.dump(regressor, filename)