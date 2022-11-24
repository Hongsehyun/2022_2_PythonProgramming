x = input("x = ")
y = input("y = ")
### YOUR CODE STARTS HERE
temp = x
x    = y
y    = temp
### YOUR CODE ENDS HERE
print("## Swapped")
print("x =", x)
print("y =", y)

"""
### YOUR EXPLANATION STARTS HERE
The program will display... Swapping value of x and y.
For example, if x=3 and y=33, then this program will display x=33 and y=3.

Because, I created a temporary storage variable to swap two numbers.
When we overwrite the value of 'y' on 'x', lose the value of the existing 'x'. So we need a temporary storage variable to store the existing 'x' value.
### YOUR EXPLANATION ENDS HERE
"""