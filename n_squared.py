def solver(S,T):
    
    dp = [ [0 for i in range(len(S))] for j in range(len(S))]

    for i in range(len(S)):
        if i >= len(T) or T[i] == S[0]:
            dp[i][i] = 1 

    for i in range(1,len(S)):
        k = 0
        for j in range(i,len(S)):
 
            if k >= len(T) or S[i] == T[k]:
                dp[k][j] += dp[k+1][j]
            if j >= len(T) or S[i] == T[j]:
                dp[k][j] += dp[k][j-1]
            k+=1
            
    return dp[0][len(S)-1]

if __name__ == '__main__':
    S = input('S:')
    T = input("T")
    print(solver(S,T))