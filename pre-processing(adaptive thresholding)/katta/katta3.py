import cv2
import matplotlib.pyplot as plt


def main(filename):
    #   path = "D:\\Youtube Code\\Python\\Python OpenCV3\\Python-OpenCV3\\Dataset\\"
    #   imgpath1 =  path + ""

    path = "test/" + filename
    #    print(path)
    #    image = Image.open(path)
    img = cv2.imread(path, 0)

    #    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    block_size = 33
    constant = 2
    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)

    output = [img, th1, th2]

    titles = ['Original', 'Mean Adaptive', 'Gaussian Adaptive']

    for i in range(3):
        plt.subplot(1, 3, i + 1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        cv2.imwrite('test_cleaned/'+titles[i]+'_'+filename,output[i])

    plt.show()
