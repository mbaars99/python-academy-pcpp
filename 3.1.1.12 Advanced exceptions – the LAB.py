class RocketNotReadyError(Exception):
    pass

def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e

def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    try:
        if battery_level < 81:
            raise ValueError('Battery level too low.')
        print('Batteries are charged {}%'.format(battery_level))
    except ValueError as e:
        raise RocketNotReadyError('Battery check failed') from e

def circuits_check():
    try:
        if not circuits_state:
            raise ValueError('Circuits are not 100%.')
        print('Circuit checks are 100%')
    except ValueError as e:
        raise RocketNotReadyError('Problem with circuit check') from e

crew = ['John', 'Mary', 'Mike']
fuel = 100
battery_level = 80
circuits_state = False
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
