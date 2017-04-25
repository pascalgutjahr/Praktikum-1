import numpy as np

x = [84, 97, 123, 138, 155]
P =  5
xp = P * np.array(x)
print('Mittelwert:', np.mean(xp))
print('Std:', np.std(xp))

y =np.array( [162,154, 146, 117,206]) 
yp = P * np.array(y)
print('Mittelwert:', np.mean(yp))
print('Std:', np.std(yp))


z =np.array( [164, 158, 172, 184, 227])
zp = P * np.array(z)
a =zp-yp 
print('Differenz zy:',a) 
print('Mittelwert der Differenz:', np.mean(a))
print('Std der Differenz:', np.std(a))
