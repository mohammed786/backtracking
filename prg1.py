def getCombirec(arr,ele,n):
    if(ele > n):
        print(arr)
        return
    for i in range(0,2*n):
        if(arr[i] == -1 and (i + ele + 1) < 2*n and arr[i + ele + 1] == -1):
            arr[i] = ele
            arr[i+ele+1] = ele
            getCombirec(arr,ele+1,n)
            arr[i] = -1
            arr[i + ele + 1] = -1
        
            
            
def getCombination(n):
    arr = [];
    for i in range(0,2*n):
        arr.append(-1)
    ele = 1
    getCombirec(arr,ele,n)

def main():
    n = 3
    getCombination(n)
    
if __name__ == "__main__": main()