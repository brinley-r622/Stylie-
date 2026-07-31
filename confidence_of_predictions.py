import numpy as np
import tensorflow as tf
from PIL import Image

# ==========================================================
# CLASS NAMES
# ==========================================================

FACE_CLASSES = [
    "Heart",
    "Oblong",
    "Oval",
    "Round",
    "Square"
]

HAIR_CLASSES = [
    "Straight",
    "Wavy",
    "Curly",
    "Dreadlocks",
    "Kinky"
]

SKIN_CLASSES = [
    "Black",
    "Brown",
    "White"
]


# ==========================================================
# IMAGE PREPROCESSING
# ==========================================================

def preprocess_image(image_path): 

    image = Image.open(image_path) 

    image = image.convert("RGB")

    image = image.resize((224,224))

    image = np.array(image).astype(np.float32) 

    image = tf.keras.applications.mobilenet_v2.preprocess_input(image) 

    image = np.expand_dims(image, axis=0) 

    return image


# ==============
# FACE SHAPE
# ==============

def predict_face_shape(image_path):

    image = preprocess_image(image_path)  

    prediction = face_model.predict(image, verbose=0)[0] 

    index = np.argmax(prediction) 

    confidence = prediction[index]

    return FACE_CLASSES[index], confidence 

    


# ==============
# HAIR TYPE
# ============

def predict_hair_type(image_path):

    image = preprocess_image(image_path)

    prediction = hair_model.predict(image, verbose=0)[0]

    index = np.argmax(prediction)

    confidence = prediction[index]

    return HAIR_CLASSES[index], confidence


# ============
# SKIN TONE
# ============

def predict_skin_tone(image_path):

    image = preprocess_image(image_path)

    prediction = skin_model.predict(image, verbose=0)[0]

    index = np.argmax(prediction)

    confidence = prediction[index]

    return SKIN_CLASSES[index], confidence


# RUN ALL THREE AI MODELS


def analyze_user(image_path):

    face_shape, face_conf = predict_face_shape(image_path)

    hair_type, hair_conf = predict_hair_type(image_path)

    skin_tone, skin_conf = predict_skin_tone(image_path)

    print("="*50) 
    print("AI ANALYSIS")
    print("="*50) 

    print(f"\nFace Shape : {face_shape}") 
    print(f"Confidence : {face_conf:.1%}") 

    print(f"\nHair Type  : {hair_type}")
    print(f"Confidence : {hair_conf:.1%}")

    print(f"\nSkin Tone  : {skin_tone}")
    print(f"Confidence : {skin_conf:.1%}")

    return {

        "face_shape":face_shape,

        "face_confidence":face_conf,

        "hair_type":hair_type,

        "hair_confidence":hair_conf,

        "skin_tone":skin_tone,

        "skin_confidence":skin_conf

    }
uploaded = files.upload() 

image_path = list(uploaded.keys())[0] 

results = analyze_user(image_path) 


# Connect AI predictions to Stylie recommendation engine

predicted_face_shape = results["face_shape"]
predicted_skin_tone = results["skin_tone"]
