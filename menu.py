import functions as fct
import variables as var
import user_input as inpt
import text as tx

tx.witaj()

while 2137:  #Główny program
    print("Wpisany wielomian: ", var.wielomian)
    print("Zakres: [",var.początek,"; ", var.koniec,"]")
    action = int(input("""
1 - Wprowadź wielomian
2 - Wprowadź zakres
3 - Rysuj wykres
4 - Rysuj pochodną
5 - Szukaj miejsc zerowych wielomianu
6 - Informacje (Pomoc)
7 - Przewidywany czas oczekiwania
-1 - Koniec programu

Wprowadź cyfrę: """))

    if action == -1:
        break

    if action == 1:
        var.wielomian = inpt.get_wielomian_od_użytkownika()

    if action == 2:
        inpt.get_zakres_od_użytkownika()

    if action == 3:
        fct.rysuj_wykres()

    if action == 4:
        fct.rysuj_pochodna()

    if action == 5:
        fct.szukaj_zerowych()
        for i in range(len(var.zerowe)):
            print("Miejsce zerowe to: ", var.zerowe[i])
    
    if action == 6:
        tx.informacje()

    if action == 7:
        tx.przewidywania()
