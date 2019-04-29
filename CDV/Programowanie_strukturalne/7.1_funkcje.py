#Przekazywanie elementow przez referencje
def show(name):
#print(f'Przed modyfikacją: {name}')
    print('Przed modyfikacją:',name)
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacji: {name}')
    print(f'Po modyfikacji: {id(name)}')


data = ['Anna','Agnieszka','Andrzej']

print(f'Przed wywołaniem funkcji show: {data}')
print(f'Id objektu show: {id(data)}')

show(data)
print(f'Po wywołaniu funkcji show: {data}')

    ################## slownik ################

data1 = {

        0:'Artur',
        1:'Andrzej'

}
print(f'\nPrzed wywołaniem funkcji show: {data1}')
show(data1)

    #Przekazywanie argumentów przez wartość

print(f'#############Przekazywanie elementów przez wartość\n')

def show1(city):
    pass
    print(f'Przed modyfikacją: {city}')
    #// print('Przed modyfikacją:',name)
    city[0] = 'Berlin'
    city[1] = 'Bukareszt'
    print(f'Po modyfikacji: {city}')
    print(f'Po modyfikacji: {id(city)}')

miasto = ['Poznań','Gniezno']
print(f'Przed wywołaniem funkcji show1: {miasto}')
print(f'Id objektu show1: {id(miasto)}')
show1(miasto)
print(f'Po wywołaniu funkcji show1: {miasto}')


################## slownik ################
print(f'#############Przekazywanie elementów przez wartość\n')

miasto1 = {0:'Poznań', 1:'Dnipro'}

print(f'Przed wywołaniem funkcji show1: {miasto}')
print(f'Id objektu show1: {id(miasto)}')
show1(miasto)
print(f'Po wywołaniu funkcji show1: {miasto}')









