# Libraries
import matplotlib.pyplot as plt
import cv2


# We create the erosion function
def erosion(img, new_img):
    for i in range(0, img.shape[0] - 1):
        for j in range(0, img.shape[1] - 1):
            if img[i, j][0] == 0:
                if i == 0 and j != 0 and j != img.shape[1]:
                    if img[i, j - 1][0] == 255 or img[i + 1, j - 1][0] == 255 or img[i + 1, j][0] == 255 or \
                            img[i + 1, j + 1][0] == 255 or img[i, j + 1][0] == 255:
                        new_img[i, j] = [0, 0, 0]
                elif j == 0 and i != 0 and i != img.shape[0]:
                    if img[i - 1, j][0] == 255 or img[i + 1, j][0] == 255 or img[i - 1, j + 1][0] == 255 or \
                            img[i, j + 1][0] == 255 or img[i + 1, j + 1][0] == 255:
                        new_img[i, j] = [255, 255, 255]
                elif i == img.shape[0] and j != 0 and j != img.shape[1]:
                    if img[i - 1, j - 1][0] == 255 or img[i, j - 1][0] == 255 or img[i - 1, j][0] == 255 or \
                            img[i - 1, j + 1][0] == 255 or img[i, j + 1][0] == 255:
                        new_img[i, j] = [255, 255, 255]
                elif j == img.shape[1] and i != 0 and i != img.shape[0]:
                    if img[i - 1, j - 1][0] == 255 or img[i, j - 1][0] == 255 or img[i + 1, j - 1][0] == 255 or \
                            img[i - 1, j][0] == 255 or img[i + 1, j][0] == 255:
                        new_img[i, j] = [255, 255, 255]
                elif j == 0 and i == 0:
                    if img[i + 1, j][0] == 255 or img[i + 1, j + 1][0] == 255 or img[i, j + 1][0] == 255:
                        new_img[i, j] = [255, 255, 255]
                elif j == img.shape[1] and i == 0:
                    if img[i, j - 1][0] == 255 or img[i + 1, j - 1][0] == 255 or img[i + 1, j][0] == 255:
                        new_img[i, j] = [255, 255, 255]
                elif j == img.shape[1] and i == img.shape[0]:
                    if img[i - 1, j - 1][0] == 255 or img[i, j - 1][0] == 255 or img[i - 1, j][0] == 255:
                        new_img[i, j] = [255, 255, 255]
                elif j == 0 and i == img.shape[0]:
                    if img[i - 1, j][0] == 255 or img[i - 1, j + 1][0] == 255 or img[i, j + 1][0] == 255:
                        new_img[i, j] = [255, 255, 255]
                else:
                    if img[i, j - 1][0] == 255 or img[i, j + 1][0] == 255 or img[i - 1, j][0] == 255 or img[i + 1, j][
                        0] == 255 \
                            or img[i - 1, j - 1][0] == 255 or img[i + 1, j + 1][0] == 255 or img[i - 1, j + 1][0] == 255 \
                            or img[i + 1, j - 1][0] == 255:
                        new_img[i, j] = [255, 255, 255]
    return new_img


# We read our image
img = cv2.imread('Images/TD2/morph_1.pgm')
img2 = cv2.imread('Images/TD2/morph_1.pgm')

limit = 200
# We use a "for" loop to change every pixel
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        for k in range(3):
            if img[i, j][k] < limit:
                img[i, j][k] = 0
                img2[i, j][k] = 0
            else:
                img[i, j][k] = 255
                img2[i, j][k] = 255

erode_image = erosion(img, img2)

# We create the image in the file Images.
cv2.imwrite('Images/modifiees/TD2/limit_image.jpg', img)
cv2.imwrite('Images/modifiees/TD2/erode_image.jpg', erode_image)

