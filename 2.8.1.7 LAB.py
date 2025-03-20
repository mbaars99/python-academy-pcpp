import random

class Tires:
    def __init__(self, size):
        self.tyre_size = size
        self.pressure = 0

    def get_pressure(self):
        return self.pressure

    def pump(self):
        self.pressure += 1
        return

class Vehicle(Tires):
    def __init__(self, vin, engine, tires):
        super().__init__(tires)
        self.vin = vin
        self.engine = engine

class Engine:
    def __init__(self, fuel):
        self.fuel_type = fuel
        self.state = None 
        
    def start(self):
        self.state = 'MOVING'
        return 

    def stop(self):
        self.state = 'STOP'
        return

    def get_state(self):
        return self.state

citycar = Vehicle('VIN1234', Engine('ELECTRIC'), '15')
allterrain = Vehicle('VIN5189', Engine('PETROL'), '18')

print(f"Tyre pressure for VIN: {citycar.vin} is: {citycar.get_pressure()}")
for i in range(1, random.randint(1, 50)):
    citycar.pump()
print(f"Tyre pressure after pumping: {citycar.get_pressure()}")

print(f"\nTyre pressure for VIN: {allterrain.vin} is: {allterrain.get_pressure()}")
for i in range(1, random.randint(1, 50)):
    allterrain.pump()
print(f"Tyre pressure after pumping: {allterrain.get_pressure()}")

print(f"\nThe state of {citycar.vin} is: {citycar.engine.get_state()}")
citycar.engine.start()
print(f"The state of {citycar.vin} is: {citycar.engine.get_state()}")
citycar.engine.stop()
print(f"The state of {citycar.vin} is: {citycar.engine.get_state()}")

print(f"\nThe state of {allterrain.vin} {allterrain.engine.fuel_type} is: {allterrain.engine.get_state()}")
allterrain.engine.start()
print(f"The state of {allterrain.vin} {allterrain.engine.fuel_type} is: {allterrain.engine.get_state()}")
allterrain.engine.stop()
print(f"The state of {allterrain.vin} {allterrain.engine.fuel_type} is: {allterrain.engine.get_state()}")





    

