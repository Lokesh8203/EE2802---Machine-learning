import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from math import *
import matplotlib.cm as cm
import matplotlib.legend as Legend

import sys   
sys.path.insert(0,'/home/lokesh/EE2802/EE2802-Machine_learning/CoordGeo')

#local imports
from line.funcs import *
from triangle.funcs import *
from params import *

def parab_gen(x, a):
    y = (x**2)/(4*a)
    return y

x = np.linspace(-50, 50, 200)
a = 20 #random value of A for representative figure
y = parab_gen(x, a)

O = np.array([0, 0])
A = np.array([-50, parab_gen(-50, a)])
B = np.array([50, parab_gen(50, a)])
C1 = np.array([[-50, -6]])
C = np.array([0, -6])

plt.plot(x,y,label='$Hyperbola$', color = 'blue')

#Labeling the coordinates
plot_coords = np.vstack((O,A,B,C, C1)).T
vert_labels = ['$O$','$A$','$B$','$C$', '$C1$']
for i, txt in enumerate(vert_labels):
    plt.scatter(plot_coords[0,i], plot_coords[1,i], s=15)
    plt.annotate(txt, # this is the text
                (plot_coords[0,i], plot_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,5), # distance from text to points (x,y)
                 fontsize=7,
                 ha='center') # horizontal alignment can be left, right or center

ground_lvl1 = np.array([-50, -6])
ground_lvl2 = np.array([50, -6])
ground = line_gen(ground_lvl1, ground_lvl2)

centre_pt1 = np.array([0, -10])
centre_pt2 = np.array([0, 35])
centre_line = line_gen(centre_pt1, centre_pt2)

plt.plot(ground[0,:],ground[1,:] ,label = 'ground')
plt.plot(centre_line[0,:], centre_line[1, :], 'g--' )

plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/11.11.5.3/figs/1.png')
plt.clf()

V = np.array([[1, 0], [0, 0]])
u = np.array([0, -625/12])
f = 0
e = 1 #parabola
a = np.linalg.norm(u)/2

w,v = np.linalg.eig(V)
#w eigenvalues
#v eigenvectors

o = np.array([0, 0])
A = np.array([[-50, parab_gen(-50, a)]])
B = np.array([[50, parab_gen(50, a)]])
C = np.array([[0, -6]])
C1 = np.array([[-50, -6]])
D = np.array([[18, parab_gen(18, a)]])

x = np.arange(-50,50,1)
y = parab_gen(x,a)

plt.plot(x,y,label='$Parabola$')
plt.grid()
plt.plot(ground[0,:],ground[1,:] ,label = 'ground')
plt.plot(centre_line[0,:], centre_line[1, :], 'g--' )

plot_coords = np.vstack((O,A,B,C,D, C1)).T
vert_labels = ['$O$','$A$','$B$','$C$', '$D$', '$C1$']
for i, txt in enumerate(vert_labels):
    plt.scatter(plot_coords[0,i], plot_coords[1,i], s=15)
    plt.annotate(txt, # this is the text
                (plot_coords[0,i], plot_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,5), # distance from text to points (x,y)
                 fontsize=7,
                 ha='center') # horizontal alignment can be left, right or center

plt.savefig('/home/lokesh/EE2802/EE2802-Machine_learning/11.11.5.3/figs/parabola.png')