scores = [
    25, 32, 55, 0, 61,
    24, 89, 88, 53, 64,
    58, 80, 2, 4, 44,
    30, 6, 50, 37, 82,
    95, 22, 82, 86, 10,
    5, 70, 94, 27, 32,
    13, 63, 79, 1, 57,
    99, 55, 22, 87, 39,
    87, 17, 64, 63
]

new_score = input("Score? ")
### YOUR CODE STARTS HERE
scores.append(int(new_score))
print("Average = {}".format(sum(scores)/len(scores)))
### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
This program will display the average value of 'scores' which type is LIST

Line by Line Explanation
Line 01 ~ 11 : Create LIST name as 'scores' and typed 44 values in it.
Line 13      : Ask user to enter a one score(assume that users always enter some integers between 0 and 100).
Line 15      : Change the variable type to INT and add the variable(new_score) to the LIST called 'scores'
               Because, the type of variable received as 'input' function is string, so it must be converted to INT.
Line 16      : Calculate and Print the average of LIST named 'scores'.
               To Calculate average, I used 'len' and 'sum' function which return length and sum result of all values in the LIST.
### YOUR EXPLANATION ENDS HERE
"""