import numpy as np


cW = 1464
cL = 331
cA = 2730 

t_oben = np.array([17.7, 15.3, 46, 40.7, 35.3, 29.8, 24, 18.2, 12.4, 6.7, 42])
t_oben = np.array(t_oben)*(10**(-6))
t_unten = np.array([45, 48, 11.3, 17.3, 23.6, 29.9, 35.6, 41.3, 47.1, 53.5, 12.7])
t_unten = np.array(t_unten)*(10**(-6))

# sW = 0.5 * cW * np.array(t)
# sL = 0.5 * cL * t*
sA_oben = 0.5 * cA * np.array(t_oben)
sA_unten = 0.5 * cA * np.array(t_unten)

S = 0.5 * cA * 60*10**(-6)
D_A = S - sA_oben - sA_unten
print('Strecke Acryl von oben A-Scan:', sA_oben)
print('Streche Acryl von unten A-Scan:',sA_unten)
print('Durchmesser:', D_A)


t_obenB = np.array([15.3,14.2,45.7,40.3,35.0,29.5,23.7,17.9,12.2,6.6,41.9])
t_obenB = np.array(t_obenB)*(10**(-6))
t_untenB = np.array([45.2,46.2,11.1,17,23.1,29.5,35.2,41.1,47,0,12.4])
t_untenB = np.array(t_untenB)*(10**(-6))
sA_obenB = 0.5 * cA * np.array(t_obenB)
sA_untenB = 0.5 * cA * np.array(t_untenB)
S = 0.5 * cA * 60*10**(-6)
D_B = S - sA_obenB - sA_untenB
print('Strecke Acryl von oben B-Scan:', sA_obenB)
print('Streche Acryl von unten B-Scan:',sA_untenB)
print('Durchmesser:', D_B)

t_o = np.array([14.6,13.4])
t_o = np.array(t_o)*10**(-6)
t_u = np.array([44,45])
t_u = np.array(t_u)*10**(-6)

S_oben = 0.5 * cA * np.array(t_o)
S_unten = 0.5 *cA * np.array(t_u)
D_Auf = S - S_oben - S_unten

print('Auflösungsvermögen von oben, A-Scan:', S_oben)
print('Auflösungsvermögen von unten, A-Scan:', S_unten)
print('Durchmesser:', D_Auf)

t_diastolisch = np.array([26.7, 29.2, 28.5, 29.2, 27.9, 29.2, 32, 31.5, 29.6, 31.2, 29, 28.4, 27.4, 26.3])*10**(-6)
S_diastolisch = 0.5 * cW * np.array(t_diastolisch)
S_systolisch = 0.5 * cW * 43.5*10**(-6)
h = S_systolisch - S_diastolisch
print('Strecke diastolisch:',S_diastolisch)
print('Strecke systolisch:',S_systolisch)
print('Höhen h des Herzens:', h)
a = 0.0285
V = np.pi * h / 6 * (3 * a**2 + h**2)
print('Volumen:',V)

V= V * 10**3
print('Volumen in Liter:',V)
# Vol = np.mean(V) + np.std(V)
print('gemitteltes Volumen in Liter:', np.mean(V),'±', np.std(V)) 

D_schieb = np.array([0.26, 0.17, 0.62, 0.52, 0.43, 0.33, 0.33, 0.24, 0.32, 0.25, 0.96])*10**(-2)
Fehler_A =( D_schieb - D_A ) / D_schieb
Fehler_B = (D_schieb - D_B ) / D_schieb
print('relative Abweichung Schieblehre/A-Scan:',Fehler_A)
print('relative Abweichung Schieblehre/B-Scan:',Fehler_B)
