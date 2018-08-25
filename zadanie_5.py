
liczba = int(input('Podaj liczbę: '))

g = 1
s = liczba - 1

while s >= 0:
    for i in range(0, s):
        print(' ', end = '')
    for i in range(0, g):
        print('*', end = '')
    print('\n')
    s = s - 1
    g = g + 2

