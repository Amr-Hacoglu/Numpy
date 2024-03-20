import numpy as np
import matplotlib.pyplot as plt

#Normal Exmple
xpoints = np.array([3,8,1,10])
ypoints = np.array([2,7,4,3])

plt.plot(xpoints,ypoints,marker='o')
plt.show()

#Scatter Chart
X_data = np.random.random(50) * 100
Y_data = np.random.random(50) * 100

plt.scatter(X_data,Y_data)
plt.grid(True)
plt.show()


#Line Chart
population = [123,243,456,690]
year = [1995,1996,1997,1998]

plt.plot(year,population)
plt.grid(False)
plt.show()


#Histogram Chart 
age = [20,56,67,40,89,90,23,45,68,23,11,18]
plt.hist(age,bins=3)
plt.show()


#Bar Chart 
data = {'C':20,'C++':15,'Java':30,'Python':35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5))

plt.bar(courses,values,color='maroon',width=0.4)

plt.xlabel("Courses Offered")
plt.ylabel("No, Of students enrolled")
plt.title("students entrolled in different courses")
plt.show()

#Pie
newpie = np.array([35,25,25,15])

plt.pie(newpie)
plt.show()


#Label Example
x = np.array([80,25,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

font1 = {'family':'serif','color':'blue','size':'20'}
font2 = {'family':'serif','color':'darkred','size':'15'}

plt.title("Sports Watch Data",loc = 'left', fontdict=font1)

plt.xlabel("Average Pluse",fontdict=font2)
plt.title("Calorie Burnage",fontdict=font2)

plt.plot(x,y)
plt.show()

#Plot Example
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()


# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
				notch ='True', vert = 0)

colors = ['#0000FF', '#00FF00', 
		'#FFFF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
	patch.set_facecolor(color)

# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
	whisker.set(color ='#8B008B',
				linewidth = 1.5,
				linestyle =":")

# changing color and linewidth of
# caps
for cap in bp['caps']:
	cap.set(color ='#8B008B',
			linewidth = 2)

# changing color and linewidth of
# medians
for median in bp['medians']:
	median.set(color ='red',
			linewidth = 3)

# changing style of fliers
for flier in bp['fliers']:
	flier.set(marker ='D',
			color ='#e7298a',
			alpha = 0.5)
	
# x-axis labels
ax.set_yticklabels(['data_1', 'data_2', 
					'data_3', 'data_4'])

# Adding title 
plt.title("Customized box plot")

# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
	
# show plot
plt.show()