import os
import katta1
import katta3
import cv2

for filename in os.listdir("test"):
    katta1.clean(filename)
    katta3.main(filename)


cv2.destroyAllWindows()