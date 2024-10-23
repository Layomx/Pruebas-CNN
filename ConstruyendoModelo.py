from tensorflow.keras import Model
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam

# Verificando disponibilidad de GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPU disponible:", gpus)
else:
    print("No se encontró GPU, usando la CPU.")

train_path = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/train'
validation_path = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/validate'

trainGenerator = ImageDataGenerator(preprocessing_function = preprocess_input).flow_from_directory(train_path, target_size=(224, 224), batch_size=30)
validGenerator = ImageDataGenerator(preprocessing_function = preprocess_input).flow_from_directory(validation_path, target_size=(224, 224), batch_size=30)

# Construyendo el modelo
baseModel = MobileNetV2(weights='imagenet', include_top = False) # Se detiene la ultima capa

x = baseModel.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation = 'relu')(x)
x = Dense(256, activation = 'relu')(x)
x = Dense(128, activation = 'relu')(x)

predictLayer = Dense(27, activation = 'softmax')(x) # Densidad de 27 por la cantidad de clases (letras del abecedario)

model = Model(inputs= baseModel.input, outputs = predictLayer)

print(model.summary())

# Congelando capas del anterior modelo

for layer in model.layers[:-5]:
    layer.trainable = False
    
# Compilando el modelo

epochs = 25
optimizer = Adam(learning_rate = 0.001)

model.compile(loss = "categorical_crossentropy", optimizer = optimizer, metrics = ['accuracy'])

# Entrenamiento

model.fit(trainGenerator, validation_data = validGenerator, epochs = epochs)

# Guardando el modelo
path_for_saved_model = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/AlfabetoV2.h5'
model.save(path_for_saved_model)