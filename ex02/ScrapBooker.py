import numpy as np


class ScrapBooker:
    def __init__(self, data=[], shape=()):
        self.data = data
        self.shape = shape

    def crop(self, array, dimensions, position=(0, 0)):
        try:
            size = np.shape(array)
            if dimensions[0] <= 0 or dimensions[1] <= 0:
                print("ERROR dimension need greater than 0")
                quit()
            if size[0] < dimensions[0] or size[1] < dimensions[1]:
                print("ERROR dimension too large for image")
                quit()
            for line in range(dimensions[0]):
                self.data.append(array[line + position[0]]
                                      [position[1]:dimensions[1] +
                                       position[1]])
                self.shape = np.shape(self.data)
            return self.data
        except IndexError:
            print("ERROR")
            quit()

    def thin(self, array, n, axis):
        self.data = []
        i = 1
        for line in array:
            if axis == 1:
                if i != n:
                    print(i)
                    self.data.append(line)
                else:
                    i = 0
                i += 1
            else:
                tmp = []
                j = 1
                for c in line:
                    if j != n:
                        tmp.append(c)
                    else:
                        j = 0
                    j += 1
                self.data.append(tmp)
        self.shape = np.shape(self.data)
        return self.data

    def juxtapose(self, array, n, axis):
        self.data = array
        i = 0
        while i < n:
            self.data = np.concatenate((self.data, array), axis)
            i += 1
        self.shape = np.shape(self.data)
        return self.data

    def mosaic(self, array, dimensions):
        self.data = np.tile(array, dimensions)
        self.shape = np.shape(self.data)
        return self.data


test = ScrapBooker()
test_arr = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50],
            [11, 22, 33, 44, 55], [100, 200, 300, 400, 500],
            [111, 222, 333, 444, 555]]
test.crop(test_arr, (2, 2))
print(test_arr)
test_2 = ScrapBooker()
test_2.crop(test_arr, (5, 5), (0, 0))
test_2.thin(test_arr, 1, 0)
test_2.juxtapose(test_arr, 2, 1)
test_2.mosaic(test_arr, (3, 3))
print(test_2.data)
