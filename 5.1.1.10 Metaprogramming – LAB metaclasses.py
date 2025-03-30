import time
import random

def get_instantiation_time(cls):
    return cls.instantiation_time

class My_Meta(type):
    instantiation_log = []

    def __new__(mcs, name, bases, dictionary):
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = classmethod(get_instantiation_time)
    
        obj = super().__new__(mcs, name, bases, dictionary)
        time.sleep(random.random()) #add delay for different timestamp
        obj.instantiation_time = time.time()
        mcs.instantiation_log.append([obj.__name__, obj.instantiation_time])
        return obj
    
#self → instance of a class, cls → the class itself, mcs → the metaclass

class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    pass

myobj1 = My_Class1()
myobj2 = My_Class2()
print("My_Class1 instantiation_time:", My_Class1.get_instantiation_time())
print("My_Class2 instantiation_time:", My_Class2.get_instantiation_time())
 
print("\nInstantiation Log:")
for entry in My_Meta.instantiation_log:
    print(f"Class: {entry[0]}, Timestamp: {entry[1]}")
