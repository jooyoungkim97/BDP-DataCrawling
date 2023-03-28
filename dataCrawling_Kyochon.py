#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 필요 라이브러리 import
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


# In[2]:


page_dict = {1:25,2:16,3:8,4:10,5:5,6:5,7:5,8:16,9:44,10:18,11:15,12:17,13:15,14:22,15:24,16:22,17:2}


# In[3]:


result = []


# In[4]:


for page_sido1 in page_dict:
    for page_sido2 in range(1,page_dict[page_sido1]+1):
        Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' %(page_sido1, page_sido2)
        #print(Kyochon_url)
        html = urllib.request.urlopen(Kyochon_url)
        soupKyochon = BeautifulSoup(html, 'html.parser')
        tag_ul = soupKyochon.find('ul', attrs={'class':'list'})
        for store in tag_ul.find_all('li'):
            if len(store) <= 1:
                break
            store_name = store.find('strong').string
            store_em_text = store.find('em').text
            store_em_list = store_em_text.split('(')[0].split()
            store_sido = store_em_list[0]
            store_gungu = store_em_list[1]
            store_address = ' '.join(store_em_list)
            result.append([store_name]+[store_sido]+[store_gungu]+[store_address])


# In[5]:


len(result) # 국내 모든 교촌 치킨 매장의 수


# In[6]:


result[0]


# In[7]:


result[1369]


# In[8]:


Kyochon_tbl = pd.DataFrame(result, columns = ('store', 'sido','gungu','store_address'))


# In[9]:


Kyochon_tbl.to_csv("C:/Users/김주영/Desktop/2023-1/빅데이터처리/dataCrawling/Kyochon.csv", encoding = 'cp949', mode = 'w', index=True)

