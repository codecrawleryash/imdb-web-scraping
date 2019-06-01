
# coding: utf-8

# In[3]:


from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
browser = webdriver.Chrome()
browser.get("http://www.facebook.com")

html_doc=browser.page_source

soup=BeautifulSoup(html_doc,"lxml")
print(soup.prettify())

browser.quit()


# In[9]:


from bs4 import BeautifulSoup
x=list(soup.find_all("link"))


# In[10]:


len(x)


# In[11]:


x[0]


# In[15]:


c=list(soup.find_all("a"))


# In[19]:


c[1]


# In[18]:


soup.find_all("a",class_="_42ft _4jy0 _55pi _2agf _4o_4 _63xb _p _4jy3 _517h _51sy")


# In[22]:


h=soup.find_all("a",{"id":"u_0_f"})


# In[23]:


h


# In[45]:


cc=soup.find("link")


# NBA project

# # NBA Project

# In[46]:


from   selenium import webdriver
from   selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
browser = webdriver.Chrome()
browser.get("https://in.global.nba.com/playerindex/")

html_doc=browser.page_source

soup=BeautifulSoup(html_doc,"lxml")
print(soup.prettify())


# In[49]:


cc=soup.find("div",class_="nba-stat-table__overlay")


# In[57]:


xx=cc.find_all("tr")


# In[63]:


lis=[]
for td in xx:
    lis.append(td.text.strip())


# In[76]:


lis

