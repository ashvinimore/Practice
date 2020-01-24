import pytesseract
import PIL
import re
from wand.image import Image as Img
import cv2
import string
from nltk.corpus import stopwords
from scripts.comm.config import SCRIPT_PATH
import os
stop_words = (set(stopwords.words('english')))

def get_string(img1,txt_file):
    # print(img1)
    data_ex = []
    extract = {}
#    print(txt_file)
    output = pytesseract.image_to_string(PIL.Image.open(img1).convert("RGB"), lang='eng')
    f=open(txt_file,"w")
    f.write(output)
    if 'AdharAddress.txt' in txt_file:
        os.remove(img1)
    if 'AdharName.txt' in txt_file :
        f = open(txt_file,"r")
        data = f.readlines()
        for info in data:
            try:
                info = info.replace(' ','')
                digits = int(info)
                print(len(str(digits)))
                if len(str(digits))  > 8:
                    adharnum = info
                    print("adhaar number:",info)

            except Exception as e:
                # print(type(info), info)
                pass

        clean = [word for word in data if word not in stop_words]
        # print("Clean",clean)
        data = []
        for d in clean:
           if(len(d) > 4):
                d3 = (d.split(' '))
                if(len(d3) >= 2):
                   for leng in d3:
                       flag = 0
                       if(len(leng) >=3):
                           flag = 1
                       else:
                           break
                   if flag == 1:
                    d = str(d3)
                    data.append(d.strip('[').strip(']'))

        # print(data)

        for value in data:
            value = re.sub('[^A-Za-z0-9]+', '', value)
            if (len(value) < 4) or ((len(value) <= 10 and re.findall("[@_!#$%^&*()<>?/\|//}{~:]",value) == True))  :
                pass
            else:
                data_ex.append(value.strip('n'))
        # print(data_ex)
        name = ''
        dob = ''
        gender =''
        AdharNumber = 0
        for i,value in enumerate(data_ex):
                i = int(i)
                # print('valueee',value)
                if len(str(data_ex[i])) <= 10 or value[0].isupper() == False :
                    pass
                else:
                    # print(value.isnumeric())
                    if (value.isnumeric() == True):
                        pass
                    else:
                        try:
                            name = re.sub('[^A-Za-z]', '', data_ex[i])
                            dob = re.sub('[^0-9]+', '', data_ex[i+1])
                            gender = re.sub('[^A-Za-z]+', '', data_ex[i+2])
                            # AdharNumber = re.sub('[^0-9]+', '', data_ex[i+3])
                        except IndexError as E:
                            # print(E)
                            pass
                        break

        name = re.sub( r"([A-Z])", r" \1", name).split()
        # extract['name'] = name
        if name :
            try:
                if len(name) < 3:
                    extract['FirstName'] = name[0]
                    extract['LastName'] = name[1]
                else:
                    extract['FirstName'] = name[0]
                    extract['MiddleName'] = name[1]
                    extract['LastName'] = name[2]
            except IndexError as E:
                # print(E)
                pass

        extract['DOB'] = dob

        if 'F' in gender:
            extract['Gender'] = 'Female'
        else:
            extract['Gender'] = 'Male'
        # print(extract)

        # extract['AdharNumber'] = AdharNumber
        os.remove(txt_file)
        os.remove(img1)   #
        return extract,adharnum
 #
    elif 'PanName.txt' in  txt_file:
        adharnum = ''
        # path = SCRIPT_PATH.replace('/scripts', '')
        # txt_file = path + txt_file
    #    print("in function")
        f = open(txt_file, "r")
        data = f.read()
        clean = [word for word in data.split() if word not in stop_words if len(word) > 3 if re.compile('[@_!#$%^&*()<>?/\|}{~:]').search(word) == None if word.isupper() == True if word != 'INCOMETAXDEPARTMENT']
        clean = (list(set(clean)))
        os.remove(txt_file)
        os.remove(img1)
        return  clean,adharnum


#
# def allimages():
#     src_path = "image/"
#     images_list = os.listdir(src_path)
#     print(images_list)
#
#     for image in images_list:
#         print(image)
#         get_string(src_path+image)
#
# allimages()

# extract = get_string('/home/sagar/Music/bluecrest/ashvini/acc/image/pan3.jpg','PanName.txt')
# print(extract)
