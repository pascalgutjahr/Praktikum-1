from sympy import *
import numpy as np
import scipy as sp
import math

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
f = (x**2 * y)/z
DelX = f.diff(x)
DelY = f.diff(y)
DelZ = f.diff(z)
print('Ableitung nach x =', DelX)
print('Ableitung nach y =', DelY)
print('Ableitung nach z =', DelZ)
