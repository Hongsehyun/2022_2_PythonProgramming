# Ask the user to enter a radius value.
radius=input("Radius? ")
# Since the 'input radius' is in string format, we must convert variable type to 'float' to calculate the Area.
# And we should use the round function to print only up to the third decimal.
print("Area={}".format(round(float(radius)*float(radius)*3.141592,3)))