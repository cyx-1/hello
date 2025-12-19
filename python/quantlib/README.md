# QuantLib Python Example

This example demonstrates the key features of QuantLib, a comprehensive library for quantitative finance in Python.

## Requirements

- Python >= 3.11
- QuantLib >= 1.34

## Running the Example

```bash
uv run python main_quantlib.py
```

## What This Example Covers

1. **Date Handling and Calendar Operations** - Working with business calendars and date arithmetic
2. **Day Count Conventions** - Different methods for calculating time fractions
3. **Interest Rate Calculations** - Discount factors, compounding, and rate conversions
4. **Bond Pricing and Yield Calculations** - Fixed-rate bond valuation
5. **Option Pricing** - Black-Scholes model implementation
6. **Yield Curve Construction** - Building curves from market instruments
7. **Forward Rate Calculations** - Computing forward rates from the yield curve

---

## Example 1: Date Handling and Calendar Operations

### Source Code (Lines 26-47)

```python
26: print("=" * 70)
27: print("Example 1: Date Handling and Calendar Operations")
28: print("=" * 70)
29:
30: # Create dates using QuantLib
31: date1 = ql.Date(15, 1, 2024)
32: print(f"Line 29: Created date: {date1}")  # Line 29
33:
34: # Get today's date
35: today = ql.Date.todaysDate()
36: print(f"Line 33: Today's date: {today}")  # Line 33
37:
38: # Calendar operations - US Government Bond calendar
39: us_calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
40: print(f"Line 37: Is {date1} a business day? {us_calendar.isBusinessDay(date1)}")  # Line 37
41:
42: # Advance date by 5 business days
43: advanced_date = us_calendar.advance(date1, 5, ql.Days)
44: print(f"Line 41: Date advanced by 5 business days: {advanced_date}")  # Line 41
45:
46: # Calculate business days between two dates
47: business_days = us_calendar.businessDaysBetween(date1, advanced_date)
```

### Output

```
======================================================================
Example 1: Date Handling and Calendar Operations
======================================================================
Line 29: Created date: January 15th, 2024
Line 33: Today's date: December 19th, 2025
Line 37: Is January 15th, 2024 a business day? False
Line 41: Date advanced by 5 business days: January 22nd, 2024
Line 45: Business days between January 15th, 2024 and January 22nd, 2024: 4
```

### Explanation

- **Line 31**: Creates a QuantLib Date object for January 15, 2024
- **Line 35**: Gets the current date from the system
- **Line 39**: Creates a US Government Bond calendar to handle business day rules
- **Line 40**: Checks if January 15, 2024 is a business day (it's not - MLK Day)
- **Line 43**: Advances the date by 5 business days (skips weekends)
- **Line 47**: Counts only 4 business days because the start date isn't a business day

---

## Example 2: Day Count Conventions

### Source Code (Lines 53-70)

```python
53: start_date = ql.Date(1, 1, 2024)
54: end_date = ql.Date(1, 7, 2024)
55:
56: # Different day count conventions
57: day_counters = [
58:     ("Actual/365", ql.Actual365Fixed()),
59:     ("Actual/360", ql.Actual360()),
60:     ("30/360", ql.Thirty360(ql.Thirty360.BondBasis)),
61:     ("Actual/Actual", ql.ActualActual(ql.ActualActual.ISDA)),
62: ]
63:
64: print(f"Line 65: Period from {start_date} to {end_date}:")  # Line 65
65: for name, dc in day_counters:
66:     year_fraction = dc.yearFraction(start_date, end_date)
67:     print(f"Line 68:   {name}: {year_fraction:.6f} years")  # Line 68
```

### Output

```
======================================================================
Example 2: Day Count Conventions
======================================================================
Line 65: Period from January 1st, 2024 to July 1st, 2024:
Line 68:   Actual/365: 0.498630 years
Line 68:   Actual/360: 0.505556 years
Line 68:   30/360: 0.500000 years
Line 68:   Actual/Actual: 0.497268 years
```

### Explanation

Day count conventions are crucial in fixed income calculations. The same 6-month period yields different year fractions:

- **Actual/365**: Uses actual days (182) divided by 365 = 0.4986 years
- **Actual/360**: Uses actual days (182) divided by 360 = 0.5056 years
- **30/360**: Assumes 30 days per month = 180/360 = 0.5000 years
- **Actual/Actual**: ISDA method accounts for leap years = 0.4973 years

These differences impact interest calculations on bonds and swaps.

---

## Example 3: Interest Rate Calculations

### Source Code (Lines 76-94)

```python
76: # Create an interest rate: 5% annual rate with Actual/365 day count, annual compounding
77: annual_rate = ql.InterestRate(0.05, ql.Actual365Fixed(), ql.Compounded, ql.Annual)
78: print(f"Line 80: Interest rate: {annual_rate}")  # Line 80
79:
80: # Calculate discount factor
81: discount_factor = annual_rate.discountFactor(1.0)  # 1 year
82: print(f"Line 84: Discount factor for 1 year: {discount_factor:.6f}")  # Line 84
83:
84: # Calculate compound factor
85: compound_factor = annual_rate.compoundFactor(1.0)  # 1 year
86: print(f"Line 88: Compound factor for 1 year: {compound_factor:.6f}")  # Line 88
87:
88: # Convert to different compounding
89: continuous_rate = annual_rate.equivalentRate(ql.Continuous, ql.NoFrequency, 1.0)
90: print(f"Line 92: Equivalent continuous rate: {continuous_rate.rate():.6f}")  # Line 92
```

### Output

```
======================================================================
Example 3: Interest Rate Calculations
======================================================================
Line 80: Interest rate: 5.000000 % Actual/365 (Fixed) Annual compounding
Line 84: Discount factor for 1 year: 0.952381
Line 88: Compound factor for 1 year: 1.050000
Line 92: Equivalent continuous rate: 0.048790
```

### Explanation

- **Line 81**: Discount factor = 1/(1+0.05) = 0.952381 - present value of $1 received in 1 year
- **Line 85**: Compound factor = 1.05 - future value of $1 invested for 1 year
- **Line 89**: Converts 5% annual compounding to continuous compounding (4.879%)
  - Formula: continuous_rate = ln(1 + 0.05) = 0.04879

---

## Example 4: Bond Pricing and Yield Calculations

### Source Code (Lines 100-153)

```python
100: # Set up evaluation date
101: eval_date = ql.Date(15, 1, 2024)
102: ql.Settings.instance().evaluationDate = eval_date
103: print(f"Line 104: Evaluation date: {eval_date}")  # Line 104
104:
105: # Bond parameters
106: settlement_days = 2
107: face_amount = 100.0
108: coupon_rate = 0.05  # 5% annual coupon
109: issue_date = ql.Date(15, 1, 2024)
110: maturity_date = ql.Date(15, 1, 2029)  # 5-year bond
111:
112: # Create schedule
113: calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
114: schedule = ql.Schedule(
115:     issue_date,
116:     maturity_date,
117:     ql.Period(ql.Semiannual),  # Coupon frequency
118:     calendar,
119:     ql.Unadjusted,  # Business day convention
120:     ql.Unadjusted,
121:     ql.DateGeneration.Backward,
122:     False,  # End of month
123: )
124:
125: print(f"Line 126: Bond schedule created with {len(schedule)} dates")  # Line 126
126: print(f"Line 127: Payment dates: {[str(d) for d in schedule]}")  # Line 127
127:
128: # Create fixed rate bond
129: day_count = ql.ActualActual(ql.ActualActual.Bond)
130: bond = ql.FixedRateBond(
131:     settlement_days, face_amount, schedule, [coupon_rate], day_count
132: )
133:
134: # Set bond price and calculate yield
135: bond_price = 98.50  # Price at 98.50
136: bond_yield = bond.bondYield(
137:     ql.BondPrice(bond_price, ql.BondPrice.Clean),
138:     day_count,
139:     ql.Compounded,
140:     ql.Semiannual,
141: )
142: print(f"Line 139: Bond price: ${bond_price:.2f}")  # Line 139
143: print(f"Line 140: Bond yield: {bond_yield * 100:.4f}%")  # Line 140
144:
145: # Calculate clean and dirty price from yield
146: yield_rate = 0.055  # 5.5% yield
147: clean_price = bond.cleanPrice(yield_rate, day_count, ql.Compounded, ql.Semiannual)
148: dirty_price = bond.dirtyPrice(yield_rate, day_count, ql.Compounded, ql.Semiannual)
149: accrued_interest = dirty_price - clean_price
```

### Output

```
======================================================================
Example 4: Bond Pricing and Yield Calculations
======================================================================
Line 104: Evaluation date: January 15th, 2024
Line 126: Bond schedule created with 11 dates
Line 127: Payment dates: ['January 15th, 2024', 'July 15th, 2024', 'January 15th, 2025', 'July 15th, 2025', 'January 15th, 2026', 'July 15th, 2026', 'January 15th, 2027', 'July 15th, 2027', 'January 15th, 2028', 'July 15th, 2028', 'January 15th, 2029']
Line 139: Bond price: $98.50
Line 140: Bond yield: 5.3431%
Line 148: At 5.50% yield:
Line 149:   Clean price: $97.8285
Line 150:   Dirty price: $97.8560
Line 151:   Accrued interest: $0.0275
```

### Explanation

This example prices a 5-year US Treasury bond with 5% semiannual coupons:

- **Line 114-123**: Creates payment schedule with 11 dates (issue + 10 semiannual payments)
- **Line 136-141**: Given price of $98.50, calculates yield = 5.3431%
  - Price < Par ($100) means yield > coupon rate (5%)
- **Line 147-149**: Given 5.5% yield, calculates prices:
  - Clean price: $97.83 (excludes accrued interest)
  - Dirty price: $97.86 (includes accrued interest)
  - Accrued interest: $0.03 (minimal since we're at issue date)

---

## Example 5: Option Pricing using Black-Scholes Model

### Source Code (Lines 159-227)

```python
159: # Option parameters
160: option_type = ql.Option.Call
161: underlying_price = 100.0
162: strike_price = 105.0
163: risk_free_rate = 0.05
164: volatility = 0.20
165: dividend_yield = 0.02
166: maturity = 1.0  # 1 year
...
207: # Create Black-Scholes-Merton process
208: bs_process = ql.BlackScholesMertonProcess(
209:     spot_handle, dividend_ts, flat_ts, flat_vol_ts
210: )
211:
212: # Price the option using analytical engine
213: european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bs_process))
214:
215: # Get option price and Greeks
216: option_price = european_option.NPV()
217: delta = european_option.delta()
218: gamma = european_option.gamma()
219: vega = european_option.vega()
220: theta = european_option.theta()
221: rho = european_option.rho()
```

### Output

```
======================================================================
Example 5: Option Pricing using Black-Scholes Model
======================================================================
Line 169: Option parameters:
Line 170:   Type: Call
Line 171:   Underlying price: $100.00
Line 172:   Strike price: $105.00
Line 173:   Risk-free rate: 5.00%
Line 174:   Volatility: 20.00%
Line 175:   Dividend yield: 2.00%
Line 176:   Time to maturity: 1.0 year
Line 219: Black-Scholes results:
Line 220:   Option price: $6.9869
Line 221:   Delta: 0.4925
Line 222:   Gamma: 0.0196
Line 223:   Vega: 39.1036
Line 224:   Theta: -5.0384
Line 225:   Rho: 42.2596
```

### Explanation

Prices a European call option using the Black-Scholes-Merton model:

- **Option Value**: $6.99 - fair price for the right (not obligation) to buy at $105
- **Delta (0.49)**: Option price increases by $0.49 for each $1 increase in stock price
  - Roughly 49% probability of finishing in-the-money
- **Gamma (0.0196)**: Delta increases by 0.0196 for each $1 stock price increase
  - Measures curvature of option value
- **Vega (39.10)**: Option price increases by $39.10 for 1% absolute increase in volatility
  - Options are very sensitive to volatility changes
- **Theta (-5.04)**: Option loses $5.04 per year from time decay (per day: -$0.014)
- **Rho (42.26)**: Option price increases by $42.26 for 1% absolute increase in interest rates

---

## Example 6: Yield Curve Construction

### Source Code (Lines 233-308)

```python
233: # Set evaluation date
234: curve_date = ql.Date(15, 1, 2024)
235: ql.Settings.instance().evaluationDate = curve_date
236: print(f"Line 237: Curve construction date: {curve_date}")  # Line 237
237:
238: # Define market rates for different tenors
239: deposits = {
240:     "1M": 0.0450,
241:     "3M": 0.0460,
242:     "6M": 0.0475,
243: }
244:
245: swaps = {
246:     "1Y": 0.0490,
247:     "2Y": 0.0510,
248:     "3Y": 0.0530,
249:     "5Y": 0.0560,
250:     "7Y": 0.0580,
251:     "10Y": 0.0600,
252: }
...
301: # Construct the yield curve
302: yield_curve = ql.PiecewiseLogCubicDiscount(curve_date, helpers, day_count_curve)
303: yield_curve.enableExtrapolation()
```

### Output

```
======================================================================
Example 6: Yield Curve Construction
======================================================================
Line 237: Curve construction date: January 15th, 2024
Line 255: Market rates:
Line 256: Deposits: {'1M': 0.045, '3M': 0.046, '6M': 0.0475}
Line 257: Swaps: {'1Y': 0.049, '2Y': 0.051, '3Y': 0.053, '5Y': 0.056, '7Y': 0.058, '10Y': 0.06}
Line 306: Yield curve constructed with 9 instruments
```

### Explanation

Constructs a yield curve using market instruments:

- **Deposits (short end)**: 1M, 3M, 6M rates for the front of the curve
- **Swaps (long end)**: 1Y through 10Y for the rest of the curve
- **Line 302**: Uses piecewise log-cubic interpolation for smooth discount factors
- **Result**: A complete term structure for pricing and risk management

The upward sloping curve (4.5% at 1M to 6% at 10Y) indicates a normal yield curve where longer-term rates are higher.

---

## Example 7: Forward Rate Calculations

### Source Code (Lines 314-345)

```python
314: # Calculate spot and forward rates
315: years = [0.25, 0.5, 1, 2, 3, 5, 7, 10]
316: print("Line 317: Zero rates and forward rates:")  # Line 317
317: print(f"Line 318: {'Tenor':<10} {'Zero Rate':<15} {'Discount':<15}")  # Line 318
318:
319: for year in years:
320:     date_future = curve_date + ql.Period(int(year * 365), ql.Days)
321:     zero_rate = yield_curve.zeroRate(year, ql.Compounded, ql.Annual)
322:     discount = yield_curve.discount(date_future)
323:     print(
324:         f"Line 324: {year:<10.2f} {zero_rate.rate() * 100:<15.4f} {discount:<15.6f}"
325:     )  # Line 324
...
331: # Calculate 1-year forward rates starting at different points
332: forward_starts = [0, 1, 2, 3, 5, 7]
333: for start_year in forward_starts:
334:     end_year = start_year + 1
335:     if end_year <= 10:
336:         date_start = curve_date + ql.Period(int(start_year * 365), ql.Days)
337:         date_end = curve_date + ql.Period(int(end_year * 365), ql.Days)
338:         forward_rate = yield_curve.forwardRate(
339:             date_start, date_end, day_count_curve, ql.Compounded, ql.Annual
340:         )
```

### Output

```
======================================================================
Example 7: Forward Rate Calculations
======================================================================
Line 317: Zero rates and forward rates:
Line 318: Tenor      Zero Rate       Discount
Line 324: 0.25       4.6693          0.988526
Line 324: 0.50       4.7986          0.976576
Line 324: 1.00       4.8133          0.953447
Line 324: 2.00       5.0139          0.905445
Line 324: 3.00       5.2225          0.856358
Line 324: 5.00       5.5390          0.760538
Line 324: 7.00       5.7601          0.671608
Line 324: 10.00      5.9926          0.553852

Line 328: Forward rates (1-year forward rates):
Line 329: Start      End        Forward Rate
Line 343: 0          1          4.8141         %
Line 343: 1          2          5.2270         %
Line 343: 2          3          5.6513         %
Line 343: 3          4          5.9256         %
Line 343: 5          6          6.2661         %
Line 343: 7          8          6.4841         %
```

### Explanation

Demonstrates spot rates and forward rate calculations:

- **Zero Rates**: Rates for borrowing/lending from today to a future date
  - Increase from 4.67% (3M) to 5.99% (10Y) - upward sloping curve

- **Discount Factors**: Present value of $1 received in the future
  - Decrease from 0.9885 (3M) to 0.5539 (10Y)

- **Forward Rates**: Implied future rates between two forward dates
  - 1Y forward starting now: 4.81% (same as 1Y zero rate)
  - 1Y forward starting in 1Y: 5.23% (higher due to curve shape)
  - 1Y forward starting in 7Y: 6.48% (much higher)

Forward rates are critical for:
- Hedging future borrowing costs
- Valuing interest rate derivatives
- Understanding market expectations

---

## Version Requirements

This example uses QuantLib 1.40 with Python 3.11. The QuantLib-Python bindings provide access to the full QuantLib C++ library for quantitative finance calculations.

**Note**: Some API methods like `bondYield()` require specific parameter types (e.g., `BondPrice` objects rather than simple floats). Always refer to the QuantLib documentation for precise method signatures.
