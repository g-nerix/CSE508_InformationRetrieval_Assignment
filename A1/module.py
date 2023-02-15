import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import string


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


    print(s)

preprocess("SDHCdevj to a and not hello we'll help y'all")