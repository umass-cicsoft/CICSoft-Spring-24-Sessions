"""
Given an integer array nums, and an integer k, find the maximum product of any k non-adjacent elements in the array. 
If it is not possible to find k non-adjacent elements, return 0.

Example 1:

Input: nums = [3, 4, 5, -2, 1], k = 2
Output: 15
Explanation: The maximum product is achieved by selecting the elements 3 and 5, as 3 * 5 = 15. 
Note that the elements are non-adjacent.
Example 2:

Input: nums = [1, 0, -1, 2, 3, -5, 4], k = 3
Output: 12
Explanation: The maximum product of 3 non-adjacent elements is achieved by selecting 1, 3, and 4, resulting in 1 * 3 * 4 = 12. 

Example 3:

Input: nums = [1, 3], k = 3
Output: 0
Explanation: There are not enough non-adjacent elements to select 3, so the result is 0.
Constraints:

1 <= nums.length <= 10^4
1 <= k <= nums.length
-10^4 <= nums[i] <= 10^4
Additional Notes:
This problem requires you to consider combinations rather than subsequences or contiguous subarrays, 
which adds a layer of complexity in selecting elements. You'll need to ensure that no two selected elements are adjacent, 
which makes the problem more challenging and unique. 
This modification should provide a robust challenge and stimulate more advanced algorithmic strategies.
"""


## TODO: Implement the balanced_array function below
def maxProduct(nums, k) -> bool:
    pass
