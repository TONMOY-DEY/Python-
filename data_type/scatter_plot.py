import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(100)
y=2*x+1+0.1*np.random.randn(100)

plt.scatter(x,y)
plt.title('Scatter plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()