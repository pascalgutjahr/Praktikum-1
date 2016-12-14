Fehler.pyimport sympy as sp
import numpy as np
from IPython.display import display, Math, Latex
L,C,R1,R2 = sp.symbols ('L C R1 R2')
variablen = [L,C,R1,R2]
variablen_werte = [3.53e-3, 5.015e-9, 30.3, 271.6]
fehler_werte = [0.03e-3, 0.015e-9, 0.1, 0.3]
funktion = sp.sqrt((4*L)/C)
fehler = 0
fehlersymbole = []
ableitung_quadr = []

for var in variablen:
    d = sp.symbols('d' + var.name)
    fehlersymbole.append(d)
    partial = sp.diff(funktion, var) * d
    ableitung_quadr.append(partial**2)
    fehler = fehler + partial**2

fehler_abs=sp.simplify(sp.sqrt(fehler))
fehler_rel=sp.simplify(sp.sqrt(fehler/funktion**2))
funktions_wert=sp.Subs(funktion, variablen,variablen_werte).doit()

err1=sp.Subs(fehler, variablen, variablen_werte).doit()

err2=sp.Subs(err1, fehlersymbole, fehler_werte).doit()

print('Funktion:')
display(Math('f='+sp.latex(funktion)))

 print('Messwerte:')
 for i in range(len(variablen)):
     display(Math(str(variablen[i])+'='+str(variablen_werte[i])+'\pm'+str(fehler_werte[i])))

 print('Absoluter Fehler:')
 display(Math(r'\Delta f='+sp.latex(fehler_abs).replace("d",r'\Delta')))

 print('Relativer Fehler:')
 display(Math(r"\Delta f/f="+sp.latex(fehler_rel).replace('d',r'\Delta ')))
 display(Math("f= %6.2f \pm %6.2f" %(funktions_wert,sp.sqrt(err2))))
 display(Math("f= %6.2f \pm %6.1f %s" %(funktions_wert,sp.sqrt(err2)/funktions_wert*100," \%")))
