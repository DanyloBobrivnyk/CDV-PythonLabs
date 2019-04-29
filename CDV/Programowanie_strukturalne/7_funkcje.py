def witaj():
    print("witaj Janusz")


witaj()


###############

def wyswietlWiek(wiek):
    print("Twój wiek :", wiek)


wyswietlWiek(23)


###############

def iloczyn(a, b):
    return a * b


iloczyn1 = iloczyn(2, 4)
print(iloczyn1)


def iloraz(a, b):
    return a / b


iloraz1 = iloraz(2, 4)

print(iloraz1)


# uzytkownik podaje z klawiatury
# marka,model,pojemnosc,predkosc max
# zrob funkcje co pobierze wartości i przypisze je do słownika
# utworz 2 funkcje co to wypisze w oddzielnych liniach
def wypisz(dane):
    for key, value in dane.items():
        print(f'{key}:{value}')


def zrobauto():
    print('Podaj marke')
    marka = input()
    print('Podaj model')
    model = input()
    print('Podaj pojemnosc')
    pojemnosc = input()
    print('Podaj predkosc max')
    predkosc_max = input()

    samochod = {
        'marka': marka,
        'model': model,
        'pojemnosc': pojemnosc,
        'predkosc max': predkosc_max
    }
    wypisz(samochod)


zrobauto()