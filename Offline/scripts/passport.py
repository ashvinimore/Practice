from passporteye import read_mrz
import os
from scripts.comm.config import SCRIPT_PATH
import pandas as pd
import numpy
from sklearn.metrics import accuracy_score

def passport_accuracy(filename):
    script_path = SCRIPT_PATH + 'scripts/'
    mrz = read_mrz(filename, save_roi=True)
    os.remove(filename)

    extract = {}
    try:
        mrz_data = mrz.to_dict()

        for key, value in mrz_data.items():
            # print(key,value)
            if key == 'names' or key == 'surname' or key == 'sex' or key == 'country' or key == 'nationality' or key == 'date_of_birth' or key == 'number':
                extract[key] = value
            if key == 'valid_score':
                accuracy = value
                accuracy = float(accuracy/100)

        csvfile = script_path + 'UserClass.csv'
        csvfileaddress = script_path + 'address.csv'
        df = pd.read_csv(csvfile)  #
        dfadd =  pd.read_csv(csvfileaddress)
        bag = {}

        Parameters = list(df['Parameters'])
        Parametersadd = list(dfadd['Parameters'])
        # Parameters.remove("DOB")
        Information = list(df['Information'])
        Informationadd =  list(dfadd['Information'])
        #     del Information[9]
        if Parameters.index("DOB"):
            i = Parameters.index("DOB")
            Parameters.remove("DOB")
            del Information[i]
        if Parameters.index("MartialStatus"):
            i = (Parameters.index("MartialStatus"))
            Parameters.remove("MartialStatus")
            del Information[i]
            Information.append(Informationadd[1])
        print(Information)
        passportpara = []
        passportpara.append(extract['country'])
        if(extract['names']):
            na = (extract['names'].split(' '))
        if(extract['sex'] == 'M'):
            sex = 'Male'
        else:
            sex = 'Female'
        if(extract['country'] == 'IND'):
            country = 'India'
        if(len(na) >= 2):
            passportpara.append(na[0])
            passportpara.append(na[1])
        passportpara.append(country)
        passportpara.append(sex)
        passportpara.append(extract['surname'])
        passportnumber = extract['number']
        bags = numpy.ones(len(Information))
        bag_vector = numpy.zeros(len(Information))
        i = 0
        if(accuracy  > 0.60):
            try:
                for val in Information:
                    for value in passportpara:
                        if str(val).lower() in (str(value).lower()):
                            i = i + 1
                            break

                for val in range(0, i):
                    bag_vector[val] = 1
            except Exception as e:
                # print("eeee",e)
                pass
        acc = (accuracy_score(bags, bag_vector))
        print("acc",acc)
        if acc < 0.70:
            verifystatus = True
        else:
            verifystatus = False
        os.remove(script_path +  'UserClass.csv')

    except:
        # print("not extracted")
        extract,extractionaccuracy,verifystatus =  '0',0,'Verification Failed';
    return extract,acc,verifystatus,passportnumber