search = input("?")

### YOUR CODE STARTS HERE
book_chapter, verse = search.split(":")

if len(book_chapter.split(" "))==2:
    book, chapter = book_chapter.split(" ")
else:
    book_1, book_2, chapter = book_chapter.split(" ")
    book = book_1 + " " + book_2
### YOUR CODE ENDS HERE

print("Book =", book)
print("Chapter =", chapter)
print("Verse =", verse)

"""
### YOUR EXPLANATION STARTS HERE
This program will extract and display Book&Chapter&Verse from the entered String named 'search'

Line by Line Explanation
Line 01      : Ask user to enter a Book&Chapter&Verse String.
               Example format  :  Psalm 23:4
                               :  2 Corinthians 6:10  
Line 04      : Split the input string named 'search' based on ':'.
Line 06 ~ 07 : Split the input string named 'book_chapter' based on ' ' and return the number of splitted words.
               And, if the number of splitted words is 2, I defined splitted word's variable name as 'book' and 'chapter'.
Line 08 ~ 10 : If the number of splitted words is not 2, I defined splitted word's variable name as 'book_1', 'book_2' and 'chapter'.
               And, I defined the printing format as (book_1 + " " + book_2) for variable named 'book'
Line 13 ~ 15 : Print the splitted variables such as book, chapter and verse.
### YOUR EXPLANATION ENDS HERE
"""