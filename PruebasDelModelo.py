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
model = tf.keras.models.load_mode(path_for_saved_model)

print(model.summary())
