import matplotlib.pyplot as plt
import numpy as np

thetas = np.linspace(0,2,10)
x = np.linspace(0,5,200)
fig,ax = plt.subplots()
for theta in thetas:
	fx = np.cos(np.pi * theta * x)*np.exp(-x)
	ax.plot(x,fx,linewidth =1, alpha =0.6)
plt.show()