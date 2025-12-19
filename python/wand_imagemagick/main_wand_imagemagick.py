#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "wand>=0.6.13",
# ]
# ///

"""
Comprehensive demonstration of Wand - Python ImageMagick binding.
This script showcases various image manipulation capabilities.
"""

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def demo_image_creation():
    """Demonstrate creating a simple image from scratch."""
    print_section("1. Creating Images from Scratch")

    # Create a blank canvas
    with Image(width=200, height=100, background=Color("skyblue")) as img:
        print(f"Created image: {img.width}x{img.height} pixels")
        print(f"Format: {img.format}")
        print(f"Background color: {img.background_color}")
        print(f"Color space: {img.colorspace}")


def demo_image_info():
    """Demonstrate reading image properties."""
    print_section("2. Reading Image Information")

    # Create a sample image
    with Image(width=400, height=300, background=Color("lightgreen")) as img:
        img.format = "png"  # Set format for blob generation

        # Add some text
        with Drawing() as draw:
            draw.font_size = 30
            draw.fill_color = Color("darkgreen")
            draw.text(80, 150, "Wand Demo")
            draw(img)

        print(f"Dimensions: {img.width} x {img.height}")
        print(f"Format: {img.format}")
        print(f"Size in bytes: {len(img.make_blob())} bytes")
        print(f"Depth: {img.depth} bits")
        print(f"Type: {img.type}")
        print(f"Signature: {img.signature[:16]}...")


def demo_image_resize():
    """Demonstrate resizing operations."""
    print_section("3. Resizing and Scaling Images")

    with Image(width=800, height=600, background=Color("coral")) as img:
        print(f"Original size: {img.width}x{img.height}")

        # Clone and resize
        with img.clone() as resized:
            resized.resize(400, 300)
            print(f"Resized to: {resized.width}x{resized.height}")

        # Clone and thumbnail (maintains aspect ratio)
        with img.clone() as thumb:
            thumb.transform(resize="200x200")
            print(f"Thumbnail size: {thumb.width}x{thumb.height}")

        # Sample (faster but lower quality)
        with img.clone() as sampled:
            sampled.sample(200, 150)
            print(f"Sampled size: {sampled.width}x{sampled.height}")


def demo_image_rotation():
    """Demonstrate rotation and flip operations."""
    print_section("4. Rotation and Flipping")

    with Image(width=300, height=200, background=Color("lavender")) as img:
        # Add directional indicator
        with Drawing() as draw:
            draw.fill_color = Color("purple")
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


def demo_image_effects():
    """Demonstrate various image effects."""
    print_section("5. Image Effects and Filters")

    with Image(width=300, height=200, background=Color("white")) as img:
        # Add some content
        with Drawing() as draw:
            draw.fill_color = Color("red")
            draw.circle((150, 100), (200, 100))
            draw(img)

        print("Original image created")

        # Blur effect
        with img.clone() as blurred:
            blurred.blur(radius=5, sigma=3)
            print("Applied blur (radius=5, sigma=3)")

        # Sharpen effect
        with img.clone() as sharpened:
            sharpened.sharpen(radius=0, sigma=3)
            print("Applied sharpen (radius=0, sigma=3)")

        # Edge detection
        with img.clone() as edges:
            edges.edge(radius=2)
            print("Applied edge detection (radius=2)")

        # Emboss effect
        with img.clone() as embossed:
            embossed.emboss(radius=3, sigma=1)
            print("Applied emboss (radius=3, sigma=1)")


def demo_color_manipulation():
    """Demonstrate color manipulation operations."""
    print_section("6. Color Manipulation")

    with Image(width=250, height=250, background=Color("gold")) as img:
        print(f"Original background: {img.background_color}")

        # Negate colors
        with img.clone() as negated:
            negated.negate()
            print("Applied color negation")

        # Grayscale
        with img.clone() as gray:
            gray.type = "grayscale"
            print(f"Converted to grayscale: {gray.type}")

        # Sepia tone
        with img.clone() as sepia:
            sepia.sepia_tone(threshold=0.8)
            print("Applied sepia tone (threshold=0.8)")

        # Colorize
        with img.clone() as colorized:
            colorized.colorize(color=Color("blue"), alpha=Color("rgb(30%, 30%, 30%)"))
            print("Applied colorize with blue")


def demo_drawing():
    """Demonstrate drawing operations."""
    print_section("7. Drawing Shapes and Text")

    with Image(width=400, height=300, background=Color("white")) as img:
        with Drawing() as draw:
            # Set drawing properties
            draw.stroke_color = Color("black")
            draw.stroke_width = 2
            draw.fill_color = Color("lightblue")

            # Draw rectangle
            draw.rectangle(left=50, top=50, right=150, bottom=120)
            print("Drew rectangle at (50,50) to (150,120)")

            # Draw circle
            draw.fill_color = Color("lightcoral")
            draw.circle((250, 85), (300, 85))
            print("Drew circle centered at (250,85)")

            # Draw line
            draw.stroke_color = Color("green")
            draw.stroke_width = 3
            draw.line((50, 150), (350, 200))
            print("Drew line from (50,150) to (350,200)")

            # Draw text
            draw.fill_color = Color("darkblue")
            draw.font_size = 24
            draw.text(120, 250, "Wand Drawing Demo")
            print("Drew text 'Wand Drawing Demo' at (120,250)")

            # Apply to image
            draw(img)

        print(f"\nFinal image: {img.width}x{img.height}")


def demo_image_cropping():
    """Demonstrate cropping operations."""
    print_section("8. Cropping Images")

    with Image(width=500, height=400, background=Color("wheat")) as img:
        # Add a border for reference
        with Drawing() as draw:
            draw.stroke_color = Color("brown")
            draw.stroke_width = 5
            draw.fill_color = Color("transparent")
            draw.rectangle(left=0, top=0, right=499, bottom=399)
            draw(img)

        print(f"Original size: {img.width}x{img.height}")

        # Crop from center
        with img.clone() as cropped:
            cropped.crop(left=100, top=50, width=300, height=200)
            print(f"Cropped to: {cropped.width}x{cropped.height}")
            print("Crop region: left=100, top=50, width=300, height=200")


def demo_image_composite():
    """Demonstrate image composition/overlay."""
    print_section("9. Image Composition and Overlay")

    # Create base image
    with Image(width=400, height=300, background=Color("lightgray")) as base:
        print(f"Base image: {base.width}x{base.height}")

        # Create overlay image
        with Image(width=150, height=150, background=Color("pink")) as overlay:
            # Add content to overlay
            with Drawing() as draw:
                draw.fill_color = Color("red")
                draw.circle((75, 75), (100, 75))
                draw(overlay)

            print(f"Overlay image: {overlay.width}x{overlay.height}")

            # Composite images
            base.composite(overlay, left=125, top=75)
            print("Composited overlay at position (125, 75)")
            print(f"Final composite: {base.width}x{base.height}")


def demo_format_conversion():
    """Demonstrate format conversion."""
    print_section("10. Format Conversion")

    with Image(width=200, height=150, background=Color("turquoise")) as img:
        print(f"Original format: {img.format}")

        # Convert to different formats by setting format property
        formats_to_test = ["PNG", "JPEG", "GIF", "BMP"]

        for fmt in formats_to_test:
            with img.clone() as converted:
                converted.format = fmt
                blob = converted.make_blob()
                print(f"Converted to {fmt}: {len(blob)} bytes")


def demo_image_properties():
    """Demonstrate modifying image properties."""
    print_section("11. Image Properties and Metadata")

    with Image(width=300, height=200, background=Color("peachpuff")) as img:
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


def demo_border_and_frame():
    """Demonstrate adding borders and frames."""
    print_section("12. Borders and Frames")

    with Image(width=250, height=200, background=Color("mintcream")) as img:
        print(f"Original: {img.width}x{img.height}")

        # Add simple border
        with img.clone() as bordered:
            bordered.border(color=Color("navy"), width=10, height=10)
            print(f"With border: {bordered.width}x{bordered.height}")
            print("Added 10px navy border")

        # Add frame effect
        with img.clone() as framed:
            framed.frame(
                matte=Color("gold"), width=15, height=15, inner_bevel=5, outer_bevel=5
            )
            print(f"With frame: {framed.width}x{framed.height}")
            print("Added gold frame with 15px width/height")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 60)
    print("  WAND - Python ImageMagick Binding Demonstration")
    print("=" * 60)

    # Run all demos
    demo_image_creation()
    demo_image_info()
    demo_image_resize()
    demo_image_rotation()
    demo_image_effects()
    demo_color_manipulation()
    demo_drawing()
    demo_image_cropping()
    demo_image_composite()
    demo_format_conversion()
    demo_image_properties()
    demo_border_and_frame()

    print("\n" + "=" * 60)
    print("  All demonstrations completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
