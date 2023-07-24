StorageSize = int(input("Enter the amount of GBs your SSD has: "))
Years = int(input("Enter the amount of guaranteed years you would like: "))

math = StorageSize * 1000
math = math / Years
math = math / 365

print("You would be able to achieve", math, "GB per day to not exceed your SSD estimated lifespan in", Years, "years.")