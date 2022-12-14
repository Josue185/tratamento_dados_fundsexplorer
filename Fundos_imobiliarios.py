#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)


# In[2]:


driver.get("https://www.fundsexplorer.com.br/ranking")

#tabela = driver.find_element(By.ID, 'table-ranking').text
#print(tabela)

fundo1 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[1]').text
fundo2 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[2]').text
fundo3 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[3]').text
fundo4 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[4]').text
fundo5 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[5]').text
fundo6 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[6]').text
fundo7 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[7]').text
fundo8 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[8]').text
fundo9 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[9]').text
fundo10 = driver.find_element("xpath",'//*[@id="table-ranking"]/tbody/tr[10]').text

#transformando em lista
tabelaInvest1 = []
tabelaInvest1.append(fundo1)
print(tabelaInvest1)

tabelaInvest2 = []
tabelaInvest2.append(fundo2)

tabelaInvest3 = []
tabelaInvest3.append(fundo3)

tabelaInvest4 = []
tabelaInvest4.append(fundo4)

tabelaInvest5 = []
tabelaInvest5.append(fundo5)

tabelaInvest6 = []
tabelaInvest6.append(fundo6)

tabelaInvest7 = []
tabelaInvest7.append(fundo7)

tabelaInvest8 = []
tabelaInvest8.append(fundo8)

tabelaInvest8 = []
tabelaInvest8.append(fundo8)

tabelaInvest9 = []
tabelaInvest9.append(fundo9)

tabelaInvest10 = []
tabelaInvest10.append(fundo10)

#lista Geral
principaisFundos = [tabelaInvest1, tabelaInvest2, tabelaInvest3, tabelaInvest4, tabelaInvest5, tabelaInvest6, tabelaInvest7, tabelaInvest8, tabelaInvest9, tabelaInvest10]


# In[3]:


df = pd.DataFrame(principaisFundos)
df


# In[4]:


#salvando os dados tratados como csv.
df.to_csv('FundosFonte/FundosImobiliarios.csv', index = False)


# In[5]:


FundosAtualizados = pd.read_csv('FundosFonte/FundosImobiliarios.csv', sep =' ')


# In[6]:


#Separando o CSV por espaço vazio, dessa forma pude ver cada dado no arquivo.
FundosFinal = FundosAtualizados['0'].str.split(' ',expand = True)
FundosFinal


# In[7]:


#como se trata apenas de um view ao renomear a coluna ela se uni denovo.
#FundosFinal.rename(columns = {'0': 'Código do Fundo'})
#FundosFinal


# In[8]:


FundosFinal.to_csv('FundosFonte/FundosImobiliariosFinal.csv', index = False)


# In[9]:


FundosProntos = pd.read_csv('FundosFonte/FundosImobiliariosFinal.csv', sep =',')
FundosProntos


# In[10]:


FundosProntos.drop(columns=['6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26', '27', '28','29','30','31','32'], inplace=True)


# In[11]:


FundosProntos


# In[12]:


FundosTratados = FundosProntos.rename(columns = {'0': 'Fundo','1': 'Setor','2':'Moeda','3':'Preço Atual','4':'Liquidez Diaria','5':'Dividendo'})
FundosTratados


# In[13]:


FundosTratados.to_csv('FundosFonte/FundosImobiliariosTratados.csv', sep=';') 


# In[ ]:





# In[ ]:




