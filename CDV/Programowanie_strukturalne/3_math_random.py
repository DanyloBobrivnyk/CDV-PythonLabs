# liczba pi
import math
pi = math.pi
print(pi)

# pierwiastek
pierw = math.sqrt(9)#Korień
print(pierw)

#moduł random

import random
losuj = random.random()
print(losuj)

losujZlisty = random.choice([1,2,33,4])
print(losujZlisty)

'''
Użytkownik podaje z klawiatuy 2 wartości, min i maks z przedziału z którego będzie losowane 5 liczb całkowitych
Liczby wyświetl w formacie Liczba 1... Liczba 2... Liczba 3... (DO DOMU)
'''
#Zadanie
print("Podaj min wartość :",end=" ")
minWartosc = input()
minWartosc = int(minWartosc)

print("\nPodaj max wartość:",end=" ")
maxWartosc = input()
maxWartosc = int(maxWartosc)

Lista = [minWartosc]
print("minWartosc type :",type(minWartosc))
a = minWartosc

while(a<maxWartosc):
        a = a + 1
        Lista.append(a)
print(Lista)
a=0
print("Losowane liczby z listy:")
while(a != 5):
    a = a + 1
    losujZlisty = random.choice(Lista)
    print(f'Liczba({a}):',losujZlisty)

