# nasz głowny program Calculator


from calculus.base_1 import Calculation
# Słownik mozliwych działań
function = {}
value_out = 0.0
calc_1 = {}

d = input("Podaj jakie dzialanie add, sub, mul, div, mod :")
a = int(input("podaj cyfrę a : "))
b = int(input("podaj cyfrę b : "))

function['operation'] = d

if (function['operation'] == 'add'):
    calc_1 = Calculation()
    res = calc_1.add(a, b)
    value_out = res

if function['operation'] == 'sub':
    calc_1 = Calculation()
    res = calc_1.subtract(a, b)
    value_out = res

if function['operation'] == 'mul':
    calc_1 = Calculation()
    res = calc_1.add(a, b)
    value_out = res

if function['operation'] == 'div':
    calc_1 = Calculation()
    res = calc_1.multiply(a, b)
    value_out = res

if function['operation'] == 'mod':
    calc_1 = Calculation()
    res = calc_1.modulo(a, b)
    value_out = res


print(value_out)


