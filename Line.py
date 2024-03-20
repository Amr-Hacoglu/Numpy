import numpy as np
import matplotlib.pyplot as plt

#Line Chart
population = [123,243,456,690]
year = [1995,1996,1997,1998]

plt.plot(year,population,linestyle = 'dotted',linewidth='10')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

# 'solid' (default)	'-'	
# 'dotted'	':'	
# 'dashed'	'--'	
# 'dashdot'	'-.'	
# 'None'