import os
from tensorflow.keras.preprocessing import image # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore
import numpy as np
import tensorflow as tf
import cv2

# Lista de las clases
categories = os.listdir('C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/train')
categories.sort()

test_path = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/dataset/test'
test = ImageDataGenerator(preprocessing_function=preprocess_input)

test_images = test.flow_from_directory(
    test_path,
    target_size=(224, 224),
    batch_size=30,
    class_mode='categorical'
)

# Cargar el modelo guardado
path_for_saved_model = "C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/Alfabeto25V2.h5"
model = tf.keras.models.load_model(path_for_saved_model)

# Compilar el modelo
optimizer = Adam(learning_rate=0.0001)
model.compile(loss="categorical_crossentropy", optimizer=optimizer, metrics=['accuracy'])

# Directorio que contiene las imágenes de prueba sin clasificación
test_dir = 'C:/Users/drake/OneDrive/Documentos/Universidad/test'

# Nos aseguramos que el tamaño de las imágenes coincida con el tamaño que espera el modelo MobileNet
image_size = (224, 224)  # Declaramos el tamaño esperado

# Listamos todas las imágenes en la carpeta de test
test_images = [f for f in os.listdir(test_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Haciendo predicciones para cada imagen
for image_name in test_images:
    # Cargar y preprocesar la imagen
    img_path = os.path.join(test_dir, image_name)
    img = cv2.imread(img_path)
    img = cv2.resize(img, image_size)
    img = img.astype('float32') / 255.0  # Escalar los valores de los píxeles
    img = np.expand_dims(img, axis=0)  # Añadir dimensión para el batch
    
    # Haciendo la prediccion
    prediction = model.predict(img)
    
    # Obteniendo la clase predicha
    predicted_class = np.argmax(prediction, axis=-1)
    
    print(f"Imagen: {image_name}, Predicción: {predicted_class}")
