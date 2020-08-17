secret = 9
guess_count = 3

while guess_count > 0:

    print(guess_count, secret)
    answer = int(input('enter the secret no.'))
    guess_count -= 1
    if answer == secret:
        print(f'you answer {answer} is correct')
        break
else:
    print('try again')