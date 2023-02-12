#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. Scrape the details of most viewed videos on YouTube from Wikipedia.
# Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos
# You need to find following details:
# A) Rank
# B) Name
# C) Artist
# D) Upload date
# E) Views


# In[52]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from bs4 import BeautifulSoup


# In[4]:


driver = webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32.exe')


# In[5]:


driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")


# In[7]:


designation=driver.find_element(By.CLASS_NAME,"headerSort")


# In[8]:


rank=[]
name=[]
artist=[]
upload_date=[]
views=[]


# In[9]:


# rank_tags=driver.find_elements(By.XPATH,'//td[@class="wikitable sortable jquery-tablesorter"]')
#  for i in rank_tags[0:30]:
#     rnk=i.text
#     rank.append(rnk)
    
    
    
    
    
name_tags=driver.find_elements(By.XPATH,'//a[@class="mw-redirect"]')
for i in name_tags[0:30]:
    nm=i.text
    name.append(nm)  
    
    
    
    
# artist_tags=driver.find_elements(By.XPATH,'//a[@class="mw-redirect"]')
# for i in artist_tags[0:30]:
#      artst=i.text
#         artist.append(artst)
    
    
    
    
    
    
# upload_date_tags=driver.find_elements(By.XPATH,'//a[@class="mw-redirect"]')
# for i in upload_date_tags[0:30]:
#     upld=i.text
#     upload_date.append(upld)
    
    
    
    
    
    
# views_tags=driver.find_elements(By.XPATH,'//a[@class="mw-redirect"]')
# for i in views_tags[0:30]:
#     vws=i.text
#     views.append(vws)
    


# In[10]:


df = [name]
df


# In[11]:


driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")
time.sleep(5)
try:
    element=driver.find_element(By.XPATH,'//td[@class="wikitable sortable jquery-tablesorter"]')
    element.click()
except ElementNotInteractableException as  e:
    print("Exception Raised",e)
    element=driver.find_element(By.XPATH,'//a[@class="mw-redirect"]')
    driver.get(element.get_attribute('href'))


# In[12]:


# Scrape the details team India’s internationalfixtures from bcci.tv.
# Url = https://www.bcci.tv/.
# You need to find following details:
# A) Match title (I.e. 1stODI)
# B) Series
# C) Place
# D) Date
# E) Time
#  Note: - From bcci.tv home page you have reach to the international fixture page through code.


# In[13]:


driver = webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32.exe')
driver.get("https://www.bcci.tv/")


# In[14]:


search=driver.find_element(By.CLASS_NAME,'nav-item')
search.click()


# In[17]:


time.sleep(5)
try:
    search=driver.find_element(By.CLASS_NAME,'nav-link active ')
    search.click()
except NoSuchElementException as  e:
    print("element is not valid",e)
    element=driver.find_element(By.XPATH,'nav-item')
    driver.get(element.get_attribute('href'))


# In[18]:


# 3. Scrape the details of State-wise GDP ofIndia fromstatisticstime.com.
# Url = http://statisticstimes.com/
# You have to find following details:
# A) Rank
# B) State
# C) GSDP(18-19)- at current prices
# D) GSDP(19-20)- at current prices
# E) Share(18-19)
# F) GDP($ billion)
# Note: - From statisticstimes home page you have to reach to economy page through code.


# In[39]:


driver = webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32.exe')
driver.get("http://statisticstimes.com/")
time.sleep(5)
search=driver.find_element(By.CLASS_NAME,'dropbtn')
search.click()


# In[40]:


try:
    search=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
    search.click()
except ElementNotInteractableException as  e:
    print("element is not found",e)
    element=driver.find_element(By.LINK_TEXT,'India')
    driver.get(element.get_attribute('href'))
        


# In[21]:


# 4. Scrape the details of trending repositories on Github.com.
# Url = https://github.com/
# You have to find the following details:
# A) Repository title
# B) Repository description
# C) Contributors count
# D) Language used
#Note: - From the home page you have to click on the trending option from Explore menu through code.


# In[22]:


driver = webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32.exe')


# In[23]:


driver.get("https://github.com/")
time.sleep(5)


# In[24]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
search.click()
time.sleep(5)


# In[25]:



search=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/ul[3]/li[3]/a')
search.click()
time.sleep(5)


# In[26]:


try:
    element=driver.find_element(By.CLASS_NAME,'h3 lh-condensed')
    element.click()
except NoSuchElementException as  e:
    print("element is not valid",e)
    element=driver.find_element(By.XPATH,'nav-item')
    driver.get(element.get_attribute('href'))


# In[27]:


# 5. Scrape the details of top 100 songs on billiboard.com.
# Url = https:/www.billboard.com/
# You have to find the following details:
# A) Song name
# B) Artist name
# C) Last week rank
# D) Peak rank
# E) Weeks on board
# Note: - From the home page you have to click on the charts option then hot 100-page link through code.


# In[53]:


driver = webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32.exe')
driver.get("https:/www.billboard.com/")


# In[54]:


search=driver.find_element(By.LINK_TEXT,'Charts')
search.click()
    


# In[ ]:


search=driver.find_element(By.LINK_TEXT,'Hot Trending Songs')
search.click()


# In[31]:


try:
    search=driver.find_element(By.LINK_TEXT,'Charts')
    search.click()

except ElementClickInterceptedException  as  e:
    print("element is not traceble",e)
    element=driver.find_element(By.XPATH,'/html/body/div[3]/header/div/div[3]/div/nav/ul/li[5]/a')
    driver.get(element.get_attribute('href'))


# In[32]:


# 7. Scrape the details most watched tv series of all time from imdb.com.
# Url = https://www.imdb.com/list/ls095964455/
# You have to find the following details:
# A) Name
# B) Year span
# C) Genre
# D) Run time
# E) Ratings
# F) Votes


# In[33]:


driver = webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32.exe')
driver.get("https://www.imdb.com/list/ls095964455/")


# In[34]:


try:
    element=driver.find_element(By.CLASS_NAME,'lister-item-index unbold text-primary')
    element.click()
except NoSuchElementException as  e:
    print("element is not found",e)
    element=driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[3]/div[1]/div/h1')
    driver.get(element.get_attribute('href'))


# In[35]:


# 8. Details of Datasets from UCI machine learning repositories.
# Url = https://archive.ics.uci.edu/
# You have to find the following details:
# A) Dataset name
# B) Data type
# C) Task
# D) Attribute type
# E) No of instances
# F) No of attribute
# G) Year
# Note: - from the home page you have to go to the ShowAllDataset page through code.


# In[46]:


#driver.maximize_window()
driver = webdriver.Chrome(r'C:\Users\Admin\Downloads\chromedriver_win32.exe')
driver.get("https://archive.ics.uci.edu/")


# In[47]:


search=driver.find_element(By.LINK_TEXT,'view all data sets')
search.click()
time.sleep(5)


# In[51]:


try:
    designation=driver.find_element(By.XPATH,'//p[@"normal"]')
    designation.click()
except InvalidSelectorException   as  e:
    print("element is not found",e)
    element=driver.find_element(By.XPATH,'/html/body/table[2]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/p')
    driver.get(element.get_attribute('href'))


# In[ ]:




