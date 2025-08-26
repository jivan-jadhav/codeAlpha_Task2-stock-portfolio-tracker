# Task 2: Stock Portfolio Tracker


stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 120,
    "MSFT": 300,
    "IREDA":150,
    "IRFC":125
}


n = int(input("How many different stocks do you want to add? "))

portfolio = {}
total_investment = 0

for _ in range(n):
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    
    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        portfolio[stock] = investment
        total_investment += investment
    else:
        print(f" {stock} not found in stock price dictionary.")

print("\n Portfolio Summary:")
for stock, investment in portfolio.items():
    print(f"{stock}: ${investment}")

print(f"\n Total Investment: ${total_investment}")


with open("portfolio.txt", "w") as f:
    for stock, investment in portfolio.items():
        f.write(f"{stock}: ${investment}\n")
    f.write(f"\nTotal Investment: ${total_investment}\n")

print("\nResults saved to portfolio.txt")
