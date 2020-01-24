#Training and Saving model
import os
from tqdm import tqdm
from PIL import Image, ImageChops, ImageEnhance
import numpy as np
from sklearn.model_selection import train_test_split

#Save model directory
modelDIR = "/home/ashish/Anomoly-detection/Image-forgery-detection/model2/"
#training dataset directory location
posDIR = "./dataset/extracteddataset/"
#testing dataset directory location
testDIR = "./dataset/Testdataset/"
#Training image size
imgSize = 128
lr = 0.001

MODEL_NAME = 'Image-Forgery-{}.model'.format('CNN')

#Labeling the data so that output can be classified based on their for i.e. positive or negative
def data_label(imgtag):
    address = imgtag
    word_label = address.split(".")[0]
    #Creating labels for training images
    #so that they can be compared on the basis of percentage of Real or Fake
    if word_label == "positive":
        return np.array([1,0])

    elif word_label == "negative":
        return np.array([0,1])


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



#Global training, testing dataset and label
x = []
y = []
x_train = []
y_train = []
x_val = []
y_val = []

def training_data(direc):
    trainingData = []

    for img in tqdm(os.listdir(direc)):
        label = data_label(img) 
        pathImg = os.path.join(direc, img)
        elaImg = convert_ela(pathImg, 90)

        x.append(np.array(elaImg.resize((128, 128))).flatten() / 255.0)
        y.append(label)
    trainingData.append([x,y])
    # print(trainingData)
    np.save('training_data.npy', trainingData)
    return



# x_test = []
# y_test = []
# def testing_data(direc):
#     testingData= []

#     for img in tqdm(os.listdir(direc)):
#         pathImg = os.path.join(direc, img)
#         elaImg = convert_ela(pathImg, 90)
#         num = pathImg.split('.')[2]
#         print(num)
#         x_test.append(np.array(elaImg.resize((128, 128))).flatten() / 255.0)
#         y_test.append(num)
#     testingData.append([x_test,y_test])
#     np.save('testing_data.npy', testingData)
#     return testingData



if __name__ == '__main__':
    traindata = training_data(posDIR)

    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=3)

    x_train = np.array(x_train)
    x_val = np.array(x_val)
    x_val = x_val.reshape(-1, imgSize, imgSize, 3)
    x_train = x_train.reshape(-1, imgSize, imgSize, 3)

    print(np.array(x_val).shape)
    print(np.array(x_train).shape)

    import tflearn
    from tflearn.layers.conv import conv_2d, max_pool_2d
    from tflearn.layers.core import input_data, dropout, fully_connected
    from tflearn.layers.estimator import regression

    # 6-Hidden and 1-output layer CNN model using tflearn
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

    model = tflearn.DNN(convnet, tensorboard_verbose=1)
    with tf.Session() as sess:
        writer = tf.summary.FileWriter("/home/ashish/Anomoly-detection/Image-forgery-detection/log", sess.graph)
    
    #Training operation
    history = model.fit({'input': x_train},{'targets': y_train}, n_epoch=60,
              validation_set=({'input':x_val},{'targets': y_val}), snapshot_step=500,
              show_metric=True, run_id=MODEL_NAME)

    model.save(modelDIR+MODEL_NAME)  