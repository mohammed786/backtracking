cX = [1,2,-1,-2,1,-2,-1,2]
cY = [2,1,-2,-1,-2,1,2,-1]

def fillBoard(board,x,y,count,n):
    for i in range(0,8):
        if(x+cX[i] < n and y+cY[i] < n and x+cX[i]>=0 and y+cY[i]>=0):
            if(board[x+cX[i]][y+cY[i]] == -1):
                board[x+cX[i]][y+cY[i]] = count
                fillBoard(board,x+cX[i],y+cY[i],count+1,n)
                board[x+cX[i]][y+cY[i]] = -1
    print(x,y,count, board)
    exit(0)
    return
#        if((x+cX[i] < n and y+cY[i] < n) and (x+cX[i] >= 0 and y+cY[i] >= 0)):
#            if(board[x+cX[i]][y+cY[i]] == -1):
#                board[x+cX[i]][y+cY[i]] = count
#                fillBoard(board,x+cX[i],y+cY[i],count+1,n)
#    board[x+cX[i]][y+cY[i]] = -1
                    
def getBoard(n):
    board = [[]];
    board = [[-1 for i in range(n)] for i in range(n)]
    count = 0
    x = 0;
    y = 0;
    fillBoard(board,x,y,count,n)
    print(board)
def main():
    n = 8
    getBoard(n)
    
if __name__ == "__main__": main()
    

[[-1, 20, 31, -1, 25, -1, -1, -1],
 [32, -1, 0, 21, 30, -1, 24, -1], 
 [19, 44,33, 26, 1, 22, 29, -1], 
 [-1, -1, 18, 45, 34, 27, 2, 23], 
 [43, 12, -1, -1, 17, 4, 35, 28], 
 [-1, 9, 40, 13, 6, 37, 16, 3], 
 [11, 42, -1, 8, 39, 14, 5, 36], 
 [-1, -1, 10, 41, -1, 7, 38, 15]]