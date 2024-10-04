def maxProfit(prices):
    if not prices:
        return 0
    
    minPrice = float('inf')
    maxProfit = 0
    
    for price in prices:
        if price < minPrice:
            minPrice = price
        else:
            profit = price - minPrice
            if profit > maxProfit:
                maxProfit = profit
                
    return maxProfit