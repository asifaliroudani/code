numbers = [1, 2, 30, 4, 5]

# method:1

numbers.sort()
print(numbers)
print(f'largest no. in number list is {numbers[-1]}')

numbers = [1, 2, 30, 4, 5]

# method:2
print(numbers)
print(f'the largest no. in list is {max(numbers)}')


# method:3

def mymax1(mylist):
    mylist.sort()
    print(mylist)
    max = mylist[0]
    for x in mylist:
        print(x)
        if x > max:
            print(f'x: {x} and max:{max}')
            max = x
    return max


print(f'the largest no. is {mymax1(numbers)}')
