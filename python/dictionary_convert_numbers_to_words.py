numbers_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: 'zero'
}

# variables
user_numbers = []
user_numbers_words = ''


user_input = input('Enter Number ')

for digit in user_input:
    user_numbers.append(int(digit))

for user_number in user_numbers:
    if user_number in numbers_dict:
        user_numbers_words += numbers_dict[user_number] + ' '
print(user_numbers_words)