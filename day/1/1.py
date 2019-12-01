import math

# 1. Open the data file and read each line into a list
with open('1-data') as f:
    lines = [line.rstrip('\n') for line in open('1-data')]

# declare the accumulator variable
fuel_required = 0

# 2. loop thru each line to get the mass and calculate fuel required
for mass in lines:
    fuel_required = fuel_required + math.floor(int(mass)/3) - 2
print(fuel_required)
