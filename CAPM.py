import numpy as np
import pandas as pd
import yfinance as yf

# Define the stock tickers and the market index
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META', 'TSLA', 'JPM', 'WMT', 'BAC', 'NFLX']
market_index = '^GSPC'

# Create a DataFrame to store the adjusted close prices
data = pd.DataFrame()

# Download adjusted close price data for each ticker and the market index
all_tickers = tickers + [market_index]
for t in all_tickers:
    data[t] = yf.download(t, start='2020-1-1', end='2024-1-1')['Adj Close']

# Calculate the log returns for each stock and the market index
sec_returns = np.log(data / data.shift(1))

# Calculate the covariance matrix of log returns (annualized)
cov = sec_returns.cov() * 252

# Calculate the risk-free rate
risk_free_rate = 0.0426  # 4.26% annual rate

# Initialize an empty dictionary to store CAPM expected returns for each stock
expected_returns = {}

# Calculate expected return for each stock
for ticker in tickers:
    # Extract the beta for the stock
    beta = cov.loc[ticker, market_index] / cov.loc[market_index, market_index]
    
    # Calculate expected return using the CAPM formula
    expected_return = risk_free_rate + beta * (sec_returns[market_index].mean() * 252 - risk_free_rate)
    
    # Store expected return in the dictionary
    expected_returns[ticker] = expected_return

# Create a DataFrame to present expected returns as a table
expected_returns_df = pd.DataFrame(expected_returns.items(), columns=['Ticker', 'Expected Return'])

print(expected_returns_df)