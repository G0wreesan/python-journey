import random

vehicles =["Car", "Truck", "Motorcycle", "Bus", "Bicycle"]
random_vehicle = random.choice(vehicles)
print(random_vehicle)
random_vehicle = vehicles[random.randint(0, len(vehicles)-1)]
print(random_vehicle)
random_vehicle = vehicles[random.randrange(len(vehicles))]
print(random_vehicle)