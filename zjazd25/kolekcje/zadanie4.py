
podzielne = 0


for liczba in range(101):
    if liczba % 3 == 0 or liczba % 5 == 0:
        podzielne += 1
    print(liczba)

print(f'pint podzielne przez 3 i 5 {podzielne}')

