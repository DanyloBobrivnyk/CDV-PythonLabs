slowniki = {
    'klucz1':'wartosc1',
    'klucz2':'wartosc2'
    }

#slownik o nazwie pracownik zawierajacy klucze
#imie nazwisko miasto wiek imiona dzieci imiona rodziców

pracownik = {
    'imie':'Jan',
    'nazwisko':'Dzban',
    'miasto':'Poznań',
    'wiek':'29',
    'imionaDzieci':['Anna','Sebastian'],
    'imionaRodzicow':['Piotr','Elżbieta']
}
print(pracownik['imionaDzieci'])
print(pracownik['imionaDzieci'][0])
#Dodawanie nowych kluczy
pracownik['wzrost'] = 175
pracownik['waga'] = 80
print(pracownik)

##################################

pracownik1={
    'imie':'Anna',
    'nazwisko':'Dzbanna',
    'miasto':'Poznań',
    'wiek':'20',
}
print()
print(pracownik1)

klucz = 'wiek'

if klucz in pracownik1:
    del pracownik1[klucz]
    print(f'Klucz {klucz} został usunięty')
else:
    print(f'Klucz {klucz} nie został usunięty')

print('\n')

print(pracownik1.keys())
print(pracownik1.values())
print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value,end=" ")

print('\n')

for key,value in pracownik1.items():
print(f'{key}:{value}')