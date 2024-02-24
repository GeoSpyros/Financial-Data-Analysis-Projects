import numpy as np 
import pandas as pd  
import yfinance as yf 
import matplotlib.pyplot as plt  

# List of stock market indices ticker symbols
tickers = ['^DJI', '^GSPC', '^IXIC']

# Create an empty DataFrame to store index data
ind_data = pd.DataFrame()

# Loop through each ticker symbol in the list
for t in tickers:
    ind_data[t] = yf.download(t, start='2000-1-1')['Adj Close']

# Normalize the index data by dividing each value by the initial value and then multiplying by 100,
# this allows us to compare the performance of different indices starting from the same point
(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6))
plt.show()

# Calculate daily returns for each index by taking the percentage change from one day to the next
ind_returns = (ind_data / ind_data.shift(1)) - 1

# Display the last few rows of daily returns data
print(ind_returns.tail())

# Calculate annualized returns for each index by taking the mean daily return and multiplying by 252
# (the number of trading days in a year)
annual_ind_returns = ind_returns.mean() * 252

print("Annualized Returns:")
print(annual_ind_returns)