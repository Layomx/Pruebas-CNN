import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from PIL import Image
import numpy as np 
import tensorflow as tf 
import cv2 

# Lista de las clases
categories = os.listdir('C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/train')
categories.sort
print(categories)

# Cargamos el modelo guardado
path_for_saved_model = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/AlfabetoV2.h5'
model = tf.keras.models.load_model(path_for_saved_model)

print(model.summary())

def classify_image(imageFile):
    x = []

    img = Image.open(imageFile).convert('L')
    img = img.convert('RGB')
    img.load()
    img = img.resize((224, 224), Image.Resampling.LANCZOS)

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    x = preprocess_input(x)
    print(x.shape)

    pred = model.predict(x)
    categoryValue = np.argmax(pred, axis = 1)
    print(categoryValue) 

    categoryValue = categoryValue[0]
    print(categoryValue)

    result = categories[categoryValue]

    return result

imagePath = "C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/dataset/train/Letter_s_min_872.png"
resultText = classify_image(imagePath)
print(resultText)

