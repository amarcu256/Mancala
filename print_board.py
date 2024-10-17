def printBoard(x,player1Score,player2Score):
    print("  "+str(player1Score))
    for i in range(6):
        print(str(x[i][0])+ "   " + str(x[i][1]))

    print("  "+str(player2Score))
    
my_array = [
    [1, 2],
    [5, 6],
    [9, 10],
    [3, 9],
    [4, 12],
    [7, 2]
]

printBoard(my_array,7,9)
