import numpy as np

class ReLu:
    def __init__(self, x):
        self.mask = None
    
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx
