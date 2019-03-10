# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:52:41 2019

@author: admin
https://towardsdatascience.com/gentle-start-to-natural-language-processing-using-python-6e46c07addf3
https://likegeeks.com/nlp-tutorial-using-python-nltk/
"""
"""
import nltk
nltk.download()
"""
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

url = "https://www.sec.gov/Archives/edgar/data/882095/000088209519000006/a2018form10-k.htm"

def get_tokenizedtext(url):
    response =  urllib.request.urlopen(url)
    html = response.read()
    #print(html)
    soup = BeautifulSoup(html,'html5lib')
    text = soup.get_text(strip = True)
    #print(text)
    
    tokens = [t for t in text.split()]
    #words
    #tokens = word_tokenize(" ".join(tokens))
    #Sentences
    #tokens = sent_tokenize(" ".join(tokens))
    
    #total word counts
    #freq = nltk.FreqDist(tokens)
    #freq.plot(20, cumulative=False)
    #print(tokens.encode("utf-8"))
    return tokens

#--- ---#

def plot_word_count(tokens):
    #sr = stopwords.words('english')
    clean_tokens = tokens[:]
    drugs = []
    
    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)
            
    freq = nltk.FreqDist(clean_tokens)
    #print(clean_tokens)
    
    for key,val in freq.items():
        #if "Gilead" in key:
        #if "BUSINESS" in key.upper():
        #if "®" in key:
            #print(str(key.encode("utf-8")) + ':' + str(val))
        print(str(key) + ':' + str(val))
        drugs.append(key)
        pass
    
    #freq = nltk.FreqDist(drugs)
        
    freq.plot(30, cumulative=False)
# =============================================================================
# Main 
# =============================================================================
plot_word_count(get_tokenizedtext(url))


# =============================================================================
# End of file.
# =============================================================================
