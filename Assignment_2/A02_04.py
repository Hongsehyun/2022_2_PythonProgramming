animals = ["dog", "cat", "alligator", "cow", "Snake", "elephant", "Chicken"]

### YOUR CODE STARTS HERE
animals = sorted(animals, key=str.casefold)
### YOUR CODE ENDS HERE

print(animals)

"""
### YOUR EXPLANATION STARTS HERE
This program will sort LIST in alphabetical case-insensitive manner.
For example,   if input LIST is ["dog", "cat", "alligator", "cow", "Snake", "elephant", "Chicken"]
               then, this program must return ['alligator', 'cat', 'Chicken', 'cow', 'dog', 'elephant', 'Snake']

Especially,    I noted that the uppercase and lowercase format of the data entered must remain after sorting.
For instance,  if entered data is 'TiGer'
               then output data must be exactly the same as 'TiGer'.

Line by Line Explanation
Line 01      : Define the LIST for sorting.
Line 04      : Sorting given LIST in alphabetical case-insensitive manner.
               For sort, I used python function named 'sorted' and used function command named 'key' to define operating type.
               Here I used 'key=str.casefold'. This means 'removing all case distinctions in the string'.
Line 07      : Print sorted result.

Reference Link : https://stackoverflow.com/questions/10269701/case-insensitive-list-sorting-without-lowercasing-the-result
### YOUR EXPLANATION ENDS HERE
"""