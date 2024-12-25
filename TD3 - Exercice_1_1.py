# Libraries
from matplotlib import pyplot as plt
import cv2

# We read our image
img = cv2.imread('./images/01_stego.png', cv2.IMREAD_GRAYSCALE)


# function
def binary_to_ascii(binary_string):
    binary = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    ascii_characters = [chr(int(chunk, 2)) for chunk in binary]
    decoded_string = ''.join(ascii_characters)
    return decoded_string


# We use a "for" loop to change every pixel
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if img[i, j] % 2 == 0:
            img[i, j] = 0
        else:
            img[i, j] = 1

stg = ""
for i in range(0, 3):
    for j in range(0, img.shape[0]):
        stg += str(img[i, j])

print(binary_to_ascii(stg))


