class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_arr = 0
        profit = 0
        if prices is None:
            return 0
        for i in range(len(prices)-1):
            next_price = prices[i+1]
            if prices[i] < next_price:
                profit = next_price - prices[i]
                profit_arr += profit
            print("profit_arr: ", profit_arr)
        return profit_arr
