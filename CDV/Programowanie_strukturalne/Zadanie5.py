import random
counter = 0
i = 2
n = int(input('Enter n:'))
def PrimeCheck(n):
    if(n<2):
        return 0
    while(i*i<=n):
        if(n%i==0):
            return 0
    return 1
print(PrimeCheck(n))
# while(counter != 3):
#     a = random.randrange(1,n - 1)
#     if((a**n)%n==a%n):
#         counter = counter + 1
#     else:
#         print("Number is not prime")
#         break;
# if(counter == 5):
#     print("Number is prime")