import os
import random

# Ruta principal que contiene las carpetas de letras (a, b, ..., z)
carpeta_principal = ''

# Extensión de los archivos a procesar (puedes cambiarla si no son .png)
extension = ".png"

# Cantidad maxima de imágenes que queremos por subcarpeta (may o min)
max_imagenes = 450

# Recorremos cada carpeta de letras (a, b, ..., z)
for letra in os.listdir(carpeta_principal):
    ruta_letra = os.path.join(carpeta_principal, letra)

    # Verificamos que sea una carpeta (la de la letra)
    if os.path.isdir(ruta_letra):
        # Recorremos las subcarpetas 'may' y 'min' dentro de cada letra
        for subcarpeta in ['may', 'min']:
            ruta_subcarpeta = os.path.join(ruta_letra, subcarpeta)

            # Verificamos que la subcarpeta 'may' o 'min' existe
            if os.path.exists(ruta_subcarpeta):
                # Listamos todas las imágenes .png en la subcarpeta
                imagenes = [f for f in os.listdir(ruta_subcarpeta) if f.endswith(extension)]
                
                # Si hay más imágenes de las necesarias, eliminamos al azar
                if len(imagenes) > max_imagenes:
                    exceso = len(imagenes) - max_imagenes
                    # Elegiendo imagenes al azar
                    imagenes_a_eliminar = random.sample(imagenes, exceso)
                    
                    # Eliminamos las imágenes seleccionadas
                    for imagen in imagenes_a_eliminar:
                        ruta_imagen = os.path.join(ruta_subcarpeta, imagen)
                        os.remove(ruta_imagen)
                        print(f'Eliminada: {ruta_imagen}')

                else:
                    print(f'La carpeta {subcarpeta} en {letra} tiene {len(imagenes)} imágenes, no se necesita eliminar.')

print("Proceso completado.")
