correct_amount = False
while (correct_amount != True) :
    amount = int(input('Write how many elements you want to sort <1..10> :'))
    if amount<1:
        print('Try to enter another number !')
        continue
    elif amount>10:
        print('Try to enter another number !')
        continue
    else:
        correct_amount = True

loop = 0
array = []
while loop < amount:
    arr_part = int(input(f'Write number [{loop+1}]:'))
    array.append(arr_part)
    loop = loop + 1
print(f'Size of array:{(len(array))}')
print(array)
print('Elements of sorted array:')


for number in range(len(array)-1,0,-1):
    for i in range(number):
        if array[i]>array[i+1]:
            buff = array[i+1]
            array[i+1]=array[i]
            array[i]=buff


print(array)