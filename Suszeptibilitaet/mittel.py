import numpy as np

x = [84, 97, 123, 138, 155]
P =  5
xp = P * np.array(x)
print('Mittelwert:', np.mean(xp))
print('Std:', np.std(xp))

x = [84, 97, 123, 138, 155]
x = x * 5
print('Mittelwert:', np.mean(x))
print('Std:', np.std(x))
