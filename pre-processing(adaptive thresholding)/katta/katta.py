import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('extras/degrad1.jpg',0)
img = cv2.medianBlur(img,5)
blockSize = 11
constant = 2

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret1,th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
ret2,th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(3):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    cv2.imwrite('test_cleaned/' + titles[i] + '_' + filename, output[i])
plt.show()

