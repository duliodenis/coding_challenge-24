# Part 2 - calculate the fuel for the fuel
import math

# 1. Open the data file and read each line into a list
with open('1-data') as f:
    lines = [line.rstrip('\n') for line in open('1-data')]

# declare the accumulator variable
fuel_required = 0

# 2. write a recursive function to calculate the fuel for the fuel
def fuel_for(fuel):
    fuel_required = math.floor(int(fuel)/3) - 2
    # base case if less than or equal to zero
    if fuel_required <= 0 :
        return 0
    else:
        return fuel_required + fuel_for(fuel_required)

# 2. loop thru each line to get the mass and calculate fuel required
for mass in lines:
    fuel = math.floor(int(mass)/3) - 2
    fuel_required = fuel_required + fuel + fuel_for(fuel)

print(fuel_required)
