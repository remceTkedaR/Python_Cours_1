##
# Algorytm sortowania przez zliczanie liczb całkowitych
# Tecmer Radosław
# radek69tecmer@gmail.com
###

import random

#  Wprowadzenie danych;
#  Wielkość zbioru do sortowania i zakres zbioru

N = int(input("Podaj rozmiar danych do sortowania: "))
Z = int(input("Podaj zakres danych od 0 do :  "))

Data = [0] * N  # inicjacja wielkości listy
Max_Data = Z  # Ustawienie zakresu max listy


def input_number():

    for i in range(N):
        Data[i] = random.randint(0, Z)  # generowanie losowych liczb całkowitych zpodanego zakresu
                                     #a[i] = int(input("Podaj liczbę z zakresu 0-99: "))
        if Data[i] < 0:
            Data[i] = 0
        if Data[i] > Max_Data:
            Data[i] = Max_Data

#  drukowanie generowanej listy


def out_number():
    for i in range(N):
        print(Data[i])

#  sortowanie listy


def sort_numbers():
    counter = [0] * (Max_Data + 1)         #  wypełnienie licznika listy zerami do max +1 ustalonej wielkości zbioru
    for i in range(N):
        counter[Data[i]] = counter[Data[i]] + 1  #  W wyniku tej operacji w każdym liczniku otrzymaliśmy ilość wartości
                                           #  mniejszych lub równych numerowi licznika, które występują
                                           #  w zbiorze wejściowym
    index = 0
    for i in range(Max_Data + 1):          #  główna pętla sortowania
        for j in range(counter[i]):  #  sortowanie przpisanie liczby bo pozycji
            Data[index] = i
            index = index + 1

    print(Data)


input_number()
out_number()
print(" Dane sortowane przez zliczanie ")
sort_numbers()

#  Koniec