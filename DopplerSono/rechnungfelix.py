import numpy as np
#berechnung der Dopplerwinkel
cl = 1800 #meterpersecond
cp = 2700 #meterpersecond
teta = np.array([15, 30, 60])
alpha = np.round((np.pi/2 - np.arcsin(np.sin((teta/360)*2*np.pi)*(cl/cp)))/(2*np.pi)*360, 2)
print("Dopplerwinkel alpha für 15,30,60 grad :",alpha)


#Bestimmung der Strömungseschwindigkeit als funkt des Dopplerwinkel
#dünnes Rohr
dünnerst  = np.array([171,317,476])
dünnzweit = np.array([293,513,793])
dünndritt = np.array([330,676,964])
dünnviert = np.array([415,891,1233])
dünnfünft = np.array([647,1355,1941])

vdünn1 = np.round((dünnerst * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vdünn2 = np.round((dünnzweit * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vdünn3 = np.round((dünndritt * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vdünn4 = np.round((dünnviert * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vdünn5 = np.round((dünnfünft * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
print("dünnes Rohr")
print("Geschwindigkeiten für dünnes Rohr bei 35.4 prozent 15,30,45 grad ", vdünn1,"Mittelwert", np.round(np.mean(vdünn1),2), "+-", np.round(np.std(vdünn1),2))
print("Geschwindigkeiten für dünnes Rohr bei 45.2 prozent 15,30,45 grad ", vdünn2,"Mittelwert", np.round(np.mean(vdünn2),2), "+-", np.round(np.std(vdünn2),2))
print("Geschwindigkeiten für dünnes Rohr bei 50.0 prozent 15,30,45 grad ", vdünn3,"Mittelwert", np.round(np.mean(vdünn3),2), "+-", np.round(np.std(vdünn3),2))
print("Geschwindigkeiten für dünnes Rohr bei 55.2 prozent 15,30,45 grad ", vdünn4,"Mittelwert", np.round(np.mean(vdünn4),2), "+-", np.round(np.std(vdünn4),2))
print("Geschwindigkeiten für dünnes Rohr bei 70.0 prozent 15,30,45 grad ", vdünn5,"Mittelwert", np.round(np.mean(vdünn5),2), "+-", np.round(np.std(vdünn5),2))

#mittleres Rohr

mittelerst  = np.array([110,171,269])
mittelzweit = np.array([159,244,464])
mitteldritt = np.array([208,305,574])
mittelviert = np.array([220,366,720])
mittelfünft = np.array([330,598,1062])

vmittel1 = np.round((mittelerst * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vmittel2 = np.round((mittelzweit * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vmittel3 = np.round((mitteldritt * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vmittel4 = np.round((mittelviert * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vmittel5 = np.round((mittelfünft * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
print("mittleres Rohr")
print("Geschwindigkeiten für mittleres Rohr bei 35.2 prozent 15,30,45 grad", vmittel1,"Mittelwert", np.round(np.mean(vmittel1),2), "+-", np.round(np.std(vmittel1),2))
print("Geschwindigkeiten für mittleres Rohr bei 45.2 prozent 15,30,45 grad", vmittel2,"Mittelwert", np.round(np.mean(vmittel2),2), "+-", np.round(np.std(vmittel2),2))
print("Geschwindigkeiten für mittleres Rohr bei 50.0 prozent 15,30,45 grad", vmittel3,"Mittelwert", np.round(np.mean(vmittel3),2), "+-", np.round(np.std(vmittel3),2))
print("Geschwindigkeiten für mittleres Rohr bei 55.2 prozent 15,30,45 grad", vmittel4,"Mittelwert", np.round(np.mean(vmittel4),2), "+-", np.round(np.std(vmittel4),2))
print("Geschwindigkeiten für mittleres Rohr bei 70.0 prozent 15,30,45 grad", vmittel5,"Mittelwert", np.round(np.mean(vmittel5),2), "+-", np.round(np.std(vmittel5),2))


#dickes Rohr
dickerst  = np.array([73,85,143])
dickzweit = np.array([85,122,195])
dickdritt = np.array([98,134,232])
dickviert = np.array([122,171,281])
dickfünft = np.array([171,256,452])

vdick1 = np.round((dickerst * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vdick2 = np.round((dickzweit * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vdick3 = np.round((dickdritt * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vdick4 = np.round((dickviert * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
vdick5 = np.round((dickfünft * cl)/(2* 2*10**6 * np.cos((alpha/360)*2*np.pi)),2)
print("dickes Rohr")
print("Geschwindigkeiten für dickes Rohr bei 35.2 prozent 15,30,45 grad", vdick1,"Mittelwert", np.round(np.mean(vdick1),2), "+-", np.round(np.std(vdick1),2))
print("Geschwindigkeiten für dickes Rohr bei 45.2 prozent 15,30,45 grad", vdick2,"Mittelwert", np.round(np.mean(vdick2),2), "+-", np.round(np.std(vdick2),2))
print("Geschwindigkeiten für dickes Rohr bei 50.0 prozent 15,30,45 grad", vdick3,"Mittelwert", np.round(np.mean(vdick3),2), "+-", np.round(np.std(vdick3),2))
print("Geschwindigkeiten für dickes Rohr bei 55.2 prozent 15,30,45 grad", vdick4,"Mittelwert", np.round(np.mean(vdick4),2), "+-", np.round(np.std(vdick4),2))
print("Geschwindigkeiten für dickes Rohr bei 70.0 prozent 15,30,45 grad", vdick5,"Mittelwert", np.round(np.mean(vdick5),2), "+-", np.round(np.std(vdick5),2))

nu70 = np.array([415,427,476,500,513,500,476,427,341,342])
v70 = np.round((nu70 * cl)/(2* 2*10**6 * np.cos((80.06/360)*2*np.pi)),2)
print('Geschwindigkeiten bei 70.0 percent Leistung, unter 15 grad:',v70)

nu45 = np.array([220,232,245,256,269,256,244,232,195,195])
v45 = np.round((nu45 * cl)/(2* 2*10**6 * np.cos((80.06/360)*2*np.pi)),2)
print('Geschwindigkeiten bei 45.0 percent Leistung, unter 15 grad:',v45)
