# pobieranie wiersza z pliku

import linecache

# pobranie 4 lini z pliku
line = linecache.getline('file_data1.csv', 4)
print(line)