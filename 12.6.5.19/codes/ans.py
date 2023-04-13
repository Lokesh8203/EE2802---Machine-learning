import numpy
import matplotlib.pyplot as plt
import cvxpy as cp

#plot a cirlce with a rectangle inscribed in it
#name the vertices of rectangle as A,B,C,D
#mention the coordinates of A - cos theta and sin theta, B - -cos theta and sin theta, C - -cos theta and -sin theta, D - cos theta and -sin theta

#plot the circle
theta = numpy.linspace(0,2*numpy.pi,100)
x = numpy.cos(theta)
y = numpy.sin(theta)
plt.plot(x,y)

theta = numpy.pi/6

#plot the rectangle
plt.plot([numpy.cos(theta),-numpy.cos(theta),-numpy.cos(theta),numpy.cos(theta),numpy.cos(theta)],[numpy.sin(theta),numpy.sin(theta),-numpy.sin(theta),-numpy.sin(theta),numpy.sin(theta)])

#Make all rectangle lines dotted
#plot the line joining A and B
plt.plot([numpy.cos(theta),-numpy.cos(theta)],[numpy.sin(theta),numpy.sin(theta)], linestyle='dotted')

#plot the line joining B and C
plt.plot([-numpy.cos(theta),-numpy.cos(theta)],[-numpy.sin(theta),numpy.sin(theta)], linestyle='dotted')

#plot the line joining C and D
plt.plot([-numpy.cos(theta),numpy.cos(theta)],[-numpy.sin(theta),-numpy.sin(theta)], linestyle='dotted')

#plot the line joining A and D
plt.plot([numpy.cos(theta),numpy.cos(theta)],[numpy.sin(theta),-numpy.sin(theta)], linestyle='dotted')

plt.axis('equal')
plt.xlabel('$x-Axis$')
plt.ylabel('$y-Axis$')
plt.grid()

#label the vertices wiht theta notations with legend
#this text should not overlap with figure

plt.text(numpy.cos(theta),numpy.sin(theta),'$A$')
plt.text(-numpy.cos(theta),numpy.sin(theta),'$B$')
plt.text(-numpy.cos(theta),-numpy.sin(theta),'$C$')
plt.text(numpy.cos(theta),-numpy.sin(theta),'$D$')

#show the plot
plt.savefig('12.6.5.19/figs/circle_rectangle.png')

x = cp.Variable()

#Cost function
f =  -16*x**4 + 16*x**2
obj = cp.Maximize(f)

#Constraints
constraints = [x >= 0, x <= 1]

#solution
prob  = cp.Problem(obj, constraints)
solution = prob.solve()

print("Optimal value:", solution)
print("Optimal var:", x.value)

