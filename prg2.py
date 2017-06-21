def getNQueen(board,col,n):
    if(col == n):
        print(board)
        return True
    for i in range(0,n):
        if(isSafe(board,i,col,n)):
            board[i][col] = col+1
            getNQueen(board,col+1,n)
            board[i][col] = -1
    return False

def isSafe(board,row,col,n):
    for i in range(0,col):
        if(board[row][i] != -1):
            return False
    i = row
    j = col
    while(i>=0 and j >=0):
        if(board[i][j] != -1):
            return False
        i-=1
        j-=1
    i = row
    j = col
    while(i<n and j>=0):
        if(board[i][j] != -1):
            return False
        i+=1
        j-=1
    return True
    

def getBoard(n):
    board = [[]];
    board = [[-1 for i in range(n)] for i in range(n)]
    col = 0
    getNQueen(board,col,n)

def main():
    n = 6
    getBoard(n)
    
if __name__ == "__main__": main()