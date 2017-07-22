import numpy as np

a = np.array([30,15,60,90])
a = a * 2 * np.pi / 360
print('Winkel in Bogenmaß:', a)

alpha = 1.57079633- np.arcsin(np.sin(a) * 1800 / 2700)
print ('Winkel alpha in Bogenmaß:', alpha)

nu30 = np.array([85,122,134,171,256,171,244,305,366,598,317,513,676,891,1355])
v30 = nu30 * 1800 / (2 * 2 * 10**6 * np.cos(1.231))
print('Geschwindigkeiten bei 30 grad:', v30)

nu15 = np.array([73,85,98,122,171,110,159,208,220,330,171,293,330,415,647])
v15 = nu15 * 1800 / ( 2 * 2* 10**6 * np.cos(1.397))
print('Geschwindigkeiten bei 15 grad:', v15)

nu60 = np.array([143,195,232,281,452,269,464,574,720,1062,476,793,964,1233,1941])
v60 = nu60 * 1800 / (2 * 2 * 10**6 * np.cos(0.955))
print('Geschwindigkeiten bei 60 grad:', v60)

