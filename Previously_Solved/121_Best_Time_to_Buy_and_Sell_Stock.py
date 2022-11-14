class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1
        profit = 0
        
        while(sell<len(prices)):
            if(prices[buy] < prices[sell]):
                if(prices[sell]-prices[buy] > profit):
                    profit = prices[sell]-prices[buy]
            else:
                #we take the buy pointer to the next minimum
                buy = sell
            sell+=1
                
        return profit
                
        