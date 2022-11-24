success = False
### YOUR CODE STARTS HERE
actual_pw = "2CO8:21"
itr       = 0

while not success:
    pw = input("password: ")
    
    if pw == actual_pw:
        success = True
    else:
        itr = itr + 1
        if itr == 3 : break
### YOUR CODE ENDS HERE
if success:
    print("Access granted!")
else:
    print("Your account is locked.")

"""
### YOUR EXPLANATION STARTS HERE
This program asks user to enter a password.
The output statements are defined separately, when entered correctly and when entered incorrectly(three times).

Line by Line Explanation
Line 01      : Defines the Bool variable to False and Set name as 'success'.

Line 03      : Defines actual password. (Here, I set ground truth password as 2CO8:21")
Line 04      : Defines the variable to count the number of iterations.

Line 06      : Defines an infinite loop.
Line 07      : Ask the user to enter a password.
Line 09 ~ 10 : If the password user enter matches the actual password, replace the bool variable 'success' with True.
               (+) If the boolean variable is true, the infinite loop ends.
Line 11 ~ 12 : If the password entered by the user is different from the actual password, increase the number of attempts(variable name is itr) by 1.
Line 13      : If the user has tried to enter a password three times and failed to enter the actual password, end the infinite loop using 'break' command.

Line 15 ~ 16 : If the user enters the password correctly, the 'success' variable is 'True' and the 'Access granted!' statement is print out.
Line 17 ~ 18 : If the user didn't enters the password correctly, the 'success' variable is 'False' and the 'Your account is locked.' statement is print out.
### YOUR EXPLANATION ENDS HERE
"""