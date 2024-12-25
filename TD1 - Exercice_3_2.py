# Libraries
import matplotlib.pyplot as plt
import cv2

# We read our image
img = cv2.imread('Images/TD1/lena.jpg')
imgVert = cv2.imread('Images/TD1/lena.jpg')
imgBleu = cv2.imread('Images/TD1/lena.jpg')
imgRouge = cv2.imread('Images/TD1/lena.jpg')

# We use a "for" loop to change every pixel
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        imgVert[i, j] = (0.0721 * img[i, j][0] + 0.7154 * img[i, j][1] + 0.2125 * img[i, j][2])
        imgVert[i, j][0] = 0
        imgVert[i, j][2] = 0

        imgBleu[i, j] = (0.0721 * img[i, j][0] + 0.7154 * img[i, j][1] + 0.2125 * img[i, j][2])
        imgBleu[i, j][1] = 0
        imgBleu[i, j][2] = 0

        imgRouge[i, j] = (0.0721 * img[i, j][0] + 0.7154 * img[i, j][1] + 0.2125 * img[i, j][2])
        imgRouge[i, j][0] = 0
        imgRouge[i, j][1] = 0

# We create the image in the file Images.
cv2.imwrite('Images/modifiees/lena_green.jpg', imgVert)
cv2.imwrite('Images/modifiees/lena_blue.jpg', imgBleu)
cv2.imwrite('Images/modifiees/lena_red.jpg', imgRouge)
