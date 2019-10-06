a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = a + b
if c == 0:
    print('Proba dzielenia przez zero.')
else:
    res = (a**2+b)/(a+b)**2
    print(f'Wartosc wyrazenia wynosi:{res}')