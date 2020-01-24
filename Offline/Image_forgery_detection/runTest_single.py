import os
from tqdm import tqdm
from PIL import Image, ImageChops, ImageEnhance
import numpy as np
from sklearn.model_selection import train_test_split
from scripts.comm.config import  SCRIPT_PATH

#testing data directory
# testDIR = "./dataset/Testdataset/"testDIR = "./dataset/Testdataset/"testDIR = "./dataset/Testdataset/"

#Test image resize size
imgSize = 128

#learning rate of model
lr = 0.001
#/home/pavan/Unipruf/o/Anomoly-detection/object_detection1/object_detection/Image-forgery-detection/model

MODEL_NAME = SCRIPT_PATH + 'Image_forgery_detection/model/Image-Forgery-{}.model'.format('CNN')


#Function to convert images to their ELA form so that the CNN can be trained on these ELA images
def convert_ela(path, qual):
    filename = path
    resaved_filename = filename.split('.')[0] + '.resaved.jpg'
    im = Image.open(filename).convert('RGB')
    im.save(resaved_filename, 'JPEG', quality=qual)
    temp = Image.open(resaved_filename)
    diff = ImageChops.difference(im, temp)
    extrema = diff.getextrema()
    max_diff = max([ex[1] for ex in extrema])

    if max_diff == 0:
        max_diff = 1

    scale = 255.0 / max_diff
    diff = ImageEnhance.Brightness(diff).enhance(scale)
    return diff


def run(imgPath):
    import tflearn
    from tflearn.layers.conv import conv_2d, max_pool_2d
    from tflearn.layers.core import input_data, dropout, fully_connected
    from tflearn.layers.estimator import regression

    import tensorflow as tf

    tf.reset_default_graph()
    convnet = input_data(shape=[None, imgSize, imgSize, 3], name='input')

    convnet = conv_2d(convnet, 32, 5, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 5, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 128, 5, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 64, 5, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 32, 5, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = fully_connected(convnet, 1024, activation='relu')
    convnet = dropout(convnet, 0.8)

    convnet = fully_connected(convnet, 2, activation='softmax')
    convnet = regression(convnet, optimizer='adam', learning_rate=lr,
                         loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(convnet, tensorboard_verbose=3)

    model.load(MODEL_NAME)


    x_test = []
    y_test = []
    #extracting test iamges
    # for img in tqdm(os.listdir(testDIR)):
    #     pathImg = os.path.join(testDIR, img)
        
    #     #creating ELA format of test iamges so that it can be compared
    elaImg = convert_ela(imgPath, 90)
    num = imgPath.split('.')[1]

    #resizing image to fit the model configurations
    x_test.append(np.array(elaImg.resize((imgSize, imgSize))).flatten() / 255.0)
    y_test.append(num)


    #Reshaping and converting list to array
    x_test = np.array(x_test)
    x_test = x_test.reshape(-1, imgSize, imgSize, 3)
    output = []
    i=0;
    for img in x_test:
        #Creating single input image test data
        img = np.expand_dims(img, 0)
        #Input image prediction process
        pred = model.predict(img)
        #If prediction % of real>fake then output real image
        pred2 = (model.predict(img) > 0.5).astype(int)
        if pred2[0][0] == 0:
            output.append(False)
        else:
            output.append(True)
        acc =  str(pred[0][0] * 100)
        acc = acc[:5]
        # print("Image no.", y_test[i], output[-1])
        i=i+1
    return  acc, output[-1]


# if __name__ == '__main__':
#     import tflearn
#     from tflearn.layers.conv import conv_2d, max_pool_2d
#     from tflearn.layers.core import input_data, dropout, fully_connected
#     from tflearn.layers.estimator import regression
#
#     import tensorflow as tf
#
#     tf.reset_default_graph()
#     convnet = input_data(shape=[None, imgSize, imgSize, 3], name='input')
#
#     convnet = conv_2d(convnet, 32, 5, activation='relu')
#     convnet = max_pool_2d(convnet, 2)
#
#     convnet = conv_2d(convnet, 64, 5, activation='relu')
#     convnet = max_pool_2d(convnet, 2)
#
#     convnet = conv_2d(convnet, 128, 5, activation='relu')
#     convnet = max_pool_2d(convnet, 2)
#
#     convnet = conv_2d(convnet, 64, 5, activation='relu')
#     convnet = max_pool_2d(convnet, 2)
#
#     convnet = conv_2d(convnet, 32, 5, activation='relu')
#     convnet = max_pool_2d(convnet, 2)
#
#     convnet = fully_connected(convnet, 1024, activation='relu')
#     convnet = dropout(convnet, 0.8)
#
#     convnet = fully_connected(convnet, 2, activation='softmax')
#     convnet = regression(convnet, optimizer='adam', learning_rate=lr,
#                          loss='categorical_crossentropy', name='targets')
#
#     model = tflearn.DNN(convnet, tensorboard_verbose=3)
#
#     model.load(MODEL_NAME)
#
path2 = '/home/pavan/Desktop/images/6_type1.jpeg'
run(path2)



   
