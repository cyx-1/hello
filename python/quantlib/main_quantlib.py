# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "QuantLib>=1.34",
# ]
# ///
"""
QuantLib Example: Quantitative Finance Library Demonstration

This example showcases key QuantLib concepts:
1. Date handling and calendar operations
2. Day count conventions
3. Interest rate calculations
4. Bond pricing and yield calculations
5. Option pricing using Black-Scholes model
6. Yield curve construction
7. Forward rate calculations
"""

import QuantLib as ql


# Example 1: Date Handling and Calendar Operations
print("=" * 70)
print("Example 1: Date Handling and Calendar Operations")
print("=" * 70)

# Create dates using QuantLib
date1 = ql.Date(15, 1, 2024)
print(f"Line 29: Created date: {date1}")  # Line 29

# Get today's date
today = ql.Date.todaysDate()
print(f"Line 33: Today's date: {today}")  # Line 33

# Calendar operations - US Government Bond calendar
us_calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
print(f"Line 37: Is {date1} a business day? {us_calendar.isBusinessDay(date1)}")  # Line 37

# Advance date by 5 business days
advanced_date = us_calendar.advance(date1, 5, ql.Days)
print(f"Line 41: Date advanced by 5 business days: {advanced_date}")  # Line 41

# Calculate business days between two dates
business_days = us_calendar.businessDaysBetween(date1, advanced_date)
print(f"Line 45: Business days between {date1} and {advanced_date}: {business_days}")  # Line 45
print()


# Example 2: Day Count Conventions
print("=" * 70)
print("Example 2: Day Count Conventions")
print("=" * 70)

start_date = ql.Date(1, 1, 2024)
end_date = ql.Date(1, 7, 2024)

# Different day count conventions
day_counters = [
    ("Actual/365", ql.Actual365Fixed()),
    ("Actual/360", ql.Actual360()),
    ("30/360", ql.Thirty360(ql.Thirty360.BondBasis)),
    ("Actual/Actual", ql.ActualActual(ql.ActualActual.ISDA)),
]

print(f"Line 65: Period from {start_date} to {end_date}:")  # Line 65
for name, dc in day_counters:
    year_fraction = dc.yearFraction(start_date, end_date)
    print(f"Line 68:   {name}: {year_fraction:.6f} years")  # Line 68
print()


# Example 3: Interest Rate Calculations
print("=" * 70)
print("Example 3: Interest Rate Calculations")
print("=" * 70)

# Create an interest rate: 5% annual rate with Actual/365 day count, annual compounding
annual_rate = ql.InterestRate(0.05, ql.Actual365Fixed(), ql.Compounded, ql.Annual)
print(f"Line 80: Interest rate: {annual_rate}")  # Line 80

# Calculate discount factor
discount_factor = annual_rate.discountFactor(1.0)  # 1 year
print(f"Line 84: Discount factor for 1 year: {discount_factor:.6f}")  # Line 84

# Calculate compound factor
compound_factor = annual_rate.compoundFactor(1.0)  # 1 year
print(f"Line 88: Compound factor for 1 year: {compound_factor:.6f}")  # Line 88

# Convert to different compounding
continuous_rate = annual_rate.equivalentRate(ql.Continuous, ql.NoFrequency, 1.0)
print(f"Line 92: Equivalent continuous rate: {continuous_rate.rate():.6f}")  # Line 92
print()


# Example 4: Bond Pricing and Yield Calculations
print("=" * 70)
print("Example 4: Bond Pricing and Yield Calculations")
print("=" * 70)

# Set up evaluation date
eval_date = ql.Date(15, 1, 2024)
ql.Settings.instance().evaluationDate = eval_date
print(f"Line 104: Evaluation date: {eval_date}")  # Line 104

# Bond parameters
settlement_days = 2
face_amount = 100.0
coupon_rate = 0.05  # 5% annual coupon
issue_date = ql.Date(15, 1, 2024)
maturity_date = ql.Date(15, 1, 2029)  # 5-year bond

# Create schedule
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
schedule = ql.Schedule(
    issue_date,
    maturity_date,
    ql.Period(ql.Semiannual),  # Coupon frequency
    calendar,
    ql.Unadjusted,  # Business day convention
    ql.Unadjusted,
    ql.DateGeneration.Backward,
    False,  # End of month
)

print(f"Line 126: Bond schedule created with {len(schedule)} dates")  # Line 126
print(f"Line 127: Payment dates: {[str(d) for d in schedule]}")  # Line 127

# Create fixed rate bond
day_count = ql.ActualActual(ql.ActualActual.Bond)
bond = ql.FixedRateBond(
    settlement_days, face_amount, schedule, [coupon_rate], day_count
)

# Set bond price and calculate yield
bond_price = 98.50  # Price at 98.50
bond_yield = bond.bondYield(
    ql.BondPrice(bond_price, ql.BondPrice.Clean),
    day_count,
    ql.Compounded,
    ql.Semiannual,
)
print(f"Line 139: Bond price: ${bond_price:.2f}")  # Line 139
print(f"Line 140: Bond yield: {bond_yield * 100:.4f}%")  # Line 140

# Calculate clean and dirty price from yield
yield_rate = 0.055  # 5.5% yield
clean_price = bond.cleanPrice(yield_rate, day_count, ql.Compounded, ql.Semiannual)
dirty_price = bond.dirtyPrice(yield_rate, day_count, ql.Compounded, ql.Semiannual)
accrued_interest = dirty_price - clean_price
print(f"Line 148: At {yield_rate * 100:.2f}% yield:")  # Line 148
print(f"Line 149:   Clean price: ${clean_price:.4f}")  # Line 149
print(f"Line 150:   Dirty price: ${dirty_price:.4f}")  # Line 150
print(f"Line 151:   Accrued interest: ${accrued_interest:.4f}")  # Line 151
print()


# Example 5: Option Pricing using Black-Scholes Model
print("=" * 70)
print("Example 5: Option Pricing using Black-Scholes Model")
print("=" * 70)

# Option parameters
option_type = ql.Option.Call
underlying_price = 100.0
strike_price = 105.0
risk_free_rate = 0.05
volatility = 0.20
dividend_yield = 0.02
maturity = 1.0  # 1 year

print("Line 169: Option parameters:")  # Line 169
print("Line 170:   Type: Call")  # Line 170
print(f"Line 171:   Underlying price: ${underlying_price:.2f}")  # Line 171
print(f"Line 172:   Strike price: ${strike_price:.2f}")  # Line 172
print(f"Line 173:   Risk-free rate: {risk_free_rate * 100:.2f}%")  # Line 173
print(f"Line 174:   Volatility: {volatility * 100:.2f}%")  # Line 174
print(f"Line 175:   Dividend yield: {dividend_yield * 100:.2f}%")  # Line 175
print(f"Line 176:   Time to maturity: {maturity} year")  # Line 176

# Set up Black-Scholes process
calculation_date = ql.Date(15, 1, 2024)
ql.Settings.instance().evaluationDate = calculation_date

maturity_date_option = calculation_date + ql.Period(int(maturity * 365), ql.Days)
payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.EuropeanExercise(maturity_date_option)
european_option = ql.VanillaOption(payoff, exercise)

# Create flat term structures
spot_handle = ql.QuoteHandle(ql.SimpleQuote(underlying_price))
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, risk_free_rate, ql.Actual365Fixed())
)
dividend_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, dividend_yield, ql.Actual365Fixed())
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date, calendar, volatility, ql.Actual365Fixed())
)

# Create Black-Scholes-Merton process
bs_process = ql.BlackScholesMertonProcess(
    spot_handle, dividend_ts, flat_ts, flat_vol_ts
)

# Price the option using analytical engine
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bs_process))

# Get option price and Greeks
option_price = european_option.NPV()
delta = european_option.delta()
gamma = european_option.gamma()
vega = european_option.vega()
theta = european_option.theta()
rho = european_option.rho()

print("Line 219: Black-Scholes results:")  # Line 219
print(f"Line 220:   Option price: ${option_price:.4f}")  # Line 220
print(f"Line 221:   Delta: {delta:.4f}")  # Line 221
print(f"Line 222:   Gamma: {gamma:.4f}")  # Line 222
print(f"Line 223:   Vega: {vega:.4f}")  # Line 223
print(f"Line 224:   Theta: {theta:.4f}")  # Line 224
print(f"Line 225:   Rho: {rho:.4f}")  # Line 225
print()


# Example 6: Yield Curve Construction
print("=" * 70)
print("Example 6: Yield Curve Construction")
print("=" * 70)

# Set evaluation date
curve_date = ql.Date(15, 1, 2024)
ql.Settings.instance().evaluationDate = curve_date
print(f"Line 237: Curve construction date: {curve_date}")  # Line 237

# Define market rates for different tenors
deposits = {
    "1M": 0.0450,
    "3M": 0.0460,
    "6M": 0.0475,
}

swaps = {
    "1Y": 0.0490,
    "2Y": 0.0510,
    "3Y": 0.0530,
    "5Y": 0.0560,
    "7Y": 0.0580,
    "10Y": 0.0600,
}

print("Line 255: Market rates:")  # Line 255
print(f"Line 256: Deposits: {deposits}")  # Line 256
print(f"Line 257: Swaps: {swaps}")  # Line 257

# Build curve using deposit and swap helpers
calendar_curve = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
day_count_curve = ql.Actual360()
helpers = []

# Add deposit helpers
for tenor_str, rate in deposits.items():
    tenor = ql.Period(tenor_str)
    helper = ql.DepositRateHelper(
        ql.QuoteHandle(ql.SimpleQuote(rate)),
        tenor,
        2,
        calendar_curve,
        ql.ModifiedFollowing,
        False,
        day_count_curve,
    )
    helpers.append(helper)

# Add swap helpers
swap_fixed_leg_frequency = ql.Annual
swap_fixed_leg_convention = ql.ModifiedFollowing
swap_fixed_leg_day_count = ql.Thirty360(ql.Thirty360.BondBasis)
swap_index = ql.USDLibor(ql.Period(3, ql.Months))

for tenor_str, rate in swaps.items():
    tenor = ql.Period(tenor_str)
    helper = ql.SwapRateHelper(
        ql.QuoteHandle(ql.SimpleQuote(rate)),
        tenor,
        calendar_curve,
        swap_fixed_leg_frequency,
        swap_fixed_leg_convention,
        swap_fixed_leg_day_count,
        swap_index,
    )
    helpers.append(helper)

# Construct the yield curve
yield_curve = ql.PiecewiseLogCubicDiscount(curve_date, helpers, day_count_curve)
yield_curve.enableExtrapolation()

print(f"Line 306: Yield curve constructed with {len(helpers)} instruments")  # Line 306
print()


# Example 7: Forward Rate Calculations
print("=" * 70)
print("Example 7: Forward Rate Calculations")
print("=" * 70)

# Calculate spot and forward rates
years = [0.25, 0.5, 1, 2, 3, 5, 7, 10]
print("Line 317: Zero rates and forward rates:")  # Line 317
print(f"Line 318: {'Tenor':<10} {'Zero Rate':<15} {'Discount':<15}")  # Line 318

for year in years:
    date_future = curve_date + ql.Period(int(year * 365), ql.Days)
    zero_rate = yield_curve.zeroRate(year, ql.Compounded, ql.Annual)
    discount = yield_curve.discount(date_future)
    print(
        f"Line 324: {year:<10.2f} {zero_rate.rate() * 100:<15.4f} {discount:<15.6f}"
    )  # Line 324

print()
print("Line 328: Forward rates (1-year forward rates):")  # Line 328
print(f"Line 329: {'Start':<10} {'End':<10} {'Forward Rate':<15}")  # Line 329

# Calculate 1-year forward rates starting at different points
forward_starts = [0, 1, 2, 3, 5, 7]
for start_year in forward_starts:
    end_year = start_year + 1
    if end_year <= 10:
        date_start = curve_date + ql.Period(int(start_year * 365), ql.Days)
        date_end = curve_date + ql.Period(int(end_year * 365), ql.Days)
        forward_rate = yield_curve.forwardRate(
            date_start, date_end, day_count_curve, ql.Compounded, ql.Annual
        )
        print(
            f"Line 343: {start_year:<10} {end_year:<10} {forward_rate.rate() * 100:<15.4f}%"
        )  # Line 343

print()
print("=" * 70)
print("Line 347: All QuantLib examples completed successfully!")  # Line 347
print("=" * 70)
