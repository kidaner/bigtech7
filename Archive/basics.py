import yfinance as yf
import csv

tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA']

# Create and open the CSV file in write mode
with open('stock_info.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(['Ticker', 'Sector', 'Industry', 'Description'])

    for ticker in tickers:
        info = yf.Ticker(ticker).info

        # Get information or default to 'N/A'
        sector = info['sector']
        industry = info['industry']
        description = info['longBusinessSummary']

        # Write the information to the CSV file
        writer.writerow([ticker, sector, industry, description])

print("Data has been saved to 'stock_info.csv'")
