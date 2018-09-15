
# coding: utf-8

# In[14]:

import requests
from bs4 import BeautifulSoup
res = requests.get("https://world.taobao.com/product/%E5%A4%9A%E6%A8%A3%E5%B1%8B-%E8%91%AB%E8%98%86-%E4%BF%9D%E6%BA%AB%E6%9D%AF.htm")
soup = BeautifulSoup(res.text)
for info in soup.select('.info'):
    print(info.select('.price')[0].text)
    print(info.select('.title')[0].text.strip())
    print(info.select('.J_NickPopup')[0].text)


# In[ ]:



