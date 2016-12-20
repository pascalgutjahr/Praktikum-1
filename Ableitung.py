from sympy import *
import numpy as np
import scipy as sp
import math

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
f = 1/0.14*(z)*1/y*x
DelX = f.diff(x)
DelY = f.diff(y)
DelZ = f.diff(z)
print('Ableitung nach x =', DelX)
print('Ableitung nach y =', DelY)
print('Ableitung nach z =', DelZ)
