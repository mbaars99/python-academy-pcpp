#in v1 version still using seconds_to_hours_notation() which ideally should be handeled by a better __str method

import sys

class TimeInterval:

    def __init__(self, hours, minutes, seconds):

            if not (self.time_type(hours) and self.time_type(minutes) and self.time_type(seconds)):
                raise TypeError("Time values must be non-negative integers.") 
            
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
                
    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval instances.")
        return self.seconds_to_hours_notation(self.total_seconds + other.total_seconds)
        
    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval instances.")
        return self.seconds_to_hours_notation(self.total_seconds - other.total_seconds)

    def __mul__(self, factor):
        return self.seconds_to_hours_notation(self.total_seconds * factor)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def time_type(self, value):
        return True if isinstance(value, int) and value >= 0 and value < 60 else False

    def seconds_to_hours_notation(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

time1 = TimeInterval(21, 58, 50)
time2 = TimeInterval(1, 45, 22)

print(f"The first time interval is: {time1}")
print(f"The second time interval is: {time2}")
print('-' * 40)
print(f"The result of addition is: {time1 + time2}")
print(f"The result of substraction is: {time1 - time2}")
print(f"The result of multiplication is: {time1 * 2}")

