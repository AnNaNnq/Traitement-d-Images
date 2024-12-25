# Libraries
import matplotlib.pyplot as plt
import cv2

# We read our image
gray = cv2.imread('Images/TD1/lena.jpg', cv2.IMREAD_GRAYSCALE)

# We use a "for" loop to change every pixel
for i in range(0, gray.shape[0]):
    for j in range(0, gray.shape[1]):
        gray[i, j] = 255 - gray[i, j]

# We show the image to be sure everything's ok
plt.imshow(gray, cmap='gray', vmin=0, vmax=255)
plt.title('Gray using imread function')
plt.show()

# We create the image in the file Images.
cv2.imwrite('Images/modifiees/TD1/lena_inverse.jpg', gray)
