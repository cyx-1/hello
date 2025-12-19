# Wand - Python ImageMagick Binding Demonstration

This example demonstrates comprehensive usage of **Wand**, a Python binding for ImageMagick. Wand provides a simple and Pythonic interface to ImageMagick's powerful image manipulation capabilities.

## Requirements

- **Python**: >=3.9
- **System Dependencies**: ImageMagick and libmagickwand-dev
  ```bash
  apt-get install imagemagick libmagickwand-dev
  ```
- **Python Package**: wand>=0.6.13 (specified in inline script metadata)

## Running the Example

```bash
uv run --with wand python main_wand_imagemagick.py
```

## Code Overview

The demonstration is organized into 12 sections showcasing different Wand capabilities:

### 1. Creating Images from Scratch (Lines 29-38)

```python
def demo_image_creation():
    """Demonstrate creating a simple image from scratch."""
    print_section("1. Creating Images from Scratch")

    # Create a blank canvas
    with Image(width=200, height=100, background=Color('skyblue')) as img:
        print(f"Created image: {img.width}x{img.height} pixels")
        print(f"Format: {img.format}")
        print(f"Background color: {img.background_color}")
        print(f"Color space: {img.colorspace}")
```

**Output:**
```
============================================================
  1. Creating Images from Scratch
============================================================

Created image: 200x100 pixels
Format:
Background color: srgb(255,255,255)
Color space: srgb
```

**Key Points:**
- Line 34: `Image()` constructor creates new images with specified dimensions and background
- Line 35-38: Image properties can be accessed directly through attributes
- Background color is reported in sRGB color space format

### 2. Reading Image Information (Lines 41-61)

```python
def demo_image_info():
    """Demonstrate reading image properties."""
    print_section("2. Reading Image Information")

    # Create a sample image
    with Image(width=400, height=300, background=Color('lightgreen')) as img:
        img.format = 'png'  # Set format for blob generation

        # Add some text
        with Drawing() as draw:
            draw.font_size = 30
            draw.fill_color = Color('darkgreen')
            draw.text(80, 150, 'Wand Demo')
            draw(img)

        print(f"Dimensions: {img.width} x {img.height}")
        print(f"Format: {img.format}")
        print(f"Size in bytes: {len(img.make_blob())} bytes")
        print(f"Depth: {img.depth} bits")
        print(f"Type: {img.type}")
        print(f"Signature: {img.signature[:16]}...")
```

**Output:**
```
============================================================
  2. Reading Image Information
============================================================

Dimensions: 400 x 300
Format: PNG
Size in bytes: 2324 bytes
Depth: 8 bits
Type: palettematte
Signature: a929eefad0e1b520...
```

**Key Points:**
- Line 47: Setting `img.format` is required before calling `make_blob()` to serialize the image
- Lines 50-54: The `Drawing` context manager provides drawing operations
- Line 58: `make_blob()` returns the image as a binary blob (useful for network transfers or storage)
- Line 60: Image type is automatically determined based on content (palettematte indicates transparency)

### 3. Resizing and Scaling (Lines 64-85)

```python
def demo_image_resize():
    """Demonstrate resizing operations."""
    print_section("3. Resizing and Scaling Images")

    with Image(width=800, height=600, background=Color('coral')) as img:
        print(f"Original size: {img.width}x{img.height}")

        # Clone and resize
        with img.clone() as resized:
            resized.resize(400, 300)
            print(f"Resized to: {resized.width}x{resized.height}")

        # Clone and thumbnail (maintains aspect ratio)
        with img.clone() as thumb:
            thumb.transform(resize='200x200')
            print(f"Thumbnail size: {thumb.width}x{thumb.height}")

        # Sample (faster but lower quality)
        with img.clone() as sampled:
            sampled.sample(200, 150)
            print(f"Sampled size: {sampled.width}x{sampled.height}")
```

**Output:**
```
============================================================
  3. Resizing and Scaling Images
============================================================

Original size: 800x600
Resized to: 400x300
Thumbnail size: 200x150
Sampled size: 200x150
```

**Key Points:**
- Line 72: `clone()` creates a copy of the image for non-destructive operations
- Line 73: `resize()` changes dimensions using high-quality resampling
- Line 77: `transform(resize='200x200')` maintains aspect ratio within bounds
- Line 81: `sample()` is faster but uses simpler pixel averaging (lower quality)

### 4. Rotation and Flipping (Lines 88-112)

```python
def demo_image_rotation():
    """Demonstrate rotation and flip operations."""
    print_section("4. Rotation and Flipping")

    with Image(width=300, height=200, background=Color('lavender')) as img:
        # Add directional indicator
        with Drawing() as draw:
            draw.fill_color = Color('purple')
            draw.rectangle(left=10, top=10, right=50, bottom=40)
            draw(img)

        print(f"Original: {img.width}x{img.height}")

        # Rotate 90 degrees
        with img.clone() as rotated:
            rotated.rotate(90)
            print(f"Rotated 90°: {rotated.width}x{rotated.height}")

        # Flip vertically
        with img.clone() as flipped:
            flipped.flip()
            print("Flipped vertically")

        # Flop horizontally
        with img.clone() as flopped:
            flopped.flop()
            print("Flopped horizontally")
```

**Output:**
```
============================================================
  4. Rotation and Flipping
============================================================

Original: 300x200
Rotated 90°: 200x300
Flipped vertically
Flopped horizontally
```

**Key Points:**
- Line 103: `rotate(90)` rotates the image; note dimensions swap (300x200 → 200x300)
- Line 108: `flip()` mirrors the image vertically (top becomes bottom)
- Line 113: `flop()` mirrors the image horizontally (left becomes right)
- Rectangle drawn at lines 94-97 provides visual reference for transformations

### 5. Image Effects and Filters (Lines 115-145)

```python
def demo_image_effects():
    """Demonstrate various image effects."""
    print_section("5. Image Effects and Filters")

    with Image(width=300, height=200, background=Color('white')) as img:
        # Add some content
        with Drawing() as draw:
            draw.fill_color = Color('red')
            draw.circle((150, 100), (200, 100))
            draw(img)

        print("Original image created")

        # Blur effect
        with img.clone() as blurred:
            blurred.blur(radius=5, sigma=3)
            print(f"Applied blur (radius=5, sigma=3)")

        # Sharpen effect
        with img.clone() as sharpened:
            sharpened.sharpen(radius=0, sigma=3)
            print(f"Applied sharpen (radius=0, sigma=3)")

        # Edge detection
        with img.clone() as edges:
            edges.edge(radius=2)
            print(f"Applied edge detection (radius=2)")

        # Emboss effect
        with img.clone() as embossed:
            embossed.emboss(radius=3, sigma=1)
            print(f"Applied emboss (radius=3, sigma=1)")
```

**Output:**
```
============================================================
  5. Image Effects and Filters
============================================================

Original image created
Applied blur (radius=5, sigma=3)
Applied sharpen (radius=0, sigma=3)
Applied edge detection (radius=2)
Applied emboss (radius=3, sigma=1)
```

**Key Points:**
- Line 130: `blur(radius, sigma)` applies Gaussian blur; larger sigma = more blur
- Line 135: `sharpen(radius, sigma)` enhances edges and details
- Line 140: `edge(radius)` performs edge detection, highlighting boundaries
- Line 145: `emboss(radius, sigma)` creates 3D embossed effect
- All effects use `radius` and `sigma` parameters to control intensity

### 6. Color Manipulation (Lines 148-177)

```python
def demo_color_manipulation():
    """Demonstrate color manipulation operations."""
    print_section("6. Color Manipulation")

    with Image(width=250, height=250, background=Color('gold')) as img:
        print(f"Original background: {img.background_color}")

        # Negate colors
        with img.clone() as negated:
            negated.negate()
            print("Applied color negation")

        # Grayscale
        with img.clone() as gray:
            gray.type = 'grayscale'
            print(f"Converted to grayscale: {gray.type}")

        # Sepia tone
        with img.clone() as sepia:
            sepia.sepia_tone(threshold=0.8)
            print("Applied sepia tone (threshold=0.8)")

        # Colorize
        with img.clone() as colorized:
            colorized.colorize(color=Color('blue'), alpha=Color('rgb(30%, 30%, 30%)'))
            print("Applied colorize with blue")
```

**Output:**
```
============================================================
  6. Color Manipulation
============================================================

Original background: srgb(255,255,255)
Applied color negation
Converted to grayscale: grayscale
Applied sepia tone (threshold=0.8)
Applied colorize with blue
```

**Key Points:**
- Line 157: `negate()` inverts all colors (creates a negative effect)
- Line 162: Setting `type = 'grayscale'` converts to black and white
- Line 167: `sepia_tone(threshold)` applies vintage sepia effect; threshold controls intensity
- Line 172: `colorize(color, alpha)` tints the image with specified color and opacity

### 7. Drawing Shapes and Text (Lines 180-217)

```python
def demo_drawing():
    """Demonstrate drawing operations."""
    print_section("7. Drawing Shapes and Text")

    with Image(width=400, height=300, background=Color('white')) as img:
        with Drawing() as draw:
            # Set drawing properties
            draw.stroke_color = Color('black')
            draw.stroke_width = 2
            draw.fill_color = Color('lightblue')

            # Draw rectangle
            draw.rectangle(left=50, top=50, right=150, bottom=120)
            print("Drew rectangle at (50,50) to (150,120)")

            # Draw circle
            draw.fill_color = Color('lightcoral')
            draw.circle((250, 85), (300, 85))
            print("Drew circle centered at (250,85)")

            # Draw line
            draw.stroke_color = Color('green')
            draw.stroke_width = 3
            draw.line((50, 150), (350, 200))
            print("Drew line from (50,150) to (350,200)")

            # Draw text
            draw.fill_color = Color('darkblue')
            draw.font_size = 24
            draw.text(120, 250, 'Wand Drawing Demo')
            print("Drew text 'Wand Drawing Demo' at (120,250)")

            # Apply to image
            draw(img)

        print(f"\nFinal image: {img.width}x{img.height}")
```

**Output:**
```
============================================================
  7. Drawing Shapes and Text
============================================================

Drew rectangle at (50,50) to (150,120)
Drew circle centered at (250,85)
Drew line from (50,150) to (350,200)
Drew text 'Wand Drawing Demo' at (120,250)

Final image: 400x300
```

**Key Points:**
- Lines 187-189: Set stroke and fill properties for subsequent drawing operations
- Line 192: `rectangle(left, top, right, bottom)` draws filled rectangle
- Line 197: `circle((origin_x, origin_y), (perimeter_x, perimeter_y))` draws circle
- Line 203: `line((x1, y1), (x2, y2))` draws a line between two points
- Line 209: `text(x, y, text_string)` renders text at specified position
- Line 212: Calling `draw(img)` applies all drawing operations to the image

### 8. Cropping Images (Lines 220-238)

```python
def demo_image_cropping():
    """Demonstrate cropping operations."""
    print_section("8. Cropping Images")

    with Image(width=500, height=400, background=Color('wheat')) as img:
        # Add a border for reference
        with Drawing() as draw:
            draw.stroke_color = Color('brown')
            draw.stroke_width = 5
            draw.fill_color = Color('transparent')
            draw.rectangle(left=0, top=0, right=499, bottom=399)
            draw(img)

        print(f"Original size: {img.width}x{img.height}")

        # Crop from center
        with img.clone() as cropped:
            cropped.crop(left=100, top=50, width=300, height=200)
            print(f"Cropped to: {cropped.width}x{cropped.height}")
            print("Crop region: left=100, top=50, width=300, height=200")
```

**Output:**
```
============================================================
  8. Cropping Images
============================================================

Original size: 500x400
Cropped to: 300x200
Crop region: left=100, top=50, width=300, height=200
```

**Key Points:**
- Line 237: `crop(left, top, width, height)` extracts a rectangular region
- Cropped image dimensions (300x200) match the specified width and height
- Original image remains unchanged due to `clone()` usage

### 9. Image Composition and Overlay (Lines 241-262)

```python
def demo_image_composite():
    """Demonstrate image composition/overlay."""
    print_section("9. Image Composition and Overlay")

    # Create base image
    with Image(width=400, height=300, background=Color('lightgray')) as base:
        print(f"Base image: {base.width}x{base.height}")

        # Create overlay image
        with Image(width=150, height=150, background=Color('pink')) as overlay:
            # Add content to overlay
            with Drawing() as draw:
                draw.fill_color = Color('red')
                draw.circle((75, 75), (100, 75))
                draw(overlay)

            print(f"Overlay image: {overlay.width}x{overlay.height}")

            # Composite images
            base.composite(overlay, left=125, top=75)
            print("Composited overlay at position (125, 75)")
            print(f"Final composite: {base.width}x{base.height}")
```

**Output:**
```
============================================================
  9. Image Composition and Overlay
============================================================

Base image: 400x300
Overlay image: 150x150
Composited overlay at position (125, 75)
Final composite: 400x300
```

**Key Points:**
- Line 247: Base image serves as the canvas for composition
- Line 251: Create overlay image with different content
- Line 260: `composite(overlay, left, top)` places overlay onto base at specified position
- Final image maintains base dimensions while incorporating overlay content

### 10. Format Conversion (Lines 265-282)

```python
def demo_format_conversion():
    """Demonstrate format conversion."""
    print_section("10. Format Conversion")

    with Image(width=200, height=150, background=Color('turquoise')) as img:
        print(f"Original format: {img.format}")

        # Convert to different formats by setting format property
        formats_to_test = ['PNG', 'JPEG', 'GIF', 'BMP']

        for fmt in formats_to_test:
            with img.clone() as converted:
                converted.format = fmt
                blob = converted.make_blob()
                print(f"Converted to {fmt}: {len(blob)} bytes")
```

**Output:**
```
============================================================
  10. Format Conversion
============================================================

Original format:
Converted to PNG: 159 bytes
Converted to JPEG: 644 bytes
Converted to GIF: 290 bytes
Converted to BMP: 90138 bytes
```

**Key Points:**
- Line 277: Simply setting `format` property converts between image formats
- Line 278: `make_blob()` serializes the image in the specified format
- BMP format is uncompressed, resulting in much larger file size (90,138 bytes vs 159-644 bytes)
- JPEG produces larger output than PNG/GIF for this simple image due to its compression algorithm

### 11. Image Properties and Metadata (Lines 285-302)

```python
def demo_image_properties():
    """Demonstrate modifying image properties."""
    print_section("11. Image Properties and Metadata")

    with Image(width=300, height=200, background=Color('peachpuff')) as img:
        # Set compression quality (for JPEG)
        img.compression_quality = 85
        print(f"Compression quality: {img.compression_quality}")

        # Set image depth
        original_depth = img.depth
        img.depth = 8
        print(f"Depth changed from {original_depth} to {img.depth}")

        # Image size info
        print(f"Image dimensions: {img.size}")
        print(f"Image width: {img.width}")
        print(f"Image height: {img.height}")
```

**Output:**
```
============================================================
  11. Image Properties and Metadata
============================================================

Compression quality: 85
Depth changed from 8 to 8
Image dimensions: (300, 200)
Image width: 300
Image height: 200
```

**Key Points:**
- Line 291: `compression_quality` controls JPEG compression (0-100, higher = better quality)
- Line 295: `depth` specifies bits per color channel (8-bit = 256 colors per channel)
- Line 299: `size` property returns dimensions as a tuple (width, height)
- Image properties can be both read and modified

### 12. Borders and Frames (Lines 305-325)

```python
def demo_border_and_frame():
    """Demonstrate adding borders and frames."""
    print_section("12. Borders and Frames")

    with Image(width=250, height=200, background=Color('mintcream')) as img:
        print(f"Original: {img.width}x{img.height}")

        # Add simple border
        with img.clone() as bordered:
            bordered.border(color=Color('navy'), width=10, height=10)
            print(f"With border: {bordered.width}x{bordered.height}")
            print("Added 10px navy border")

        # Add frame effect
        with img.clone() as framed:
            framed.frame(matte=Color('gold'), width=15, height=15, inner_bevel=5, outer_bevel=5)
            print(f"With frame: {framed.width}x{framed.height}")
            print("Added gold frame with 15px width/height")
```

**Output:**
```
============================================================
  12. Borders and Frames
============================================================

Original: 250x200
With border: 270x220
Added 10px navy border
With frame: 280x230
Added gold frame with 15px width/height
```

**Key Points:**
- Line 314: `border(color, width, height)` adds solid border; dimensions increase by 2×width and 2×height
- Border increases image from 250×200 to 270×220 (adds 10px on each side)
- Line 319: `frame(matte, width, height, inner_bevel, outer_bevel)` adds 3D frame effect
- Frame increases image from 250×200 to 280×230 (adds 15px on each side)
- Bevels create depth perception on the frame

## Complete Program Output

```
============================================================
  WAND - Python ImageMagick Binding Demonstration
============================================================

============================================================
  1. Creating Images from Scratch
============================================================

Created image: 200x100 pixels
Format:
Background color: srgb(255,255,255)
Color space: srgb

============================================================
  2. Reading Image Information
============================================================

Dimensions: 400 x 300
Format: PNG
Size in bytes: 2324 bytes
Depth: 8 bits
Type: palettematte
Signature: a929eefad0e1b520...

============================================================
  3. Resizing and Scaling Images
============================================================

Original size: 800x600
Resized to: 400x300
Thumbnail size: 200x150
Sampled size: 200x150

============================================================
  4. Rotation and Flipping
============================================================

Original: 300x200
Rotated 90°: 200x300
Flipped vertically
Flopped horizontally

============================================================
  5. Image Effects and Filters
============================================================

Original image created
Applied blur (radius=5, sigma=3)
Applied sharpen (radius=0, sigma=3)
Applied edge detection (radius=2)
Applied emboss (radius=3, sigma=1)

============================================================
  6. Color Manipulation
============================================================

Original background: srgb(255,255,255)
Applied color negation
Converted to grayscale: grayscale
Applied sepia tone (threshold=0.8)
Applied colorize with blue

============================================================
  7. Drawing Shapes and Text
============================================================

Drew rectangle at (50,50) to (150,120)
Drew circle centered at (250,85)
Drew line from (50,150) to (350,200)
Drew text 'Wand Drawing Demo' at (120,250)

Final image: 400x300

============================================================
  8. Cropping Images
============================================================

Original size: 500x400
Cropped to: 300x200
Crop region: left=100, top=50, width=300, height=200

============================================================
  9. Image Composition and Overlay
============================================================

Base image: 400x300
Overlay image: 150x150
Composited overlay at position (125, 75)
Final composite: 400x300

============================================================
  10. Format Conversion
============================================================

Original format:
Converted to PNG: 159 bytes
Converted to JPEG: 644 bytes
Converted to GIF: 290 bytes
Converted to BMP: 90138 bytes

============================================================
  11. Image Properties and Metadata
============================================================

Compression quality: 85
Depth changed from 8 to 8
Image dimensions: (300, 200)
Image width: 300
Image height: 200

============================================================
  12. Borders and Frames
============================================================

Original: 250x200
With border: 270x220
Added 10px navy border
With frame: 280x230
Added gold frame with 15px width/height

============================================================
  All demonstrations completed successfully!
============================================================
```

## Key Wand Concepts

### Context Managers
Wand uses Python's context manager protocol (`with` statements) for automatic resource cleanup:
```python
with Image(width=100, height=100) as img:
    # Image operations
    pass
# Image resources automatically released
```

### Non-Destructive Operations
Use `clone()` to preserve the original image:
```python
with img.clone() as modified:
    modified.resize(50, 50)  # Original 'img' unchanged
```

### Color Specification
Wand accepts multiple color formats:
- Named colors: `Color('red')`
- Hex: `Color('#FF0000')`
- RGB: `Color('rgb(255, 0, 0)')`
- RGBA: `Color('rgba(255, 0, 0, 0.5)')`

### Drawing Operations
Drawing operations are batched and applied at once:
```python
with Drawing() as draw:
    draw.circle(...)
    draw.rectangle(...)
    draw(img)  # Apply all operations
```

## Version Notes

This example works with:
- **Wand** >= 0.6.13
- **ImageMagick** 6.x or 7.x
- **Python** >= 3.9

The inline script metadata in `main_wand_imagemagick.py` ensures the correct Wand version is automatically installed when using `uv run`.

## Additional Resources

- [Wand Documentation](https://docs.wand-py.org/)
- [ImageMagick Documentation](https://imagemagick.org/)
- [Wand GitHub Repository](https://github.com/emcconville/wand)
