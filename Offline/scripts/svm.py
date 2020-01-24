import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize,RegexpTokenizer
import numpy
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import textwrap
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from scripts.comm.config import SCRIPT_PATH
# from ocr import allimages
from random import shuffle
import os

# print(os.getcwd() + '/')

def classify(txt_file):
    script_path = SCRIPT_PATH + 'scripts/'
    stop_words = (set(stopwords.words('english')))
    bag = {}
    df = pd.read_csv(script_path + 'address.csv')
    # print(df)

    # print(parameters)
    words = list(df['Information'])
    param = list(df['Parameters'])
    bow1 = (str(words + param))

    tokenizer = RegexpTokenizer(r'\w+')
    bow = (tokenizer.tokenize(bow1))
    f = open(txt_file)
    f = (f.read())
    tokenizer = RegexpTokenizer(r'\w+')
    input = (tokenizer.tokenize(f))
    input = [i for i in input if len(i) >= 3]
    input = list(set(input))
    # print(input,bow)
    filtered_sentence = [w for w in input if not w in stop_words]
    bags = numpy.ones(len(bow))
    bag_vector = numpy.zeros(len(bow))

    for i,value in enumerate(bow):
        for val in (input):
            len1 = int(len(val)/2) + 2
            if( str(val).lower()[:len1]) in (str(value)).lower():
                bag_vector[i] = 1

    acc = (accuracy_score(bags, bag_vector))
    f = f.replace('\n',' ')
    os.remove(script_path + 'address.csv')
    os.remove(txt_file)
    # print(f)
    return acc,f


