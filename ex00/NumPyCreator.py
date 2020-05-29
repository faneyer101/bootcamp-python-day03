import numpy as np
import typing


class NumPyCreator:
    def __init__(self, data=[], shape=[]):
        self.data = data
        self.shape = shape

    def from_list(self, lst):
        if not isinstance(lst, list):
            print("ERROR Type. Need list")
            quit()
        self.data = np.array(lst)
        self.shape = np.shape(self.data)
        return self.data

    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple):
            print("ERROR Type. Need tuple")
            quit()
        self.data = np.array(tpl)
        self.shape = np.shape(self.data)
        return self.data

    def from_iterable(self, itr):
        if not isinstance(itr, typing.Iterable):
            print("ERROR Type. Need iterable")
            quit()
        start = itr[0]
        end = 0
        for key in itr:
            end += 1
        self.data = np.arange(start, end, 1)
        self.shape = np.shape(self.data)
        return self.data

    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple):
            print("ERROR Type. Need tuple")
            quit()
        self.data = np.full(shape, value)
        self.shape = np.shape(self.data)
        return self.data

    def random(self, shape):
        if not isinstance(shape, tuple):
            print("ERROR Type. Need tuple")
            quit()
        self.data = np.random.random_sample(shape)
        self.shape = np.shape(self.data)
        return self.data

    def identity(self, n):
        if not isinstance(n, int):
            print("ERROR Type. Need integer")
            quit()
        self.data = np.identity(n)
        self.shape = np.shape(self.data)

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

    def __repr__(self):
        return str(self.data)


npc = NumPyCreator()
npc.from_list([[1, 2, 3], [6, 3, 4]])
print("-----------\n", npc)
npc.from_tuple(("a", "b", "c"))
print("-----------\n", npc)
npc.from_iterable(range(5))
print("-----------\n", npc)
shape = (3, 4)
npc.from_shape(shape)
print("-----------\n", npc)
npc.random(shape)
print("-----------\n", npc)
npc.identity(10)
print("-----------\n", npc)
