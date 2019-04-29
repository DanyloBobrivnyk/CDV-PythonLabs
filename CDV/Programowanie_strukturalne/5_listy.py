programowanie = ['Python','PHP','C#','JS','JAVA']
print(programowanie[0])

#trzy elementy

print(programowanie[0:3])
#ostatni

print(programowanie[-1])
#dodawanie ostatniego na koniec listy

programowanie.append('R')
programowanie.append('Python')
print(programowanie[-2])

#zliczanie elementów w liście
print(programowanie.count('Python'))

#ilość elementów w liście
print('Liczba elementów :',len(programowanie))

#połączenie listy
inneJezyki = ['C','C++']

programowanie.extend(inneJezyki)
print(programowanie)

#czyszczenie listy
nowa = programowanie
print('Nowa :',end="")
print(nowa)
#czyści obie listy
nowa.clear()
print('Lista czysta :',nowa)
print(programowanie)