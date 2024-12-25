# Libraries
from matplotlib import pyplot as plt
import cv2

def tatouage(image_path, message_binaire, positions_a_tatouer):
    image = cv2.imread(image_path)

    # Convertir le message binaire en une liste d'entiers (0 ou 255)
    tatouage_data = [0 if bit == '0' else 255 for bit in message_binaire]

    # Copier l'image pour éviter de modifier l'originale
    image_tatouee = image.copy()

    # Tatouer le message binaire sur l'image
    for position, tatouage_bit in zip(positions_a_tatouer, tatouage_data):
        x, y = position
        image_tatouee[y, x] = tatouage_bit  # Remplacer le pixel à la position spécifiée

    return image_tatouee

image_path = "./images/01_stego.png"
message_binaire = "01101000 01100101 01101100 01101100 01101111"
positions_a_tatouer = [(0, 0), (0, 0)]

image_tatouee = tatouage(image_path, message_binaire, positions_a_tatouer)

cv2.imshow("Image Tatouée", image_tatouee)
