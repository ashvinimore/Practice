#convert PNG images to JPG format

from PIL import Image
from tqdm import tqdm
import os

path = "/home/ashish/Anomoly-detection/Image-forgery-detection/dataset/png/"

for img in tqdm(os.listdir(path)):
	pathx = os.path.join(path, img)
	image = Image.open(pathx).convert('RGB')
	name = img.split('.')[1]
	image.save(path + name + '.jpg')