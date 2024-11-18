"# python solution" 
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        n = len(A)
        dp = [ [ 0 for x in range(n)  ] for y in range(n) ]
        
        for i in range(n):
            dp[i][i] = 1
            
        adder = 1
        for k in range(n-1,0,-1):
            for i in range(0,k):
                x = i
                y = x+adder
                #print(x,y)
                if A[x] == A[y]:
                    dp[x][y] = 2 + dp[x+1][y-1]
                else:
                    dp[x][y] = max( dp[x+1][y] , dp[x][y-1])
            adder += 1
            #print("--------------")
        
        #for i in range(0,n):
        #    print(dp[i])
            
        return dp[0][n-1]
