import csv
import random

# Martyna Kupidłowska

# Nie wiedziałam, czy należy zwrócić ten czas czy go wypisać w odczytywaniu, więc obecnie robi obie rzeczy

typy = ["Model", "Wynik", "Czas"]
lista = ["A", "B", "C"]

def zapis (nazwa):  # Funkcja zapis (nazwa pliku) tworzy losowe dane według specyfikacji (A/B/C, wynik od 0 do 1000, czas od 0 do 1000 z dodanym "s").
    lista2 = []
    s = random.randint(0, 1000)
    w = random.randint(0, 1000)
    kt = random.randint(0, 2)
    lista2.append(lista[kt])
    lista2.append(s)
    lista2.append(str(w) + "s")
    with open(nazwa, "w", newline="", encoding="utf-8") as plik:
        pisarz = csv.writer(plik)
        pisarz.writerow(typy)
        pisarz.writerow(lista2)


def odczytCzasu (nazwa): # Funkcja odczytCzasu (nazwa pliku).
    i = 0
    with open(nazwa, "r", encoding="utf-8") as plik:
        czytelnik = csv.reader(plik)
        next(czytelnik)
        for wiersze in czytelnik:
            if wiersze[0] == "A": # Sprawdza czy wartość w 1 kolumnie w każdym wierszu to "A", jeśli tak to dodaje czas (usuwa "s") i dodaje int wartość do sumy.
                i += int(wiersze[2].replace("s", "").strip())
    print("Czas A: " + str(i))
    return i
