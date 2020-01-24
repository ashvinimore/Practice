from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
from keras.regularizers import l2
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K
import os
from tqdm import tqdm
from PIL import Image, ImageChops, ImageEnhance
import numpy as np
from sklearn.model_selection import train_test_split

Orig = "./dataset/thumb.jpeg"
posDIR = "./dataset/Training_data/"
testDIR = "./dataset/Testdataset/"
imgSize = 128
lr = 0.001
chanDim = -1
inputShape = (imgSize, imgSize, 3)

MODEL_NAME = 'Image-Forgery-{}.model'.format('keras')

#Labeling the data so that output can be classified based on their for i.e. positive or negative
def data_label(imgtag):
    address = imgtag
    word_label = address.split(".")[0]
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
        label = data_label(img)   #Labeling training images based on their types positive or negative
        pathImg = os.path.join(direc, img)
        elaImg = convert_ela(pathImg, 90)

        x.append(np.array(elaImg.resize((128, 128))).flatten() / 255.0)
        y.append(label)
    trainingData.append([x,y])
    # print(trainingData)
    np.save('training_data.npy', trainingData)
    return



x_test = []
y_test = []
def testing_data(direc):
    testingData= []

    for img in tqdm(os.listdir(direc)):
        pathImg = os.path.join(direc, img)
        elaImg = convert_ela(pathImg, 90)
        num = pathImg.split('.')[2]
        print(num)
        x_test.append(np.array(elaImg.resize((128, 128))).flatten() / 255.0)
        y_test.append(num)
    testingData.append([x_test,y_test])
    np.save('testing_data.npy', testingData)
    return testingData



if __name__ == '__main__':
	traindata = training_data(posDIR)

	x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=3)

	x_train = np.array(x_train)
	x_val = np.array(x_val)
	x_val = x_val.reshape(-1, imgSize, imgSize, 3)
	x_train = x_train.reshape(-1, imgSize, imgSize, 3)
	y_train =np.array(y_train)
	y_val = np.array(y_val)

	print(np.array(x_val).shape)
	print(np.array(x_train).shape)

	model = Sequential()
	init="he_normal"
	reg=l2(0.0005)

	model = Sequential()
	model.add(Conv2D(32, kernel_size=(5, 5), padding="valid", input_shape=inputShape, activation='relu')) 
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

	model.add(Conv2D(64, kernel_size=(5, 5), padding="same", activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

	model.add(Conv2D(128, kernel_size=(5, 5), padding="same", activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

	model.add(Conv2D(64, kernel_size=(5, 5), padding="same", activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

	model.add(Conv2D(32, kernel_size=(5, 5), padding="same", activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

	model.add(Flatten())
	model.add(Dense(1000, activation='relu'))
	model.add(Dense(2, activation='softmax'))

	model.compile(loss='mean_absolute_error', optimizer='adam')


	callbacks = [
	    EarlyStopping(monitor='val_mean_squared_error', patience=2, verbose=1),
	]
	verbose =1;
	early_stopping = EarlyStopping(monitor='val_loss', patience=20, verbose=verbose, mode='auto')
	model.fit(x_train,
	      y_train,
	      nb_epoch=50, verbose=verbose,
	      validation_data=(x_val, y_val))

	model.save(MODEL_NAME)