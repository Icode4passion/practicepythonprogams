import matplotlib.pyplot as plt  
import numpy as numpy

fs = 100
f = 2

x = np.arange(fs)

y = [np.sin(2*np.pi*f * (i/fs) for i in np.arange(fs))]


plt.stem(x,y,"r")
plt.plot(x,y)