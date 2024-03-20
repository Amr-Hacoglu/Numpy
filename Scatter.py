import numpy as np
import matplotlib.pyplot as plt

#Scatter Chart
X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

plt.scatter(X_data,Y_data)
plt.grid(True)
plt.show()