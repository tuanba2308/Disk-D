#input C:\DevOps\FirstProject\Tuanizback\PJ01-tuanizback\Learn\Hangul\Dream Project\Filtered Subtitie\Dream-dual-sub2.md
#output: mongodb with 4 column: number, text, original, mean
# steps:
# - get file
# - convert to pandas
# - get line with **
# - add line with ** to pandas (original)
# - translate and add to col:mean
# - connect to mongodb
# - add to mongodb
# - bonus: create new md file with original, mean
# display on website

# let go
# import libraby
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import pandas as pd
import pprint
import pymongo
import pymongoarrow
import re
import time
# declare
#source / subtitle file
source=r'C:\DevOps\FirstProject\Tuanizback\PJ01-tuanizback\Learn\Hangul\Youth\Filter\Youth-01-netflix-dual-sub.md'
#pandas
df = pd.read_csv(source,encoding = 'utf-8',on_bad_lines='skip',sep = ';', header = None)
df = pd.DataFrame(df.values.reshape(-1, 2), 
                   columns=['number', 'Sentence'])#reshap to 2 column: number, Sentence
df['Selection']=''
df['Meaning']=''
#regex
df['Word']=''
pattern = r'(\*\*|__)(.*?)\1'
#URl
url='https://korean.dict.naver.com/kovidict/#/search?query='
# headless browser
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)

#translate from a list source['Selection'][index]
def translate(source):
  result=[]
  search=[]
  if len(source)==0:
    return result, search
  else:
    for i in source:
      driver.get(url+i[1])
      time.sleep(2)
      try:
          mean=driver.find_elements(By.CLASS_NAME, "mean")[0].get_attribute("innerText").split()[1:] #it worked
          result.append(' '.join(mean))
          search.append(driver.find_elements(By.CLASS_NAME, "highlight")[0].get_attribute("innerText"))###
      except:
          print("Something went wrong when writing to the URL")
    return result, search

#get bold word form a dataframe
def get_bold_word(pattern, source):
  for index in source.index:
    source['Selection'][index]=re.findall(pattern,source['Sentence'][index])
    source['Meaning'][index], source['Word'][index]=translate(source['Selection'][index])
    print(source['Word'][index])
    print(source['Meaning'][index])
    if index > 20:
      break

get_bold_word(pattern,df)

### connect to mongodb
client = MongoClient('mongodb+srv://tmtdbAdmin:LQCVpi0yiJd0iICl@tmtdb.alrrmch.mongodb.net/')
db = client['korean-dictionary-youth']
collection = db['records']
documents = df.to_dict(orient='records')
collection.insert_many(documents)