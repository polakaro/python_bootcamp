liczba1 = int(input('Podaj pierwszą liczbę: '))
liczba2 = int(input('Podaj drugą liczbę: '))
operacja = input('Podaj rodzaj operacji: ')

if operacja == '+':
    wynik = liczba1 + liczba2
elif operacja == '-':
    wynik = liczba1 - liczba2
elif operacja == '*':
    wynik = liczba1 * liczba2
elif operacja == '/':
    wynik = liczba1 / liczba2
else:
    wynik = None

if wynik is not None:
	print(f'Wynik: {wynik}')
	print(f'A pomnożnony przez 100 {100 * wynik}')
else:
	print('Nieznana operacja')
