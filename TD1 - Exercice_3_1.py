# Libraries
import matplotlib.pyplot as plt
import cv2

# We read our image
img = cv2.imread('Images/TD1/lena.jpg')

# We use a "for" loop to change every pixel
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        img[i, j] = (0.0721 * img[i, j][0] + 0.7154 * img[i, j][1] + 0.2125 * img[i, j][2])

# We show the image to be sure everything's ok
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.title('my picture rgb')
plt.show()

# We create the image in the file Images.
cv2.imwrite('Images/modifiees/lena_grey.jpg', img)
