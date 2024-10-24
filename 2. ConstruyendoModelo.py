import tensorflow as tf
from tensorflow.keras import Model # type: ignore
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input # type: ignore
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
from tensorflow.keras.callbacks import EarlyStopping # type: ignore

# Verificando disponibilidad de GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPU disponible:", gpus)
else:
    print("No se encontró GPU, usando la CPU.")

# Carga de los archivos de entrenamiento y validacion
train_path = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/train'
validation_path = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/validate'

# Preprocesamos las imagenes que se vayan obteniendo de el dataset
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

trainGenerator = train_datagen.flow_from_directory(
    train_path,
    target_size=(224, 224),
    batch_size=30
)

valid_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

validGenerator = valid_datagen.flow_from_directory(
    validation_path,
    target_size=(224, 224),
    batch_size=30
)

# Este bloque es especifico para construir el modelo
baseModel = MobileNetV2(weights='imagenet', include_top = False) # Detenemos la ultima capa

x = baseModel.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)  # Añadimos Dropout para evitar posibles sobreajustes
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(128, activation='relu')(x)

predictLayer = Dense(27, activation = 'softmax')(x) # Densidad de 27 por la cantidad de clases (letras del abecedario)

model = Model(inputs= baseModel.input, outputs = predictLayer)

print(model.summary())

# Congelando capas del anterior modelo

for layer in model.layers[:-5]:
    layer.trainable = False
    
# Compilando el modelo

epochs = 25
optimizer = Adam(learning_rate = 0.0001)
model.compile(loss = "categorical_crossentropy", optimizer = optimizer, metrics = ['accuracy'])

# Implementacion de Early Stopping para evitar un sobreajuste
early_stopping = EarlyStopping(monitor='val_loss', patience = 5, restore_best_weights=True)

# Entrenamiento del modelo 
model.fit(trainGenerator, validation_data = validGenerator, epochs = epochs, callbacks = [early_stopping])

# Guardando el modelo en la direccion que queramos
path_for_saved_model = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model/Alfabeto25V2.h5'
model.save(path_for_saved_model)
