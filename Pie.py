import numpy as np
import matplotlib.pyplot as plt

newpie = np.array([35,25,25,15])
mylables = ["Apples","Bannanes","Cherries","Dates"]
mycolors = ["Black","Hotpink","b","#4CAD50"]
myexplode = [0.2,0,0,0]

plt.pie(newpie,labels=mylables,startangle= -90,explode=myexplode,shadow=True,colors=mycolors)
plt.legend()
plt.show()



# Colors
# 'r' - Red
# 'g' - Green
# 'b' - Blue
# 'c' - Cyan
# 'm' - Magenta
# 'y' - Yellow
# 'k' - Black
# 'w' - White