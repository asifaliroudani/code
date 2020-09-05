numbers = [1, 2, 3, 3, 4, 4, 5]
number_count = 0
for number in numbers:
    print(f'for number "{number}"')
    number_count = numbers.count(number)
    print(number_count)
    if number_count > 1:
        numbers.remove(number)
        print(f'number {number} is a duplicate. removing it ')
    else:
        print(f'number {number} is not a duplicate.')
print(numbers)
