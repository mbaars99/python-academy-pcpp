class TimeInterval:

    def __init__(self, hours=0, minutes=0, seconds=0):

            if not (self.time_type(hours) and self.time_type(minutes) and self.time_type(seconds)):
                raise TypeError("Time values must be non-negative integers.") 
            
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
                
    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval instances.")
        return TimeInterval(seconds=self.total_seconds + other.total_seconds) 
    #create and return a new instance that will be handeld by the __dunders and eventually python garbage will discard/clean it since it is not assigned to a variable.
        
    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval instances.")
        return TimeInterval(seconds=self.total_seconds - other.total_seconds)

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
time2 = TimeInterval(1, 45, 22)

print(f"The first time interval is: {time1}")
print(f"The second time interval is: {time2}")
print('-' * 40)
print(f"The result of addition is: {time1 + time2}")
print(f"The result of substraction is: {time1 - time2}")
print(f"The result of multiplication is: {time1 * 2}")

#use the assert statement to validate if the output of the __str__ method applied to a time interval object equals the expected value.
assert str(time1 + time2) == "23:44:12"
assert str(time1 - time2) == "20:13:28"
assert str(time1 * 2) == "43:57:40"

