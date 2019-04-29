import os
def wyswietl1(num1,num2):
    print(f'Licba 1 : {num1}')
    print(f'Licba 2 : {num2}')


wyswietl1(2,4)



############## *args ###############


print('############## *args ###############')

def wyswietlArgs(num1, *args):
    print(f'Licba 1 : {num1}')
    for i in args:
        print(f'Następna wartość: {i}')

wyswietlArgs(1,12,1000,121,111)


#####################
imiona = ['Anna','Jan','Paweł']
wyswietlArgs(imiona)
wyswietlArgs(*imiona)

os.system('cls')
############## *kwargs ###############

print('############## *kwargs ###############')
print('cls')

def pracownik(**kwargs):
    for key,val in kwargs.items():
        print(f'Klucz {key},Wartość {val}')

pracownik1 = {
    'imie':'Janusz',
    'nazwisko':'Kowalski',
    'wiek':21,
    'UmowaOPrace':True
}

pracownik(**pracownik1)
#Dwie gwiazdki są ważliwe !
