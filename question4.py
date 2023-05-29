2709. Greatest Common Divisor Traversal


You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

 

Example 1:

Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
Example 2:

Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
Example 3:

Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105

class childFind:
        
        def __init__(self, n):
            self.leads = [i for i in range(n)]
            self.postions = [1] * n
        def search_leads(self, x):
            if self.leads[x] != x:
                self.leads[x] = self.search_leads(self.leads[x])
            return self.leads[x]
        def tog(self, x, y):
            c1 = self.search_leads(x)
            c2 = self.search_leads(y)
            if c1 != c2:
                if self.postions[c1] < self.postions[c2]:
                    self.leads[c1] = c2
                elif self.postions[c1] > self.postions[c2]:
                    self.leads[c2] = c1
                
                else:
                    self.leads[c1] = c2
                    self.postions[c2] += 1

class Solution:
     def canTraverseAllPairs(self, nums: List[int]) -> bool:
            n = len(nums)
            unordered_child = childFind(n)
            dict1 = {}
            for i in range(n):
                for j in range(2, int(nums[i] ** 0.5) + 1):
                    if nums[i] % j == 0:
                        if j not in dict1:
                            dict1[j] = []
                        dict1[j].append(i)
                        while nums[i] % j == 0:
                            nums[i] //= j
                if nums[i] > 1:
                    if nums[i] not in dict1:
                        dict1[nums[i]] = []
                    dict1[nums[i]].append(i)
            for h, ind in dict1.items():
                for i in range(1, len(ind)):
                    unordered_child.tog(ind[i - 1], ind[i])
            ro = unordered_child.search_leads(0)
            for i in range(1, n):
                if unordered_child.search_leads(i) != ro:
                    return False
                return True
        