# Libraries
import matplotlib.pyplot as plt
import cv2
import numpy as np


def erosion(image_path, kernel_size=3):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    rows, cols = binary_image.shape
    eroded_image = np.zeros_like(binary_image)

    for i in range(rows):
        for j in range(cols):
            if binary_image[i, j] == 255:
                for m in range(-kernel_size // 2, kernel_size // 2 + 1):
                    for n in range(-kernel_size // 2, kernel_size // 2 + 1):
                        if 0 <= i + m < rows and 0 <= j + n < cols:
                            eroded_image[i + m, j + n] = 255
    return eroded_image


def dilatation(image_path, kernel_size=3):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    rows, cols = binary_image.shape
    dilated_image = np.zeros_like(binary_image)

    for i in range(rows):
        for j in range(cols):
            dilated_image[i, j] = 0
            for m in range(-kernel_size // 2, kernel_size // 2 + 1):
                for n in range(-kernel_size // 2, kernel_size // 2 + 1):
                    if 0 <= i + m < rows and 0 <= j + n < cols:
                        if binary_image[i + m, j + n] != 255:
                            break
                else:
                    continue
                break
            else:
                dilated_image[i, j] = 255

    return dilated_image


# We create the image in the file Images.
erode_image = erosion("Images/modifiees/TD2/limit_image.jpg")
cv2.imwrite('Images/modifiees/TD2/erode_image.jpg', erode_image)

opening_image = dilatation("Images/modifiees/TD2/erode_image.jpg")
cv2.imwrite('Images/modifiees/TD2/opening_image.jpg', opening_image)
