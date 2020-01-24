import subprocess
# #from scripts.create_images1 import create_image
from scripts.ocr import get_string
import scripts.svm as svm
import scripts.svm1 as svm1
from scripts.update import updates
from scripts.comm.config import SCRIPT_PATH
import os
import create_images1
from  scripts.dataframes import createframe
from scripts import passport

def verification(fileid,doctype,UserID):
    script_path = SCRIPT_PATH + "scripts/"
    # print(script_path)
    adharnum = '0'
    try:
        if  doctype == 'Aadhar Card':
            # print("fileiddd")
            createframe(fileid,UserID)
            ImageForgeFlag = ''
            name, address,filename,ImageForgeFlag = create_images1.create_image(fileid=fileid, type1=doctype)#
            # print( "namess",name,address,ImageForgeFlag,UserID)
        #     #create_images1.create_image(fileid=file_id, type1=type1)
            txt_file = script_path + 'AdharName.txt'
            # runTest.run(filename)
            os.remove(filename)
            accuracy_name = ''
            accuracy_address = ''
            if name != '':

                extract,adharnum = get_string(name,txt_file)
                # print("adharnumn",adharnum)
                # print("extact",extract)
                accuracy_name = svm1.classify(extract=extract, type1=doctype)
                # print(accuracy_name)

            else:
                # print("front side not attached")
                extract = ''
                status_gender = ''
                status_dob = ''
        #
            if address != '':
                txt_file = script_path + 'AdharAddress.txt'
                get_string(address, txt_file)
                accuracy_address,address = svm.classify(txt_file = txt_file)
                # print(accuracy_name,accuracy_address,address)
            else:
                # print("address side of aadhaar not attached")
                address = ''
        #
            if(accuracy_name == ''  ):
                accuracy_name = 0.0
            if(accuracy_address == ''):
                accuracy_address = 0.0
            if float(accuracy_name) < 0.60 or  float(accuracy_address) < 0.40 or str(accuracy_name) == 'nan':
                varifystatus = False
            else:
                varifystatus = True
            # print("ImageForgeFlag",ImageForgeFlag)
            update = updates(userid=UserID,type1 = doctype,ImageForgeFlag = ImageForgeFlag,IsProcessed='1',OCRStatus = varifystatus,num = adharnum)
            # print(update)
        elif doctype == 'PAN Card':
            createframe(fileid, UserID)
            filename,verify,acc = create_images1.create_image(fileid=fileid, type1=doctype)  #
            # print(filename,verify,acc)
            txt_file = script_path + 'PanName.txt'
            extract,adharnum = get_string(filename, txt_file)
            # print(extract)
            accuracy_name = svm1.classify(extract =  extract,type1 = doctype)
            # print(accuracy_name)
            # accuracy_name = str(accuracy_name)
            if float(accuracy_name) < 0.4 or accuracy_name == 'nan':
                varifystatus = False
            else:
                varifystatus = True
          #  print(varifystatus)
            update = updates(userid=UserID,type1 = doctype,ImageForgeFlag = verify,IsProcessed='1',OCRStatus = varifystatus,num = adharnum)
            # print(update)
        elif doctype == 'Passport':
            createframe(fileid, UserID)
            filename,verify,acc = create_images1.create_image(fileid=fileid, type1=doctype)  #
            extract, accuracy, verifystatus,passportnumber= passport.passport_accuracy(filename)
            update = updates(userid=UserID, type1=doctype, ImageForgeFlag=verify, IsProcessed='1',
                             OCRStatus=verifystatus, num=passportnumber)
            print(update)
            #     update = updates(userid=user_id, sr=sr, accuracy=passport_accuracy,address = "null", accuracy_address='null', extract=extraction,
            #                     type1=type1,varifystatus = verify,status_dob = 'null',status_gender = 'null')
                # print(update)
            #
    except Exception as e:
        print(e)
        try:
            varifystatus = False
            update = updates(userid=UserID, type1=doctype, ImageForgeFlag=ImageForgeFlag, IsProcessed = '2',OCRStatus=varifystatus,num = adharnum)
            # print(update)
        except Exception as e:
            # print(e)
            varifystatus = False
            ImageForgeFlag = False
            update = updates(userid=UserID, type1=doctype, ImageForgeFlag=ImageForgeFlag, IsProcessed='2',
                             OCRStatus=varifystatus,num = adharnum)


    test = os.listdir(script_path)

    for item in test:
        if item.endswith(".png") or item.endswith(".jpeg")  or item.endswith(".jpg"):
            os.remove(os.path.join(script_path, item))


# verification('ObjectId("5d776684aec5722bfc22bbd7")','Aadhar Card','ObjectId("5d76297e9f2bbb34585e628d")')