# face verification with the VGGFace2 model
from matplotlib import pyplot
from PIL import Image
from numpy import asarray
from scipy.spatial.distance import cosine
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import face_recognition

# extract a single face from a given photograph
def extract_face(filename, required_size=(197, 197)):
    # load image from file
    pixels = pyplot.imread(filename)
    # create the detector, using default weights
    detector = MTCNN()
    # detect faces in the image
    results = detector.detect_faces(pixels)
    # extract the bounding box from the first face
    x1, y1, width, height = results[0]['box']
    x2, y2 = x1 + width, y1 + height
    # extract the face
    face = pixels[y1:y2, x1:x2]
    # resize pixels to the model size
    image = Image.fromarray(face)
    image = image.resize(required_size)
    face_array = asarray(image)
    img = Image.fromarray(face_array, 'RGB')
    # img.show()
    return face_array

# extract faces and calculate face embeddings for a list of photo files
def get_embeddings(filenames):
    # extract faces
    faces = [extract_face(f) for f in filenames]
    # convert into an array of samples
    samples = asarray(faces, 'float32')
    # prepare the face for the model, e.g. center pixels
    samples = preprocess_input(samples, version=2)
    # create a vggface model
    model = VGGFace(model='resnet50', include_top=False, input_shape=(197, 197, 3), pooling='avg')
    # perform prediction
    yhat = model.predict(samples)
    return yhat

# determine if a candidate face is a match for a known face
def is_match(known_embedding, candidate_embedding, thresh=0.60):
    # calculate distance between embeddings
    dist =[]
    global score
    score = cosine(known_embedding, candidate_embedding)
    known_image = face_recognition.load_image_file(filenames[0])
    unknown_image = face_recognition.load_image_file(filenames[1])
    known_embedding2 = face_recognition.face_encodings(known_image)[0]
    candidate_embedding2 = face_recognition.face_encodings(unknown_image)[0]
    distance =face_recognition.face_distance([known_embedding2], candidate_embedding2)
    # results = face_recognition.compare_faces([known_embedding2], candidate_embedding2)
    avgscore = (score+distance[0])/2
    if avgscore <= thresh:
        print(100-(avgscore)*100,'%',' confidence - Match found (%.3f <= %.3f)' % (avgscore, thresh))
    else:
        print(100-(avgscore)*100,'%',' confidence - Match not found (%.3f <= %.3f)' % (avgscore, thresh))

# define filenames
global filenames
filenames = ['test_images/face_comparision/test2-a.jpg', 'test_images/face_comparision/test3-b.jpg']
# get embeddings file filenames
embeddings = get_embeddings(filenames)
# verify known photos of sharon
is_match(embeddings[0], embeddings[1])
