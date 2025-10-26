STRUKTURA PLIKÓW:
- lab3_zadanie1.py - główny plik programu
- odczytanie_i_zapis.py - moduł do operacji na plikach CSV

URUCHOMIENIE PROGRAMU:
python lab3_zadanie1.py

DOSTĘPNE FLAGI:
-o, --odczyt    Odczytaj pliki dane.csv z podanej struktury katalogów
                Wyświetla sumę czasu dla modelu A

-z, --zapis     Zapisz pliki dane.csv w podanej strukturze katalogów
                Tworzy katalogi i wypełnia je losowymi danymi

-h, --help      Wyświetl pomoc

DOMYŚLNE DZIAŁANIE:
Jeśli nie podano żadnej flagi, program domyślnie uruchamia się w trybie ZAPISU.

UWAGI:
- Jeśli plik już istnieje, program go nie nadpisuje
- W przypadku braku wystarczającej liczby por dnia, program domyślnie używa "rano"
