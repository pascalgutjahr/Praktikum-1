import numpy as np

x = 0.1e-3 # Strecke

U1 = 261
t_1auf = np.array([3.854, 3.769, 3.566]) / 5 # durch 5, damit auf 1 Kästchen normiert
t_1auf_mean = np.mean(t_1auf)
t_1auf_std = np.std(t_1auf)
v_1auf = x / t_1auf_mean # v = s / t

t_1ab = np.array([1.790, 1.472, 1.865]) / 5
t_1ab_mean = np.mean(t_1ab)
t_1ab_std = np.std(t_1ab)
v_1ab = x / t_1ab_mean

t_1 = np.array([1.706, 2.324, 2.446])
t_1_mean = np.mean(t_1)
t_1_std = np.std(t_1)
v_1 = x / t_1_mean
# nächste Messung

t_11auf = np.array([2.987, 3.094, 3.301]) / 5
t_11auf_mean = np.mean(t_11auf)
t_11auf_std = np.std(t_11auf)
v_11auf = x / t_11auf_mean

t_11ab = np.array([2.239, 2.513, 3.745]) / 5
t_11ab_mean = np.mean(t_11ab)
t_11ab_std = np.std(t_11ab)
v_11ab = x / t_11ab_mean

t_11 = np.array([3.244, 3.485, 5.292])
t_11_mean = np.mean(t_11)
t_11_std = np.std(t_11)
v_11 = x / t_11_mean


U2 = 271
t_2auf = np.array([6.242, 6.909, 6.275]) / 5
t_2auf_mean = np.mean(t_2auf)
t_2auf_std = np.std(t_2auf)
v_2auf = x / t_2auf_mean

t_2ab = np.array([3.949, 3.840, 4.113]) / 5
t_2ab_mean = np.mean(t_2ab)
t_2ab_std = np.std(t_2ab)
v_2ab = x / t_2ab_mean

t_2 = np.array([3.880, 3.633, 4.206])
t_2_mean = np.mean(t_2)
t_2_std = np.std(t_2)
v_2 = x / t_2_mean
# nächste Messung

t_22auf = np.array([2.529, 5.376, 4.454]) / 5
t_22auf_mean = np.mean(t_22auf)
t_22auf_std = np.std(t_22auf)
v_22auf = x / t_22auf_mean

t_22ab = np.array([2.929, 2.734, 3.650]) / 5
t_22ab_mean = np.mean(t_22ab)
t_22ab_std = np.std(t_22ab)
v_22ab = x / t_22ab_mean

t_22 = np.array([7.751, 5.010, 8.960])
t_22_mean = np.mean(t_22)
t_22_std = np.std(t_22)
v_22 = x / t_22_mean

U3 = 280
t_3auf = np.array([4.594, 4.679, 4.486]) / 5
t_3auf_mean = np.mean(t_3auf)
t_3auf_std = np.std(t_3auf)
v_3auf = x / t_3auf_mean

t_3ab = np.array([3.2698, 3.371, 2.604]) / 5
t_3ab_mean = np.mean(t_3ab)
t_3ab_std = np.std(t_3ab)
v_3ab = x / t_3ab_mean

t_3 = np.array([4.80, 4.54, 3.658])
t_3_mean = np.mean(t_3)
t_3_std = np.std(t_3)
v_3 = x / t_3_mean
# nächste Messung

t_33auf = np.array([2.576, 2.386, 2.287]) / 5
t_33auf_mean = np.mean(t_33auf)
t_33auf_std = np.std(t_33auf)
v_33auf = x / t_33auf_mean

t_33ab = np.array([2.454, 2.791, 2.611]) / 5
t_33ab_mean = np.mean(t_33ab)
t_33ab_std = np.std(t_33ab)
v_33ab = x / t_33ab_mean

t_33 = np.array([11.39, 8.549, 14.209])
t_33_mean = np.mean(t_33)
t_33_std = np.std(t_33)
v_33 = x / t_33_mean

U4 = 290
t_4auf = np.array([10.917, 10.739, 9.6]) / 5
t_4auf_mean = np.mean(t_4auf)
t_4auf_std = np.std(t_4auf)
v_4auf = x / t_4auf_mean

t_4ab = np.array([6.567, 6.332, 6.9]) / 5
t_4ab_mean = np.mean(t_4ab)
t_4ab_std = np.std(t_4ab)
v_4ab = x / t_4ab_mean

t_4 = np.array([6.899, 8.372, 8.964])
t_4_mean = np.mean(t_4)
t_4_std = np.std(t_4)
v_4 = x / t_4_mean
# nächste Messung

t_44auf = np.array([10.42, 11.383, 10.956]) / 5
t_44auf_mean = np.mean(t_44auf)
t_44auf_std = np.std(t_44auf)
v_44auf = x / t_44auf_mean

t_44ab = np.array([6.564, 6.098, 6.869]) / 5
t_44ab_mean = np.mean(t_44ab)
t_44ab_std = np.std(t_44ab)
v_44ab = x / t_44ab_mean

t_44 = np.array([6.098, 9.041, 5.195])
t_44_mean = np.mean(t_44)
t_44_std = np.std(t_44)
v_44 = x / t_44_mean

U5 = 301
t_5auf = np.array([7.467, 7.032, 6.702]) / 5
t_5auf_mean = np.mean(t_5auf)
t_5auf_std = np.std(t_5auf)
v_5auf = x / t_5auf_mean

t_5ab = np.array([3.711, 3.711, 3.858]) / 5
t_5ab_mean = np.mean(t_5ab)
t_5ab_std = np.std(t_5ab)
v_5ab = x / t_5ab_mean

t_5 = np.array([4.784, 2.987, 3.547])
t_5_mean = np.mean(t_5)
t_5_std = np.std(t_5)
v_5 = x / t_5_mean
# nächste Messung

t_55auf = np.array([8.078, 8.360, 8.220]) / 5
t_55auf_mean = np.mean(t_55auf)
t_55auf_std = np.std(t_55auf)
v_55auf = x / t_55auf_mean

t_55ab = np.array([3.216, 3.204, 3.250]) / 5
t_55ab_mean = np.mean(t_55ab)
t_55ab_std = np.mean(t_55ab)
v_55ab = x / t_55ab_mean

t_55 = np.array([3.308, 2.723, 2.444])
t_55_mean = np.mean(t_55)
t_55_std = np.std(t_55)
v_55 = x / t_55_mean

# Konstanten
rho_oel = 886
g = 9.81
rho_L = 1.1644 # im Internet nachschlagen
n_L = np.array([1.877, 1.875, 1.872, 1.872, 1.874, 1.874, 1.866, 1.866, 1.878, 1.877])*10**(-5) # aus dem Plot abgelesen
B = 6.17e-5 * 101325 / 760
p = 101300
v_auf = np.array([v_1auf, v_11auf, v_2auf, v_22auf, v_3auf, v_33auf, v_4auf, v_44auf, v_5auf, v_55auf])
print('aufsteigende Geschwindigkeiten:', np.round(v_auf,8))
v_ab = np.array([v_1ab, v_11ab, v_2ab, v_22ab, v_3ab, v_33ab, v_4ab, v_44ab, v_5ab, v_55ab])
print('absteigende Geschwindigkeiten:', np.round(v_ab, 8))
v = np.array([v_1, v_11, v_2, v_22, v_3, v_33, v_4, v_44, v_5, v_55])
print('fallende Geschwindigkeiten:', np.round(v,8))
d = 7.6250e-3
U = np.array([261, 261, 271, 271, 280, 280, 290, 290, 301, 301])

# n = eta (Viskosität)

# Formeln

r = np.sqrt((9*n_L*(v_ab-v_auf))/(2*g*(rho_oel-rho_L)))

n_eff = n_L * (1 / (1+ (B / (p * r))))

r_korr = np.sqrt((B/(2*p)**2) + (9*n_eff*v)/(2*g*rho_oel)) - (B / (2*p))

q_0 = 3 * np.pi * n_L * np.sqrt((9*n_L*(v_ab-v_auf))/(4*g*(rho_oel-rho_L))) * (v_ab + v_auf)/U *d

q = q_0 * (1 + (B/(p*r_korr)))**(3/2)

print('radius r:', r)
print('n_eff:', n_eff)
print('radius korrigiert:', r_korr)
print('Ladung q:', q_0)
print('korrigierte Ladung:', q)

# Abweichungen für aufsteigende Geschwindigkeiten
t_auf = np.array([t_1auf_mean, t_11auf_mean, t_2auf_mean, t_22auf_mean, t_3auf_mean, t_33auf_mean, t_4auf_mean, t_44auf_mean, t_5auf_mean, t_55auf_mean])
t_auf_std = np.array([t_1auf_std, t_11auf_std, t_2auf_std, t_22auf_std, t_3auf_std, t_33auf_std, t_4auf_std, t_44auf_std, t_5auf_std, t_55auf_std])
delta_v_auf = x * t_auf_std / t_auf
print('Fehler auf die aufsteigende Geschwindigkeit:', delta_v_auf)
# Abweichungen für absteigende Geschwindigkeiten
t_ab = np.array([t_1ab_mean, t_11ab_mean, t_2ab_mean, t_22ab_mean, t_3ab_mean, t_33ab_mean, t_4ab_mean, t_44ab_mean, t_5ab_mean, t_55ab_mean])
t_ab_std = np.array([t_1ab_std, t_11ab_std, t_2ab_std, t_22ab_std, t_3ab_std, t_33ab_std, t_4ab_std, t_44ab_std, t_5ab_std, t_55ab_std])
delta_v_ab = x * t_ab_std / t_ab
print('Fehler auf die absteigende Geschwindigkeit:', delta_v_ab)

# Abweichungen auf die Sinkgeschwindigkeit
t_v = np.array([t_1_mean, t_11_mean, t_2_mean, t_22_mean, t_3_mean, t_33_mean, t_4_mean, t_44_mean, t_5_mean, t_55_mean])
t_v_std = np.array([t_1_std, t_11_std, t_2_std, t_22_std, t_3_std, t_33_std, t_4_std, t_44_std, t_5_std, t_55_std])
delta_v = x * t_v_std / t_v
print('Fehler auf die Sinkgeschwindigkeit:', delta_v)

# Abweichung auf den Radius r
delta_r = np.sqrt((3*n_L / (np.sqrt((n_L*(v_ab-v_auf))/(g*(rho_oel-rho_L)))*(rho_oel-rho_L)*g*2**(3/2)))**2 * (delta_v_ab**2 +delta_v_auf**2))
print('Fehler auf den Radius:', delta_r)

# Abweichung auf n_eff
delta_n_eff = n_L*B*p /((p*r + B)**2) * delta_r
print('Fehler auf n_eff:', delta_n_eff)

# Abweichung auf korrigierten Radius
delta_r_korr = p /(4*g*rho_oel*np.sqrt(p*v*n_eff/(2*g*rho_oel)+B**2/(4*p**2))) * np.sqrt((v*delta_v)**2 + (n_eff*delta_n_eff)**2)
print('Fehler auf r_korr:', delta_r_korr)

# Abweichung auf q_0
delta_d = 0.0051e-3
#Wurzelterm
wurzel = np.sqrt(9*n_L*(v_ab-v_auf)/4*g*(rho_oel-rho_L))
delta_q_0 = (9*np.pi*d*n_L**2 * (3*v_ab-v_auf)/(4*g*(rho_oel-rho_L)*U*np.sqrt(n_L*(v_ab-v_auf)/(g*(rho_oel-rho_L)))))**2 * (delta_v_ab**2 + delta_v_auf**2) + (3*np.pi*n_L *wurzel*(v_ab+v_auf)/U)**2 * delta_d**2
delta_q_0 = np.sqrt(delta_q_0)
print('Fehler auf q_0:', delta_q_0)
q_0e = q_0 / 1.6e-19
delta_q_0e = delta_q_0 / 1.6e-19
print('q_0 auf e normiert:', q_0e, '±', delta_q_0e)

# Abweichung auf q
delta_q = np.sqrt((1+(B/(p*r_korr)))**3 * delta_q_0**2 + (3*q_0*B/(2*p*r_korr**2))**2 * (1+(B/(p*r_korr)))*delta_r_korr**2)
qe = q / 1.6e-19
delta_qe = delta_q / 1.6e-19
print('Fehler auf q:', delta_q)
print('q auf e normiert:', qe, '±', delta_qe)

elementar = np.array([1.61,1.50,1.48,1.53,1.61,1.31,1.36,1.51,1.55])
el = np.mean(elementar)
els = np.std(elementar)
print('elementarladung:', el,'±', els)
