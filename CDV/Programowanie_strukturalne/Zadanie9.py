
def SieveOfEratostehens(n):
    prime = [True for i in range(n+1)]
    p = 2
    tmp = 0
    while(p*p <= n):
        if(prime[p] == True):
            #Update all multiples for p
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    if prime[n] != True:
        print(f'{n} is not prime')
    else:
        for p in range(n+1):
            if prime[p]:
                print(p,end=',')
n = int(input('Enter the number:'))

SieveOfEratostehens(n)

