import numpy as np
# erste Messung
Lampe = 145 # in cm
G = 125
ft = 5

g1 = np.array([110,100,95,90,80,75,65,60,55,50,40])
b1 = np.array([102,93,88.3,83.4,73.5,68.7,58.8,53.7,48.8,43.9,33.9])

g = G-g1
b = g1 - b1
print(g)
print(b)

f1 = 1/(1/b+1/g)
f1_mean = np.mean(f1)
f1_rel = (ft-f1_mean)/ft
print("Die Brennweite beträgt",f1_mean,"mm")
print("Relative Abweichung =",f1_rel,"%")

g2 = np.array([115,110,95,90,80,75,65,60,55,50,40])
b2 = np.array([100.8,99.2,86.1,81.6,71.7,66.9,57.1,52.1,47.2,42.1,32])

g3 = G-g2
b3 = g2 - b2

f2 = 1/(1/b3+1/g3)
f2_mean = np.mean(f2)
f2_rel = (ft-f2_mean)/ft
print("Die Brennweite beträgt",f2_mean,"cm")
print("Relative Abweichung =",f2_rel,"%")

f_bessel_theo = 10
Schirm = 45

b_bessel_1_1 = np.array([56.4,56.5,56.6,56.8,57.2,57.5,58.3,59.1,61.7,59.8])
b_bessel_2_1 = np.array([112.8,107.7,102.6,97.2,91.7,86.2,80.7,74.6,67.5,72.2])
g_bessel = np.array ([125,120,115,110,105,100,95,90,85,88])

b_bessel_1 = b_bessel_1_1 - Schirm
b_bessel_2 = b_bessel_2_1 - Schirm
# g_bessel_1 = b_bessel_2
g_bessel_1 = g_bessel - b_bessel_2
# g_bessel_2 = b_bessel_1
g_bessel_2 = g_bessel - b_bessel_1

e_bessel_1 = g_bessel_1 + b_bessel_1
e_bessel_2 = g_bessel_2 + b_bessel_2
d_bessel_1 = g_bessel_1 - b_bessel_1
d_bessel_2 = g_bessel_2 - b_bessel_2

# e_bessel = (e_bessel_1 + e_bessel_2)/2
# d_bessel = (d_bessel_1 + d_bessel_2)/2

f_bessel_1 = (e_bessel_1**2-d_bessel_1**2)/(4*e_bessel_1)
f_bessel_2 = (e_bessel_2**2-d_bessel_2**2)/(4*e_bessel_2)
f_bessel_mean_1 = np.mean(f_bessel_1)
f_bessel_mean_2 = np.mean(f_bessel_2)
f_bessel_rel_1 = (f_bessel_theo - f_bessel_mean_1) / f_bessel_theo
f_bessel_rel_2 = (f_bessel_theo - f_bessel_mean_2) / f_bessel_theo

print("Mittelwert der Bessel-Brennweite ",f_bessel_mean_1,"cm")
print("relative Abweichung",f_bessel_rel_1,"%")
# print(f_bessel_mean_2)
# print(f_bessel_rel_2)

g_farbe = 115
farbe_schirm = np.array([45,40,35,50,55])
b_rot_1_1 = np.array([56.9,51.8,46.6,62.4,67.5])
b_rot_2_1 = np.array([102.4,102.6,102.8,102.1,101.9])
b_blau_1_1 = np.array([56.8,51.6,46.3,61.9,67.1])
b_blau_2_1 = np.array([102.8,102.9,103,102.4,102.1])

g_rot_1 = g_farbe - b_rot_1_1
g_rot_2 = g_farbe - b_rot_2_1
b_rot_1 = b_rot_1_1 - farbe_schirm
b_rot_2 = b_rot_2_1 - farbe_schirm
g_blau_1 = g_farbe - b_blau_1_1
g_blau_2 = g_farbe - b_blau_2_1
b_blau_1 = b_blau_1_1 - farbe_schirm
b_blau_2 = b_blau_2_1 - farbe_schirm

e_rot_1 = g_rot_1 + b_rot_1
d_rot_1 = g_rot_1 - b_rot_1
e_blau_1 = g_blau_1 + b_blau_1
d_blau_1 = g_blau_1 - b_blau_1

f_rot_1 = (e_rot_1**2 - d_rot_1**2)/(4*e_rot_1)
f_blau_1 = (e_blau_1**2 - d_blau_1**2)/(4*e_blau_1)

f_rot_mean_1 = np.mean(f_rot_1)
f_blau_mean_1 = np.mean(f_blau_1)
f_rot_rel_1 = (f_bessel_theo - f_rot_mean_1)  / f_bessel_theo
f_blau_rel = (f_bessel_theo - f_blau_mean_1) / f_bessel_theo

print("Brennweite Rot", f_rot_mean_1,"cm")
print("relative Abweichung",f_rot_rel_1,"%")
print("Brennweite Blau", f_blau_mean_1, "cm")
print("relative Abweichung", f_blau_rel,"%")

Perl_L_V = 3
A = 3
h_Abbe = 3
f_Abbe = 10
Schirm_Abbe = 20

g_Abbe_1_1 = np.array([125,120,115,110,105,100,130,122.5,112.5,107.5]) # hier steht das L
b_Abbe_1_1 = np.array([107.4,104,96.6,90.5,83.8,74.9,112.7,105.2,93.8,86.5])
b_Abbe_2_1 = np.array([56,56.3,57.8,59.5,60,62.9,55,56.7,57.7,59.3])

b_Abbe_1 = b_Abbe_1_1 - Schirm_Abbe
b_Abbe_2 = b_Abbe_2_1 - Schirm_Abbe
g_Abbe_1 = g_Abbe_1_1 - b_Abbe_1_1
g_Abbe_2 = g_Abbe_1_1 - b_Abbe_2_1

V1 = b_Abbe_1 / g_Abbe_1
print(np.round(V1,2))
V2 = b_Abbe_2 / g_Abbe_2
print(np.round(V2,2))
#V_Abbe_g := 1+1/V
# V_Abbe_g = g_Abbe_1 / f_Abbe + h_Abbe
# print (g_Abbe_1)
# print (V_Abbe_g)
#V_Abbe_b := 1+V
# V_Abbe_b = b_Abbe_1 / f_Abbe + h_Abbe
# print (b_Abbe_1)
# print (V_Abbe_b)
