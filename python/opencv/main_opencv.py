#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "opencv-python>=4.8.0",
#     "numpy>=1.24.0",
# ]
# ///

"""
Comprehensive OpenCV demonstration showcasing various computer vision operations.

This script demonstrates:
1. Creating and manipulating images
2. Drawing shapes and text
3. Color space conversions
4. Image transformations (resize, rotate, flip)
5. Image filtering (blur, edge detection)
6. Thresholding and morphological operations
7. Feature detection (contours, corners)
8. Image analysis
"""

import cv2
import numpy as np


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 80}")
    print(f"  {title}")
    print(f"{'=' * 80}\n")


def create_sample_image() -> np.ndarray:
    """Create a sample color image with various shapes for demonstration."""
    # Create a white canvas
    img = np.ones((400, 600, 3), dtype=np.uint8) * 255

    # Draw various shapes
    cv2.rectangle(img, (50, 50), (200, 150), (255, 0, 0), -1)  # Blue rectangle
    cv2.circle(img, (400, 100), 60, (0, 255, 0), -1)  # Green circle
    cv2.ellipse(img, (300, 250), (80, 50), 45, 0, 360, (0, 0, 255), -1)  # Red ellipse

    # Draw a triangle using polylines
    triangle_pts = np.array([[100, 300], [50, 350], [150, 350]], np.int32)
    triangle_pts = triangle_pts.reshape((-1, 1, 2))
    cv2.fillPoly(img, [triangle_pts], (255, 255, 0))  # Cyan triangle

    return img


def demonstrate_basic_operations():
    """Demonstrate basic OpenCV image operations."""
    print_section("1. Basic Image Operations")

    # Create a sample image
    img = create_sample_image()
    height, width, channels = img.shape

    print(f"Line 61: Created image with shape: {img.shape}")
    print(f"Line 62: Height: {height}, Width: {width}, Channels: {channels}")
    print(f"Line 63: Data type: {img.dtype}")
    print(f"Line 64: Image size in memory: {img.nbytes} bytes")

    # Access pixel values
    pixel = img[100, 100]
    print(f"\nLine 68: Pixel at (100, 100): BGR = {pixel}")

    # Modify pixel values
    img_copy = img.copy()
    img_copy[100:120, 100:120] = [0, 255, 255]  # Yellow square
    print("Line 73: Modified pixels at (100:120, 100:120) to yellow")

    return img


def demonstrate_drawing():
    """Demonstrate drawing shapes and text on images."""
    print_section("2. Drawing Shapes and Text")

    # Create a blank canvas
    canvas = np.zeros((500, 700, 3), dtype=np.uint8)

    # Draw line
    cv2.line(canvas, (50, 50), (650, 50), (255, 255, 255), 2)
    print("Line 88: Drew white line from (50, 50) to (650, 50)")

    # Draw rectangle
    cv2.rectangle(canvas, (100, 100), (300, 200), (0, 255, 0), 3)
    print("Line 92: Drew green rectangle with thickness 3")

    # Draw circle
    cv2.circle(canvas, (500, 150), 70, (255, 0, 0), -1)
    print("Line 96: Drew filled blue circle at (500, 150) with radius 70")

    # Draw ellipse
    cv2.ellipse(canvas, (200, 350), (100, 60), 30, 0, 270, (0, 255, 255), 2)
    print("Line 100: Drew yellow ellipse rotated 30 degrees")

    # Draw polygon
    pts = np.array([[450, 250], [550, 250], [600, 350], [500, 400], [400, 350]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(canvas, [pts], True, (147, 20, 255), 3)
    print("Line 106: Drew pink polygon with 5 vertices")

    # Add text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(canvas, "OpenCV Demo", (50, 450), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
    print("Line 111: Added text 'OpenCV Demo' with anti-aliasing")

    return canvas


def demonstrate_color_conversions():
    """Demonstrate color space conversions."""
    print_section("3. Color Space Conversions")

    img = create_sample_image()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(f"Line 124: Converted BGR to Grayscale, new shape: {gray.shape}")

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print("Line 128: Converted BGR to HSV (Hue, Saturation, Value)")

    # Split HSV channels
    h, s, v = cv2.split(hsv)
    print(f"Line 132: Split HSV channels - H shape: {h.shape}, S shape: {s.shape}, V shape: {v.shape}")

    # Convert to LAB
    cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    print("Line 136: Converted BGR to LAB (Lightness, A, B) color space")

    # Split BGR channels
    b, g, r = cv2.split(img)
    print(f"Line 140: Split BGR channels - each channel shape: {b.shape}")
    print(f"Line 141: Blue channel mean: {np.mean(b):.2f}")
    print(f"Line 142: Green channel mean: {np.mean(g):.2f}")
    print(f"Line 143: Red channel mean: {np.mean(r):.2f}")

    return gray, hsv


def demonstrate_transformations():
    """Demonstrate geometric transformations."""
    print_section("4. Geometric Transformations")

    img = create_sample_image()
    height, width = img.shape[:2]

    # Resize
    resized = cv2.resize(img, (300, 200))
    print(f"Line 158: Resized image from {img.shape[:2]} to {resized.shape[:2]}")

    # Scale with ratio
    scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    print(f"Line 162: Scaled image by 0.5x using linear interpolation: {scaled.shape[:2]}")

    # Rotation
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(img, rotation_matrix, (width, height))
    print(f"Line 168: Rotated image 45 degrees clockwise around center {center}")

    # Flip
    cv2.flip(img, 1)
    cv2.flip(img, 0)
    cv2.flip(img, -1)
    print("Line 174: Flipped image horizontally (code=1)")
    print("Line 175: Flipped image vertically (code=0)")
    print("Line 176: Flipped image both directions (code=-1)")

    # Translation
    translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
    cv2.warpAffine(img, translation_matrix, (width, height))
    print("Line 181: Translated image by (100, 50) pixels")

    return rotated, scaled


def demonstrate_filtering():
    """Demonstrate image filtering techniques."""
    print_section("5. Image Filtering")

    img = create_sample_image()

    # Gaussian blur
    gaussian = cv2.GaussianBlur(img, (15, 15), 0)
    print("Line 195: Applied Gaussian blur with kernel size (15, 15)")

    # Median blur
    cv2.medianBlur(img, 15)
    print("Line 199: Applied median blur with kernel size 15")

    # Bilateral filter (preserves edges)
    cv2.bilateralFilter(img, 15, 80, 80)
    print("Line 203: Applied bilateral filter (d=15, sigmaColor=80, sigmaSpace=80)")

    # Box filter
    cv2.boxFilter(img, -1, (15, 15))
    print("Line 207: Applied box filter with kernel (15, 15)")

    # Convert to grayscale for edge detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Sobel edge detection (X direction)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    print(f"Line 215: Applied Sobel edge detection in X direction, output range: [{sobelx.min():.2f}, {sobelx.max():.2f}]")

    # Sobel edge detection (Y direction)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    print(f"Line 219: Applied Sobel edge detection in Y direction, output range: [{sobely.min():.2f}, {sobely.max():.2f}]")

    # Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    print("Line 223: Applied Canny edge detection with thresholds (100, 200)")
    print(f"Line 224: Detected edges: {np.count_nonzero(edges)} edge pixels out of {edges.size} total")

    # Laplacian
    cv2.Laplacian(gray, cv2.CV_64F)
    print("Line 228: Applied Laplacian edge detection")

    return gaussian, edges


def demonstrate_thresholding():
    """Demonstrate thresholding techniques."""
    print_section("6. Thresholding Operations")

    img = create_sample_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binary threshold
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    print("Line 243: Applied binary threshold at 127")
    print(f"Line 244: White pixels: {np.count_nonzero(binary)}, Black pixels: {binary.size - np.count_nonzero(binary)}")

    # Binary inverse threshold
    _, binary_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    print("Line 248: Applied inverse binary threshold at 127")

    # Truncate threshold
    _, trunc = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    print("Line 252: Applied truncate threshold at 127")

    # To zero threshold
    _, tozero = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
    print("Line 256: Applied to-zero threshold at 127")

    # Otsu's threshold (automatic)
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print("Line 260: Applied Otsu's automatic threshold")

    # Adaptive threshold (mean)
    adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, 11, 2)
    print("Line 265: Applied adaptive threshold (mean) with block size 11")

    # Adaptive threshold (gaussian)
    cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, 2)
    print("Line 270: Applied adaptive threshold (Gaussian) with block size 11")

    return binary, otsu, adaptive_mean


def demonstrate_morphological():
    """Demonstrate morphological operations."""
    print_section("7. Morphological Operations")

    img = create_sample_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Create structuring element
    kernel = np.ones((5, 5), np.uint8)
    print("Line 286: Created 5x5 rectangular kernel for morphological operations")

    # Erosion
    erosion = cv2.erode(binary, kernel, iterations=1)
    print("Line 290: Applied erosion (shrinks white regions)")
    print(f"Line 291: White pixels before: {np.count_nonzero(binary)}, after: {np.count_nonzero(erosion)}")

    # Dilation
    dilation = cv2.dilate(binary, kernel, iterations=1)
    print("Line 295: Applied dilation (expands white regions)")
    print(f"Line 296: White pixels before: {np.count_nonzero(binary)}, after: {np.count_nonzero(dilation)}")

    # Opening (erosion followed by dilation)
    cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    print("Line 300: Applied opening (removes small noise)")

    # Closing (dilation followed by erosion)
    cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    print("Line 304: Applied closing (fills small holes)")

    # Gradient (difference between dilation and erosion)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
    print("Line 308: Applied morphological gradient (outline of objects)")

    # Top hat (difference between input and opening)
    cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
    print("Line 312: Applied top hat transform")

    # Black hat (difference between closing and input)
    cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)
    print("Line 316: Applied black hat transform")

    return erosion, dilation, gradient


def demonstrate_contours():
    """Demonstrate contour detection and analysis."""
    print_section("8. Contour Detection and Analysis")

    img = create_sample_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Line 332: Found {len(contours)} contours using RETR_TREE method")
    print(f"Line 333: Hierarchy shape: {hierarchy.shape if hierarchy is not None else 'None'}")

    # Draw all contours
    img_contours = img.copy()
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)
    print("Line 338: Drew all contours in green with thickness 2")

    # Analyze each contour
    for i, contour in enumerate(contours[:5]):  # Analyze first 5 contours
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        # Approximate contour
        epsilon = 0.02 * perimeter
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)

        # Minimum enclosing circle
        (cx, cy), radius = cv2.minEnclosingCircle(contour)

        print(f"\nLine 354: Contour {i}:")
        print(f"Line 355:   Area: {area:.2f} pixels")
        print(f"Line 356:   Perimeter: {perimeter:.2f} pixels")
        print(f"Line 357:   Approx vertices: {len(approx)}")
        print(f"Line 358:   Bounding box: ({x}, {y}, {w}, {h})")
        print(f"Line 359:   Min circle center: ({cx:.1f}, {cy:.1f}), radius: {radius:.1f}")

    return img_contours, len(contours)


def demonstrate_corner_detection():
    """Demonstrate corner detection."""
    print_section("9. Corner Detection")

    img = create_sample_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Harris corner detection
    harris = cv2.cornerHarris(gray, 2, 3, 0.04)
    harris = cv2.dilate(harris, None)

    # Mark corners
    img_harris = img.copy()
    img_harris[harris > 0.01 * harris.max()] = [0, 0, 255]

    corner_count = np.count_nonzero(harris > 0.01 * harris.max())
    print(f"Line 384: Detected {corner_count} Harris corners (threshold: 0.01 * max)")
    print(f"Line 385: Harris response max value: {harris.max():.2f}")

    # Shi-Tomasi corner detection
    corners = cv2.goodFeaturesToTrack(gray.astype(np.uint8), 25, 0.01, 10)

    if corners is not None:
        corners = corners.astype(int)
        print(f"Line 392: Detected {len(corners)} Shi-Tomasi corners (maxCorners=25)")

        img_shi_tomasi = img.copy()
        for corner in corners:
            x, y = corner.ravel()
            cv2.circle(img_shi_tomasi, (x, y), 5, (255, 0, 0), -1)

        print("Line 398: Drew blue circles at corner locations")

    return corner_count


def demonstrate_image_statistics():
    """Demonstrate image statistical analysis."""
    print_section("10. Image Statistics and Analysis")

    img = create_sample_image()

    # Calculate statistics for each channel
    b, g, r = cv2.split(img)

    print("Line 412: Blue channel statistics:")
    print(f"Line 413:   Mean: {np.mean(b):.2f}")
    print(f"Line 414:   Std: {np.std(b):.2f}")
    print(f"Line 415:   Min: {np.min(b)}, Max: {np.max(b)}")

    print("\nLine 417: Green channel statistics:")
    print(f"Line 418:   Mean: {np.mean(g):.2f}")
    print(f"Line 419:   Std: {np.std(g):.2f}")
    print(f"Line 420:   Min: {np.min(g)}, Max: {np.max(g)}")

    print("\nLine 422: Red channel statistics:")
    print(f"Line 423:   Mean: {np.mean(r):.2f}")
    print(f"Line 424:   Std: {np.std(r):.2f}")
    print(f"Line 425:   Min: {np.min(r)}, Max: {np.max(r)}")

    # Calculate histogram
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    print("\nLine 431: Calculated histogram for grayscale image")
    print(f"Line 432: Histogram shape: {hist.shape}")
    print(f"Line 433: Most frequent intensity: {np.argmax(hist)} with {int(hist.max())} pixels")

    # Calculate moments
    moments = cv2.moments(gray)
    print("\nLine 437: Image moments (for centroid calculation):")
    print(f"Line 438:   m00 (area): {moments['m00']:.2f}")

    if moments['m00'] != 0:
        cx = int(moments['m10'] / moments['m00'])
        cy = int(moments['m01'] / moments['m00'])
        print(f"Line 443:   Centroid: ({cx}, {cy})")

    return hist


def main():
    """Main demonstration function."""
    print("\n" + "=" * 80)
    print(" " * 20 + "OpenCV Comprehensive Demonstration")
    print("=" * 80)
    print("\nThis demo showcases various OpenCV operations for computer vision tasks.")
    print(f"OpenCV version: {cv2.__version__}")
    print(f"NumPy version: {np.__version__}")

    # Run all demonstrations
    demonstrate_basic_operations()
    demonstrate_drawing()
    demonstrate_color_conversions()
    demonstrate_transformations()
    demonstrate_filtering()
    demonstrate_thresholding()
    demonstrate_morphological()
    demonstrate_contours()
    demonstrate_corner_detection()
    demonstrate_image_statistics()

    print_section("Demo Complete")
    print("All OpenCV operations demonstrated successfully!")
    print("OpenCV is a powerful library for computer vision and image processing.")
    print("\nKey capabilities covered:")
    print("  ✓ Image creation and manipulation")
    print("  ✓ Drawing and annotation")
    print("  ✓ Color space transformations")
    print("  ✓ Geometric transformations")
    print("  ✓ Image filtering and edge detection")
    print("  ✓ Thresholding techniques")
    print("  ✓ Morphological operations")
    print("  ✓ Contour detection and analysis")
    print("  ✓ Corner detection")
    print("  ✓ Statistical analysis")


if __name__ == "__main__":
    main()
