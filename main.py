# Dependencies
import numpy as np
import keras
import tensorflow as tf
from keras.preprocessing import image
from keras.applications.inception_resnet_v2 import InceptionResNetV2

CATEGORIES = ["cardboard", "glass", "metal", "paper", "plastic", "trash"]


# method for predicting the category
def getPrediction(filename):
    model = keras.models.load_model('pretrained_model.h5')

    img = image.load_img('static/'+filename, target_size=(200, 200))
    img = image.img_to_array(img, dtype=np.uint8)
    img = np.array(img)/255.0

    # returns a numpy array
    pred = model.predict(img[np.newaxis, ...])
    # finds the index of the category
    pred_cat = np.argmax(pred)
    # converts index to actual label
    pred_cat_label = CATEGORIES[pred_cat]
    transform = getTransform(pred_cat_label)

    return pred_cat_label, filename, transform

def getTransform(label):
    transformInfo = 'placeholder'
    
    if (label == 'cardboard'):
        transformInfo = 'Cool cardboad stuff'
    elif (label == 'glass'):
        transformInfo = 'Cool glass stuff'
    elif (label == 'metal'):
        transformInfo = 'Cool metal stuff'
    elif (label == 'paper'):
        transformInfo = 'Cool paper stuff'
    elif (label == 'plastic'):
        transformInfo = 'Cool plastic stuff'
    elif (label == 'trash'):
        transformInfo = 'Nothing, this is trash'    

    return transformInfo