commandz = ['Start - car will start',
            'Stop  - car will stop',
            'Quit  - will exit the program']
state = ''
posi = ''

while True:

    state = input('>').lower()
    if state == 'start':
        if posi == 'started':
            print('car already started ')
        else:
            print('Car has started')
            posi = 'started'

    elif state == 'stop':
        if posi == 'stopped':
            print('car has already stopped')
        else:
            print('Car has stopped')
            posi = 'stopped'

    elif state == 'help':
        for item in commandz:
            print(item)
    elif state == 'quit':
        break
    else:
        print('Does not recognise this statement')

# print(commands[0])
