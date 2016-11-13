class MaxSizeList(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.alist = []

    def push(self, value):
        self.alist.append(value)
        if len(self.alist) > self.maxsize:
            self.alist.pop(0)

    def get_list(self):
        return self.alist