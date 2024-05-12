import numpy as np 
import matplotlib.pyplot as plt 

years = [2006  + x for x in range(16)]
weights = [80, 83, 85, 86, 87, 84, 81 , 79, 81, 80,84, 84, 87, 85, 89,87]

#line chart 

plt.plot(years, weights)
plt.show
