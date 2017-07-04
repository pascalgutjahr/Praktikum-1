import numpy as np

h = 6.625e-34
e_0 = 1.6e-19
m_0 = 9.11e-31
k = 1.38e-23
# e_0phi = -np.log(j*h**3 / (4*np.pi*e_0*m_0*k*T**2))

f = 0.35e-4
eta = 0.28
sigma = 5.7e-8
N_WL = 1
I_f = np.array([1.8,1.9,2,2.2,2.4])
U_f = np.array([3.9,4,4.2,5,6])

T = (((I_f*U_f)-N_WL)/(f*eta*sigma))**(1/4)

print(T)

I_s = np.array([10e-9,30e-9,70e-9,280e-9,1370e-9])
eps_0 = 8.85418e-12
Phi = - np.log((I_s*h**3)/(4*np.pi*e_0*m_0*k**2*T**2))*(k*T)/(e_0) / e_0
W = Phi * e_0
print(W)
