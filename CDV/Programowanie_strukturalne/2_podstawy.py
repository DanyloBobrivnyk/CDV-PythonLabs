tekst ="Anna, paweł, TomEK"
tab = tekst.split(", ")
print(tekst)
print(tab)#rozpatrz
print(type(tab)) #list


imie1 = tab[0]
print(imie1)

print("Twoje imie : " + imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)
#sprawdzanie zawartości
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)
print(type(zawartosc))#bool

nazwisko = ""
print(nazwisko.isalpha())


imie = "Julia"
print("\nDane uzytkownika\nMasz na imie :",imie)

text1 ="Jan\n"
text2 ="Nowak"
print(text1 + text2)

text1=text1.rstrip()
print(text1 + text2)
print(text1 +" "+ text2)

#Wyświetlanie łancuchów znaków
text = "%s, Java i %s" % ("PHP","Phyton")
print(text)

#Nowsze versji Phyton'a >2.6

text = "{0}, Java i {1}".format("PHP", "Phyton")
print(text)


#help(text.replace)
new = text.replace("PHP","C#")
print(new)

#wypisanie danych
rok = 2019
miesiac = "marzec"
dzien = 25

print("Data: ",end="")
print(dzien,miesiac,rok)


print("Data: ",end="")
print(dzien,miesiac,rok, sep=" c=3 ")


print()
print('Wiktor najlepszy')
