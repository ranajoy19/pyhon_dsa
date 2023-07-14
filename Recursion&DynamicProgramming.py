

# # 1) DYNAMIC PROOGRAMMING LONGEST COMMON SUBSEQUENCE


# QUESTION 1: Write a function to find the length of the longest common subsequence 
            #between two sequences. E.g. Given the strings "serendipitous" and "precipitation",
            # the longest common subsequence is "reipito" and its length is 7.

            # A "sequence" is a group of items with a deterministic ordering. Lists, tuples
            # and ranges are some common sequence types in Python.

            # A "subsequence" is a sequence obtained by deleting zero or more elements 
            #from another sequence. For example, "edpt" is a subsequence of "serendipitous".




# Recursive Solution

# Create two counters idx1 and idx2 starting at 0. Our recursive function will 
#compute the LCS of seq1[idx1:] and seq2[idx2:]

# If seq1[idx1] and seq2[idx2] are equal, 
#then this character belongs to the LCS of seq1[idx1:] and seq2[idx2:] (why?).
# Further the length this is LCS is one more than LCS of seq1[idx1+1:] and seq2[idx2+1:]


# def lcs(seq1, seq2,idx1=0,idx2=0):
#     if len(seq1) == idx1 or len(seq2) == idx2:
#         return 0
#     elif seq1[idx1] == seq2[idx2]:
#         return 1 + lcs(seq1, seq2,idx1+1,idx2+1)
#     else:
#         return max(lcs(seq1, seq2,idx1+1,idx2), lcs(seq1, seq2, idx1, idx2+1))



# print(lcs('abcde','ace'))

# solution works but Time Limit Exceeded time complexity to high 
 

# Memomization Solution
       
# def lcs_memo(seq1, seq2):
#     memo={}
#     def recursive(idx1, idx2):
#         key=(idx1, idx2)
#         if key in memo:
#             return memo[key]
#         if len(seq1) == idx1 or len(seq2) == idx2:
#             return 0
#         elif seq1[idx1] == seq2[idx2]:
#             memo[key]= 1+ recursive(idx1+1,idx2+1)
#         else:
#             memo[key]= max(recursive(idx1+1,idx2), recursive(idx1, idx2+1))
#         return memo[key]
#     return recursive(0,0)

# print(lcs_memo('pmjghexybyrgzczy','hafcdqbgncrcbihkd'))




# 3 Dynamic programming solution


# def lcs_dp(seq1, seq2):
#     m = len(seq1)
#     n = len(seq2)
#     dp = [[0 for i in range(n+1)] for j in range(m+1)]
#     for idx1 in range(m-1,-1,-1):
#         for idx2 in range(n-1,-1,-1):
#             if len(seq1) == idx1 or len(seq2) == idx2:
#                 return 0
#             elif seq1[idx1] == seq2[idx2]:
#                 dp[idx1][idx2] = 1+dp[idx1+1][idx2+1]
#             else:
#                 dp[idx1][idx2] = max(dp[idx1+1][idx2], dp[idx1][idx2+1])
#     return dp[0][0]

# print(lcs_dp('pmjghexybyrgzczy','hafcdqbgncrcbihkd'))



 # #  2  0-1 knapsack problem


# Problem statement
# You’re in charge of selecting a football (soccer) team from a large pool of players.
# Each player has a cost, and a rating. You have a limited budget. What is the highest 
# total rating of a team that fits within your budget.Assume that there’s no minimum 
# or maximum team size.


# solution
# capacity is fixed cost here and weights are payers profit are rating of players
 
# General problem statemnt:

# Given n elements, each of which has a weight and a profit, determine the maximum profit 
# that can be obtained by selecting a subset of the elements weighing no more than w.


# def knapsack(capacity,weight,profits,idx):
#     if len(weight) == idx:
#         return 0
#     elif weight[idx] > capacity :
#         # if current element is more than capacity left that element go with other  element
#         return knapsack(capacity,weight,profits,idx+1)
#     else:
#         #  find the max ((cuurent element profit + and go on) or next element)  
#         return max(profits[idx]+knapsack(capacity-weight[idx],weight,profits,idx+1),knapsack(capacity,weight,profits,idx+1))

# print(knapsack(165,[23, 31, 29, 44, 53, 38, 63, 85, 89, 82],[92, 57, 49, 68, 60, 43, 67, 84, 87, 72],0))


# def knapsack_memo(capacity,weight,profits):
#     memo={}
#     def recur(idx,remaining):
#         key=(idx,remaining)
#         if key in memo:
#             return memo[key]
#         if len(weight) == idx:
#             return 0
#         elif weight[idx] > remaining :
#             # if current element is more than capacity left that element go with other  element
#             memo[key] = recur(idx+1,remaining)
#         else:
#             #  find the max ((cuurent element profit + and go on) or next element)  
#             memo[key] = max(profits[idx]+recur(idx+1,remaining-weight[idx]),recur(idx+1,remaining))
#         return memo[key]
    
#     return recur(0,capacity)            

# print(knapsack_memo(165,[23, 31, 29, 44, 53, 38, 63, 85, 89, 82],[92, 57, 49, 68, 60, 43, 67, 84, 87, 72]))
