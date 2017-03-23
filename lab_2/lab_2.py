#biblioteka do rysowania wykresow
#import  nazwa biblioteki  as alias
import matplotlib.pyplot as plt
#odwolujac sie do biblioteki piszemy plt.funkcja


##czytanie danych##
##zadeklarowanie tablic
x = []
y = []
c = []
##otwarcie pliku
##plik = open(sciezka* + nazwa_pliku)
f = open('train')
##iterowanie po liniach
for line in f:
    ##dzielimy wedlug spacji i zapisujemy w odpowiednich tablicach
    ##pamietamy o tym ,ze w pliku sa zapisane litery, a my potrzebujemy liczby
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
    c.append(float(line.split()[2]))

print(x)
print(y)

##ustawienie pola widzenia na diagramie
plt.axis([-10,10,-10,10])
##stworzenie diagramu wszystkich punktow
##plt.plot(xy , ygreki, ksztalt, color = kolor


for i in range(len(c)):
    if c[i] == 1.0:
        plt.plot(x[i],y[i], 'ro', color = 'red')
    elif c[i] == 0:
        plt.plot(x[i], y[i], 'ro', color='blue')
    else:
        plt.plot(x[i], y[i], 'ro', color='black')

##wyswietlenie diagramu
plt.show()

