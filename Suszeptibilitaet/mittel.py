import numpy as np

x = np.array([84, 97, 123, 138, 155])
x * 5
print('Mittelwert:', np.mean(x))
print('Std:', np.std(x))

x = [84, 97, 123, 138, 155]
x = x * 5
print('Mittelwert:', np.mean(x))
print('Std:', np.std(x))
