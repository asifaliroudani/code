numbers = [5, 2, 1, 2, 7, 4]
numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

print(numbers.index(5))

print(2 in numbers)

print(numbers.count(2))

numbers.remove(5)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers2.append(100)
print(numbers2)

numbers.pop()
print(numbers)

numbers.clear()
print(numbers)