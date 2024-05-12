import numpy as np 
import matplotlib.pyplot as plt 

X_data = np.random.random(1000)*100
Y_data = np.random.random(1000)*100

#Scatter Plot 

plt.scatter(X_data, Y_data, c='blue', marker='*', s=150, alpha=0.3 )
plt.show()
