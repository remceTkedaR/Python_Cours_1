## działanie na macierzy

M = [[1, 2, 3],                    ##  Macierz 3x3 w postaci list zagnieżdżonych
     [4, 5, 6],                ##  Kod może się rozciągać na kilka wierszy, jeśli znajduje się w nawiasach
     [7, 8, 9]]

coll2 = M[1][2]      #  Pobranie drugiego wiersza, a z niego trzeciego elementu
print('drugi wiersz trzeci element to: ', coll2)

coll2 = [row[1] for row in [M]]  # Zebranie elementów z drugiej kolumny to jest 2, 5, 8
print("Druga kolumna to: ", coll2)

coll3 = [row[1] + 1 for row in M]  #  Dodanie 1 do każdego elementu w drugiej kolumnie
print("Dodanie 1 do liczby w drugiej kolumnie", coll3)

coll4 = [row[1] for row in M if row[1] % 2 == 0]  # Odfiltrowanie elementów nieparzystych
print("liczby parzyste to: ", coll4)

coll5 = [M[i][i] for i in [0, 1, 2]]      # Pobranie przekątnej z macierzy
print("przekątna macierzy: ", coll5)

G = {sum(row) for row in M}                 # Utworzenie zbioru sum wierszy
print("suma wierszy ale wyświetlana niepokolei: ", G)

H = {i : sum(M[i]) for i in range(3)}       # Utworzenie tabeli klucz-wartość sum wierszy
print("tabela klucz-wiersz : ", H)
print("wybieranie liczby z tabeli po kluczu np. 0 to: ", H[0])

