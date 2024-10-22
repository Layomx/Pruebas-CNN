import os
import random
import shutil

splitsize = .85
categories = []

source_folder = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/Dataset'
folders = os.listdir(source_folder)
print(folders)

for subfolder in folders:
    if os.path.isdir(source_folder + '/' + subfolder):
        categories.append(subfolder)

categories.sort()
print(categories)

# Creando una carpeta destino
target_folder = 'C:/Users/drake/OneDrive/Documentos/Universidad/6) Tercer Año, Segundo Semestre/Hackaton/Dataset/Set-Original/dataset_for_model'
existDataSetPath = os.path.exists(target_folder)
if existDataSetPath == False:
    os.mkdir(target_folder)
    
# Creando una función para separar los datos de entrenamiento y validación
def split_data(SOURCE, TRAINING, VALIDATION, SPLIT_SIZE):
    files = []

    # Recorriendo las subcarpetas de mayúsculas y minúsculas
    for case_folder in ['may', 'min']:  # Definición de las subcarpetas
        case_folder_path = os.path.join(SOURCE, case_folder)  # Ruta completa de la subcarpeta

        if os.path.isdir(case_folder_path):  # Verificando que sea una carpeta
            # Lista todos los archivos en la subcarpeta
            for filename in os.listdir(case_folder_path):
                file_path = os.path.join(case_folder_path, filename)  # Ruta completa del archivo
                print(file_path)

                if os.path.getsize(file_path) > 0:  # Verifica que el archivo no esté vacío o sea invalido
                    files.append(file_path)
                else:
                    print(filename + ' is 0 length, ignore it ....')

    print(f'Total valid files: {len(files)}')

    # Calcula el número de archivos para entrenamiento
    training_length = int(len(files) * SPLIT_SIZE)
    shuffle_set = random.sample(files, len(files))  # Mezclando  aleatoriamente los archivos
    training_set = shuffle_set[:training_length]  # Seleccionando el conjunto de entrenamiento
    valid_set = shuffle_set[training_length:]  # Seleccionando el conjunto de validación

    # Copiando las imágenes de entrenamiento
    for file_path in training_set:
        # Determina la subcarpeta correspondiente (may o min)
        case_folder = 'may' if 'may' in file_path else 'min'
        destination = os.path.join(TRAINING, case_folder, os.path.basename(file_path))  # Destino del archivo
        os.makedirs(os.path.dirname(destination), exist_ok=True)  # Crea la carpeta destino si no existe
        shutil.copyfile(file_path, destination)  # Copia el archivo
        print(f'Copied to training: {destination}')

    # Copiando las imágenes de validación
    for file_path in valid_set:
        # Determina la subcarpeta correspondiente (may o min)
        case_folder = 'may' if 'may' in file_path else 'min'
        destination = os.path.join(VALIDATION, case_folder, os.path.basename(file_path))  # Destino del archivo
        os.makedirs(os.path.dirname(destination), exist_ok=True)  # Crea la carpeta destino si no existe
        shutil.copyfile(file_path, destination)  # Copia el archivo
        print(f'Copied to validation: {destination}')

# Definiciones de rutas y creación de carpetas destino
target_folder = r'C:\Users\drake\OneDrive\Documentos\Universidad\6) Tercer Año, Segundo Semestre\Hackaton\Dataset\Set-Original\dataset_for_model'
train_path = os.path.join(target_folder, 'train')
validate_path = os.path.join(target_folder, 'validate')

# Creando las carpetas destino
if not os.path.exists(train_path):
    os.mkdir(train_path)
if not os.path.exists(validate_path):
    os.mkdir(validate_path)

# Lista de las carpetas de letras
categories = ['a', 'b', 'c', 'd' , 'e' , 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n_', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # Agrega las letras que necesites

# Ejecutando la función para cada carpeta de letra
for category in categories:
    # Crear las carpetas para la letra en entrenamiento y validación
    train_dest_path = os.path.join(train_path, category)
    validate_dest_path = os.path.join(validate_path, category)

    if not os.path.exists(train_dest_path):
        os.mkdir(train_dest_path)
    if not os.path.exists(validate_dest_path):
        os.mkdir(validate_dest_path)

    source_path = os.path.join(r'C:\Users\drake\OneDrive\Documentos\Universidad\6) Tercer Año, Segundo Semestre\Hackaton\Dataset\Set-Original\Dataset', category)

    print(f'Copying from: {source_path} to: {train_dest_path} and {validate_dest_path}')

    # Llamando a la función de separación de datos, pasándole las rutas correctas
    split_data(source_path, train_dest_path, validate_dest_path, 0.85)  # Ajusta el SPLIT_SIZE si es necesario
