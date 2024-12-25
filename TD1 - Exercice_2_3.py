# Libraries
import matplotlib.pyplot as plt
import cv2
import numpy as np

# We read our image
img = cv2.imread('Images/TD1/circles_in_a_circle.jpg')

blue_channel, green_channel, red_channel = cv2.split(img)

adjusted_blue_channel = green_channel
adjusted_green_channel = red_channel
adjusted_red_channel = blue_channel

# Assembler les canaux avec le canal vert ajusté
merged_image = cv2.merge([adjusted_blue_channel, adjusted_green_channel, adjusted_red_channel])

# We create the image in the file Images.
cv2.imwrite('Images/modifiees/circle_in_a_circle_changed_colors.jpg', merged_image)
