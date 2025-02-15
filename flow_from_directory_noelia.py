# INTRODUCIDAS POR NOELIA
from typing import Generator, Iterator, Tuple
import numpy as np
import pandas as pd
from PIL import Image
from pathlib import Path
import xml.etree.ElementTree as ET
import cv2
from sklearn.model_selection import train_test_split
import os
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import cv2
import mediapipe as mp
import sklearn

DATA_DIR = Path("data")
IMG_SIZE = 224
NUM_POINTS = 10


def restaurar_imagen(image: "array", iMGWI, IMGHI):

    imagen_redimensionada = Image.fromarray(image)
    imagen_redimensionada.save("imagen_redimensionada.jpg")

    # Devolver la imagen a su tamaño original
    imagen_restaurada = imagen_redimensionada.resize((iMGWI, IMGHI))
    # imagen_restaurada = cv2.cvtColor(imagen_restaurada, cv2.COLOR_BGR2RGB)
    imagen_restaurada.save("imagen_restaurada.jpg")

    plt.imshow(imagen_restaurada)

    imagen_bgr = cv2.imread("imagen_restaurada.jpg")

    # Convertir de BGR a RGB usando NumPy
    imagen_rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)

    # Guardar la imagen convertida a RGB
    cv2.imwrite("imagen_restaurada.jpg", imagen_rgb)
    plt.imshow(imagen_rgb)
    return imagen_rgb  # se queda guardada en rgb


def crear_pares(lista_coordenadas):
    pares = []
    for i in range(0, len(lista_coordenadas), 2):
        if i + 1 < len(
            lista_coordenadas
        ):  # Asegurar que haya suficientes elementos para formar el par
            par = (lista_coordenadas[i], lista_coordenadas[i + 1])
            pares.append(par)

    return pares


# para hacer comprobaciones coge puntos e imagen original para dibujar


def compare_keypoints(path, y, yhat):

    imagen = cv2.imread(path)

    pares_yhat = crear_pares(yhat)
    pares_y = crear_pares(y)

    for x, y in pares_yhat:

        cv2.circle(
            img=imagen,
            center=(int(x), int(y)),
            radius=13,
            color=(0, 255, 0),
            thickness=-1,
        )

    for x, y in pares_y:

        cv2.circle(
            img=imagen,
            center=(int(x), int(y)),
            radius=8,
            color=(255, 50, 50),
            thickness=-1,
        )

    plt.imshow(imagen)
    plt.show()
    return imagen


def df_for_test(path, image_name_list):
    df2 = pd.DataFrame()
    input_images_path2 = path

    for image in image_name_list:

        image_path = input_images_path2 + "/" + image.replace("//", "/")
        imagen = cv2.imread(image_path)

        # path2.append(image_path)
        image_array = np.asarray(imagen)

        nueva_fila = pd.DataFrame({"nombre": image, "array": [image_array]})

        df2 = pd.concat([df2, nueva_fila], ignore_index=True)
    return df2
