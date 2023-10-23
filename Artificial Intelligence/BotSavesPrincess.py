import math

def displayPathtoPrincess(n,grid):
    #find princess in corner
    princessX = 0
    princessY = 0
    if grid[0][n-1] == "p":
        princessX = n-1
    elif grid[n-1][0] == "p":
        princessY = n-1
    elif grid[n-1][n-1] == "p":
        princessX = n-1
        princessY = n-1

    #only other case, P is in 0,0
    startX = startY = math.floor(n/2)

    #order - left, right, up, down
    while startX != princessX:
        if startX < princessX: #go right
            print("RIGHT")
            startX+=1
        else: #go left
            print("LEFT")
            startX-=1
    while startY != princessY:
        if startY > princessY: #go up
            print("UP")
            startY-=1
        else: #go down
            print("DOWN")
            startY+=1
        

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)