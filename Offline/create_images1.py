__author__ = "Sunil Barve"
__copyright__ = ""
__credits__ = [""]
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = "Development"

from bson import ObjectId
import gridfs
import base64
import datetime
import pymongo
from pdf2image import convert_from_path
from scripts.comm.config import SCRIPT_PATH
import imageio
import os
import aadhar_type
import pytesseract
import PIL
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from nltk.tokenize import RegexpTokenizer
from Image_forgery_detection  import runTest_single

import image_slicer
class MongoConn(object):
    """
        Class to handle operations on Mongodb
    """

    def __init__(self, connection_obj, collection="test"):
        """
            Constructor of Mongo Connection.
        """
        self.database = connection_obj['DATABASE']
        self.collection = collection
        self.conn = pymongo.MongoClient(host=connection_obj['HOST'], port=connection_obj['PORT'])
        self.db_obj = self.conn[self.database]

        # self.conn["UPruf"].authenticate(connection_obj['USERNAME'], connection_obj['PASSWORD'],
        #                                 mechanism=connection_obj['MECHANISM'])

    def __del__(self):
        if self.conn is not None:
            self.conn.close()


def create_image(fileid,type1):
    # print(fileid)
    SCRIPT_PATHS = SCRIPT_PATH + "scripts/"
    try:
        mongo_upruf = MongoConn({"HOST": "192.168.10.13", "PORT": 27017, "DATABASE": "ActualDB"
                              })
        grid_fs = gridfs.GridFS(mongo_upruf.db_obj)
        # out = grid_fs.find({'_id': ObjectId(fileid) })
        out = grid_fs.get(ObjectId(fileid))
        content = out.read()
        filename = out.filename
        # print(filename)

        data = base64.b64encode(content)
        # path ='/home/sagar/Music/bluecrest/ashvini/Accuracy/'
        current_date = datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S%f')
        filename = filename.split(".")
        fil_nm = filename[0] + "_" + current_date
        filename = fil_nm + "." + filename[1]
        image_64_decode = base64.decodestring(data)
        image_result = open(SCRIPT_PATHS+filename,
                            'wb')
        image_result.write(image_64_decode)
        del mongo_upruf
        filename = SCRIPT_PATHS+filename
        # print(filename)

        image = filename.split('.')
        img_path = image[0]
        ext = (image[1])
        # print(ext)
        name = ''
        address = ''
        if ext == 'pdf':
            images = convert_from_path(filename)
            # print(images)
            for page in images:
                page.save(img_path, 'JPEG')
            filename = img_path
        else:
            filename = filename
            img_path = filename


        if type1 == 'Aadhar Card':
            # path2 = filename
            # path_single =aadhar_extraction_single. runTest(path2)
            acc,verify = runTest_single.run(filename)
            # print(acc,verify)
            ImageForgeFlag = verify
            type_adhar = aadhar_type.imageclass(filename)
            # print(type_adhar)
                # To divide filename
            if str(type_adhar) == 'type-3':
                filename  = img_path
                # print(filename)
                img = imageio.imread(filename)
                height, width, value = img.shape
                # print(height,width)
                # Cut the image in half
                width_cutoff = width // 2
                s1 = img[:, :width_cutoff]
                s2 = img[:, width_cutoff:]
                # Save each half
                name = 'face1.png'
                name = SCRIPT_PATHS + name
                imageio.imsave(name, s1)
                # print("name",name)
                address = 'face2.png'
                address = SCRIPT_PATHS + address
                imageio.imsave(address, s2)
                return name,address,filename,ImageForgeFlag

            elif str(type_adhar) == 'type-1':
                try:
                    if os.path.exists("OCRR.txt"):
                        os.remove("OCRR.txt")
                except Exception as e:
                    pass

                output = pytesseract.image_to_string(PIL.Image.open(
                    filename).convert("RGB"), lang='eng')
                f = open("OCRR.txt", "a")
                f.write(output)

                f = open("OCRR.txt", "r")
                # data = f.readlines()
                f = (f.read())
                tokenizer = RegexpTokenizer(r'\w+')
                input = (tokenizer.tokenize(f))
                # print("OCRR",input)
                for inp in input:
                    if inp == 'DOB' or inp.lower() == 'MALE'.lower() or inp.lower() == 'FEMALE'.lower():
                        img = imageio.imread(filename)
                        name = 'face1.png'
                        name = SCRIPT_PATHS + name
                        imageio.imsave(name, img)
                        address = ''
                        return name, address, filename,ImageForgeFlag
                    elif inp.lower() == 'Address'.lower() or inp.lower() == "Maharashtra":
                        img = imageio.imread(filename)
                        address = 'face2.png'
                        address = SCRIPT_PATHS + address
                        imageio.imsave(address, img)
                        name = ''
                        return name, address, filename,ImageForgeFlag
            elif str(type_adhar) == 'type-2':
                # print("type222")
                try:
                    if os.path.exists("OCRR.txt"):
                        os.remove("OCRR.txt")
                except Exception as e:
                    pass
                output = pytesseract.image_to_string(PIL.Image.open(
                    filename).convert("RGB"), lang='eng')
                f = open("OCRR.txt", "a")
                f.write(output)

                f = open("OCRR.txt", "r")
                # data = f.readlines()
                f = (f.read())
                tokenizer = RegexpTokenizer(r'\w+')
                input = (tokenizer.tokenize(f))
                # print("OCRR", input)

                for inp in input:
                    if inp.lower() == 'Enrollment'.lower() or inp.lower() == 'Your'.lower() or inp.lower() == 'Male'.lower() or inp.lower() == 'Female'.lower() or inp.lower() == 'unique'.lower() or inp.lower() == 'Aadhaar'.lower():
                        img = imageio.imread(filename)
                        height, width, value = img.shape
                        croppedImage1 = img[0:int(height // 2), 0:width]
                        croppedImage2 = img[int(height // 2):height, 0:width]
                        address = 'face2.png'
                        address = SCRIPT_PATHS + address
                        imageio.imsave(address, croppedImage1)
                        name = 'face1.png'
                        name = SCRIPT_PATHS + name
                        imageio.imsave(name, croppedImage2)
                        return name,address,filename,ImageForgeFlag
                    elif inp.lower() == 'Address'.lower() or  inp.lower() == 'Maharashtra' or inp.lower() == 'Information'.lower() or inp.lower() == 'Instruction'.lower():
                        img = imageio.imread(filename)
                        height, width, value = img.shape
                        croppedImage2 = img[int(height // 2):height, 0:width]
                        address = 'face2.png'
                        address = SCRIPT_PATHS + address
                        imageio.imsave(address, croppedImage2)
                        name = ''
                        return name, address, filename,ImageForgeFlag
            elif str(type_adhar) == 'type-4':
                # print("type-4")
                tiles = image_slicer.slice(
                    filename,
                    4, save=False)
                image_slicer.save_tiles(tiles, directory=SCRIPT_PATHS)
                os.remove(SCRIPT_PATHS+'_01_01.png')
                os.remove(SCRIPT_PATHS+'_01_02.png')
                file = SCRIPT_PATHS +'_02_01.png'
                # print(file)
                img = imageio.imread(file)
                name = 'face1.png'
                name = SCRIPT_PATHS + name
                imageio.imsave(name, img)
                os.remove(SCRIPT_PATHS + '_02_01.png')
                # print("name", name)
                file = SCRIPT_PATHS + '_02_02.png'
                # print(file)
                img = imageio.imread(file)
                address = 'face2.png'
                address = SCRIPT_PATHS + address
                imageio.imsave(address, img)
                os.remove(SCRIPT_PATHS + '_02_02.png')
                # os.remove('02_01.png')
                # os.remove('02_02.png')
                return name, address, filename,ImageForgeFlag


# _          else:
#                 return name,address,filename

        elif type1 == 'PAN Card':
            acc, verify = runTest_single.run(filename)
            # print(acc,verify)
            ImageForgeFlag = verify
            return filename,verify,acc
        elif type1 == 'Passport':
            acc, verify = runTest_single.run(filename)
            return filename,verify,acc



    except Exception as e:
        # print(e)
        pass


