"""
Medium Problem:
Alice and Bob plays a game. They were given 'x' ones, 'y' twos, 'z' threes, and 't' fours. 
Each round, they are also given 3 coins, initially facing head. 
In each round, if the i^th bit of a number is 1, then they flip the i^th coin once. 
Bob wins if and only if all the three coins remain heads. 

After each round, Bob remove one of the four numbers. 
For example, if Bob decides to remove a 4, then they begin next round with 'x' ones, 'y' twos, 'z' threes, and 't-1' fours. 
Assume both players are perfect logicians, what is the maximum number of rounds that Bob can win?

Example 1:
input: [2,2,2,0] -> 3

Example 2:
input: [1,1,1,0] -> 1

Example 3:
input: [3,3,2,0] -> 3

Example 4:
input: [0,9,9,9] -> 12

Constraints:
 - 0 <= x, y, z, t <= 200
 - Total number of test cases < 10^4
"""


## TODO: Implement the balanced_array function below
def coinToss(a, b, c, d) -> bool:
    pass
