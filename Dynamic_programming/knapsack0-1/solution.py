#solution 

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        #dp = [ [ 0 for j in range(0,C+1) ] for i in range(0, len(B)+1) ]
        dp = [ [ 0 for j in range(C+1)   ] for i in range(len(B)+1)  ]
        
        for item in range(len(B)+1 ):
            for weight in range(C+1):
                # total knapsack capacity > weight of the ith item
                if weight == 0 or item == 0:
                    dp[item][ weight ] = 0
                    
                elif weight >= B[item-1]:
                    # best value would be
                    # max from two values
                    # 1. value of knapsack without item n and weight = weight
                    # => we don't add item n to the sack for weight == weight
                    # 2. value of knapsack with item n and weight => weight-w[item n ]
                    # => we add item to the sack and take the value to sack with item n-1 and 
                    # weight without the sack
                    dp[item][ weight ] = max( dp[item-1][weight] , dp[item-1][ weight-B[item-1] ] + A[item-1])
                    
                else:
                    dp[item][ weight ] = dp[item-1][weight]
            
            #print( dp[item] , item)
            
        return dp[ len(B)][C]
