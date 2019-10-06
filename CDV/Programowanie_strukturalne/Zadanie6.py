height = int(input('Enter height of your (choinka):'))
space = height-1
text = " "
star = "*"
k=2
n_times = 1
for i in range(1,height+1):
    print(text * space,end='')
    space = space - 1
    print(star * n_times)
    n_times = n_times+2
space = int(n_times/2 - 1)
while k>0:
    print(text * space,end="")
    print("|")
    k=k-1
