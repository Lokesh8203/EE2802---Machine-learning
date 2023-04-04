import matplotlib.pyplot as plt
import numpy as np
import math

# Define the vertices of the rectangle
x = np.array([0, 45, 45, 0, 0])
y = np.array([0, 0, 24, 24, 0])

# Plot the rectangle
plt.plot(x, y, 'r-')
plt.axis('equal')
plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/12.6.3.18/figs/rectangle1.png')

#Add dotted square on 4 corners of the rectangle, with length 5
x = np.array([0, 5, 5, 0, 0])
y = np.array([0, 0, 5, 5, 0])

# Plot the square
plt.plot(x, y, 'b--')
plt.axis('equal')

x = np.array([40, 45, 45, 40, 40])
y = np.array([0, 0, 5, 5, 0])

# Plot the square
plt.plot(x, y, 'b--')
plt.axis('equal')

x = np.array([40, 45, 45, 40, 40])
y = np.array([19, 19, 24, 24, 19])

# Plot the square
plt.plot(x, y, 'b--')
plt.axis('equal')

x = np.array([0, 5, 5, 0, 0])
y = np.array([19, 19, 24, 24, 19])

# Plot the square
plt.plot(x, y, 'b--')
plt.axis('equal')
plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/12.6.3.18/figs/rectangle2.png')
plt.close()

def func(x):
    return 4*(x**3) - 138*(x**2) + 1080*x  # f(x)

#Gradient descent
def func_derivative(x):
    return 12*(x**2) - 276*x + 1080  # f'(x)

#Plot the graph of fucn
x = np.linspace(-1, 13, 100)
y = func(x)
plt.plot(x,y,'r-')
plt.xlabel('$x-Axis$')
plt.ylabel('$y-Axis$')
plt.title('Plot of Function')
plt.xlim([-1, 13])
plt.grid()
plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/12.6.3.18/figs/plot.png')