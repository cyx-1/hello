# SciPy Library Demonstration

This example demonstrates comprehensive usage of the SciPy library in Python, showcasing its six major modules for scientific computing.

## Requirements

- **Python**: 3.9+ (tested on 3.11)
- **SciPy**: 1.11.0 or higher (tested on 1.14.0+)
- **NumPy**: 1.24.0 or higher

**Note**: This code uses `RegularGridInterpolator` for 2D interpolation, which is the recommended approach in SciPy 1.14.0+ (the deprecated `interp2d` function has been removed).

## Running the Code

```bash
uv run main_scipy.py
```

## Code Structure and Output

### 1. Optimization (scipy.optimize)

The code demonstrates function minimization, root finding, and curve fitting.

**Source Code (Lines 34-62):**
```python
34: def demonstrate_optimization() -> None:
35:     """Demonstrate scipy.optimize for function minimization and root finding."""
36:     print_section("1. OPTIMIZATION (scipy.optimize)")
37:
38:     # Example 1: Minimize a simple quadratic function
39:     print("Example 1.1: Minimize f(x) = (x - 3)^2 + 5")
40:
41:     def quadratic(x):
42:         return (x - 3)**2 + 5
43:
44:     result = optimize.minimize(quadratic, x0=0)
45:     print(f"  Minimum found at x = {result.x[0]:.6f}")
46:     print(f"  Minimum value f(x) = {result.fun:.6f}")
47:     print(f"  Success: {result.success}")
48:
49:     # Example 2: Root finding
50:     print("\nExample 1.2: Find root of f(x) = x^3 - 2x - 5")
51:
52:     def cubic(x):
53:         return x**3 - 2*x - 5
54:
55:     root = optimize.fsolve(cubic, x0=2)
56:     print(f"  Root found at x = {root[0]:.6f}")
57:     print(f"  Verification f({root[0]:.6f}) = {cubic(root[0]):.10f}")
58:
59:     # Example 3: Curve fitting
60:     print("\nExample 1.3: Curve fitting to exponential data")
61:
62:     def exponential_model(x, a, b, c):
```

**Output:**
```
Example 1.1: Minimize f(x) = (x - 3)^2 + 5
  Minimum found at x = 3.000000
  Minimum value f(x) = 5.000000
  Success: True

Example 1.2: Find root of f(x) = x^3 - 2x - 5
  Root found at x = 2.094551
  Verification f(2.094551) = -0.0000000000

Example 1.3: Curve fitting to exponential data
  Fitted parameters: a=2.2821, b=0.5183, c=1.2658
  Expected: a=2.5, b=0.5, c=1.0
```

**Annotations:**
- **Line 44**: `optimize.minimize()` uses the BFGS algorithm by default to find the minimum of the quadratic function starting from x=0
- **Output Line 2**: The optimizer successfully finds the minimum at x=3, which is the analytical solution
- **Line 55**: `optimize.fsolve()` uses a modified Powell hybrid method to find roots of the cubic equation
- **Output Line 6**: Root verification shows extremely high precision (10 decimal places near zero)
- **Lines 62-70**: `optimize.curve_fit()` fits an exponential model to noisy synthetic data
- **Output Lines 10-11**: Fitted parameters are close to the true values (a=2.5, b=0.5, c=1.0) despite noise

### 2. Integration (scipy.integrate)

Demonstrates numerical integration and ODE solving.

**Source Code (Lines 74-106):**
```python
74: def demonstrate_integration() -> None:
75:     """Demonstrate scipy.integrate for numerical integration."""
76:     print_section("2. INTEGRATION (scipy.integrate)")
77:
78:     # Example 1: Definite integral
79:     print("Example 2.1: Compute integral of x^2 from 0 to 3")
80:
81:     def square(x):
82:         return x**2
83:
84:     result, error = integrate.quad(square, 0, 3)
85:     print(f"  Numerical result: {result:.6f}")
86:     print(f"  Analytical result: {3**3 / 3:.6f}")
87:     print(f"  Estimated error: {error:.2e}")
88:
89:     # Example 2: Integration of a Gaussian
90:     print("\nExample 2.2: Integrate Gaussian e^(-x^2) from -∞ to ∞")
91:
92:     def gaussian(x):
93:         return np.exp(-x**2)
94:
95:     result, error = integrate.quad(gaussian, -np.inf, np.inf)
96:     print(f"  Numerical result: {result:.6f}")
97:     print(f"  Analytical result (√π): {np.sqrt(np.pi):.6f}")
98:     print(f"  Estimated error: {error:.2e}")
99:
100:     # Example 3: Solve ODE (Ordinary Differential Equation)
101:     print("\nExample 2.3: Solve ODE dy/dt = -2y, y(0) = 1")
102:
103:     def exponential_decay(t, y):
104:         return -2 * y
```

**Output:**
```
Example 2.1: Compute integral of x^2 from 0 to 3
  Numerical result: 9.000000
  Analytical result: 9.000000
  Estimated error: 9.99e-14

Example 2.2: Integrate Gaussian e^(-x^2) from -∞ to ∞
  Numerical result: 1.772454
  Analytical result (√π): 1.772454
  Estimated error: 1.42e-08

Example 2.3: Solve ODE dy/dt = -2y, y(0) = 1
  Time points: [0.         0.22222222 0.44444444 0.66666667 0.88888889]
  Solution values: [1.         0.6408121  0.41114521 0.26368819 0.16914296]
  Expected (e^(-2t)): [1.         0.64118039 0.41111229 0.26359714 0.16901332]
```

**Annotations:**
- **Line 84**: `integrate.quad()` performs adaptive quadrature integration
- **Output Line 2**: Perfect agreement with analytical result (∫x² dx from 0 to 3 = 9)
- **Output Line 3**: Error estimate is extremely small (10^-14), showing high accuracy
- **Line 95**: Integration with infinite limits using `np.inf`
- **Output Lines 6-7**: Result matches √π analytically (1.772454...)
- **Lines 103-109**: `solve_ivp()` solves the initial value problem using the Runge-Kutta method
- **Output Lines 11-12**: Numerical solution closely matches analytical solution y(t) = e^(-2t)

### 3. Interpolation (scipy.interpolate)

Shows linear, cubic spline, and 2D grid interpolation.

**Source Code (Lines 110-143):**
```python
110: def demonstrate_interpolation() -> None:
111:     """Demonstrate scipy.interpolate for data interpolation."""
112:     print_section("3. INTERPOLATION (scipy.interpolate)")
113:
114:     # Generate sample data
115:     x = np.array([0, 1, 2, 3, 4, 5])
116:     y = np.array([0, 1, 4, 9, 16, 25])  # y = x^2
117:     x_new = np.array([0.5, 1.5, 2.5, 3.5])
118:
119:     # Example 1: Linear interpolation
120:     print("Example 3.1: Linear interpolation of y = x^2")
121:     f_linear = interpolate.interp1d(x, y, kind='linear')
122:     y_linear = f_linear(x_new)
123:     print(f"  x_new: {x_new}")
124:     print(f"  Interpolated y: {y_linear}")
125:     print(f"  Actual y = x^2: {x_new**2}")
126:
127:     # Example 2: Cubic spline interpolation
128:     print("\nExample 3.2: Cubic spline interpolation")
129:     f_cubic = interpolate.interp1d(x, y, kind='cubic')
130:     y_cubic = f_cubic(x_new)
131:     print(f"  x_new: {x_new}")
132:     print(f"  Interpolated y: {y_cubic}")
133:     print(f"  Actual y = x^2: {x_new**2}")
134:     print(f"  Error: {np.abs(y_cubic - x_new**2)}")
135:
136:     # Example 3: 2D interpolation
137:     print("\nExample 3.3: 2D interpolation on a grid")
138:     x_grid = np.array([0, 1, 2])
139:     y_grid = np.array([0, 1, 2])
140:     z_values = np.array([[0, 1, 4], [1, 2, 5], [4, 5, 8]])
141:
142:     f_2d = interpolate.RegularGridInterpolator((x_grid, y_grid), z_values)
143:     z_new = f_2d([[0.5, 0.5]])
```

**Output:**
```
Example 3.1: Linear interpolation of y = x^2
  x_new: [0.5 1.5 2.5 3.5]
  Interpolated y: [ 0.5  2.5  6.5 12.5]
  Actual y = x^2: [ 0.25  2.25  6.25 12.25]

Example 3.2: Cubic spline interpolation
  x_new: [0.5 1.5 2.5 3.5]
  Interpolated y: [ 0.25  2.25  6.25 12.25]
  Actual y = x^2: [ 0.25  2.25  6.25 12.25]
  Error: [2.77555756e-16 4.44089210e-16 8.88178420e-16 0.00000000e+00]

Example 3.3: 2D interpolation on a grid
  Interpolated z at (0.5, 0.5): 1.0000
```

**Annotations:**
- **Lines 115-116**: Data points sampled from y = x² function
- **Line 121**: Linear interpolation connects points with straight lines
- **Output Lines 2-3**: Linear interpolation shows noticeable error (e.g., 0.5 vs 0.25 at x=0.5)
- **Line 129**: Cubic spline provides smooth, higher-order interpolation
- **Output Lines 7-8**: Cubic spline achieves near-perfect accuracy (errors < 10^-15) for this quadratic function
- **Line 142**: `RegularGridInterpolator` is the modern replacement for deprecated `interp2d` (SciPy 1.14+)
- **Output Line 11**: 2D interpolation at point (0.5, 0.5) gives z = 1.0

### 4. Statistics (scipy.stats)

Demonstrates statistical distributions, hypothesis testing, and correlation.

**Source Code (Lines 147-193):**
```python
147: def demonstrate_statistics() -> None:
148:     """Demonstrate scipy.stats for statistical analysis."""
149:     print_section("4. STATISTICS (scipy.stats)")
150:
151:     # Example 1: Descriptive statistics
152:     print("Example 4.1: Descriptive statistics of normal distribution")
153:     data = np.random.normal(loc=100, scale=15, size=1000)
154:     print(f"  Mean: {np.mean(data):.2f}")
155:     print(f"  Std Dev: {np.std(data, ddof=1):.2f}")
156:     print(f"  Median: {np.median(data):.2f}")
157:     desc = stats.describe(data)
158:     print(f"  Skewness: {desc.skewness:.4f}")
159:     print(f"  Kurtosis: {desc.kurtosis:.4f}")
160:
161:     # Example 2: Probability distributions
162:     print("\nExample 4.2: Normal distribution properties")
163:     normal_dist = stats.norm(loc=0, scale=1)
164:     print(f"  P(X ≤ 1.96) = {normal_dist.cdf(1.96):.4f}")
165:     print(f"  P(X ≤ -1.96) = {normal_dist.cdf(-1.96):.4f}")
166:     print(f"  95th percentile: {normal_dist.ppf(0.95):.4f}")
167:
168:     # Example 3: Hypothesis testing (t-test)
169:     print("\nExample 4.3: Two-sample t-test")
170:     group1 = np.random.normal(100, 15, 50)
171:     group2 = np.random.normal(105, 15, 50)
172:     t_stat, p_value = stats.ttest_ind(group1, group2)
173:     print(f"  Group 1 mean: {np.mean(group1):.2f}")
174:     print(f"  Group 2 mean: {np.mean(group2):.2f}")
175:     print(f"  t-statistic: {t_stat:.4f}")
176:     print(f"  p-value: {p_value:.4f}")
177:     print(f"  Significant at α=0.05? {p_value < 0.05}")
```

**Output:**
```
Example 4.1: Descriptive statistics of normal distribution
  Mean: 100.70
  Std Dev: 14.71
  Median: 100.72
  Skewness: 0.0996
  Kurtosis: 0.0444

Example 4.2: Normal distribution properties
  P(X ≤ 1.96) = 0.9750
  P(X ≤ -1.96) = 0.0250
  95th percentile: 1.6449

Example 4.3: Two-sample t-test
  Group 1 mean: 99.90
  Group 2 mean: 108.74
  t-statistic: -3.0026
  p-value: 0.0034
  Significant at α=0.05? True

Example 4.4: Pearson correlation
  Correlation coefficient: 0.9764
  p-value: 4.5040e-67
```

**Annotations:**
- **Line 153**: Generate 1000 samples from N(100, 15²) distribution
- **Output Lines 2-4**: Sample statistics closely match population parameters (mean≈100, std≈15)
- **Output Line 5**: Skewness near 0 indicates symmetric distribution (as expected for normal)
- **Line 164**: `cdf()` computes cumulative distribution function P(X ≤ x)
- **Output Lines 8-9**: Standard normal critical values for 95% confidence (±1.96)
- **Line 172**: `ttest_ind()` performs independent two-sample t-test
- **Output Line 16**: p-value = 0.0034 < 0.05, indicating significant difference between groups
- **Lines 180-184**: Pearson correlation between x and y = 2x + noise
- **Output Line 19**: High correlation (0.9764) confirms strong linear relationship

### 5. Linear Algebra (scipy.linalg)

Shows solving linear systems, eigenvalue problems, and matrix decompositions.

**Source Code (Lines 195-234):**
```python
195: def demonstrate_linear_algebra() -> None:
196:     """Demonstrate scipy.linalg for linear algebra operations."""
197:     print_section("5. LINEAR ALGEBRA (scipy.linalg)")
198:
199:     # Example 1: Solve linear system Ax = b
200:     print("Example 5.1: Solve linear system Ax = b")
201:     A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
202:     b = np.array([1, -2, 0])
203:     x = linalg.solve(A, b)
204:     print(f"  Matrix A:\n{A}")
205:     print(f"  Vector b: {b}")
206:     print(f"  Solution x: {x}")
207:     print(f"  Verification Ax: {np.dot(A, x)}")
208:
209:     # Example 2: Eigenvalues and eigenvectors
210:     print("\nExample 5.2: Eigenvalues and eigenvectors")
211:     matrix = np.array([[4, -2], [1, 1]])
212:     eigenvalues, eigenvectors = linalg.eig(matrix)
213:     print(f"  Matrix:\n{matrix}")
214:     print(f"  Eigenvalues: {eigenvalues}")
215:     print(f"  Eigenvectors:\n{eigenvectors}")
216:
217:     # Example 3: Matrix decompositions (SVD)
218:     print("\nExample 5.3: Singular Value Decomposition (SVD)")
219:     matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
220:     U, s, Vt = linalg.svd(matrix)
221:     print(f"  Original matrix shape: {matrix.shape}")
222:     print(f"  U shape: {U.shape}")
223:     print(f"  Singular values: {s}")
224:     print(f"  Vt shape: {Vt.shape}")
```

**Output:**
```
Example 5.1: Solve linear system Ax = b
  Matrix A:
[[ 3.   2.  -1. ]
 [ 2.  -2.   4. ]
 [-1.   0.5 -1. ]]
  Vector b: [ 1 -2  0]
  Solution x: [ 1. -2. -2.]
  Verification Ax: [ 1.00000000e+00 -2.00000000e+00 -2.22044605e-16]

Example 5.2: Eigenvalues and eigenvectors
  Matrix:
[[ 4 -2]
 [ 1  1]]
  Eigenvalues: [3.+0.j 2.+0.j]
  Eigenvectors:
[[0.89442719 0.70710678]
 [0.4472136  0.70710678]]

Example 5.3: Singular Value Decomposition (SVD)
  Original matrix shape: (4, 3)
  U shape: (4, 4)
  Singular values: [2.54624074e+01 1.29066168e+00 1.80972823e-15]
  Vt shape: (3, 3)

Example 5.4: Determinant and inverse
  Matrix:
[[1 2]
 [3 4]]
  Determinant: -2.0000
  Inverse:
[[-2.   1. ]
 [ 1.5 -0.5]]
  Verification (A × A^-1):
[[1.0000000e+00 0.0000000e+00]
 [8.8817842e-16 1.0000000e+00]]
```

**Annotations:**
- **Line 203**: `linalg.solve()` efficiently solves Ax = b using LU decomposition
- **Output Line 6**: Solution x = [1, -2, -2] is exact
- **Output Line 7**: Verification shows Ax = b (third component ~0 due to floating-point precision)
- **Line 212**: `linalg.eig()` computes eigenvalues and eigenvectors
- **Output Line 11**: Eigenvalues λ₁=3, λ₂=2 satisfy det(A - λI) = 0
- **Line 220**: SVD decomposes matrix A into A = U·Σ·Vᵀ
- **Output Line 17**: Three singular values (matrix has rank 2, third value ≈0)
- **Lines 226-234**: Compute determinant and matrix inverse
- **Output Line 28**: A·A⁻¹ = I (identity matrix) verifies the inverse

### 6. Signal Processing (scipy.signal)

Demonstrates signal analysis, filtering, convolution, and resampling.

**Source Code (Lines 236-275):**
```python
236: def demonstrate_signal_processing() -> None:
237:     """Demonstrate scipy.signal for signal processing."""
238:     print_section("6. SIGNAL PROCESSING (scipy.signal)")
239:
240:     # Example 1: Create and analyze a signal
241:     print("Example 6.1: Fourier transform of a composite signal")
242:     fs = 1000  # Sampling frequency
243:     t = np.linspace(0, 1, fs, endpoint=False)
244:     # Composite signal: 50 Hz + 120 Hz
245:     signal_data = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)
246:
247:     frequencies, spectrum = signal.periodogram(signal_data, fs)
248:     # Find peaks in spectrum
249:     peaks, _ = signal.find_peaks(spectrum, height=0.1)
250:     print(f"  Signal: 50 Hz + 120 Hz sine waves")
251:     print(f"  Sampling frequency: {fs} Hz")
252:     print(f"  Detected peaks at frequencies: {frequencies[peaks][:5]} Hz")
253:
254:     # Example 2: Filter design and application
255:     print("\nExample 6.2: Butterworth lowpass filter")
256:     # Design a 4th-order Butterworth lowpass filter with cutoff at 100 Hz
257:     sos = signal.butter(4, 100, btype='low', fs=fs, output='sos')
258:     filtered_signal = signal.sosfilt(sos, signal_data)
259:     print(f"  Original signal length: {len(signal_data)}")
260:     print(f"  Filtered signal length: {len(filtered_signal)}")
261:     print(f"  Filter order: 4")
262:     print(f"  Cutoff frequency: 100 Hz")
263:     print(f"  Original RMS: {np.sqrt(np.mean(signal_data**2)):.4f}")
264:     print(f"  Filtered RMS: {np.sqrt(np.mean(filtered_signal**2)):.4f}")
```

**Output:**
```
Example 6.1: Fourier transform of a composite signal
  Signal: 50 Hz + 120 Hz sine waves
  Sampling frequency: 1000 Hz
  Detected peaks at frequencies: [ 50. 120.] Hz

Example 6.2: Butterworth lowpass filter
  Original signal length: 1000
  Filtered signal length: 1000
  Filter order: 4
  Cutoff frequency: 100 Hz
  Original RMS: 0.7906
  Filtered RMS: 0.7190

Example 6.3: Signal convolution
  Original signal: [1 2 3 4 5]
  Kernel: [0.5 1.  0.5]
  Convolved signal: [2. 4. 6. 8. 7.]

Example 6.4: Signal resampling
  Original signal length: 100
  Resampled signal length: 50
  Original signal range: [-0.9999, 0.9999]
  Resampled signal range: [-0.9937, 0.9943]
```

**Annotations:**
- **Line 245**: Composite signal with two frequency components (50 Hz and 120 Hz)
- **Line 247**: `periodogram()` computes power spectral density using FFT
- **Output Line 4**: Correctly identifies both frequency peaks at 50 Hz and 120 Hz
- **Line 257**: Design 4th-order Butterworth filter with 100 Hz cutoff (uses SOS format for numerical stability)
- **Line 258**: `sosfilt()` applies the filter to remove frequencies above 100 Hz
- **Output Lines 10-11**: Filtered RMS (0.7190) < Original RMS (0.7906) because 120 Hz component is attenuated
- **Lines 266-270**: Convolution is a fundamental operation in signal processing
- **Output Line 15**: Convolution smooths the signal using kernel [0.5, 1, 0.5]
- **Line 274**: `resample()` changes sampling rate using Fourier method
- **Output Lines 17-19**: Signal downsampled from 100 to 50 points while preserving range

## Summary

This example demonstrates SciPy's six major modules:

1. **scipy.optimize**: Function minimization, root finding, curve fitting
2. **scipy.integrate**: Numerical integration, ODE solving
3. **scipy.interpolate**: 1D and 2D data interpolation
4. **scipy.stats**: Statistical distributions, hypothesis testing, correlation
5. **scipy.linalg**: Linear systems, eigenvalues, matrix decompositions
6. **scipy.signal**: Signal analysis, filtering, convolution, resampling

Each module is essential for scientific computing and data analysis in Python.
