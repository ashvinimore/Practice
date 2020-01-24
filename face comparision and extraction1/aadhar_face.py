import cv2
from mtcnn.mtcnn import MTCNN

# Declaring object
detector = MTCNN()

img_path = "test_images/face_extraction/test.png"
img_name = img_path.split(".")[0]
image = cv2.imread(img_path)
temp = image.copy()

# Detecting faces in the image
result = detector.detect_faces(image)

# If no face detected then result list will be empty, hence exiting the function
if(len(result)==0):
	print("No face detect. Invalid/low-quality face image")
	exit()

# Result is an array with all the bounding boxes detected.
images = []
for i in range(len(result)):
	# bounding_box = result[i]['box']
	# keypoints = result[i]['keypoints']
	# # cv2.rectangle(temp,
	#               (bounding_box[0], bounding_box[1]),
	#               (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
	#               (0,155,255),
	#               2)

	# Coordinates of bounding box
	x, y, w, h = result[i]['box']
	#slicing faces from image
	face = image[y-20:y+h+20, x-20:x+w+20]
	images.append(face)
i=1;
for img in images:
	width, height = img.shape[:2]
	if(width==0 or height == 0):
		print(str(i)+"-th","face detected is not clear")
		continue
	# cv2.imshow("temp",img)
	cv2.imwrite(img_name +str(i)+ "_face.jpg", face)
	i=i+1
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

# print(result)