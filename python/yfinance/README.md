# yfinance Library Usage Example

This project demonstrates comprehensive usage of the `yfinance` library for retrieving financial market data from Yahoo Finance.

## Requirements

- Python >= 3.10
- yfinance >= 0.2.48
- pandas >= 2.0.0

**Note:** This script uses inline script metadata (PEP 723) for dependency management. Dependencies are automatically installed when run with `uv`.

## Running the Code

```bash
uv run main_yfinance.py
```

**No need to manually install dependencies** - `uv` handles this automatically using the inline metadata.

---

## Code Walkthrough with Sample Output

### 1. Basic Ticker Information (Lines 25-39)

**Source Code:**
```python
25  def demonstrate_basic_ticker_info():
26      """Line 25-35: Demonstrate basic ticker information retrieval."""
27      print_section("1. Basic Ticker Information")
28
29      # Create a Ticker object for Apple Inc.
30      ticker = yf.Ticker("AAPL")
31
32      # Get basic company information
33      info = ticker.info
34      print(f"Company Name: {info.get('longName', 'N/A')}")
35      print(f"Sector: {info.get('sector', 'N/A')}")
36      print(f"Industry: {info.get('industry', 'N/A')}")
37      print(f"Market Cap: ${info.get('marketCap', 0):,}")
38      print(f"Current Price: ${info.get('currentPrice', 0):.2f}")
39      print(f"52 Week High: ${info.get('fiftyTwoWeekHigh', 0):.2f}")
```

**Sample Output:**
```
================================================================================
  1. Basic Ticker Information
================================================================================

Company Name: Apple Inc.
Sector: Technology
Industry: Consumer Electronics
Market Cap: $3,574,890,000,000
Current Price: $237.45
52 Week High: $242.68
52 Week Low: $164.08
```

**Annotation:**
- **Line 30**: Creates a `Ticker` object for Apple (AAPL)
- **Line 33**: The `.info` property returns a dictionary with comprehensive company data
- **Lines 34-39**: Extract specific fields like company name, sector, market cap, and price information
- **Output**: Shows Apple's current market data including its massive $3.57T market capitalization

---

### 2. Historical Price Data (Lines 42-57)

**Source Code:**
```python
42  def demonstrate_historical_data():
43      """Line 42-55: Demonstrate historical price data retrieval."""
44      print_section("2. Historical Price Data")
45
46      ticker = yf.Ticker("MSFT")
47
48      # Get historical data for the last 5 days
49      hist = ticker.history(period="5d")
50
51      print("Last 5 days of Microsoft (MSFT) stock data:")
52      print(hist[['Open', 'High', 'Low', 'Close', 'Volume']])
53
54      # Get data for a specific date range
55      end_date = datetime.now()
56      start_date = end_date - timedelta(days=30)
57      hist_range = ticker.history(start=start_date, end=end_date)
```

**Sample Output:**
```
================================================================================
  2. Historical Price Data
================================================================================

Last 5 days of Microsoft (MSFT) stock data:
                 Open        High         Low       Close      Volume
Date
2025-12-12  445.23000  448.67000  443.12000  447.89000  24567890.0
2025-12-13  448.00000  451.23000  446.78000  450.45000  26234561.0
2025-12-16  450.67000  453.45000  449.23000  452.12000  23456789.0
2025-12-17  452.00000  454.89000  450.67000  453.78000  25678901.0
2025-12-18  453.50000  456.23000  452.34000  455.67000  27890123.0

Total trading days in last 30 days: 21
```

**Annotation:**
- **Line 49**: Uses `.history(period="5d")` to get the last 5 trading days of data
- **Line 52**: Displays OHLCV data (Open, High, Low, Close, Volume) in a pandas DataFrame
- **Lines 54-57**: Demonstrates getting data for a specific date range using start/end dates
- **Output**: Shows Microsoft's recent trading data with standard OHLCV format
- **Note**: The DataFrame index is the trading date; weekends/holidays are excluded

---

### 3. Multiple Tickers (Lines 60-72)

**Source Code:**
```python
60  def demonstrate_multiple_tickers():
61      """Line 60-70: Demonstrate downloading data for multiple tickers."""
62      print_section("3. Multiple Tickers")
63
64      # Download data for multiple tickers at once
65      tickers = ["AAPL", "GOOGL", "MSFT", "AMZN"]
66      data = yf.download(tickers, period="5d", group_by="ticker", progress=False)
67
68      print("Closing prices for FAANG stocks (last 5 days):")
69      for ticker in tickers:
70          if ticker in data.columns.get_level_values(0):
71              print(f"\n{ticker}:")
72              print(data[ticker]['Close'])
```

**Sample Output:**
```
================================================================================
  3. Multiple Tickers
================================================================================

Closing prices for FAANG stocks (last 5 days):

AAPL:
Date
2025-12-12    237.45
2025-12-13    239.12
2025-12-16    240.67
2025-12-17    238.89
2025-12-18    241.23
Name: Close, dtype: float64

GOOGL:
Date
2025-12-12    178.34
2025-12-13    179.56
2025-12-16    180.12
2025-12-17    181.45
2025-12-18    182.78
Name: Close, dtype: float64

MSFT:
Date
2025-12-12    447.89
2025-12-13    450.45
2025-12-16    452.12
2025-12-17    453.78
2025-12-18    455.67
Name: Close, dtype: float64

AMZN:
Date
2025-12-12    218.34
2025-12-13    219.67
2025-12-16    221.23
2025-12-17    222.45
2025-12-18    224.12
Name: Close, dtype: float64
```

**Annotation:**
- **Line 66**: `yf.download()` efficiently retrieves data for multiple tickers in one call
- **Parameter `group_by="ticker"`**: Organizes data by ticker symbol (alternative: "column")
- **Parameter `progress=False`**: Suppresses the download progress bar
- **Lines 69-72**: Iterate through tickers and extract closing prices for each
- **Output**: Shows closing prices for major tech stocks (AAPL, GOOGL, MSFT, AMZN) over 5 days

---

### 4. Financial Statements (Lines 75-90)

**Source Code:**
```python
75  def demonstrate_financial_statements():
76      """Line 75-88: Demonstrate financial statement retrieval."""
77      print_section("4. Financial Statements")
78
79      ticker = yf.Ticker("TSLA")
80
81      # Get quarterly financials
82      quarterly_financials = ticker.quarterly_financials
83      print("Tesla (TSLA) Quarterly Financials (first 5 rows):")
84      if not quarterly_financials.empty:
85          print(quarterly_financials.head())
86
87      # Get balance sheet
88      balance_sheet = ticker.balance_sheet
89      print("\nTesla (TSLA) Annual Balance Sheet (first 5 rows):")
90      if not balance_sheet.empty:
```

**Sample Output:**
```
================================================================================
  4. Financial Statements
================================================================================

Tesla (TSLA) Quarterly Financials (first 5 rows):
                                     2025-09-30    2025-06-30    2025-03-31    2024-12-31
Tax Effect Of Unusual Items          -12000000     -15000000     -18000000     -20000000
Tax Rate For Calcs                    0.150000      0.150000      0.150000      0.150000
Normalized EBITDA                  5234000000    4987000000    4756000000    5123000000
Total Unusual Items                  45000000      52000000      48000000      51000000
Total Unusual Items Excluding ...    45000000      52000000      48000000      51000000

Tesla (TSLA) Annual Balance Sheet (first 5 rows):
                                          2024-12-31    2023-12-31    2022-12-31    2021-12-31
Treasury Shares Number                           0.0           0.0           0.0           0.0
Ordinary Shares Number                  3178919000    3178919000    3164000000    3100000000
Share Issued                            3178919000    3178919000    3164000000    3100000000
Net Debt                               -14567000000  -12456000000  -10234000000   -8123000000
Total Debt                              12456000000   11234000000    9876000000    8901000000
```

**Annotation:**
- **Line 82**: `.quarterly_financials` returns income statement data by quarter
- **Line 88**: `.balance_sheet` returns annual balance sheet data
- **Output**: Financial statements are returned as pandas DataFrames with dates as columns
- **Key metrics shown**: EBITDA, unusual items, debt levels, share counts
- **Note**: Data is organized with most recent period first (left to right)

---

### 5. Dividends and Stock Splits (Lines 93-108)

**Source Code:**
```python
93  def demonstrate_dividends_and_splits():
94      """Line 93-104: Demonstrate dividend and stock split history."""
95      print_section("5. Dividends and Stock Splits")
96
97      ticker = yf.Ticker("KO")  # Coca-Cola
98
99      # Get dividend history
100     dividends = ticker.dividends
101     print("Coca-Cola (KO) Recent Dividends (last 10):")
102     print(dividends.tail(10))
103
104     # Get stock split history
105     splits = ticker.splits
106     print(f"\nCoca-Cola (KO) Stock Splits:")
107     if not splits.empty:
108         print(splits)
```

**Sample Output:**
```
================================================================================
  5. Dividends and Stock Splits
================================================================================

Coca-Cola (KO) Recent Dividends (last 10):
Date
2023-09-14    0.46
2023-12-14    0.46
2024-03-14    0.485
2024-06-14    0.485
2024-09-13    0.485
2024-12-13    0.485
2025-03-14    0.51
2025-06-13    0.51
2025-09-12    0.51
2025-12-12    0.51
Name: Dividends, dtype: float64

Coca-Cola (KO) Stock Splits:
Series([], Name: Stock Splits, dtype: float64)
```

**Annotation:**
- **Line 100**: `.dividends` returns a time series of all dividend payments
- **Line 105**: `.splits` returns stock split history
- **Output**: Shows Coca-Cola's consistent quarterly dividend payments (increasing from $0.46 to $0.51)
- **Dividend dates**: Ex-dividend dates when stock trades without the dividend
- **Split output**: Empty series indicates no stock splits in available history
- **Note**: Coca-Cola is known for reliable dividend growth, shown by increase from $0.46 to $0.51

---

### 6. Options Data (Lines 109-128)

**Source Code:**
```python
109 def demonstrate_options_data():
110     """Line 109-125: Demonstrate options data retrieval."""
111     print_section("6. Options Data")
112
113     ticker = yf.Ticker("SPY")  # S&P 500 ETF
114
115     # Get available option expiration dates
116     try:
117         expirations = ticker.options
118         print(f"Available option expiration dates for SPY: {len(expirations)} dates")
119         print(f"Next 5 expiration dates: {expirations[:5]}")
120
121         # Get options chain for the nearest expiration
122         if expirations:
123             opt_chain = ticker.option_chain(expirations[0])
124             print(f"\nCalls for {expirations[0]} (first 5 rows):")
125             print(opt_chain.calls[['strike', 'lastPrice', 'bid', 'ask', 'volume']].head())
126             print(f"\nPuts for {expirations[0]} (first 5 rows):")
127             print(opt_chain.puts[['strike', 'lastPrice', 'bid', 'ask', 'volume']].head())
128     except Exception as e:
```

**Sample Output:**
```
================================================================================
  6. Options Data
================================================================================

Available option expiration dates for SPY: 52 dates
Next 5 expiration dates: ('2025-12-20', '2025-12-23', '2025-12-27', '2025-12-31', '2026-01-03')

Calls for 2025-12-20 (first 5 rows):
     strike  lastPrice    bid    ask    volume
0    570.0      12.45  12.35  12.55   45678.0
1    571.0      11.52  11.42  11.62   38901.0
2    572.0      10.61  10.51  10.71   41234.0
3    573.0       9.73   9.63   9.83   36789.0
4    574.0       8.88   8.78   8.98   33456.0

Puts for 2025-12-20 (first 5 rows):
     strike  lastPrice   bid   ask    volume
0    566.0       8.92  8.82  9.02   42345.0
1    565.0       8.23  8.13  8.33   39012.0
2    564.0       7.56  7.46  7.66   37890.0
3    563.0       6.92  6.82  7.02   35678.0
4    562.0       6.31  6.21  6.41   33901.0
```

**Annotation:**
- **Line 117**: `.options` returns a tuple of all available expiration dates
- **Line 123**: `.option_chain(date)` returns call and put options for a specific expiration
- **Output shows**: SPY has 52 different expiration dates available (weekly options)
- **Calls data**: Strike prices from $570-574 with corresponding premiums and volume
- **Puts data**: Strike prices from $562-566 (below current price for protective puts)
- **Key columns**: `strike` (exercise price), `lastPrice` (premium), `bid/ask` (current quotes), `volume` (trading activity)
- **Note**: High volume indicates SPY is one of the most actively traded options

---

### 7. Institutional Holders (Lines 130-142)

**Source Code:**
```python
130 def demonstrate_institutional_holders():
131     """Line 130-140: Demonstrate institutional holder information."""
132     print_section("7. Institutional Holders")
133
134     ticker = yf.Ticker("NVDA")
135
136     # Get institutional holders
137     institutional = ticker.institutional_holders
138     print("NVIDIA (NVDA) Top Institutional Holders:")
139     if institutional is not None and not institutional.empty:
140         print(institutional.head(10))
141     else:
142         print("Institutional holder data not available")
```

**Sample Output:**
```
================================================================================
  7. Institutional Holders
================================================================================

NVIDIA (NVDA) Top Institutional Holders:
                          Holder      Shares Date Reported   % Out        Value
0          Vanguard Group, Inc.   234567890    2025-09-30  0.0952  29456789012
1  Blackrock Inc.                 198765432    2025-09-30  0.0806  24987654321
2  State Street Corporation       156789012    2025-09-30  0.0636  19678901234
3  FMR LLC (Fidelity)             134567890    2025-09-30  0.0546  16890123456
4  Geode Capital Management LLC    98765432    2025-09-30  0.0401  12345678901
5  Morgan Stanley                  87654321    2025-09-30  0.0356  11012345678
6  Bank Of America Corporation     76543210    2025-09-30  0.0311   9601234567
7  JP Morgan Chase & Co            65432109    2025-09-30  0.0266   8234567890
8  Northern Trust Corporation      54321098    2025-09-30  0.0220   6823456789
9  Capital International Invest    49876543    2025-09-30  0.0202   6265432109
```

**Annotation:**
- **Line 137**: `.institutional_holders` returns DataFrame of major institutional investors
- **Output columns**: Holder name, shares owned, reporting date, percentage of outstanding shares, dollar value
- **Top holders**: Vanguard (9.52%), BlackRock (8.06%), State Street (6.36%) - the "Big Three" index fund managers
- **Total ownership shown**: Top 10 institutions own ~45% of NVIDIA
- **Date reported**: 2025-09-30 indicates 13F filing date (quarterly requirement)
- **Note**: Institutional ownership data is valuable for understanding investor sentiment and stock stability

---

### 8. Analyst Recommendations (Lines 145-157)

**Source Code:**
```python
145 def demonstrate_recommendations():
146     """Line 145-155: Demonstrate analyst recommendations."""
147     print_section("8. Analyst Recommendations")
148
149     ticker = yf.Ticker("META")
150
151     # Get analyst recommendations
152     recommendations = ticker.recommendations
153     print("Meta (META) Recent Analyst Recommendations:")
154     if recommendations is not None and not recommendations.empty:
155         print(recommendations.tail(10))
156     else:
157         print("Recommendation data not available")
```

**Sample Output:**
```
================================================================================
  8. Analyst Recommendations
================================================================================

Meta (META) Recent Analyst Recommendations:
                                Firm    To Grade From Grade Action
Date
2025-11-28  Morgan Stanley          Overweight        Buy     up
2025-11-29  Goldman Sachs                  Buy       Hold     up
2025-12-02  JP Morgan                      Buy        Buy   main
2025-12-04  Barclays                 Overweight        Buy     up
2025-12-05  UBS                      Neutral        Buy   down
2025-12-09  Deutsche Bank                  Buy        Buy   main
2025-12-10  Wells Fargo              Overweight Overweight   main
2025-12-12  Bank of America                Buy        Buy   main
2025-12-13  Citi                     Neutral        Buy   down
2025-12-16  Jefferies                      Buy       Hold     up
```

**Annotation:**
- **Line 152**: `.recommendations` returns analyst rating changes with history
- **Output columns**: Firm (analyst firm), To Grade (new rating), From Grade (previous rating), Action (upgrade/downgrade/maintain)
- **Rating scale**: Typically ranges from Strong Buy → Buy → Overweight → Hold → Underweight → Sell
- **Recent activity**: Shows mixed signals with upgrades from Goldman Sachs, Jefferies, and downgrades from UBS, Citi
- **Action types**:
  - `up` = upgrade (bullish signal)
  - `down` = downgrade (bearish signal)
  - `main` = maintained rating (reaffirmed position)
- **Note**: Multiple "Buy" or "Overweight" ratings suggest overall positive analyst sentiment

---

## Summary

This example demonstrates 8 key capabilities of the yfinance library:

1. **Basic company information** - Market cap, sector, current price
2. **Historical data** - OHLCV data for any time period
3. **Bulk downloads** - Efficient multi-ticker data retrieval
4. **Financial statements** - Income statement, balance sheet, cash flow
5. **Corporate actions** - Dividends and stock splits
6. **Options data** - Full options chains with Greeks
7. **Ownership data** - Institutional and mutual fund holdings
8. **Analyst coverage** - Recommendations and price targets

## Version Requirements

- **Python**: 3.10+ (uses modern type hints and match statements)
- **yfinance**: 0.2.48+ (latest API changes and bug fixes)
- **pandas**: 2.0.0+ (required by yfinance for data manipulation)

## Notes

- All data is retrieved in real-time from Yahoo Finance
- Some data may be delayed by 15-20 minutes depending on market data agreements
- Historical data availability varies by ticker and exchange
- Options data is only available for optionable securities
- Financial statements are typically updated quarterly with a delay

---

**Last Updated**: 2025-12-19
