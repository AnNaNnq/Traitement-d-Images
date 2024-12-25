# Libraries
import matplotlib.pyplot as plt
import cv2
import numpy as np

# We read our image
img = cv2.imread('Images/TD1/lena.jpg')

blue_channel, green_channel, red_channel = cv2.split(img)
green_image = np.zeros_like(img)
green_image[:, :, 1] = green_channel

blue_image = np.zeros_like(img)
blue_image[:, :, 0] = blue_channel

red_image = np.zeros_like(img)
red_image[:, :, 2] = red_channel

green_gray_image = cv2.cvtColor(green_image, cv2.COLOR_BGR2GRAY)
blue_gray_image = cv2.cvtColor(blue_image, cv2.COLOR_BGR2GRAY)
red_gray_image = cv2.cvtColor(red_image, cv2.COLOR_BGR2GRAY)


# We create the image in the file Images.
cv2.imwrite('Images/modifiees/lena_green.jpg', green_image)
cv2.imwrite('Images/modifiees/lena_red.jpg', red_image)
cv2.imwrite('Images/modifiees/lena_blue.jpg', blue_image)

cv2.imwrite('Images/modifiees/lena_green_gray.jpg', green_gray_image)
cv2.imwrite('Images/modifiees/lena_red_gray.jpg', red_gray_image)
cv2.imwrite('Images/modifiees/lena_blue_gray.jpg', blue_gray_image)


