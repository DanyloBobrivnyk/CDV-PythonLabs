print("CDV")
print(2)

#potęga
potega = 2 ** 10
print(potega)

tekst = "CDV"
print(tekst * 10)

#Pobieranie danny z klawy
imie = input()
print("Twoje imię podane z klawiatury: " + imie)

nazwisko = input()
print("Twoje imię:" + imie +" , Twoje Nazwisko: " + nazwisko)

dlugosc = len(nazwisko)
print(type(nazwisko)) #str
print(type(dlugosc)) #int

print("Długosc nazwiska :" , dlugosc)
dlugosc =str(dlugosc) #konwertacja typow danych int\str
print("Długosc nazwiska : " + dlugosc)

#Uzytkownik wpisuje z klawy swoj wiek
#wyswietl dane w formacie : Twoj wiek:.. lat
print ("\nWpisz swój wiek: ", end="-> ")
wiek = input()
print(type(wiek))
wiek= str(wiek)
print("Sposób + Twój wiek: " + wiek +" lat")
print("Sposób , Twój wiek: " , wiek ," lat")

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print (pierwszyZnak)

ostatniZnak = nazwisko[len(nazwisko) - 1]
print(ostatniZnak)
ostatniZnak = nazwisko[- 1]
print(ostatniZnak)

#konwersja
x = "5"
print(type(x))
x = int(x)
print(type(x))

y = 4
print(type(y))#int
y = y/2
print(type(y))#float
print(y) #2.0

nazwisko = "Kowalski"
print(nazwisko[0])
print(nazwisko[0:3])
print(nazwisko[-2])#k od końca
print(nazwisko[-2:]) #ki
print(nazwisko[0:-2]) #Kowals
print(nazwisko[:-2:2]) #Kwl



print()
