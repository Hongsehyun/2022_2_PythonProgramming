search = input("?")

### YOUR CODE STARTS HERE
temp, verse = search.split(":")
temp = temp.split(" ")

chapter = temp.pop()
book = ' '.join(temp)
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
               This code allows you to extract 'verse' immediately.
Line 05      : Split the input string named 'temp' based on ' '.
               This code breaks the string based on ' ' and broken characters are going to include in the list.
Line 07      : Gets the character stored at the end of the list.
               This code allows you to extract 'chapter' immediately.
Line 08      : Converts the values stored in the list to a string.
               If you convert multiple values, this code adds ' ' between the values.
               This code allows you to extract 'book' finally.
Line 11 ~ 13 : Print the splitted variables such as book, chapter and verse.
### YOUR EXPLANATION ENDS HERE
"""