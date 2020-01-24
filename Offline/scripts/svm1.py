import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize,RegexpTokenizer
import numpy
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
import textwrap
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from scripts.comm.config import SCRIPT_PATH
import re
import os
#
#
# def classify():
def classify(extract,type1):
    # script_path = (SCRIPT_PATH)
    script_path = SCRIPT_PATH + "scripts/"
    # print(script_path)

    # type1 == 'PAN Card'
    if type1 == 'Aadhar Card':
        input = list(extract.values())
        csvfile = script_path + 'UserClass.csv'
        df = pd.read_csv(csvfile)  #
        bag = {}
        # parameters = df['Parameters'].to_dict()
        words = list(df['Information'])
        # print(type(words[3]))
        words = [x for x in words if str(x) != 'nan']
        # print(words,input)

        # for key in parameters:
        #     if key in words:
        #         value = (parameters.get(key))
                # print(value,input)

#Overall Accuracy
        bags = numpy.ones(len(input))
        bag_vector = numpy.zeros(len(input))
        # print(bags)
        i = -1
        try:
            for val in input:
                for value in words:
                    if str(val).lower() == str(value).lower() :
                        if(i < len(input)-1):
                            i = i + 1
                        bag_vector[i] = 1
                        # print(value)
                        break
                    else:
                        if (i < len(input)-1):
                            i = i + 1
                        bag_vector[i] = 0


        except Exception as e:
            # print("eeeeee",e)
            pass
        acc = (accuracy_score(bags, bag_vector))
        os.remove(script_path + 'UserClass.csv')
        return acc

    elif type1 == 'PAN Card':
        inputs = extract
        csvfile = script_path + 'PanName.csv'
        df = pd.read_csv(csvfile)  # )
        # parameters = df['Paramters'].to_dict()
        words = df['Information']
        words = [x for x in words if str(x) != 'nan']
        # print(words,inputs)
        bags = (numpy.ones(len(words)))
        bag_vector = (numpy.zeros(len(words)))
        i = 0
        try:
            for val in words:
                for value in inputs:
                    if str(val).lower() == str(value).lower():
                        i = i + 1
                        break

            for val in range(0,i):
               bag_vector[val] = 1
        except Exception as e:
            # print("eeee",e)
            pass
        acc = (accuracy_score(bags, bag_vector))
        os.remove(script_path + 'UserClass.csv')
        os.remove(script_path + 'PanName.csv')
        # print(acc)# # accuracy_score1 = 100 - acc
        return acc







#logic for dob and gender
  #       i = 0
  #       status_dob = 'Verification Failed'
  #       status_gender = 'Verification Failed'
  #       for key,value in bag.items():
  #           for keys,values in input.items():
  #               if key == keys:
  #                   if keys == 'Gender':
  #                       bag_vector[i] = 1
  #                       i = i + 1
  #                       if str(values).lower() == str(value).lower():
  #                          status_gender = 'OCR Verified'
  #                       else:
  #                           status_gender = 'OCR Verification Failed'
  #                   elif keys == 'DOB':
  #                       bag_vector[i] = 1
  #                       i = i + 1
  #                       if str(values).lower() == str(value).lower():
  #                          status_dob = 'UniPruf Verified'
  #                       else:
  #                           status_dob = 'Verification Failed'
  #                   elif keys == 'AdharNumber':
  #                       bag_vector[i] = 1
  #                       i = i + 1
  #                   else:
  #                       len1 = len(str(values)) /2+1
  #                       len1 = int(len1)
  #                       values = str(values)[:len1]
  #                       if str(values).lower() in str(value).lower() :
  # #                          print(value, values)
  #                           bag_vector[i] = 1
  #                           i = i+1
  #           else:
  #               pass
  #  #     print((bags),(bag_vector))


