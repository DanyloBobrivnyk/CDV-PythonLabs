#Pętla FOR

colors = ['red', 'blue', 'green', 'magneta']
print(colors)
print(type(colors))

for color in colors:
    print(color)

print('\n')

#Wypisz tekst

string = 'CDV - uczelnia ludzi ciekawych'
for litera in string:
    print(litera,end = " ")
print()
#Wypisz liczby od 1 - 10

for number in range(1, 11):
    print(number,end = ' ')

print()

#Wypisz element z listy do momentu wartości 'end','q','quit'

lista = ['a','b','c','d','q','e','quit','end']
for element in lista:
    if element == 'quit':#|| element == 'q' || element == 'end':
        break
        else
        print(element,end = ' ')
