#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "yfinance>=0.2.48",
#     "pandas>=2.0.0",
# ]
# ///
"""
Comprehensive demonstration of yfinance library usage for financial data retrieval.
"""

import yfinance as yf
from datetime import datetime, timedelta


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'=' * 80}")
    print(f"  {title}")
    print(f"{'=' * 80}\n")


def demonstrate_basic_ticker_info():
    """Line 25-35: Demonstrate basic ticker information retrieval."""
    print_section("1. Basic Ticker Information")

    # Create a Ticker object for Apple Inc.
    ticker = yf.Ticker("AAPL")

    # Get basic company information
    info = ticker.info
    print(f"Company Name: {info.get('longName', 'N/A')}")
    print(f"Sector: {info.get('sector', 'N/A')}")
    print(f"Industry: {info.get('industry', 'N/A')}")
    print(f"Market Cap: ${info.get('marketCap', 0):,}")
    print(f"Current Price: ${info.get('currentPrice', 0):.2f}")
    print(f"52 Week High: ${info.get('fiftyTwoWeekHigh', 0):.2f}")
    print(f"52 Week Low: ${info.get('fiftyTwoWeekLow', 0):.2f}")


def demonstrate_historical_data():
    """Line 42-55: Demonstrate historical price data retrieval."""
    print_section("2. Historical Price Data")

    ticker = yf.Ticker("MSFT")

    # Get historical data for the last 5 days
    hist = ticker.history(period="5d")

    print("Last 5 days of Microsoft (MSFT) stock data:")
    print(hist[["Open", "High", "Low", "Close", "Volume"]])

    # Get data for a specific date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    hist_range = ticker.history(start=start_date, end=end_date)
    print(f"\nTotal trading days in last 30 days: {len(hist_range)}")


def demonstrate_multiple_tickers():
    """Line 60-70: Demonstrate downloading data for multiple tickers."""
    print_section("3. Multiple Tickers")

    # Download data for multiple tickers at once
    tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]
    data = yf.download(tickers, period="5d", group_by="ticker", progress=False)

    print("Closing prices for FAANG stocks (last 5 days):")
    for ticker in tickers:
        if ticker in data.columns.get_level_values(0):
            print(f"\n{ticker}:")
            print(data[ticker]["Close"])


def demonstrate_financial_statements():
    """Line 75-88: Demonstrate financial statement retrieval."""
    print_section("4. Financial Statements")

    ticker = yf.Ticker("TSLA")

    # Get quarterly financials
    quarterly_financials = ticker.quarterly_financials
    print("Tesla (TSLA) Quarterly Financials (first 5 rows):")
    if not quarterly_financials.empty:
        print(quarterly_financials.head())

    # Get balance sheet
    balance_sheet = ticker.balance_sheet
    print("\nTesla (TSLA) Annual Balance Sheet (first 5 rows):")
    if not balance_sheet.empty:
        print(balance_sheet.head())


def demonstrate_dividends_and_splits():
    """Line 93-104: Demonstrate dividend and stock split history."""
    print_section("5. Dividends and Stock Splits")

    ticker = yf.Ticker("KO")  # Coca-Cola

    # Get dividend history
    dividends = ticker.dividends
    print("Coca-Cola (KO) Recent Dividends (last 10):")
    print(dividends.tail(10))

    # Get stock split history
    splits = ticker.splits
    print("\nCoca-Cola (KO) Stock Splits:")
    if not splits.empty:
        print(splits)
    else:
        print("No stock splits in available history")


def demonstrate_options_data():
    """Line 109-125: Demonstrate options data retrieval."""
    print_section("6. Options Data")

    ticker = yf.Ticker("SPY")  # S&P 500 ETF

    # Get available option expiration dates
    try:
        expirations = ticker.options
        print(f"Available option expiration dates for SPY: {len(expirations)} dates")
        print(f"Next 5 expiration dates: {expirations[:5]}")

        # Get options chain for the nearest expiration
        if expirations:
            opt_chain = ticker.option_chain(expirations[0])
            print(f"\nCalls for {expirations[0]} (first 5 rows):")
            print(
                opt_chain.calls[["strike", "lastPrice", "bid", "ask", "volume"]].head()
            )
            print(f"\nPuts for {expirations[0]} (first 5 rows):")
            print(
                opt_chain.puts[["strike", "lastPrice", "bid", "ask", "volume"]].head()
            )
    except Exception as e:
        print(f"Options data unavailable: {e}")


def demonstrate_institutional_holders():
    """Line 130-140: Demonstrate institutional holder information."""
    print_section("7. Institutional Holders")

    ticker = yf.Ticker("NVDA")

    # Get institutional holders
    institutional = ticker.institutional_holders
    print("NVIDIA (NVDA) Top Institutional Holders:")
    if institutional is not None and not institutional.empty:
        print(institutional.head(10))
    else:
        print("Institutional holder data not available")


def demonstrate_recommendations():
    """Line 145-155: Demonstrate analyst recommendations."""
    print_section("8. Analyst Recommendations")

    ticker = yf.Ticker("META")

    # Get analyst recommendations
    recommendations = ticker.recommendations
    print("Meta (META) Recent Analyst Recommendations:")
    if recommendations is not None and not recommendations.empty:
        print(recommendations.tail(10))
    else:
        print("Recommendation data not available")


def main():
    """Main function to run all demonstrations."""
    print("\n" + "=" * 80)
    print("  YFINANCE LIBRARY DEMONSTRATION")
    print("  Comprehensive examples of financial data retrieval")
    print("=" * 80)

    try:
        demonstrate_basic_ticker_info()
        demonstrate_historical_data()
        demonstrate_multiple_tickers()
        demonstrate_financial_statements()
        demonstrate_dividends_and_splits()
        demonstrate_options_data()
        demonstrate_institutional_holders()
        demonstrate_recommendations()

        print("\n" + "=" * 80)
        print("  All demonstrations completed successfully!")
        print("=" * 80 + "\n")

    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
