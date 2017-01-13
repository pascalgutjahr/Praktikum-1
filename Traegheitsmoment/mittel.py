import numpy as np

# Zylinder 1
T_z1 = [0.95,0.93,0.98,0.98,0.99]
print('Mittelwert T Zylinder 1:', np.mean(T_z1))
print('Standard T Zylinder 1:', np.std(T_z1))

T_z2 = [0.81,0.90,0.81,0.79,0.80]
print('Mittelwert T Zylinder 2:', np.mean(T_z2))
print('Standard T Zylinder 2:', np.std(T_z2))


# Maße der Puppe
a = [1.5,1.7,2.1,1.2,1.2]
x = [16.5,15.0,17.5,16,16.5]
print('Mittelwert d Bein:', np.mean(a))
print('Standard d Bein:', np.std(a))
print('Mittelwert l Bein:', np.mean(x))
print('Standard l Bein:', np.std(x))

b = [1.6,1.1,1.4,1.0,1.6]
y = [14.0,14.2,14.1,14.3,14.2]
print('Mittelwert d Arm:', np.mean(b))
print('Standard d Arm:', np.std(b))
print('Mittelwert l Arm:', np.mean(y))
print('Standard l Arm:', np.std(y))

c = [2.5,3.9,4.2,3.9,3.7]
z = [9.8,9.8,9.7,9.6,9.6]
print('Mittelwert d Rumpf:', np.mean(c))
print('Standard d Rumpf:', np.std(c))
print('Mittelwert d Rumpf:', np.mean(z))
print('Standard l Rumpf:', np.std(z))

d = [3.1,1.6,2.5,3.0,2.2]
w = [5.6,5.5,5.5,5.6,5.5]
print('Mittelwert d Kopf:', np.mean(d))
print('Standard d Kopf:', np.std(d))
print('Mittelwert l Kopf:', np.mean(w))
print('Standard l Kopf:', np.std(w))

# Stellung 1
T1 = [0.59,0.6,0.68,0.59,0.55,0.55]
print('Mittelwert T1:', np.mean(T1))
print('Standard T1:', np.std(T1))

# Stellung 2
T2 = [0.88,0.90,0.91,0.94,0.95,1]
print('Mittelwert T2:', np.mean(T2))
print('Standard T2:', np.std(T2))
