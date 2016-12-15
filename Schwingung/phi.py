import numpy as np

R = 271.6
C = 5.015 /(10**9)
L = 3.53 /(10**3)

om = np.sqrt((1)/(L*C) - ((R**2)/(2*L**2)))
om1 = R/(2*L) + np.sqrt(((R**2)/(4*L**2))+((1)/(L*C)))
om2 = -(R/(2*L)) + np.sqrt(((R**2)/(4*L**2))+((1)/(L*C)))



v, U = np.genfromtxt('tables/phase.txt', unpack=True, skip_header=2)
U_0 = 6.7

print(U/U_0)
print(om/(2*np.pi))
print(om1/(2*np.pi))
print(om2/(2*np.pi))
