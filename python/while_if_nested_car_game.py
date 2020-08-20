user_input = ''
started = False

while True:
    user_input = input('what shall I do: ').lower()
    if user_input == 'help':
        print('start - to start the car')
        print('stop - to stop the cat')
        print('quit - to exit')
    elif user_input == 'start':
        if started:
            print("car is already started")
        else:
            started = True
            print('Car started... Ready to go')
    elif user_input == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            print('Car stopped.')
            started = False
    elif user_input == 'quit':
        break
    else:
        print("I don't understand that...")