import numpy as np

def simpleMA(data,period):
    weights=np.repeat(1.0,period)/period
    sma=np.convolve(data,weights,"valid")
    return sma
