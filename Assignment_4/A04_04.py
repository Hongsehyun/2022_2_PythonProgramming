records = [["John", 90, 80, 79], ["Daniel", 84, 99, 91], ["Isaiah", 95, 80, 72]]
transcripts = {}
### YOUR CODE STARTS HERE
for idx in range(len(records)):
    transcripts[records[idx][0]]=sum(records[idx][1:])/len(records[idx][1:])
### YOUR CODE ENDS HERE
for name, avg in transcripts.items():
    print(f"{name}'s average = {avg:.2f}")
    
"""
### YOUR EXPLANATION STARTS HERE
This program stores each student's name and average score in the transcripts dictoinary and prints out the dictionary.

Line by Line Explanation
Line 01      : By using the nested list, defines a data table of 3 by 4.
Line 02      : Defines dictionary variable named transcripts.

Line 04      : Performs as many iterations as the number of rows.
               Since the index starts at 0, I used 'range' function to access the index.
Line 05      : The first column is the name of the student corresponding to 'Key', so I defined it as 'transcripts[ records[idx][0]'.
               Since the 'Value' correspond to the values from the second column to the end column, the average was calculated using the formula 'sum/len'.
               
Line 07      : When the 'item()' function is applied to the dictionary format, it returns 'Key' and 'Value'.
Line 08      : Defines the type of output, and sets the average to output only to the second decimal point.
### YOUR EXPLANATION ENDS HERE
"""    