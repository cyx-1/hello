# OpenCV Python Demonstration

A comprehensive demonstration of OpenCV (Open Source Computer Vision Library) capabilities in Python, showcasing various image processing and computer vision operations.

## Overview

This example illustrates the core features of OpenCV including:
- Image creation and basic operations
- Drawing shapes and text on images
- Color space conversions (BGR, Grayscale, HSV, LAB)
- Geometric transformations (resize, rotate, flip, translate)
- Image filtering (Gaussian, median, bilateral, Sobel, Canny)
- Thresholding techniques (binary, Otsu's, adaptive)
- Morphological operations (erosion, dilation, opening, closing)
- Contour detection and analysis
- Corner detection (Harris, Shi-Tomasi)
- Statistical image analysis

## Requirements

- Python 3.10 or higher
- OpenCV 4.8.0 or higher (tested with OpenCV 4.12.0)
- NumPy 1.24.0 or higher (compatible with NumPy 2.x)

## Running the Demo

```bash
uv run python main_opencv.py
```

The script uses inline script metadata for dependency management, so `uv` will automatically install the required packages.

## Source Code with Annotations

### 1. Basic Image Operations (Lines 34-75)

**Source Code (Lines 54-64):**
```python
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
```

**Output:**
```
================================================================================
  1. Basic Image Operations
================================================================================

Line 61: Created image with shape: (400, 600, 3)
Line 62: Height: 400, Width: 600, Channels: 3
Line 63: Data type: uint8
Line 64: Image size in memory: 720000 bytes
```

**Annotation:** Lines 61-64 demonstrate creating a sample image and accessing its properties. The image is 400 pixels high, 600 pixels wide, with 3 color channels (BGR format). Each pixel uses uint8 data type (0-255), resulting in 720,000 bytes total (400 × 600 × 3).

**Source Code (Lines 66-73):**
```python
    # Access pixel values
    pixel = img[100, 100]
    print(f"\nLine 68: Pixel at (100, 100): BGR = {pixel}")

    # Modify pixel values
    img_copy = img.copy()
    img_copy[100:120, 100:120] = [0, 255, 255]  # Yellow square
    print(f"Line 73: Modified pixels at (100:120, 100:120) to yellow")
```

**Output:**
```
Line 68: Pixel at (100, 100): BGR = [255   0   0]
Line 73: Modified pixels at (100:120, 100:120) to yellow
```

**Annotation:** Line 68 shows accessing individual pixels in BGR format [Blue, Green, Red]. The pixel at (100, 100) is pure blue [255, 0, 0]. Line 73 demonstrates modifying a 20×20 region to yellow [0, 255, 255].

---

### 2. Drawing Shapes and Text (Lines 78-114)

**Source Code (Lines 85-111):**
```python
def demonstrate_drawing():
    # Create a blank canvas
    canvas = np.zeros((500, 700, 3), dtype=np.uint8)

    # Draw line
    cv2.line(canvas, (50, 50), (650, 50), (255, 255, 255), 2)
    print(f"Line 88: Drew white line from (50, 50) to (650, 50)")

    # Draw rectangle
    cv2.rectangle(canvas, (100, 100), (300, 200), (0, 255, 0), 3)
    print(f"Line 92: Drew green rectangle with thickness 3")

    # Draw circle
    cv2.circle(canvas, (500, 150), 70, (255, 0, 0), -1)
    print(f"Line 96: Drew filled blue circle at (500, 150) with radius 70")

    # Draw ellipse
    cv2.ellipse(canvas, (200, 350), (100, 60), 30, 0, 270, (0, 255, 255), 2)
    print(f"Line 100: Drew yellow ellipse rotated 30 degrees")

    # Add text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(canvas, "OpenCV Demo", (50, 450), font, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
    print(f"Line 111: Added text 'OpenCV Demo' with anti-aliasing")
```

**Output:**
```
================================================================================
  2. Drawing Shapes and Text
================================================================================

Line 88: Drew white line from (50, 50) to (650, 50)
Line 92: Drew green rectangle with thickness 3
Line 96: Drew filled blue circle at (500, 150) with radius 70
Line 100: Drew yellow ellipse rotated 30 degrees
Line 106: Drew pink polygon with 5 vertices
Line 111: Added text 'OpenCV Demo' with anti-aliasing
```

**Annotation:** OpenCV provides rich drawing capabilities. Negative thickness values (Line 96) create filled shapes. The `cv2.LINE_AA` flag (Line 111) enables anti-aliasing for smooth text rendering.

---

### 3. Color Space Conversions (Lines 117-145)

**Source Code (Lines 120-143):**
```python
def demonstrate_color_conversions():
    img = create_sample_image()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(f"Line 124: Converted BGR to Grayscale, new shape: {gray.shape}")

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(f"Line 128: Converted BGR to HSV (Hue, Saturation, Value)")

    # Split HSV channels
    h, s, v = cv2.split(hsv)
    print(f"Line 132: Split HSV channels - H shape: {h.shape}, S shape: {s.shape}, V shape: {v.shape}")

    # Split BGR channels
    b, g, r = cv2.split(img)
    print(f"Line 140: Split BGR channels - each channel shape: {b.shape}")
    print(f"Line 141: Blue channel mean: {np.mean(b):.2f}")
    print(f"Line 142: Green channel mean: {np.mean(g):.2f}")
    print(f"Line 143: Red channel mean: {np.mean(r):.2f}")
```

**Output:**
```
================================================================================
  3. Color Space Conversions
================================================================================

Line 124: Converted BGR to Grayscale, new shape: (400, 600)
Line 128: Converted BGR to HSV (Hue, Saturation, Value)
Line 132: Split HSV channels - H shape: (400, 600), S shape: (400, 600), V shape: (400, 600)
Line 136: Converted BGR to LAB (Lightness, A, B) color space
Line 140: Split BGR channels - each channel shape: (400, 600)
Line 141: Blue channel mean: 229.47
Line 142: Green channel mean: 225.26
Line 143: Red channel mean: 224.04
```

**Annotation:** Line 124 shows grayscale conversion reduces the image to 2D (loses color dimension). Lines 141-143 show the mean intensity values for each color channel, indicating this image has slightly more blue (229.47) than green or red.

---

### 4. Geometric Transformations (Lines 148-184)

**Source Code (Lines 155-181):**
```python
def demonstrate_transformations():
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
    flip_horizontal = cv2.flip(img, 1)
    flip_vertical = cv2.flip(img, 0)
    flip_both = cv2.flip(img, -1)
    print(f"Line 174: Flipped image horizontally (code=1)")
    print(f"Line 175: Flipped image vertically (code=0)")
    print(f"Line 176: Flipped image both directions (code=-1)")

    # Translation
    translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
    translated = cv2.warpAffine(img, translation_matrix, (width, height))
    print(f"Line 181: Translated image by (100, 50) pixels")
```

**Output:**
```
================================================================================
  4. Geometric Transformations
================================================================================

Line 158: Resized image from (400, 600) to (200, 300)
Line 162: Scaled image by 0.5x using linear interpolation: (200, 300)
Line 168: Rotated image 45 degrees clockwise around center (300, 200)
Line 174: Flipped image horizontally (code=1)
Line 175: Flipped image vertically (code=0)
Line 176: Flipped image both directions (code=-1)
Line 181: Translated image by (100, 50) pixels
```

**Annotation:** Lines 158-162 demonstrate two resizing methods: direct size specification and scaling factors. Line 168 uses an affine transformation matrix for rotation. Lines 174-176 show the flip codes: 1 for horizontal, 0 for vertical, -1 for both axes.

---

### 5. Image Filtering (Lines 187-231)

**Source Code (Lines 192-228):**
```python
def demonstrate_filtering():
    img = create_sample_image()

    # Gaussian blur
    gaussian = cv2.GaussianBlur(img, (15, 15), 0)
    print(f"Line 195: Applied Gaussian blur with kernel size (15, 15)")

    # Median blur
    median = cv2.medianBlur(img, 15)
    print(f"Line 199: Applied median blur with kernel size 15")

    # Bilateral filter (preserves edges)
    bilateral = cv2.bilateralFilter(img, 15, 80, 80)
    print(f"Line 203: Applied bilateral filter (d=15, sigmaColor=80, sigmaSpace=80)")

    # Sobel edge detection (X direction)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    print(f"Line 215: Applied Sobel edge detection in X direction, output range: [{sobelx.min():.2f}, {sobelx.max():.2f}]")

    # Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    print(f"Line 223: Applied Canny edge detection with thresholds (100, 200)")
    print(f"Line 224: Detected edges: {np.count_nonzero(edges)} edge pixels out of {edges.size} total")

    # Laplacian
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    print(f"Line 228: Applied Laplacian edge detection")
```

**Output:**
```
================================================================================
  5. Image Filtering
================================================================================

Line 195: Applied Gaussian blur with kernel size (15, 15)
Line 199: Applied median blur with kernel size 15
Line 203: Applied bilateral filter (d=15, sigmaColor=80, sigmaSpace=80)
Line 207: Applied box filter with kernel (15, 15)
Line 215: Applied Sobel edge detection in X direction, output range: [-10848.00, 10848.00]
Line 219: Applied Sobel edge detection in Y direction, output range: [-10848.00, 10848.00]
Line 223: Applied Canny edge detection with thresholds (100, 200)
Line 224: Detected edges: 1641 edge pixels out of 240000 total
Line 228: Applied Laplacian edge detection
```

**Annotation:** Line 203 shows bilateral filtering preserves edges while smoothing. Line 215 demonstrates Sobel produces gradient values (positive and negative). Line 224 reveals Canny detected 1,641 edge pixels (0.68% of the 240,000 total pixels).

---

### 6. Thresholding Operations (Lines 234-272)

**Source Code (Lines 239-270):**
```python
def demonstrate_thresholding():
    img = create_sample_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binary threshold
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    print(f"Line 243: Applied binary threshold at 127")
    print(f"Line 244: White pixels: {np.count_nonzero(binary)}, Black pixels: {binary.size - np.count_nonzero(binary)}")

    # Otsu's threshold (automatic)
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print(f"Line 260: Applied Otsu's automatic threshold")

    # Adaptive threshold (mean)
    adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, 11, 2)
    print(f"Line 265: Applied adaptive threshold (mean) with block size 11")

    # Adaptive threshold (gaussian)
    adaptive_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, 2)
    print(f"Line 270: Applied adaptive threshold (Gaussian) with block size 11")
```

**Output:**
```
================================================================================
  6. Thresholding Operations
================================================================================

Line 243: Applied binary threshold at 127
Line 244: White pixels: 212012, Black pixels: 27988
Line 248: Applied inverse binary threshold at 127
Line 252: Applied truncate threshold at 127
Line 256: Applied to-zero threshold at 127
Line 260: Applied Otsu's automatic threshold
Line 265: Applied adaptive threshold (mean) with block size 11
Line 270: Applied adaptive threshold (Gaussian) with block size 11
```

**Annotation:** Line 244 shows 88.3% of pixels are white (above threshold 127). Line 260 demonstrates Otsu's method automatically determines the optimal threshold. Lines 265-270 show adaptive thresholding which calculates different thresholds for different regions.

---

### 7. Morphological Operations (Lines 275-319)

**Source Code (Lines 284-316):**
```python
def demonstrate_morphological():
    img = create_sample_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Create structuring element
    kernel = np.ones((5, 5), np.uint8)
    print(f"Line 286: Created 5x5 rectangular kernel for morphological operations")

    # Erosion
    erosion = cv2.erode(binary, kernel, iterations=1)
    print(f"Line 290: Applied erosion (shrinks white regions)")
    print(f"Line 291: White pixels before: {np.count_nonzero(binary)}, after: {np.count_nonzero(erosion)}")

    # Dilation
    dilation = cv2.dilate(binary, kernel, iterations=1)
    print(f"Line 295: Applied dilation (expands white regions)")
    print(f"Line 296: White pixels before: {np.count_nonzero(binary)}, after: {np.count_nonzero(dilation)}")

    # Opening (erosion followed by dilation)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    print(f"Line 300: Applied opening (removes small noise)")

    # Gradient (difference between dilation and erosion)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
    print(f"Line 308: Applied morphological gradient (outline of objects)")
```

**Output:**
```
================================================================================
  7. Morphological Operations
================================================================================

Line 286: Created 5x5 rectangular kernel for morphological operations
Line 290: Applied erosion (shrinks white regions)
Line 291: White pixels before: 212012, after: 209892
Line 295: Applied dilation (expands white regions)
Line 296: White pixels before: 212012, after: 214068
Line 300: Applied opening (removes small noise)
Line 304: Applied closing (fills small holes)
Line 308: Applied morphological gradient (outline of objects)
Line 312: Applied top hat transform
Line 316: Applied black hat transform
```

**Annotation:** Line 291 shows erosion reduced white pixels from 212,012 to 209,892 (1% reduction). Line 296 shows dilation increased white pixels to 214,068 (1% increase). These operations are useful for noise removal and shape analysis.

---

### 8. Contour Detection and Analysis (Lines 322-362)

**Source Code (Lines 328-359):**
```python
def demonstrate_contours():
    img = create_sample_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(f"Line 332: Found {len(contours)} contours using RETR_TREE method")

    # Analyze each contour
    for i, contour in enumerate(contours[:5]):
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
```

**Output:**
```
================================================================================
  8. Contour Detection and Analysis
================================================================================

Line 332: Found 2 contours using RETR_TREE method
Line 333: Hierarchy shape: (1, 2, 4)
Line 338: Drew all contours in green with thickness 2

Line 354: Contour 0:
Line 355:   Area: 12552.00 pixels
Line 356:   Perimeter: 437.59 pixels
Line 357:   Approx vertices: 8
Line 358:   Bounding box: (233, 183, 135, 135)
Line 359:   Min circle center: (300.0, 250.0), radius: 80.6

Line 354: Contour 1:
Line 355:   Area: 15000.00 pixels
Line 356:   Perimeter: 500.00 pixels
Line 357:   Approx vertices: 4
Line 358:   Bounding box: (50, 50, 151, 101)
Line 359:   Min circle center: (125.0, 100.0), radius: 90.1
```

**Annotation:** Line 332 found 2 major contours in the image. Contour 0 (red ellipse) has 8 approximated vertices with area 12,552 pixels. Contour 1 (blue rectangle) has 4 vertices (as expected) with area 15,000 pixels (approximately 150×100).

---

### 9. Corner Detection (Lines 365-400)

**Source Code (Lines 373-398):**
```python
def demonstrate_corner_detection():
    img = create_sample_image()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Harris corner detection
    harris = cv2.cornerHarris(gray, 2, 3, 0.04)
    harris = cv2.dilate(harris, None)

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

        print(f"Line 398: Drew blue circles at corner locations")
```

**Output:**
```
================================================================================
  9. Corner Detection
================================================================================

Line 384: Detected 723 Harris corners (threshold: 0.01 * max)
Line 385: Harris response max value: 282785248.00
Line 392: Detected 25 Shi-Tomasi corners (maxCorners=25)
Line 398: Drew blue circles at corner locations
```

**Annotation:** Line 384 shows Harris corner detection found 723 corners. Line 392 demonstrates Shi-Tomasi method (also known as "good features to track") which is more selective, finding exactly 25 corners as requested.

---

### 10. Image Statistics and Analysis (Lines 403-446)

**Source Code (Lines 410-443):**
```python
def demonstrate_image_statistics():
    img = create_sample_image()

    # Calculate statistics for each channel
    b, g, r = cv2.split(img)

    print(f"Line 412: Blue channel statistics:")
    print(f"Line 413:   Mean: {np.mean(b):.2f}")
    print(f"Line 414:   Std: {np.std(b):.2f}")
    print(f"Line 415:   Min: {np.min(b)}, Max: {np.max(b)}")

    # Calculate histogram
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    print(f"\nLine 431: Calculated histogram for grayscale image")
    print(f"Line 432: Histogram shape: {hist.shape}")
    print(f"Line 433: Most frequent intensity: {np.argmax(hist)} with {int(hist.max())} pixels")

    # Calculate moments
    moments = cv2.moments(gray)
    print(f"\nLine 437: Image moments (for centroid calculation):")
    print(f"Line 438:   m00 (area): {moments['m00']:.2f}")

    if moments['m00'] != 0:
        cx = int(moments['m10'] / moments['m00'])
        cy = int(moments['m01'] / moments['m00'])
        print(f"Line 443:   Centroid: ({cx}, {cy})")
```

**Output:**
```
================================================================================
  10. Image Statistics and Analysis
================================================================================

Line 412: Blue channel statistics:
Line 413:   Mean: 229.47
Line 414:   Std: 76.54
Line 415:   Min: 0, Max: 255

Line 417: Green channel statistics:
Line 418:   Mean: 225.26
Line 419:   Std: 81.85
Line 420:   Min: 0, Max: 255

Line 422: Red channel statistics:
Line 423:   Mean: 224.04
Line 424:   Std: 83.29
Line 425:   Min: 0, Max: 255

Line 431: Calculated histogram for grayscale image
Line 432: Histogram shape: (256, 1)
Line 433: Most frequent intensity: 255 with 198122 pixels

Line 437: Image moments (for centroid calculation):
Line 438:   m00 (area): 54090330.00
Line 443:   Centroid: (309, 205)
```

**Annotation:** Lines 413-425 show color channel statistics. Blue has highest mean (229.47) and lowest standard deviation (76.54), indicating more uniform blue values. Line 433 reveals intensity 255 (white) is most frequent with 198,122 pixels. Line 443 calculates the image centroid at (309, 205), near the geometric center of the 600×400 image.

---

## Program Output Summary

```
================================================================================
                    OpenCV Comprehensive Demonstration
================================================================================

This demo showcases various OpenCV operations for computer vision tasks.
OpenCV version: 4.12.0
NumPy version: 2.2.6

[... all sections output as shown above ...]

================================================================================
  Demo Complete
================================================================================

All OpenCV operations demonstrated successfully!
OpenCV is a powerful library for computer vision and image processing.

Key capabilities covered:
  ✓ Image creation and manipulation
  ✓ Drawing and annotation
  ✓ Color space transformations
  ✓ Geometric transformations
  ✓ Image filtering and edge detection
  ✓ Thresholding techniques
  ✓ Morphological operations
  ✓ Contour detection and analysis
  ✓ Corner detection
  ✓ Statistical analysis
```

## Key Insights

1. **Image Representation**: OpenCV uses NumPy arrays with BGR color ordering (not RGB). Each image has shape (height, width, channels).

2. **Color Spaces**: Different color spaces serve different purposes:
   - BGR: Standard for display
   - Grayscale: Simplifies processing
   - HSV: Better for color-based segmentation
   - LAB: Perceptually uniform color space

3. **Edge Detection**: Multiple methods available:
   - Sobel: Gradient-based, directional
   - Canny: Multi-stage algorithm with hysteresis
   - Laplacian: Second derivative based

4. **Thresholding**: Adaptive methods work better for images with varying illumination than global thresholding.

5. **Morphological Operations**: Essential for shape analysis:
   - Erosion/Dilation: Basic operations
   - Opening: Removes small objects
   - Closing: Fills small holes
   - Gradient: Extracts object boundaries

6. **Contour Analysis**: Provides geometric properties useful for object recognition and measurement.

7. **Corner Detection**:
   - Harris: Detects many corners but can be noisy
   - Shi-Tomasi: More selective, better for tracking

## Version Notes

This code is compatible with:
- **Python 3.10+** (uses match statements and type hints)
- **OpenCV 4.8+** (tested with 4.12.0)
- **NumPy 2.x** (uses `.astype(int)` instead of deprecated `np.int0`)

The inline script metadata ensures `uv` automatically installs compatible versions of all dependencies.
