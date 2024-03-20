import numpy as np
import matplotlib.pyplot as plt

x = np.array([80,25,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':'serif','color':'blue','size':'20'}
font2 = {'family':'serif','color':'darkred','size':'15'}

plt.title("Sports Watch Data",loc = 'left', fontdict=font1)

plt.xlabel("Average Pluse",fontdict=font2)
plt.ylabel("Calorie Burnage",fontdict=font2)

plt.plot(x,y)
plt.grid(axis = 'x')
plt.show()