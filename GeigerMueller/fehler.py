import numpy as np

N_60 = np.array([17919,18485,18816,19267,19079,18757,19033,19287,19307,19245,19330,19591,19648,19482,19597,19468,19688,19627,19439,19559,19427,19399,19492,19473,19583,19421,19640,19686,19718,19816,20138,19965,20213,20120,20105,20600,20600,20659,20611,21140])
N_1 = np.round((N_60 / 60),1)
N_list = np.vstack(N_1)
F = np.round((np.sqrt(N_1)),1)
F_list = np.vstack(F)
print('Impulsrate pro Sekunde:',N_list,'+-', F_list)

U = np.array([310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700])
