import sys

class TimeInterval:

    def __init__(self, hours=0, minutes=0, seconds=0):

            if not (self.time_type(hours) and self.time_type(minutes) and self.time_type(seconds)):
                raise TypeError("Time values must be non-negative integers.") 
            
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
                
    def __add__(self, other):
        #create and return a new instance that will be handeld by the __dunders and eventually python garbage will discard/clean it since it is not assigned to a variable. 
        if isinstance(other, TimeInterval):
            return TimeInterval(seconds=self.total_seconds + other.total_seconds) 
        elif isinstance(other, int) and other >= 0:
            return TimeInterval(seconds=self.total_seconds + other) 
        else:
            raise TypeError("Can only add TimeInterval instances.")
        
    def __sub__(self, other):
        #create and return a new instance that will be handeld by the __dunders and eventually python garbage will discard/clean it since it is not assigned to a variable. 
        if isinstance(other, TimeInterval):
            return TimeInterval(seconds=self.total_seconds - other.total_seconds) 
        elif isinstance(other, int) and other >= 0:
            return TimeInterval(seconds=self.total_seconds - other) 
        else:
            raise TypeError("Can only add TimeInterval instances.")

    def __mul__(self, factor):
        return TimeInterval(seconds=self.total_seconds * factor)

    def __str__(self):
        hours = self.total_seconds // 3600
        minutes = (self.total_seconds % 3600) // 60
        seconds = self.total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def time_type(self, value):
        return True if isinstance(value, int) and value >= 0 else False #the seconds value can be larger than 60

time1 = TimeInterval(21, 58, 50)
print(f"The first time interval is: {time1}")
print('-' * 40)

time2 = time1 + 62
print(f"The result of addition is: {time2}")

time3 = time1 - 62
print(f"The result of substraction is: {time3}")

#use the assert statement to validate if the output of the __str__ method applied to a time interval object equals the expected value.
try:
    assert str(time2) == "21:59:52"
    assert str(time3) == "21:57:48"
except AssertionError:
    print('AssertionError: Something did not add up.....')

# the time interval (tti) is hours=21, minutes=58, seconds=50
# the expected result of addition (tti + 62) is 21:59:52
# the expected result of subtraction (tti - 62) is 21:57:48