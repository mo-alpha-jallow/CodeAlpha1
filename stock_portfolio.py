stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 420.00,
    "AMZN": 185.00
}

stock = input("Enter stock symbol: ").upper()

if stock in stock_prices:
    print("Stock found!")

    shares = int(input("Enter number of shares: "))

    price = stock_prices[stock]

    investment_value = shares * price

    print(f"\n___Portfolio summary___")
    print(f"Stock: {stock}")
    print(f"Price per share: ${stock_prices[stock]}")
    print(f"Number of shares: {shares}")
    print(f"Investment value: ${investment_value}")

else :
    print("Stock not found!")
