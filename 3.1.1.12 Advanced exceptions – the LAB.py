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


# Final check procedure
#         The captain's name is John
#         The pilot's name is Mary
#         The mechanic's name is Mike
# RocketNotReady exception: "Crew is incomplete", caused by "list index out of range"
# RocketNotReady exception: "Problem with fuel gauge", caused by "division by zero"
# RocketNotReady exception: "Battery check failed", caused by "Battery level too low."

Advanced exceptions - the traceback attribute. Each exception object owns a __traceback__ attribute.
Python allows us to operate on the traceback details because each exception object (not only chained ones) owns a __traceback__ attribute.

What does f.__traceback__ do?
- f.__traceback__ contains the traceback object, which holds information about where the exception occurred.
- Printing it directly shows details about the exception's call stack (i.e., where in the code the error happened).

<traceback object at 0x000001F37196F080>
<class 'traceback'>

#How to Make Traceback Information Useful
import traceback
try:
    1 / 0  # This will cause a ZeroDivisionError
except Exception as e:
    print("Exception occurred!")
    print("Traceback details:")
    traceback.print_tb(e.__traceback__)  # Prints the detailed call stack

Exception occurred!
Traceback details:
  File "d:\Documents\OneDrive - M Baars\BAARS NETSEC CONSULTING\study\python\python academy\pcpp\Untitled-1adad.py", line 4, in <module>
    1 / 0  # This will cause a ZeroDivisionError
    ~~^~~




