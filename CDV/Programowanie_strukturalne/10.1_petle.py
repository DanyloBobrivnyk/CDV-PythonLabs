#pętle zadania
#
#Podaj wartosc początkową i końcową, która będzie
#wypisana w porządku malejącym

x = int(input('Podaj x:'))
y = int(input('Podaj y:')) - 1

if y>x:
    pom = x
    x = y + 1
    y = pom - 1

for number in range(x, y, -1):
    #print(number,end=' ')
    print(f'{number}',end =' ')
    #print(f'->:{number}')
print()
#Dwie pętli

for value in range(1,6):
    for j in range(1,value+1):
        print('*', end='')
    print()

#zrobić to za pomocą jednej for
#Użytkownik pokaże znak dla wypisu i ilość wierszy

i = 1
ilosc = int(input('Podaj ilość wierszy: '))+1  #Bo cycle for goes from 1 to variable ILOSC
znak = input('Podaj znak: ')
print()

for i in range(1,ilosc):
    print(znak * i)
    i = i+1

print()

#Zadanie#########################################################
a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
Suma = a + b
if Suma ==0:
    print("Sproba dzielenia przez zero")
else:
    dzialanie = (a*a + b)/((a+b)*(a+b))
if Suma != 0:
    print(f'Wartość wyrażenia wynosi: {dzialanie}')

#try except
##################################
school = 'CDV Poznan'

for character in school:
    if character == 'V' or character == ' ':
        continue
    else:
        print(character,end=" ")
print()

#Pętla while
#####################
x = 10
while x>0:
    x = x - 1
    if x == 6:
        continue
    print(f'{x}',end = ' ')
print()
print("->Koniec programu !")

#Zadanie
#################
import os
os.system('cls')
proba = 0
while (proba < 3):
    proba = proba + 1
    password = input('Podaj haslo: ')
    if(password == 'okon'):
        print(f"Podales prawidlowe haslo za {proba} razy !")
        break
    if(proba == 0):
        print("Limit prob zostal skonczony!")
    else:
        continue

