##  Operacje na słownikach i listach

rec = {'dane osobowe': {'imię': 'Robert', 'nazwisko': 'Zielony'},
           'zawód': ['programista', 'inżynier'],
           'wiek': 40.5}

# 'dane osobowe' to zagnieżdżony słownik
print(rec['dane osobowe'])

# Indeksowanie zagnieżdżonego słownika
print("Indeksowanie zagnieżdżonego słowa (nazwisko) ", rec['dane osobowe']['nazwisko'])

# Indeksowanie zagnieżdżonej listy
print("Indeksowanie zagnieżdżonej listy: ", rec['zawód'][-1])

rec['zawód'].append('leśniczy')          # Rozszerzenie listy zawodów Roberta
print(rec)

D = {}  # pusty słownik
D['imię'] = 'Jan'        # Tworzenie kluczy przez przypisanie
D['nazwisko'] = 'Malajkat'
D['wiek'] = 40
print("Słównik z zawartością : ", D)
print('Drukowanie po kluczu: ', D['imię'])


D_list = {'a': 1, 'c': 2, 'b': 3}  # lista z kluczami
K_list = list(D_list.keys())  # Nieuporządkowana lista kluczy
print("Lista nieuporzadkowana: ", K_list)

L_list = K_list
L_list.sort()
print('Uporządkowana lista: ', L_list)
