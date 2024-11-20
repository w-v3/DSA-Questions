#solution 
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def solve(self, A, B, C):
        maxc = max(  list( A ) )
        n = len(B)
        
        dp = [ 0 for x in range(maxc+1) ]
        
        
        for i in range(1,maxc+1):
            minc = float("inf")
            for j in range(0,n):
                if i-B[j] >= 0:
                    minc = min( minc , dp[ i-B[j] ] + C[j] )
            
            dp[i] = minc
        #print(dp)
        counter = 0
                
        for i in range(0,len(A)):
            counter += dp[ A[i] ]
            
        
        return counter
