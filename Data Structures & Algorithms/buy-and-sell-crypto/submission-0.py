class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini=1000
        i=0
        while i<len(prices):
            mini=min(mini,prices[i])
            print(mini,"mini")
            profit=max(profit,prices[i]-mini)
            print(profit,"profit")
            i+=1
        return profit        