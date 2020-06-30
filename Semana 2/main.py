#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[27]:


black_friday = pd.DataFrame(black_friday)


# In[28]:


black_friday.info()


# In[29]:


black_friday.head()


# In[30]:


black_friday.shape


# In[41]:


black_friday['User_ID'].nunique()


# In[42]:


black_friday.isnull().sum()/len(black_friday)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[43]:


def q1():
    return (black_friday.shape[0], black_friday.shape[1])
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    return len(black_friday[(black_friday['Age'] == '26-35') & (black_friday['Gender'] == 'F')])
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    return black_friday['User_ID'].nunique()
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[32]:


def q4():
    return black_friday.dtypes.nunique()
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[33]:


def q5():
    return sum(black_friday.isnull().sum(axis=1)!= 0)/black_friday.shape[0]
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[40]:


def q6():
    return int(black_friday['Product_Category_3'].isnull().sum())
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[36]:


def q7():
    return float(black_friday['Product_Category_3'].mode())
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[37]:


def q8():
    purchase = black_friday['Purchase']
    normalized_purchase = (purchase-purchase.min())/(purchase.max()-purchase.min())
    return float(normalized_purchase.mean())
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[38]:


def q9():
    purchase = black_friday['Purchase']

    normalized = (purchase - purchase.mean()) / purchase.std()
    return int(normalized.apply(lambda x: 1 if x >= -1 and x <= 1 else 0).sum())

    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[39]:


def q10():
    return black_friday.dropna().shape[0] == black_friday.dropna(subset = ['Product_Category_3']).shape[0]
    pass


# In[ ]:




