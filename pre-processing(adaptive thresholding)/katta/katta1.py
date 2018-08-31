import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import ImageEnhance, Image


def clean(filename):
    path = "test/" + filename
#    print(path)
    image = Image.open(path)

    enhancer = ImageEnhance.Sharpness(image)
    # for i in range(8):
    factor = 15
    enhancer.enhance(factor).save("check.png")

    # load original image

    img = cv2.imread('check.png')
    #img = cv2.medianBlur(img, 5)
    print ('type of img',type(img))

    fgbg = cv2.createBackgroundSubtractorMOG2()
    fgmask = fgbg.apply(img)
    img = fgmask

    # global thresholding
    ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#    print(ret1)
#   print(th1)


    cv2.imwrite("test_cleaned/" + filename, th1)
    katta = cv2.imread("test_cleaned/" + filename)
    cv2.imshow("Global", katta)
    cv2.waitKey(1)
