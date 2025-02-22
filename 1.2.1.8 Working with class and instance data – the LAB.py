import random

weight_limit = 300
quantity = 1000
store_product = []

class Apple:

    counter = 0
    total_weight = 0.0

    def __init__(self):
        self.weight = random.uniform(0.2, 0.4)
        Apple.total_weight += self.weight
        Apple.counter += 1

    def stop_packaging(self):
        pass # dummy for stopping packaging process
        if Apple.counter >= quantity:
            print("Packaging stopped: Maximum quantity reached")
        elif Apple.total_weight + 0.2 >= weight_limit:
            print("Packaging stopped: Weight limit exceeded")
        else:
            print("Packaging stopped: ()")

while Apple.counter < quantity and Apple.total_weight + 0.2 < weight_limit:
    store_product.append(Apple())
    
if store_product:
    store_product[0].stop_packaging()

print(f"Number of apple class objects created: {Apple.counter}")
print(f"The total weight of apple class objects created: {round(Apple.total_weight, 3)}")







    

 