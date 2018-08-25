lista = [1, 10, -2, -3, 30, 22, 21, 24]
ujemne = 0
dodatnie = 0

for liczba in lista:
    if liczba > 0:
        dodatnie += 1
    elif liczba < 0:
        ujemne += 1
print(f' ujemne {ujemne}, dodatnie {dodatnie}' )