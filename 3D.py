from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.tri import Triangulation

#Example-1
fig = plt.figure()
ax = plt.axes(projection='3d')


#Example-2
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining all 3 axis
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
 
# plotting
ax.plot3D(x, y, z, 'green')
ax.set_title('3D line plot geeks for geeks')
plt.show()

#Example-3
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# defining axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
c = x + y
ax.scatter(x, y, z, c = c)
 
# syntax for plotting
ax.set_title('3d Scatter plot geeks for geeks')
plt.show()

#Example-4
# defining surface and axes
x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 2 + y ** 3)
 
fig = plt.figure()
 
# syntax for 3-D plotting
ax = plt.axes(projection='3d')
 
# syntax for plotting
ax.plot_surface(x, y, z, cmap='viridis',\
                edgecolor='green')
ax.set_title('Surface plot geeks for geeks')
plt.show()

#Example-5
# function for z axis
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
 
# x and y axis
x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)
  
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
 
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_wireframe(X, Y, Z, color ='green')
ax.set_title('wireframe geeks for geeks')

#Example-6
def function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
 
 
x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)
 
X, Y = np.meshgrid(x, y)
Z = function(X, Y)
 
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')
 
ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.8)
 
ax.set_title('3D Contour Plot of function(x, y) =\
                sin(sqrt(x^2 + y^2))', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
 
plt.show()

#Example-7

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
 
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
 
tri = Triangulation(X.ravel(), Y.ravel())
 
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
 
ax.plot_trisurf(tri, Z.ravel(), cmap='cool', edgecolor='none', alpha=0.8)
 
ax.set_title('Surface Triangulation Plot of f(x, y) =\
                sin(sqrt(x^2 + y^2))', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
 
plt.show()

#Example-8
# Define the parameters of the Möbius strip
R = 2
 
# Define the Möbius strip surface
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(-1, 1, 100)
u, v = np.meshgrid(u, v)
x = (R + v*np.cos(u/2)) * np.cos(u)
y = (R + v*np.cos(u/2)) * np.sin(u)
z = v * np.sin(u/2)
 
# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
 
# Plot the Möbius strip surface
ax.plot_surface(x, y, z, alpha=0.5)
 
# Set plot properties
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Möbius Strip')
 
# Set the limits of the plot
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
 
# Show the plot
plt.show()