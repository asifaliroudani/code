user_input = ''
user_last_input = ''

while user_input != 'quit':
    user_input = input('what shall I do: ').lower()
    if user_input == 'help':
        print('start - to start the car')
        print('stop - to stop the cat')
        print('quit - to exit')
    elif user_input == 'start' and user_input != user_last_input:
        print('Car started... Ready to go')
        user_last_input = user_input
    elif user_input == 'stop' and user_input != user_last_input:
        print('Car stopped.')
        user_last_input = user_input
    elif user_input == 'start' and user_input == user_last_input:
        print('Car already started')
    elif user_input == 'stop' and user_input == user_last_input:
        print('Car already  stopped.')
    elif user_input == 'quit':
        break
    else:
        print("I don't understand that...")
