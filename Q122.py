def maxProfit(prices):
    if not prices:
        return 0

    minPrice=float('inf')
    profit=0
    totalProfit=0

    for price in prices:
        if price < minPrice:
            minPrice = price
        else:
            profit = price - minPrice
            totalProfit += profit
            minPrice = price
                
    return totalProfit