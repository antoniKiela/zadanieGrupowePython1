#dzialanie programu uruchamia komenda master().
#Po uruchumieniu programu wpisz -help aby uzyskac dokladna instukcje tego jak powinien wygladac input

from pathlib import Path
import odczytanie_i_zapis #Wczytuje moduł pozwalający na odczyt i zapis 
import argparse

#zamienia dane podane w inpucie na dane czytelne dla dalszej czesci programu
def zmiana_danych(data):
    list_of_commands = []
    list_of_commands.append(data[1])

    str_monts = data.split('[')[1].split(']')[0]
    list_months = str_monts.split(', ')
    list_of_commands.append(list_months)

    str_days = data.split('[')[2].split(']')[0]
    list_days = str_days.split(', ')
    list_of_commands.append(list_days)

    str_pory = data.split('[')[3].split(']')[0]
    list_pory = str_pory.split(', ')
    list_of_commands.append(list_pory)

    return list_of_commands

#funkcja zamienia input dni, na czytelny dla dalszej czesci kodu zapis
def lista_dni(zakres):
    katalog_dni = ['pn', 'wt', 'sr', 'czw', 'pt', 'sb', 'nd']
    wszystkie_dni = []                                  
    if('-' in zakres):
        zakres_dni = zakres.split('-')

        num_dzien1 = katalog_dni.index(zakres_dni[0])
        num_dzien2 = katalog_dni.index(zakres_dni[1])

        if(num_dzien1 > num_dzien2):
            wszystkie_dni = katalog_dni[num_dzien1 : ] + katalog_dni[ : num_dzien2 + 1]
        else:
            wszystkie_dni = katalog_dni[num_dzien1 : num_dzien2 + 1]

    else: wszystkie_dni.append(zakres)
    return wszystkie_dni

#funkcja zamienia input por, na czytelny dla dalszej czesci kodu zapis
def zmiana_pory(pora):
    nowa_pora = []
    for char in pora:
        if(char == 'r'):
            nowa_pora.append('rano')
        else: nowa_pora.append('wieczorem')
    return nowa_pora

#funkcja zapisuje pliki we wskazanych miejscach. Jesli podany plik juz istnieje, funkcja go zignoruje.        
def zapisanie_plikow(miesiace_in, dni_in, pora_in):
    znacznik_pory = 0
    dict_days = {'pn': 'poniedzialek', 'wt': 'wtorek', 'sr': 'sroda', 'czw': 'czwartek', 'pt': 'piatek', 'sb': 'sobota', 'nd': 'niedziela'}
    for num_mies, mies in enumerate(miesiace_in):
        dni = lista_dni(dni_in[num_mies])
        pora = zmiana_pory(pora_in)

        for days in dni:
            try:
                sciezka = Path(mies, dict_days[days], pora[znacznik_pory])
                znacznik_pory += 1
            except IndexError:
                sciezka = Path(mies, dict_days[days], 'rano')

            sciezka.mkdir(parents=True, exist_ok=True)
            plik = sciezka / 'dane.csv'
            plik.touch(exist_ok=True)
            #print(plik)

            odczytanie_i_zapis.zapis(str(plik)) 

#funkcja odczytuje pliki dane.csv w podanych katalogach. Jesli nie znajdzie danego pliku, pojawi sie stosowny komunikat
def odczyt_plikow(miesiace_in, dni_in, pora_in):
    znacznik_pory = 0
    dict_days = {'pn': 'poniedzialek', 'wt': 'wtorek', 'sr': 'sroda', 'czw': 'czwartek', 'pt': 'piatek', 'sb': 'sobota', 'nd': 'niedziela'}
    for num_mies, mies in enumerate(miesiace_in):
        dni = lista_dni(dni_in[num_mies])
        pora = zmiana_pory(pora_in)

        for days in dni:
            try:
                sciezka = Path(mies, dict_days[days], pora[znacznik_pory])
                znacznik_pory += 1
            except IndexError:
                sciezka = Path(mies, dict_days[days], 'rano')

            plik = sciezka / 'dane.csv'
            try:
                odczytanie_i_zapis.odczytCzasu(str(plik))
                #zawartosc = plik.read_text(encoding="utf-8")
                #print(f"{plik}:\t|\t{zawartosc}")
            except FileNotFoundError:
                print(f"Nie znaleziono pliku:\t {plik}")



#funkcja zbierajaca wszystkie wczesniejsze funkcje, uruchamiajac ja uruchamiamy caly program
def master():
    parser = argparse.ArgumentParser(
        add_help=False
    )
    
    # 3 flagi: -o, -z, -h
    parser.add_argument('-o', '--odczyt', action='store_true', help='Odczytaj pliki')
    parser.add_argument('-z', '--zapis', action='store_true', help='Zapisz pliki')
    parser.add_argument('-h', '--help', action='store_true', help='Wyświetl pomoc')

    args = parser.parse_args()

    if args.help:
        print('FLAGI:\n-o, --odczyt    Odczytaj pliki dane.csv z podanej struktury katalogów\n\t\tWyświetla sumę czasu dla modelu A\n')
        print('-z, --zapis     Zapisz pliki dane.csv w podanej strukturze katalogów\n\t\tTworzy katalogi i wypełnia je losowymi danymi\n')
        print('-h, --help      Wyświetl tę pomoc\n')
        print('\nDomyslnie program jest wlaczony w trybie zapisu\n')
        print('\nDane podajemy w formacie:\n[miesiace], [dni], [pory]\n')
        print('Miesiace piszemy dowolnie\n')
        print('Dni zapisujemy w nastepujacy sposob:')
        print('pn -> poniedzialek \t|\t wt -> wtorek \t|\t sr -> sroda \t|\t czw -> \t|\t czwartek \t|\t pt -> piatek \t|\t sb -> sobota \t|\t nd -> niedziela')
        print('Zakresy podaje sie wstawiajac miedzy dwoma dniami myslnik, np: wt-nd\n')
        print('Pory dnia zapisujemy jako r -> rano, lub jako w -> wieczor\n')
        print('Miesiace, dni i pory grupujemy ze soba uzywajac [...]')
        print('Elementy wewnatrz nawiasow oddzielamy zapisujac \', \' (przecinek i spacja)\n')
        print('Przykladowo poprawnie sformatowany input:')
        print('[styczen, luty] [sr-pn, pt-nd] [r, w, w, w, w, r, w]')

        return

    if args.odczyt:
        print("Tryb odczytu")

    if args.zapis:
        print("Tryb zapisu")


    if not args.odczyt and not args.zapis and not args.help:
        args.zapis = True
        print("Nie podano flagi - ustawiam domyślnie tryb ZAPISU (-z)")
    
    # Tryb interaktywny
    print("Podaj dane ([miesiace], [dni], [pory])")
    data = input()

    lista_danych = zmiana_danych(data)
    miesiace = lista_danych[1]
    dni_input = lista_danych[2]
    pora_input = lista_danych[3]

    if args.odczyt:
        odczyt_plikow(miesiace, dni_input, pora_input)
    elif args.zapis:
        zapisanie_plikow(miesiace, dni_input, pora_input)

master()
