def read_test_data(filename):
    data = []
    with open(filename, "rt") as fin:
        lines = fin.read().strip().split("\n")
        for line in lines:
            row = line.split(" ")
            data.append(row)
    return data
    
def display_board(data):
    for row in data:
        print(" ".join(row))

tic_tac_toe = read_test_data(filename="test-data.txt")
print("== 3x3 Matrix (a list in a list) ==")
print(tic_tac_toe)
print()
print("== Tic-Tac-Toe Board ==")
display_board(tic_tac_toe)

### YOUR CODE STARTS HERE
marker_type = ["O", "X"]
winner_flag = 0

for marker in marker_type:
    if ((tic_tac_toe[0][0] == tic_tac_toe[0][1] == tic_tac_toe[0][2] == marker) or \
        (tic_tac_toe[1][0] == tic_tac_toe[1][1] == tic_tac_toe[1][2] == marker) or \
        (tic_tac_toe[2][0] == tic_tac_toe[2][1] == tic_tac_toe[2][2] == marker) or \
        (tic_tac_toe[0][0] == tic_tac_toe[1][0] == tic_tac_toe[2][0] == marker) or \
        (tic_tac_toe[0][1] == tic_tac_toe[1][1] == tic_tac_toe[2][1] == marker) or \
        (tic_tac_toe[0][2] == tic_tac_toe[1][2] == tic_tac_toe[2][2] == marker) or \
        (tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] == marker) or \
        (tic_tac_toe[0][2] == tic_tac_toe[1][1] == tic_tac_toe[2][0] == marker)) :
        winner = marker
        winner_flag += 1
    
if winner_flag == 0:
    print("Draw!")
elif winner_flag == 1:
    print("{} won!".format(winner))
else:
    print("Error! There are 2 winners.")
### YOUR CODE ENDS HERE

"""
### YOUR EXPLANATION STARTS HERE
This program prints the winner of Tic-Tac-Toe game written at the 'test-data' file.

Line by Line Explanation
Line 01 ~ 08 : This function reads Tic-Tac-Toe game data from '.txt' file as n by n matrix format(basically, a list in a list).
             └ Line 01 : Create Function named 'read_test_data' and parameter is filename.
             └ Line 02 : Create List named 'data'
             └ Line 03 : Open the file and Specifies the object as 'fin'.
                         Especially, python provides 'with ~ as ~' syntax. This syntax automatically close the object when 'with ~ as ~' syntax end.
                         And here, We used 'rt' option and this has the following meanings: 'r' = open for reading (default)
                                                                                            't' = text mode (default)
             └ Line 04 : Read the file, Remove spaces that exist at both ends and Split based on "\n".
             └ Line 05 : This loop executes n times in total.
                         This loop reads one line at each time just like 'O X X', 'O X O', 'X O X' etc.
             └ Line 06 : Split based on " " and save split result to variable named 'row'(list format).
             └ Line 07 : Append 'row' variable to list named 'data'.
             └ Line 08 : Return the list named 'data'.

Line 10 ~ 12 : This function prints 2 dimension matrix.
             └ Line 10 : Create Function named 'display_board' and parameter is data(list format).
             └ Line 11 : This loop executes n times in total.
                         This loop reads one List line at each time just like '['O', 'X', 'X']', '['O', 'X', 'O']', '['X', 'O', 'X']' etc.
             └ Line 12 : Converts the values stored in the list to a string.
                         If converting multiple values, this code adds ' ' between the values.

Line 14      : Reads 'test-data.txt' file as n by n matrix format(basically, a list in a list).
               At this assignment, Tic-Tac-Toe game size is always 3 by 3.
Line 15 ~ 19 : Print Tic-Tac-Toe 3 by 3 Matrix.

Line 22      : Define marker type in List format. There are two marker type: O and X.
Line 23      : Define flag variable. This variable distinguishes when there are no winners or only one winner or two winners.
               0 Winner Case = DRAW
               1 Winner Case = Winner is 'X' or 'O'.
               2 Winner Case = ERROR. Winner must be only one.
Line 25      : This loop executes 2 times in total.
               First,  check if 'O' is winner.
               Second, check if 'X' is winner.
Line 26 ~ 33 : The number of cases to win a Tic-Tac-Toe game is 8.
               For each case to win, check whether 'X' won or 'O' won.
Line 34      : If there is winner, save the winner marker to variable named winner.
Line 35      : If there is winner, raise the flag value by 1.

Line 37 ~ 38 : If flag value is 0, it means there are no winner, thus just print "Draw!".
Line 39 ~ 40 : If flag value is 1, it means there is only one winner, thus just print out who is the winner.
Line 41 ~ 42 : If flag value is 2, it means there are two winners, thus just print "Error! There are 2 winners.".
### YOUR EXPLANATION ENDS HERE
"""