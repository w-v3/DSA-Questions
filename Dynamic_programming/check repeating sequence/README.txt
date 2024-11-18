problem 
Given a string A, Check if the length of the longest repeating sub-sequence is greater than or equal to 2,
A longest repeating sub-sequence is defined such that,
the two subsequences have the same string character at the same position
any ith character in the two subsequences shouldn’t have the same index in the original string
NOTE: If the Sub-sequence length is greater than or equal to 2 return 1, else return 0.

 
Problem Constraints
 1 <= |A| <= 100


Input Format
The first and only argument of input contains a string A.


Output Format
Return an integer, 0 or 1:

    => 0 : Length of Repeating subsequence is less than 2
    => 1 : Length of Repeating subsequence is greater than or equal to 2
 



Example Input
Input 1:
 A = "abab"
Input 2:
 A = "abba"
Input 3:
 A = "aaaaa"



Example Output
Output 1:
 1
Output 2:
 0
Output 3:
 1
 



Example Explanation
Explanation 1:
 "ab" is repeated.
Explanation 2:
 There is no repeating subsequence.
Explanation 3:
 "aaaa" is repeated