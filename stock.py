# Stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "AMZN": 150
}

total = 0

print("===== STOCK PORTFOLIO TRACKER =====")

for stock in stocks:
    quantity = int(input(f"Enter quantity of {stock}: "))
    total = total + (stocks[stock] * quantity)

print("\nTotal Investment Value = $", total)