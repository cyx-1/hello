#!/usr/bin/env python3
"""
Comprehensive demonstration of SciPy library capabilities.

This script showcases various SciPy modules including optimization,
integration, interpolation, statistics, linear algebra, and signal processing.
"""

# /// script
# dependencies = [
#   "scipy>=1.11.0",
#   "numpy>=1.24.0",
# ]
# ///

import numpy as np
from scipy import optimize, integrate, interpolate, stats, linalg, signal


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"{title:^70}")
    print(f"{'=' * 70}\n")


def demonstrate_optimization() -> None:
    """Demonstrate scipy.optimize for function minimization and root finding."""
    print_section("1. OPTIMIZATION (scipy.optimize)")

    # Example 1: Minimize a simple quadratic function
    print("Example 1.1: Minimize f(x) = (x - 3)^2 + 5")

    def quadratic(x):
        return (x - 3)**2 + 5

    result = optimize.minimize(quadratic, x0=0)
    print(f"  Minimum found at x = {result.x[0]:.6f}")
    print(f"  Minimum value f(x) = {result.fun:.6f}")
    print(f"  Success: {result.success}")

    # Example 2: Root finding
    print("\nExample 1.2: Find root of f(x) = x^3 - 2x - 5")

    def cubic(x):
        return x**3 - 2*x - 5

    root = optimize.fsolve(cubic, x0=2)
    print(f"  Root found at x = {root[0]:.6f}")
    print(f"  Verification f({root[0]:.6f}) = {cubic(root[0]):.10f}")

    # Example 3: Curve fitting
    print("\nExample 1.3: Curve fitting to exponential data")

    def exponential_model(x, a, b, c):
        return a * np.exp(b * x) + c

    # Generate synthetic data
    x_data = np.linspace(0, 4, 50)
    y_data = 2.5 * np.exp(0.5 * x_data) + 1.0 + np.random.normal(0, 0.3, 50)

    params, _ = optimize.curve_fit(exponential_model, x_data, y_data)
    print(f"  Fitted parameters: a={params[0]:.4f}, b={params[1]:.4f}, c={params[2]:.4f}")
    print("  Expected: a=2.5, b=0.5, c=1.0")


def demonstrate_integration() -> None:
    """Demonstrate scipy.integrate for numerical integration."""
    print_section("2. INTEGRATION (scipy.integrate)")

    # Example 1: Definite integral
    print("Example 2.1: Compute integral of x^2 from 0 to 3")

    def square(x):
        return x**2

    result, error = integrate.quad(square, 0, 3)
    print(f"  Numerical result: {result:.6f}")
    print(f"  Analytical result: {3**3 / 3:.6f}")
    print(f"  Estimated error: {error:.2e}")

    # Example 2: Integration of a Gaussian
    print("\nExample 2.2: Integrate Gaussian e^(-x^2) from -∞ to ∞")

    def gaussian(x):
        return np.exp(-x**2)

    result, error = integrate.quad(gaussian, -np.inf, np.inf)
    print(f"  Numerical result: {result:.6f}")
    print(f"  Analytical result (√π): {np.sqrt(np.pi):.6f}")
    print(f"  Estimated error: {error:.2e}")

    # Example 3: Solve ODE (Ordinary Differential Equation)
    print("\nExample 2.3: Solve ODE dy/dt = -2y, y(0) = 1")

    def exponential_decay(t, y):
        return -2 * y

    t_span = (0, 2)
    t_eval = np.linspace(0, 2, 10)
    y0 = [1]

    solution = integrate.solve_ivp(exponential_decay, t_span, y0, t_eval=t_eval)
    print(f"  Time points: {solution.t[:5]}")
    print(f"  Solution values: {solution.y[0][:5]}")
    print(f"  Expected (e^(-2t)): {np.exp(-2 * solution.t[:5])}")


def demonstrate_interpolation() -> None:
    """Demonstrate scipy.interpolate for data interpolation."""
    print_section("3. INTERPOLATION (scipy.interpolate)")

    # Generate sample data
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0, 1, 4, 9, 16, 25])  # y = x^2
    x_new = np.array([0.5, 1.5, 2.5, 3.5])

    # Example 1: Linear interpolation
    print("Example 3.1: Linear interpolation of y = x^2")
    f_linear = interpolate.interp1d(x, y, kind='linear')
    y_linear = f_linear(x_new)
    print(f"  x_new: {x_new}")
    print(f"  Interpolated y: {y_linear}")
    print(f"  Actual y = x^2: {x_new**2}")

    # Example 2: Cubic spline interpolation
    print("\nExample 3.2: Cubic spline interpolation")
    f_cubic = interpolate.interp1d(x, y, kind='cubic')
    y_cubic = f_cubic(x_new)
    print(f"  x_new: {x_new}")
    print(f"  Interpolated y: {y_cubic}")
    print(f"  Actual y = x^2: {x_new**2}")
    print(f"  Error: {np.abs(y_cubic - x_new**2)}")

    # Example 3: 2D interpolation
    print("\nExample 3.3: 2D interpolation on a grid")
    x_grid = np.array([0, 1, 2])
    y_grid = np.array([0, 1, 2])
    z_values = np.array([[0, 1, 4], [1, 2, 5], [4, 5, 8]])

    f_2d = interpolate.RegularGridInterpolator((x_grid, y_grid), z_values)
    z_new = f_2d([[0.5, 0.5]])
    print(f"  Interpolated z at (0.5, 0.5): {z_new[0]:.4f}")


def demonstrate_statistics() -> None:
    """Demonstrate scipy.stats for statistical analysis."""
    print_section("4. STATISTICS (scipy.stats)")

    # Example 1: Descriptive statistics
    print("Example 4.1: Descriptive statistics of normal distribution")
    data = np.random.normal(loc=100, scale=15, size=1000)
    print(f"  Mean: {np.mean(data):.2f}")
    print(f"  Std Dev: {np.std(data, ddof=1):.2f}")
    print(f"  Median: {np.median(data):.2f}")
    desc = stats.describe(data)
    print(f"  Skewness: {desc.skewness:.4f}")
    print(f"  Kurtosis: {desc.kurtosis:.4f}")

    # Example 2: Probability distributions
    print("\nExample 4.2: Normal distribution properties")
    normal_dist = stats.norm(loc=0, scale=1)
    print(f"  P(X ≤ 1.96) = {normal_dist.cdf(1.96):.4f}")
    print(f"  P(X ≤ -1.96) = {normal_dist.cdf(-1.96):.4f}")
    print(f"  95th percentile: {normal_dist.ppf(0.95):.4f}")

    # Example 3: Hypothesis testing (t-test)
    print("\nExample 4.3: Two-sample t-test")
    group1 = np.random.normal(100, 15, 50)
    group2 = np.random.normal(105, 15, 50)
    t_stat, p_value = stats.ttest_ind(group1, group2)
    print(f"  Group 1 mean: {np.mean(group1):.2f}")
    print(f"  Group 2 mean: {np.mean(group2):.2f}")
    print(f"  t-statistic: {t_stat:.4f}")
    print(f"  p-value: {p_value:.4f}")
    print(f"  Significant at α=0.05? {p_value < 0.05}")

    # Example 4: Correlation
    print("\nExample 4.4: Pearson correlation")
    x = np.random.normal(0, 1, 100)
    y = 2 * x + np.random.normal(0, 0.5, 100)
    corr, p_val = stats.pearsonr(x, y)
    print(f"  Correlation coefficient: {corr:.4f}")
    print(f"  p-value: {p_val:.4e}")


def demonstrate_linear_algebra() -> None:
    """Demonstrate scipy.linalg for linear algebra operations."""
    print_section("5. LINEAR ALGEBRA (scipy.linalg)")

    # Example 1: Solve linear system Ax = b
    print("Example 5.1: Solve linear system Ax = b")
    A = np.array([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]])
    b = np.array([1, -2, 0])
    x = linalg.solve(A, b)
    print(f"  Matrix A:\n{A}")
    print(f"  Vector b: {b}")
    print(f"  Solution x: {x}")
    print(f"  Verification Ax: {np.dot(A, x)}")

    # Example 2: Eigenvalues and eigenvectors
    print("\nExample 5.2: Eigenvalues and eigenvectors")
    matrix = np.array([[4, -2], [1, 1]])
    eigenvalues, eigenvectors = linalg.eig(matrix)
    print(f"  Matrix:\n{matrix}")
    print(f"  Eigenvalues: {eigenvalues}")
    print(f"  Eigenvectors:\n{eigenvectors}")

    # Example 3: Matrix decompositions (SVD)
    print("\nExample 5.3: Singular Value Decomposition (SVD)")
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    U, s, Vt = linalg.svd(matrix)
    print(f"  Original matrix shape: {matrix.shape}")
    print(f"  U shape: {U.shape}")
    print(f"  Singular values: {s}")
    print(f"  Vt shape: {Vt.shape}")

    # Example 4: Matrix determinant and inverse
    print("\nExample 5.4: Determinant and inverse")
    matrix = np.array([[1, 2], [3, 4]])
    det = linalg.det(matrix)
    inv = linalg.inv(matrix)
    print(f"  Matrix:\n{matrix}")
    print(f"  Determinant: {det:.4f}")
    print(f"  Inverse:\n{inv}")
    print(f"  Verification (A × A^-1):\n{np.dot(matrix, inv)}")


def demonstrate_signal_processing() -> None:
    """Demonstrate scipy.signal for signal processing."""
    print_section("6. SIGNAL PROCESSING (scipy.signal)")

    # Example 1: Create and analyze a signal
    print("Example 6.1: Fourier transform of a composite signal")
    fs = 1000  # Sampling frequency
    t = np.linspace(0, 1, fs, endpoint=False)
    # Composite signal: 50 Hz + 120 Hz
    signal_data = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

    frequencies, spectrum = signal.periodogram(signal_data, fs)
    # Find peaks in spectrum
    peaks, _ = signal.find_peaks(spectrum, height=0.1)
    print("  Signal: 50 Hz + 120 Hz sine waves")
    print(f"  Sampling frequency: {fs} Hz")
    print(f"  Detected peaks at frequencies: {frequencies[peaks][:5]} Hz")

    # Example 2: Filter design and application
    print("\nExample 6.2: Butterworth lowpass filter")
    # Design a 4th-order Butterworth lowpass filter with cutoff at 100 Hz
    sos = signal.butter(4, 100, btype='low', fs=fs, output='sos')
    filtered_signal = signal.sosfilt(sos, signal_data)
    print(f"  Original signal length: {len(signal_data)}")
    print(f"  Filtered signal length: {len(filtered_signal)}")
    print("  Filter order: 4")
    print("  Cutoff frequency: 100 Hz")
    print(f"  Original RMS: {np.sqrt(np.mean(signal_data**2)):.4f}")
    print(f"  Filtered RMS: {np.sqrt(np.mean(filtered_signal**2)):.4f}")

    # Example 3: Convolution
    print("\nExample 6.3: Signal convolution")
    sig = np.array([1, 2, 3, 4, 5])
    kernel = np.array([0.5, 1, 0.5])
    convolved = signal.convolve(sig, kernel, mode='same')
    print(f"  Original signal: {sig}")
    print(f"  Kernel: {kernel}")
    print(f"  Convolved signal: {convolved}")

    # Example 4: Resample signal
    print("\nExample 6.4: Signal resampling")
    original = np.sin(2 * np.pi * 5 * np.linspace(0, 1, 100))
    resampled = signal.resample(original, 50)
    print(f"  Original signal length: {len(original)}")
    print(f"  Resampled signal length: {len(resampled)}")
    print(f"  Original signal range: [{original.min():.4f}, {original.max():.4f}]")
    print(f"  Resampled signal range: [{resampled.min():.4f}, {resampled.max():.4f}]")


def main() -> None:
    """Run all SciPy demonstrations."""
    print("\n" + "=" * 70)
    print("SciPy Library Demonstration".center(70))
    print("=" * 70)

    # Set random seed for reproducibility
    np.random.seed(42)

    # Run all demonstrations
    demonstrate_optimization()
    demonstrate_integration()
    demonstrate_interpolation()
    demonstrate_statistics()
    demonstrate_linear_algebra()
    demonstrate_signal_processing()

    print("\n" + "=" * 70)
    print("All demonstrations completed successfully!".center(70))
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
