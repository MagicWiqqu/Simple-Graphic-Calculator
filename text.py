#Welcome
def witaj():
    print("""
----------------------------------------------------------------------------------------------
Witaj użytkowniku!
Aby zarządzać menu wprowadź cyfrę, aby skorzystać z interesującej Cię opcji, 
a następnie zatwierdź ją przyciskiem ENTER. Powodzenia!
----------------------------------------------------------------------------------------------
    
""")

#Informacje dla użytkownika jeśli nie umie korzystać z programu
def informacje():
    print("""
----------------------------------------------------------------------------------------------
Drogi użytkowniku, tutaj znajdziesz informacje dot. obsługi programu.
Program ma 5 podstawowych opcji, z których możesz korzystać. 
    1 - Wprowadzenie wielomianu
        Tutaj wprowadzasz do programu pożądany wielomian.
        Zaczynasz od podania stopnia wielomianu i wprowadzasz współczynniki, 
        od wyrazu przy największej potędze to tego przy potędze zerowej. 
    2 - Wprowadzanie zakresu
        Tutaj wprowadzasz zakres osi X dla twojego wykresu (pochodnej oraz wielomianu). 
        Uwaga! Lewy kraniec zakresu musi być mniejszy od prawego. 
        Jeśli wprowadzisz na odwrót to program to automatycznie zamieni!
        Program zawsze uwzględni przecięcie osi X i Y, więc zakresy,
        które nie uwzględniają 0 i tak ukażą punkt przecięcia osi!!!
    3 - Rysuj wykres
        Tutaj program rysuje wykres dla wielomianu. Czerwonymi kropkami zaznacza miejsca zerowe.
        Uwaga! Im większy zakres tym mniejsza dokładność wykresu wielomianu! 
        Aby zobaczyć szczegóły dla danego wycinka wykresu należy odpowiednio dostosować zakres.
    4 - Rysuj pochodną
        Tutaj program rysuje wykres pochodnej wielomianu. 
        Działanie analogiczne do rysowania wykresu.
    5 - Szukaj miejsc zerowych
        Program szuka, a następnie wypisuje znalezione miejsca zerowe rzeczywiste funkcji.
---------------------------------------------------------------------------------------------
UWAGA - Podane są przewidywane czasy renderowania wykresu funcji wielomianu i pochodnej. 
Nie ma limitu wpisanego zakresu - jeśli użytkownik chce czekać, to może.
Przewidywane czasy można znaleźć w menu, po kliknięciu 7.
---------------------------------------------------------------------------------------------
        
    """)

def przewidywania():
    print("""
----------------------------------------------------------------------------------------------
Drogi użytkowniku, tutaj znajdziesz przewidywania dot. czasu oczekiwania na wynik.
----------------------------------------------------------------------------------------------
Dla wielomianu stopnia 4 o współczynnikach mieszczących się w zakresie (0,10):
    Zakres (0,100) - Około 3 sekund
    Zakres (0, 1000) - Około 3 sekund
    Zakres (0, 10000) - Około 13 sekund
    Zakres (0, 100000) - Około 3 minuty
    Zakres (0, 1000000) - Powyżej 30 minut
----------------------------------------------------------------------------------------------
Współczynniki przy wielomianie nie mają większego wpływu na czas oczekiwania.
Liczy się bardziej stopień wielomianu - im większy stopień, tym dłuższy czas oczekiwania.
Jednakże, największy wpływ na czas oczekiwania nadal ma ZAKRES.
----------------------------------------------------------------------------------------------
    
    """)