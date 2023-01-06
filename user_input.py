import variables as var

#Pobieram wielomian od użytkownika za pomocą przycisków (od największej potęgi do zerowej :))
def get_wielomian_od_użytkownika():
    wsp_wielomianu = []  # tu będą wszystkie współczynniki
    char = 0
    i = 0
    stopien = int(input("Jaki jest stopień wielomianu? (wpisz odpowiedź): "))
    if stopien<0:
        print("Stopień nie może być mniejszy od zera!")
        return wsp_wielomianu
    while i<stopien+1:
        char = float(input("""
----------------------------------------------------------------------------------------------

Wprowadź współczynnik: """))

        wsp_wielomianu.append(char)
        i = i+1

    print("""
----------------------------------------------------------------------------------------------
Koniec wprowadzania!
----------------------------------------------------------------------------------------------    

    """)
    return wsp_wielomianu

#Pobierany jest zakres wykresu od użytkownika, mechanika działania analogiczna do funkcji wyżej
def get_zakres_od_użytkownika():  
    char = float(input("""
Podaj zakres z lewej strony
Wprowadź zakres: """))
    var.początek = char

    # to samo ale dla drugiej granicy zakresu
  
    char = float(input("""
Podaj zakres z prawej strony
Wprowadź zakres: """))
    var.koniec = char   # przypisanie wpisanej liczby jako koniec zakresu
    if(var.początek>var.koniec):
        temp = var.początek        
        var.początek = var.koniec
        var.koniec = temp

