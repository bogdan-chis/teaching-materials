# 1. INPUT
base = float(input("Base fare ($): "))
rate = float(input("Rate per mile ($): "))
total = float(input("Total cost ($): "))

# 2. PROCESSING
dist_cost = total - base
miles = dist_cost / rate

# 3. OUTPUT
print("The client traveled:", miles, "miles.")