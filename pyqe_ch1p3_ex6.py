# from numpy.random import uniform
import numpy as np
import matplotlib.pyplot as plt

def delta_x (alpha =0):
	epsilon = np.random.randn(199)
	xt = [0]
	for i in range(199):
		xt.append(xt[i]*alpha+epsilon[i])

	legend = '$\\alpha$ = '+ str(round(alpha,2))
	plt.plot(xt, label= legend)
	plt.legend()

delta_x()
delta_x(0.8)
delta_x(0.98)

plt.show()