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
        transformInfo = 'Boxes, packaging, newspaper, bags, writing paper'
    elif (label == 'glass'):
        transformInfo = 'Beads, glassphalt, tiles, countertops, fiberglass insulation'
    elif (label == 'metal'):
        transformInfo = 'Cars, train tracks, airplanes, metal furnishing, artwork'
    elif (label == 'paper'):
        transformInfo = 'Insulation, lamp shades, toilet paper, greeting cards, newspaper'
    elif (label == 'plastic'):
        transformInfo = 'Phone cases, toys, backpacks, yoga mat, surfboard, swimwear'
    elif (label == 'trash'):
        transformInfo = 'This is just trash'    

    return transformInfo