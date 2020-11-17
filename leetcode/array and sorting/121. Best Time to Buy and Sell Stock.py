class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float("inf")
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                    max_profit = price - min_price
        return max_profit
    
    # price：      7, 1, 5, 3, 6, 4
    # min_price:   7, 1, 1, 1, 1, 1
    # max_profit:  0, 0, 4, 2, 5, 3
    # 等效于后一个数减前一个数值最大