book = "Romans"
chapter = 2
chapter **= 3
verse = -1
verse = verse + 3

print(book + " " + str(chapter) + ":" + str(verse))
### YOUR CODE STARTS HERE
print("For the law of the Spirit of life has set you free in Christ Jesus from the law of sin and death.")
### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
The program will display... For the law of the Spirit of life has set you free in Christ Jesus from the law of sin and death.
Because, if we write code as print('hello') then this program will display hello.

Line by Line Explanation
Line[1] : Create variable name as "book" and specifies a bible called "Romans" as a String format.
Line[2] : Create variable name as "chapter" and defines a bible chapter "2" as a Int format.
Line[3] : Update "chapter" variable to 2**3(=8) and maintains Int type.
Line[4] : Create variable name as "verse" and defines a bible verse "-1" as a Int format.
Line[5] : Update "verse" variable to -1+3(=2) and maintains Int type.
Line[7] : Update "chapter" and "verse" variable type to String.
          If we do not update variable type to str, then we cannot concat given sentence.
          Python can only concatenate str, not int!
          and, this line specifies the output format as follows: "book" "chapter":"verse"
Line[9] : Print full verse from the Bible(ESV version).
### YOUR EXPLANATION ENDS HERE
"""