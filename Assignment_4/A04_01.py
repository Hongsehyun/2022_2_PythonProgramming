books = [
    "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel",
    "Amos", "Obadiah", "Jonah", "Micah", "Nahum",
    "Habakkuk", "Zephaniah", "Haggai", "Micah", "Zechariah", "Malachi"
]

unique = []
### YOUR CODE STARTS HERE
for book in books:
    if book not in unique:
        unique.append(book)
### YOUR CODE ENDS HERE
print(unique)

"""
### YOUR EXPLANATION STARTS HERE
This program removes duplicate values in the list and prints only unique values.

Line by Line Explanation
Line 01 ~ 05 : Defines a bible list named books.
Line 07      : Defines an empty list named unique.

Line 09      : Repeats the process of storing each element in the list named 'books' in a variable named 'book'.
Line 10 ~ 11 : If the 'book' does not exist in the list called 'unique', add the 'book' to the list called 'unique'.
               Duplicate values are not added to the list called 'unique', so we can expect deduplication by running this code.

Line 13      : Prints out the result of deduplication.
### YOUR EXPLANATION ENDS HERE
"""