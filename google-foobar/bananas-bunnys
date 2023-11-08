def solution(banana_list):    
    def duos(j,loopable,visited):   #match the duos
        for i in range(len(banana_list)):
            if guards_troupe[i][j] and visited[i]==False :
                visited[i]=True
                if loopable[i]==-1 or duos(loopable[i],loopable,visited):
                    loopable[i]=j
                    return True
        return False  
    
    len_bananal= len(banana_list)
    ans=0
    guards_troupe=[[False] *len_bananal for i in range(len_bananal)]
    for i in range(len_bananal):
        for j in range(i+1):
            if(loopi(banana_list[i], banana_list[j])):
                guards_troupe[i][j]=True
                guards_troupe[j][i]=True
    ans = 0
    loopable= [-1] * len_bananal
    for i in range(len_bananal):
        visited = [False] * len_bananal
        a=duos(i, loopable,visited)

        if a:
            ans += 1
    return len_bananal -2*( ans//2)
def greatest_divisor(x, y):  #Take the greatest commom divisor of the x and y
       while(y):
           x, y = y, x % y
       return x
def loopi(i,j):
    greatest_commom = (i + j) / greatest_divisor(i, j) #call the greater divisor function
    greatest_commom=int(greatest_commom)            #use the Euclides algoritm to calcule the times will loop
    return bool((greatest_commom - 1) & greatest_commom)    #verify if the loop will be infinite
    