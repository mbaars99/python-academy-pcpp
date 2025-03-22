import random

class Vehicle:
    def __init__(self, vin, engine, tires):
        self.vin = vin
        self.engine = engine
        self.tires = tires

class Tires:
    def __init__(self, size):
        self.tyre_size = size
        self.pressure = 0

    def get_pressure(self):
        return self.pressure

    def pump(self):
        self.pressure += 1
        return

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

citycar = Vehicle('VIN1234', Engine("ELECTRIC"), Tires(15))
allterrain = Vehicle('VIN5189', Engine("PETROL"), Tires(18))

print(f"Tyre pressure for {citycar.vin} is: {citycar.tires.get_pressure()}")
for i in range(1, random.randint(1, 50)):
    citycar.tires.pump()
print(f"Tyre pressure after pumping: {citycar.tires.get_pressure()}")

print(f"\nTyre pressure for {allterrain.vin} is: {allterrain.tires.get_pressure()}")
for i in range(1, random.randint(1, 50)):
    allterrain.tires.pump()
print(f"Tyre pressure after pumping: {allterrain.tires.get_pressure()}")

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





    

