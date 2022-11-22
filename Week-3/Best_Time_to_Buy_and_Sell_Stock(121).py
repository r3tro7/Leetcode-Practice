# Time Complexity: O(N)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Here we start from index 1 to sell and initialize min as the previous element to buy
# moving forward we keep track of the curr_min to denote best day to buy
# and also keep track of the max profit at every iteration
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min:int = prices[0]
        profit:int = 0
        n:int = len(prices)

        for sell in range(1,n):
            curr_min:int = min(curr_min,prices[sell-1])
            curr_profit:int = prices[sell] - curr_min
            if curr_profit > profit:
                profit = curr_profit
        return profit