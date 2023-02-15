import re
import os
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def read_file(directory = "CSE508_Winter2023_Dataset_Processed"):
    data = {}
    for filename in os.listdir(directory):    
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as f:
            file_contents = f.read()
        data[filename] = file_contents
    return data

def remove_stop_words(s):
    s = s.split()

    stop_words = set(stopwords.words('english'))

    tokens_clean = [token for token in s if token not in stop_words]
    temp = ""
    for i in tokens_clean:
        temp +=i+" "
    return temp

def remove_punctuation(tokens):
    punctuation = string.punctuation
    lst = []
    op = ""
    for i in tokens.strip():
        temp = ""
        for j in i:
            if j not in punctuation:
                temp+=j
        op += temp
        
    return op

def preprocess(s):
    # convert to lowercase
    s = s.lower()
    # remove stopwords
    s = remove_stop_words(s)
    # remove punctuations
    s = remove_punctuation(s)
    s = s.split()
    # print(s)
    return s



# preprocess("SDHCdevj to a and not hello we'll help y'all")