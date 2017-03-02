from sympy import *
import numpy as np
import scipy as sp
import math

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
f = y**2*(x**2+y**2)**(0.5)
DelX = f.diff(x)
DelY = f.diff(y)
DelZ = f.diff(z)
print('Ableitung nach x =', DelX)
print('Ableitung nach y =', DelY)
print('Ableitung nach z =', DelZ)

