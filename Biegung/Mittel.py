# Hier den Mittelwert berechnen und ausgeben
Abstand, Auslenkung = genfromtxt('alu_rund1.txt' , unpack=True)
summe = 0
for x in Auslenkung:
    summe = summe + x
Mittelwert =summe/len (Auslenkung)

print(Mittel)
