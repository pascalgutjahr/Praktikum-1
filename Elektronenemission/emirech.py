import numpy as np

h = 6.625e-34
e_0 = 1.6e-19
m_0 = 9.11e-31
k = 1.3e-23
e_0phi = -np.log(j*h**3 / (4*np.pi*e_0*m_0*k*T**2))
