import tensorflow as tf

# Se carga el modelo H5
path_for_saved_model = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/AlfabetoV2.h5'
model = tf.keras.models.load_model(path_for_saved_model)

# Convertimos el modelo a TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Habilitar cuantizacion
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Realizar la conversion
tflite_model = converter.convert()

# Guardando el modelo
with open('C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/Alfabeto25V2.tflite', 'wb') as f:
    f.write(tflite_model)
    
print("Modelo TFLite convertido y ahora guardado")