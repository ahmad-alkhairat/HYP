# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:52:49 2018

@author: ahmad
"""

import re #regular expression library
import urllib.request #library to handle urls
from bs4 import BeautifulSoup #to extract and manage data of webpage
from datetime import datetime
start_time = datetime.now()
turl="https://www.bbc.com/sport"
html_txt = urllib.request.urlopen(turl) #opens url webpage
#soup = BeautifulSoup(html_txt,'html.parser')
soup = BeautifulSoup(html_txt)
data = soup.findAll(text=True)
#print(data)


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


result = filter(visible, data)
result1=list(result)

str1 = ''.join(result1)
#print (str1)

end_time = datetime.now()
fetching_time=end_time - start_time 


from langdetect import detect
import requests
start_time = datetime.now()
lang = detect(str1)
if (lang != 'en'):    
    url = 'http://translate.google.com/translate_a/t'
    params = {
        "text": str(str1), 
        "sl": str(lang),
        "tl": "en", 
        "client": "p"
    }
    str1=requests.get(url, params=params).content
    text = str(str1)
else:
    text = str1
end_time = datetime.now()
lang_detect=end_time - start_time 

import os

start_time = datetime.now()
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)


# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
#print("after removing stopwords : ",words[:100])


# stemming of words
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]
#print("after stemming : ",stemmed[:100])

end_time = datetime.now()
text_preprocess=end_time - start_time 


start_time = datetime.now()
direc="R:/hypersolize/manauelV3/"
files=os.listdir(direc)
#texts=[direc + text for text in files]
words=[]
c=len(files)
for text in files:
    f=open(direc + text)
    blop=f.read()
    blop=blop.replace("\n"," ")
    
    blop=blop.split(" ")
    name=text.split('.')
    words.append([name[0],blop])
    #print (c)
    #print (text)
    c-=1
    
#print (words)
retrieved=stemmed
result=[]
total=1
for categ in words:
    keywords=categ[1]
    #print(keywords)
    count=0
    for keyw in keywords:
        count+=retrieved.count(keyw.lower())
    
    total+=count
    result.append([categ[0],count])
result=sorted(result, key=lambda res: res[1])
for res in result:
    print (res,"   ","%.2f" % (res[1]/total),"%")
end_time = datetime.now()
matching_time =end_time - start_time 
print ("Fetching time is           : ",fitching_time)
print ("language detecting time is : ",lang_detect)
print ("text preprocessing time is : ",text_preprocess)
print ("Matching process time is   : ",str(matching_time))
        
    


#dictionary=Counter(words)   
#del dictionary[""]


#print (dictionary.most_common(10))