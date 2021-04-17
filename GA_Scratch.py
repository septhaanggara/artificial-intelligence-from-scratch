#!/usr/bin/env python
# coding: utf-8

# In[763]:


import random
import pandas
import numpy 
from sklearn.preprocessing import OneHotEncoder
import json


# In[706]:


datalatih=pandas.read_csv("datalatih.csv", header=None)


# In[708]:


def biner():
    biner=[]
    encode=OneHotEncoder(sparse=False)
    biner=encode.fit_transform(datalatih).astype(int)
    biner=numpy.delete(biner,14,1)
    return(biner)
biner()


# In[572]:


def acak():
    l1=[]
    for i in range(9):
        for j in range(15):
            a= random.randint(0,1)
            l1.append(a)
    l1fix=[]
    a=l1[0:15]
    b=l1[16:31]
    c=l1[32:47]
    d=l1[48:63]
    e=l1[64:79]
    f=l1[80:95]
    g=l1[96:111]
    h=l1[112:127]
    l1fix.append(a)
    l1fix.append(b)
    l1fix.append(c)
    l1fix.append(d)
    l1fix.append(e)
    l1fix.append(f)
    l1fix.append(g)
    l1fix.append(h)
    return(l1fix)
acak()


# In[675]:


def fitness():
    b = biner() 
    a = acak() 
    l=[]
    result=0
    for i in range (8):
        x = i - 1
        for j in range (80):
            j=j-1
            stat1 = "true"
            stat2 = "true"
            while(stat1=="true"):
                    for k in range(15):
                        k = k - 1
                        if (j == 14):
                            if (a[x][k] != b[j][k]):
                                stat1 = "false"
                                stst2 = "false"
                        else:
                            if (a[x][k] != b[y][k]):
                                if (b[j][k] == 1):
                                    stat1 = "false"
                                    stat2 = "false"
                        stat1 = "false"
                    if stat2=='true':
                        result=result+1
        l.append(result)
    return(l)
fitness()


# In[679]:


def persen():
    x=[]
    h1=fitness()[7]/80
    h2=h1*100
    x.append(h2)
    h3=fitness()[6]/80
    h4=h3*100
    x.append(h4)
    return (x)
persen()


# In[663]:


def crossover():
    x=acak()[7]
    y=acak()[6]
    h1=[]
    h2=[]
    r=[]
    a=x[0:3]
    b=y[3:9]
    c=x[9:15]
    d=x[0:3]
    e=y[3:9]
    f=x[9:15]

    h1.extend(a)
    h1.extend(b)
    h1.extend(c)
    h2.extend(d)
    h2.extend(e)
    h2.extend(f)
    r.append(h1)
    r.append(h2)
    return r
crossover()


# In[667]:


def mutasi():
    m1=[]
    a= crossover()[0]
    for n, i in enumerate(a):
        if i == 1:
            a[n] = 0
        else:
            a[n] = 1
    b= crossover()[0]
    for n, j in enumerate(b):
        if j == 1:
            b[n] = 0
        else:
            b[n] = 1
    m1.append(a)
    m1.append(b)
    return m1
mutasi()


# In[757]:


def fitness1():
    a = biner() 
    b = mutasi()
    l=[]
    hasil=0
    for w in range (2):
        t = w - 1
        for z in range (80):
            y=z-1
            stat1 = "true"
            stat2 = "true"
            while(stat1=="true"):
                    for i in range(15):
                        j = i - 1
                        if (j == 14):
                            if (b[t][j] != a[y][j]):
                                stat2 = "false"
                                stat1 = "false"
                        else:
                            if (b[t][j] != a[y][j]):
                                if (a[y][j] == 1):
                                    stat2 = "false"
                                    stat1 = "false"
                        stat1 = "false"
                    if stat2=='true':
                        hasil=hasil+1
        l.append(hasil)
    return(l)
fitness1()


# In[705]:


def persen1():
    x=[]
    h1=fitness1()[1]/80
    h2=h1*100
    x.append(h2)
    return (x)
persen1()


# In[711]:


datauji=pandas.read_csv("datauji.csv", header=None)


# In[744]:


def bineruji():
    biner=[]
    encode=OneHotEncoder(sparse=False)
    biner=encode.fit_transform(datauji).astype(int)
    biner=numpy.delete(biner,13,1)
    return(biner)
biner()


# In[799]:


def jawaban():
    a = bineruji()
    b = mutasi()[1]
    l=[]
    for z in range (20):
        y=z-1
        stat1 = "true"
        stat2 = "true"
        while(stat1=="true"):
                for i in range(14):
                    j = i - 1
                    if (j == 13):
                        if (b[j] != a[y][j]):
                            stat2 = "false"
                            stat1 = "false"
                    else:
                        if (b[j] != a[y][j]):
                            if (a[y][j] == 1):
                                stat2 = "false"
                                stat1 = "false"
                    stat1 = "false"
                if stat2=='true':
                    l.append(stat2)
                if stat2=='false':
                    l.append(stat2)
    w=open("jumlahtrue.txt","w")
    json.dump(l,w)
    return(l)
jawaban()


# In[ ]:





# In[ ]:




