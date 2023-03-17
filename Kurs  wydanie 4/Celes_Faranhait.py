# Przelicz stopnie Celesiusza na Faranhaita

temps = [("Berlin", 20), ("Praga", 22), ("Moskwa", 19)]


c_to_f = lambda data: (data[0], (9/5)*data[1] + 32) # nasza funkcja konwertująca C do F

print("Temeratura w F: ", list(map(c_to_f, temps))) # użucie funkcji map do przeliczenia pokolei pozycję z listy

print("Temperatura w C: ", temps)

