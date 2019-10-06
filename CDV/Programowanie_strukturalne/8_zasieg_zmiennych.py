#Zasięg zmiennych ,zmienne lokalne i globalne

#precyzja liczby (Zakrąglenie do trzech miejsc po przecinku)
# 5 : 5.000

x = "{0:.3f}".format(5)
print(x)

def plnToChf(value):
    kursChf = 3.7913
    iloscChf = value / kursChf
    iloscChf = "{0:.4f}".format(iloscChf)
    print(iloscChf)
plnToChf(1000)



###Utworz funkcje zwracającą ilość Euro jaką klient może kupić za PLN
def plnToEUR(value):
    kursEUR = 0.2329
    iloscEUR = value / kursEUR
    ilocsEUR = "{0:.4f}".format(iloscEUR)
    print(iloscEUR)
plnToEUR(100)


#Zmienna globalna
kursUSD = 4.00
print(f'Id USD: {id(kursUSD)}')

def plnToUSD(value):
#kursUSD = 3.7899
    iloscUSD = value / kursUSD
    ilocsUSD = "{0:.4f}".format(iloscUSD)
    print(f'Id USD wewnątrz funkcji:{id(kursUSD)}')
    return iloscUSD

print(f'\nKurs dolara: {kursUSD}')
pln = input('Podaj kwotę PLN jakie chcesz zamienić na USD: ')
usd = plnToUSD(float(pln))
print(f'ilość {pln} PLN = {usd} USD')
print(f'\nKurs dolata po wywołąniu funkcji: {kursUSD}')



