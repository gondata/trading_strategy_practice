# Trading Strategy based on Moving Averages Crossover

This code uses Python libraries such as NumPy, Pandas, Matplotlib, yfinance, and pandas-datareader to implement a trading strategy based on Moving Averages Crossover for the cryptocurrency Bitcoin (BTC-USD).

## Requirements

The code requires the following libraries:

- NumPy
- Pandas
- Matplotlib
- yfinance
- pandas-datareader

The required libraries can be installed using the `requirements.txt` file.

How it Works

1. First, we import the necessary libraries and set up the yfinance override.
2. We then define the assets to analyze, along with the start and end dates.
3. The data is obtained using `pdr.get_data_yahoo()` and only the 'Adj Close' column is used for analysis.
4. The short and long windows for the moving averages are defined.
5. A Pandas DataFrame is created to store the signals generated by the strategy.
6. The short and long moving averages are calculated and stored in the DataFrame.
7. The signals are generated by comparing the short and long moving averages.
8. The DataFrame is then used to calculate the positions taken by the strategy.
9. Finally, a graph is plotted to visualize the trading strategy, including the buy and sell signals generated by the strategy.
