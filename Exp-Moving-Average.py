import numpy as np
def ExpMA(data,period):
  weights=np.exp(np.linspace(-1.,0.,period))
  weights/=weights.sum()
  a=np.convolve(data,weights)[:len(values)]
  a[:period]=a[period]
  return a
  
