import copy

warehouse = [
    ("Lolly Pop", 0.4, 133),
    ("Licorice", 0.1, 251),
    ("Chocolate", 1, 601),
    ("Sours", 0.01, 513),
    ("Hard candies", 0.3, 433)
] # name, price, weight

class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name:<12} | Price: {self.price:>6.2f} | Weight: {self.weight:>4}"

# Used string formatting to ensure consistent spacing:
# :<12 → Left-aligns names (Lolly Pop etc.), width = 12
# :>6.2f → Right-aligns prices with 2 decimal places, width = 6
# :>4 → Right-aligns weight values with width = 4

treat = []

for name, price, weight in warehouse:
     treat.append(Delicacy(name, price, weight))

print('#treat original')
for item in treat:
    print(item)

treat_copy = copy.copy(treat)
treat_deepcopy = copy.deepcopy(treat)

print('\n#price change in treat')
for item in treat:
    item.price = 0

for item in treat:
    print(item)

print('\n#price change visible in treat_copy?')
for item in treat_copy:
    print(item) # Will show price = 0 because it's a shallow copy         

print('\n#price change visible in treat_deepcopy?')
for item in treat_deepcopy:
    print(item)   

