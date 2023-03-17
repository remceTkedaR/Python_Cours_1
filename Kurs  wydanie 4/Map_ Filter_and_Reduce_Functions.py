## Map Filter and Raduce

import math

def area(r):
    #  Area of circle with radius 'r'. (pole powierzchni koła o promieniu 'r')
    return math.pi * (r**2)


radii = [2, 5, 7.1, 0.3, 10]

# ------------Method 1 Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

for i in range(5):
    print("pole powierzchni koła o promieniu r=", radii[i], '=', areas[i])

#-------------Method 2 map function

areas1 = map(area, radii)
areas_1 = list(areas1)
for j in range(5):
    print("Map funkcja -Pole powierzchni koła o promieniu r=", radii[j], '=', areas_1[j])

## -----Filter

import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3,  -0.1]
avg = statistics.mean(data)
print("średnia z listy  data = ", avg)

data_m = filter(lambda x: x > avg, data)

print("liczby większe od średniej z listy to :", list(data_m))

