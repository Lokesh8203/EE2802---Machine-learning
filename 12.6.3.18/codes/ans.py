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
    return 4*(x**3) - 138*(x**2) + 1080*x # f(x)

def func_derivative(x):
    return -12*(x**2) + 276*x - 1080  # f'(x)

lamda_n = 0 # Start value at lamda_n= 0
alpha = 0.001 # step size multiplier
precision = 0.0000001
previous_step_size = 1 
max_count = 10000000 # maximum number of iterations
count = 0 # counter

while (previous_step_size > precision) & (count < max_count):
    lamda_n_minus1 = lamda_n
    lamda_n -= alpha * func_derivative(lamda_n_minus1)
    previous_step_size = abs(lamda_n - lamda_n_minus1)
    count+=1

print("The minimum value of function is at", lamda_n)

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