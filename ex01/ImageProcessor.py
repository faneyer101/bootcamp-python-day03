import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np


class ImageProcessor:
    def __init__(self, data=[], shape=[]):
        self.data = data
        self.shape = shape

    def load(self, name_img):
        try:
            self.data = mpimg.imread(name_img)
            self.shape = np.shape(self.data)
            print("Loading image of dimensions {} x {}"
                  .format(self.shape[0], self.shape[1]))
        except ValueError:
            print("Image no found")
            quit()
        return self.data

    def display(self, tab_pixel):
        try:
            try:
                mpimg.imsave("ImageWork.png", tab_pixel)
                img = pyplot.imread("ImageWork.png")
                pyplot.imshow(img)
                pyplot.show()
            except ValueError:
                print("Bad tab pixel")
                quit()
        except TypeError:
            print("Bad Type. Need Array")
            quit()

    def __str__(self):
        s = '['
        if self.shape[0] < self.data.size:
            for i, val in enumerate(self.data):
                s += '['
                type_s = self.data.dtype
                for j, key in enumerate(val):
                    if type_s == 'int64' or type_s == 'float64':
                        if j == self.shape[1] - 1:
                            s += "{}".format(key)
                        else:
                            s += "{}, ".format(key)
                    elif self.data.dtype == '<U1':
                        if j == self.shape[1] - 1:
                            s += "'{}'".format(key)
                        else:
                            s += "'{}',".format(key)
                if i != self.shape[0] - 1:
                    s += "],\n"
                else:
                    s += ']'
        else:
            for i, val in enumerate(self.data):
                if self.data.dtype == 'int64' or self.data.dtype == 'float64':
                    if i == self.shape[0] - 1:
                        s += "{}".format(val)
                    else:
                        s += "{}, ".format(val)
                elif self.data.dtype == '<U1':
                    if i == self.shape[0] - 1:
                        s += "'{}'".format(val)
                    else:
                        s += "'{}',".format(val)
        s += ']'
        return s


img = ImageProcessor()
arr = img.load("42AI.png")
print(arr)
print(arr.size)
img.display(arr)
