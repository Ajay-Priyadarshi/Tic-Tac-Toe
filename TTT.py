#Player O =  1
#Player X = -1


#ConstBoard function displays the board
def Board(board):
    print("Current State of the Board : \n\n")
    for i in  range(0, 9):
        if((i > 0) and (i % 3) == 0):    #move to next line after 3 spots
            print("\b\b\b\n")
        if(board[i] == 0):
            print("| _ ", end = "")
        if(board[i] == -1):
          print("| X ", end = "")  
        if(board[i] == 1):
          print("| O ", end = "")  
    print("\n\n")

#User 1
def User1Turn(board, u1):
    pos = int(input( u1 + " enter position from [1,2,3,4,5,6,7,8,9] : "))
    #Check if the pos select by user is empty
    if(board[pos-1] != 0):
       print("Wrong Move choose again...\n")
       User1Turn(board, u1)
    board[pos-1] = -1

#User 2
def User2Turn(board, u2):
    pos = int(input(u2 + " enter position from [1,2,3,4,5,6,7,8,9] : "))
    #Check if the pos select by user is empty
    if(board[pos-1] != 0):
       print("\nWrong Move choose again...\n")
       User2Turn(board, u2)
    board[pos-1] = 1

#Computer
def CompTurn(board):
   pos = -1                     #computer choosing best move
   value = -2                   #Starting with worst move    
   for i in range(0, 9):
        if(board[i] == 0):        #If the space is empty 
            board[i] = 1
            score = -minmax(board, -1)     #using minmax stratergy to
            board[i] = 0                   #find best move and store it in score
            if(score > value):
                value = score              #updadtion value with score
                pos = i                    #marking the new pos
   board[pos] = 1

#MinMax Algorithm
def minmax(board, player):
    x = analyzeboard(board)     
    if(x != 0):
       return(x*player)
    pos = -1                     
    value = -2                   
    for i in range(0, 9):
        if(board[i] == 0):        
            board[i] = player
            score = -minmax(board, player*(-1))     
            board[i] = 0                   
            if(score > value):
                value = score              
                pos = i 
    if(pos == -1):             #Draw condition
       return 0
    return value  

#Function to check win condtitions
def analyzeboard(board):
    #The win conditions matrix row, cols, diagonals
    WinCond = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if(board[WinCond[i][0]] != 0 and                      #Line must not be empty
           board[WinCond[i][0]] == board[WinCond[i][1]] and   #First element is  
           board[WinCond[i][0]] == board[WinCond[i][2]]):     #same as rest 2
            return board[WinCond[i][0]]
    return 0            

def main():
    # Choosiing single or multi player
    choice = int(input("\nEnter 1 for Single Player, 2 for Multiplayer : "))
    # Creating board
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #if the choice is 1 ie player vs computer
    if(choice == 1):
      print("Computer : O vs You : X.... ")
      u1 = input("Enter your name : ")
      player = int(input("Enter to player 1st or 2nd : "))
      for i in range(0, 9):
         # Check if someone has won
        if(analyzeboard(board) != 0):
            break
        #Computer's turn
        if((i + player) % 2 == 0):
           CompTurn(board)
        # Player's turn
        else:
            Board(board)      #Displays board
            User1Turn(board, u1) 

   # Player vs Player 
    else:
      u1 = input("Player 1 your name : ")
      u2 = input("Player 2 your name : ")
      player = int(input("Player 2 Enter to play 1st or 2nd : "))
      print("")
      for i in range(0, 9):
         # Check if someone has won
        if(analyzeboard(board) != 0):
            break
        #Player 1 turn
        if((i + player) % 2 == 0):
           Board(board)       #Displays board
           User1Turn(board, u1)
        # Player 2 turn
        else:
            Board(board)
            User2Turn(board, u2)

    #Storing the value of board after both players have played
    b = analyzeboard(board)
    if(b == 0):
       Board(board)
       print("!!! Its a Draw")
    if(choice == 1):
        if(b == -1):
            Board(board)
            print("!!! " + u1 + " Wins the game")
        if(b == 1):
            Board(board)
            print("!!! " + "Computer Wins the game")
    if(choice == 2):
        if(b == -1):
            Board(board)
            print("!!! " + u1 + " Wins the game")
        if(b == 1):
            Board(board)
            print("!!! " + u2 + " Wins the game")

main()     
