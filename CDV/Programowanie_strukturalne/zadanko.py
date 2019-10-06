
print("Enter your age:",end=" ")
age = int(input())
WeightList = {
    "Niedowaga":"<18,5",
    "Waga normalna":"18,5-24",
    "Lekka nadwaga":"24-26,5",
    "Nadwaga":">26,5",
    "Otyłość 1 stopnia:":"30-35",
    "Otyłość 2 stopnia:":"30-40",
}
if(age > 100):
    print("i DON'T BELIVE YOU")
elif(age < 18):
    print(f"You're not grown up, there is {18 - age} years left")
elif(age > 18):
    print("You're grown up,cool.")

print("\nWprowadz swoja wagę:",end=" ")
waga = int(input())
for key,value in WeightList.items():
    print(f"{key} : {value}")
if(waga>=18.5 and waga <= 26.5):
    print("it's ok")
elif(waga < 18.5 ):
    print("eat more")
else:
    if(waga>26.5 and waga<=35):
        print("Overweight 1-st lvl")
    else:
        print("Overweight 2-nd lvl")
print("Sorting numbers->\nEnter A: ",end =" ")
a = int(input())
print("Enter B: ",end =" ")
b = int(input())
print("Enter C: ",end =" ")
c = int(input())
tab = [a,b,c]
tab = sorted(tab)
print(tab)
print(f"Max: {max(tab)}, Min: {min(tab)}")

dict_imiona={
     "Anna" : "zenskie",
    "Julia" : "zenskie",
    "Zofia" : "zenskie",
    "Maja" : "zenskie",
    "Hania" : "zenskie",
    "Maria" : "zenskie",
    "Stanisława" : "zenskie",
    "Michał" : "meskie",
    "Antoni" : "meskie",
    "Jan" : "meskie",
    "Franciszek" : "meskie",
    "Piotr" : "meskie",
    "Wiktor" : "meskie",
"Wawrzyniec" : "meskie"
}
name = input("podaj imie:")
if(name in list(dict_imiona.keys())):
    print(f'to imię{dict_imiona[name]}')
else:
    print('tego imienia nie mam,podaj gender:')
    gender = input("m lub z ?")
    if(gender == 'm'):
        dict_imiona[name] = "meskie"
    else:
        dict_imiona[name] = 'zenskie'

for key,value in dict_imiona.items():
    print(f"{key} : {value}")

wysokosc = int(input())
char = '#'
while(wysokosc != 0):
    print(char * wysokosc)
    wysokosc = wysokosc - 1