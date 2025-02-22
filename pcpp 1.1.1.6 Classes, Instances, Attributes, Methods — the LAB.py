import random

class MobilePhone():

    def __init__(self, number):
        self.number = number

    def turn_on(self):
        print(f"mobile phone {self.number} is turned on")
        return
    
    def turn_off(self):
        print("mobile phone is turned off")
        return
    
    def call_number(self, number):
        print(f"calling {number}")
        return
    
def random_number(): # preferred for clarify over lambda
    return f"{random.randint(0,99999):05d}-{random.randint(0,999999):06d}"

mobile1 = MobilePhone(random_number())

random_number_lambda = lambda: str(random.randint(0,99999)).zfill(5) + "-" + str(random.randint(0,999999)).zfill(6)
mobile2 = MobilePhone(random_number_lambda())

mobile1.turn_on()
mobile2.turn_on()

mobile1.call_number(random_number())

mobile1.turn_off()
mobile2.turn_off()




        
    
