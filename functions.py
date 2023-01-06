import matplotlib.pyplot as plt
import numpy as np
import variables as var

plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

#Obliczam wartosc wielomianu za pomoca Schematu Hornera
def oblicz_wartosc_wielomianu(x):
    temp = 0
    for i in var.wielomian:
        temp *= x
        temp += i
    return temp

#Szuka miejsc zerowych funkcji
def szukaj_zerowych():
    var.zerowe.clear()
    find = np.roots(var.wielomian)
    for i in range(len(find)):
        if (np.isreal(find[i])):
            #print("Miejsce zerowe to: ", np.real(find[i]))
            var.zerowe.append(np.real(find[i]))

#Rysuje wykres wielomianu 
def rysuj_wykres():
    szukaj_zerowych()
    oś_x = []  # linear space do rysowana wykresów
    oś_y = []
    i = var.początek
    while i < var.koniec:
        oś_x.append(i)
        oś_y.append(oblicz_wartosc_wielomianu(i))
        i += var.rozdzielczość
    plt.title('WYKRES WIELOMIANU')
    plt.ylabel('oś y', loc = 'top')
    plt.xlabel('oś x', loc = 'right')
    plt.axvline(x=0, c="mediumvioletred")
    plt.axhline(y=0, c="mediumvioletred")
    for i in range(len(var.zerowe)):
        plt.plot(var.zerowe[i], oblicz_wartosc_wielomianu(var.zerowe[i]), 'o', color='red', zorder=2)
    plt.plot(oś_x, oś_y, zorder=1)
    plt.show()

#Obliczam pochodna 
def rysuj_pochodna():
    oś_x = []  # linear space do rysowana wykresów
    oś_y = []
    i = var.początek
    while i < var.koniec:
        oś_x.append(i)
        temp = oblicz_wartosc_wielomianu(i + var.rozdzielczość) - oblicz_wartosc_wielomianu(i)
        temp /= var.rozdzielczość
        oś_y.append(temp)
        i += var.rozdzielczość
    plt.title('WYKRES POCHODNEJ')
    plt.ylabel('oś y', loc='top')
    plt.xlabel('oś x', loc='right')
    plt.axvline(x=0, c="mediumvioletred")
    plt.axhline(y=0, c="mediumvioletred")
    plt.plot(oś_x, oś_y)
    plt.show()



 
