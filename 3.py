import numpy as np
import matplotlib.pyplot as plt
import math
x=np.arange(-10,10.01,0.01)
def y(x):
    a=1+np.tan(1/(1+(np.sin(x))**2))
    b=(x**2+1)*np.exp(-(abs(x)/10))
    return np.log(b)/np.log(a)

plt.plot(x,y(x))
plt.show()
