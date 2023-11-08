def solution(n):
    l = [[0 for x in range(0, (n + 1))] for y in range(0, (n + 1))] #l is the 2 columns
    l[0][0] = 1 #set the ground as 1 for the two columns
    for highmax in range(1, (n + 1)):  #stair total highmax
        for high in range(0, (n + 1)):    #high
            l[highmax][high] = l[highmax - 1][high]  
            if high >= highmax:             #verify the bricks amount
                l[highmax][high] += l[highmax - 1][high - highmax]
    return l[n][n] -1

print(solution(5))