from sympy import *
import numpy as np
import scipy as sp
import math

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
pi= Symbol('pi')
f = sin(x)*x

Fx = integrate(f, x)
Fy = integrate(f, y)
Fz = integrate(f, z)

print('Integral nach dx', Fx)
print('Integral nach dy', Fy)
print('Integral nach dz', Fz)
