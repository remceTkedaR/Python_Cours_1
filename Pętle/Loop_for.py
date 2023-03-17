## Loop "for"

d = [10, 8, 10, 12, 6, 8, 7, 12, 10, 16, 16, 9, 14, 9, 11, 17, 18, 9, 5, 17] ## Lista z wynikami badań

## należy teraz wprowadzić korektę wyników badań o 0,1
for i in range(len(d)):
    d[i] = d[i] + 0.1

print('długośc listy danych :', len(d))
print('drugi element list:',  d[1:2])

## wydruk z indeksowaniem
for index in range(len(d)):
    print(index, d[index])

## Loop fpr (2)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

## Loop for (3)

for index in range(10):
    x = (index + 1)
    x = x * 2
    print(x)





