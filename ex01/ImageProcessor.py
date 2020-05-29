class ImageProcessor:
     def __init__(self, data=None, shape=None):
        self.data = data
        self.shape = shape
        
    def __str__(self):
        s = '['
        if self.shape[0] < self.data.size:
            for i, val in enumerate(self.data):
                s += '['
                for j, key in enumerate(val):
                    if self.data.dtype == 'int64' or self.data.dtype == 'float64':
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