# Usefull in extraction of all the data in the particular directory
# It will extract images/pdfs even if they are in sub-folder in a particular directory


import os
import cv2
from PIL import Image
import tempfile
from pdf2image import convert_from_path

path = '/home/ashish/PycharmProjects/Image-forgery-detection/dataset/Dataset'
target = '/home/ashish/PycharmProjects/Image-forgery-detection/dataset/temp/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))
        elif '.jpeg' in file:
            files.append(os.path.join(r, file))
        elif '.png' in file:
            files.append(os.path.join(r, file))
        # elif '.pdf' in file:
        #     files.append(os.path.join(r, file))
for f in files:
    print(f)

    #for PDF extraction and convertion into JPEG format images.
    #to use pdf-extraction uncomment below code and comment images-extraction code

    # filename = f
    # with tempfile.TemporaryDirectory() as path:
    #     images_from_path = convert_from_path(filename, output_folder=path, last_page=1, first_page=0)
    #
    # base_filename = os.path.splitext(os.path.basename(filename))[0] + '.jpg'
    #
    # save_dir = target
    #
    # for page in images_from_path:
    #     page.save(os.path.join(save_dir, base_filename), 'JPEG')
    
#for images extraction 
    i=1
for path in files:
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    cv2.imwrite(os.path.join(target,str(i)+'.jpeg'),img)
    i=i+1



