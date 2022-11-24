score1 = input("Score 1= ")
score2 = input("Score 2= ")
score3 = input("Score 3= ")
score4 = input("Score 4= ")
### YOUR CODE STARTS HERE
scores = [int(score1), int(score2), int(score3), int(score4)]
scores.sort()
scores.remove(scores[0])
print("Average = {}".format(sum(scores)/len(scores)))
### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
This program will remove lowest score and display the average value of 'scores' which type is LIST

Line by Line Explanation
Line 01 ~ 04 : Ask user to enter a four scores(assume that users always enter some integers between 0 and 100).
Line 06      : Change the variable type to INT and Create a LIST named 'scores' containing four values entered by user.
               Because, the type of variable received as 'input' function is string, so it must be converted to INT.
Line 07      : Sort the LIST named 'scores' (sort in ascendig order)
Line 08      : Removes the value located in the first index of LIST named 'scores'.
               It means, Removing the lowest value in LIST named 'scores' because I already sorted the LIST.
Line 09      : Calculate and Print the average of LIST named 'scores'.
               To Calculate average, I used 'len' and 'sum' function which return length and sum result of all values in the LIST. 
### YOUR EXPLANATION ENDS HERE
"""