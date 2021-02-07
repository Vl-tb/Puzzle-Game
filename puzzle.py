'''
This module contains functions.https://github.com/Vl-tb/Puzzle-Game
'''
def check_horizontally(board: list) -> bool:
    '''
    This function checks if every line of board has no repetitions
    of same numbers and returns True or False, depending on board.
    '''
    for i in range(len(board)):
        lst = list(board[i])
        for j in range(len(lst)):
            if (lst[j] != "*" and lst[j] != " "
            and lst.count(lst[j]) > 1):
                return False
    return True

def check_vertically(board: list) -> bool:
    '''
    This function checks if every column of board has no repetitions
    of same numbers and returns True or False, depending on board.
    '''
    lst = []
    for i in range(len(board)):
        lst.extend(list(board[i]))
    i = 0
    while i < 9:
        line = ''
        for j in range(i,len(lst),9):
            line+=lst[j]
        board[i] = line
        i +=1
    return check_horizontally(board)



def check_color(board: list) -> bool:
    '''
    This function checks if every one-color section of board has no repetitions
    of same numbers and returns True or False, depending on board.
    >>> check_color([\
"****4****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     945 ",\
" 6  83  *",\
"3   5  **",\
"  8  2***",\
"  2  ****"\
])
    False
    '''
    i = len(board[0])-5
    j = 0
    koef_1 = 5
    koef_2 = 0
    while True:
        line = ""
        while j < koef_1:
            line += board[j][i]
            j+=1
        j -=1
        i +=1
        while i < len(board[0]) - koef_2:
            line += board[j][i]
            i +=1
        lst = list(line)
        for t in range(9):
            if lst[t] !=" " and lst[t] !="*" and lst.count(lst[t]) > 1:
                return False
        j-=3
        i-=6
        koef_1 +=1
        koef_2 +=1
        if i < 0:
            return True
def validate_board(board: list) -> bool:
    '''
    This is main function, which returns True, if board is ready for
    start and False otherwise.
    >>> validate_board([\
"****4****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     945 ",\
" 6  83  *",\
"3   5  **",\
"  8  2***",\
"  2  ****"\
])
    False
    '''
    if (check_color(board) and check_horizontally(board)
    and check_vertically(board)):
        return True
    return False
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(check_horizontally([
 "1***2***1",
 "***16****",
 "** 23****",
 "* 431****",
 "   679458",
 " 6 18324*",
 "3   5  **",
 "  8  2***",
 "  2  ****"
]))