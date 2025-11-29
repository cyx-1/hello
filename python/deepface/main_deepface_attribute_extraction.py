#!/usr/bin/env python3
# /// script
# dependencies = [
#   "deepface>=0.0.93",
#   "tf-keras>=2.18.0",
#   "pillow>=11.0.0",
# ]
# ///

"""
DeepFace Attribute Extraction Demo

This script demonstrates how to use the DeepFace library to extract
facial attributes from images including age, gender, race, and emotion.
"""

import json
from pathlib import Path
import tempfile
from PIL import Image, ImageDraw


def create_sample_face_image(color: str, label: str) -> str:
    """Create a simple sample face representation for demonstration.

    Args:
        color: Background color for the image
        label: Label to identify the image

    Returns:
        Path to the created image file
    """
    # Line 30: Create a simple image (in real scenarios, use actual photos)
    img = Image.new('RGB', (400, 400), color=color)
    draw = ImageDraw.Draw(img)

    # Line 35: Draw a simple face-like structure
    # Face circle
    draw.ellipse([100, 100, 300, 300], fill='beige', outline='black', width=2)
    # Eyes
    draw.ellipse([140, 160, 170, 190], fill='black')
    draw.ellipse([230, 160, 260, 190], fill='black')
    # Nose
    draw.line([200, 175, 200, 225], fill='black', width=2)
    # Mouth
    draw.arc([150, 200, 250, 270], start=0, end=180, fill='black', width=3)

    # Line 48: Save to temporary file
    temp_dir = Path(tempfile.gettempdir())
    file_path = temp_dir / f"sample_face_{label}.jpg"
    img.save(file_path)

    return str(file_path)


def analyze_face_attributes(image_path: str, use_mock: bool = False) -> dict:
    """Analyze facial attributes using DeepFace.

    Args:
        image_path: Path to the image file
        use_mock: If True, return mock data (for demo purposes)

    Returns:
        Dictionary containing facial attributes
    """
    # Line 64: Import DeepFace (imported here to show explicit usage point)
    from deepface import DeepFace

    # Line 67: Analyze the face with all available attributes
    print(f"\n{'='*60}")
    print(f"Analyzing: {Path(image_path).name}")
    print(f"{'='*60}")

    # Line 71: Return mock data if requested (useful for demo/testing)
    if use_mock:
        print("Using mock data for demonstration purposes")
        image_name = Path(image_path).name
        # Create realistic mock data
        if 'sample1' in image_name:
            return {
                'age': 28.5,
                'region': {'x': 100, 'y': 100, 'w': 200, 'h': 200, 'confidence': 0.95},
                'gender': {'Woman': 65.23, 'Man': 34.77},
                'dominant_gender': 'Woman',
                'race': {
                    'asian': 12.34,
                    'indian': 8.21,
                    'black': 5.67,
                    'white': 58.92,
                    'middle eastern': 10.45,
                    'latino hispanic': 4.41
                },
                'dominant_race': 'white',
                'emotion': {
                    'angry': 2.15,
                    'disgust': 0.05,
                    'fear': 1.23,
                    'happy': 75.68,
                    'sad': 3.45,
                    'surprise': 5.67,
                    'neutral': 11.77
                },
                'dominant_emotion': 'happy'
            }
        else:
            return {
                'age': 42.3,
                'region': {'x': 100, 'y': 100, 'w': 200, 'h': 200, 'confidence': 0.92},
                'gender': {'Woman': 22.45, 'Man': 77.55},
                'dominant_gender': 'Man',
                'race': {
                    'asian': 45.23,
                    'indian': 15.67,
                    'black': 8.34,
                    'white': 18.92,
                    'middle eastern': 7.21,
                    'latino hispanic': 4.63
                },
                'dominant_race': 'asian',
                'emotion': {
                    'angry': 1.23,
                    'disgust': 0.12,
                    'fear': 2.45,
                    'happy': 15.67,
                    'sad': 8.34,
                    'surprise': 3.21,
                    'neutral': 68.98
                },
                'dominant_emotion': 'neutral'
            }

    try:
        # Line 134: DeepFace.analyze() extracts multiple attributes at once
        # Actions: 'age', 'gender', 'race', 'emotion'
        result = DeepFace.analyze(
            img_path=image_path,
            actions=['age', 'gender', 'race', 'emotion'],
            enforce_detection=False,  # Don't fail if face not perfectly detected
            detector_backend='opencv',  # Use OpenCV detector (fastest)
            silent=True
        )

        # Line 144: If multiple faces detected, take first one
        if isinstance(result, list):
            result = result[0]

        return result

    except Exception as e:
        # Line 151: Handle analysis errors gracefully
        print(f"⚠️  Error analyzing image: {str(e)[:100]}...")
        print("Falling back to mock data for demonstration")
        return analyze_face_attributes(image_path, use_mock=True)


def display_attributes(result: dict, image_path: str) -> None:
    """Display extracted attributes in a formatted manner.

    Args:
        result: Dictionary containing analysis results
        image_path: Path to analyzed image
    """
    if not result:
        print("No attributes extracted.")
        return

    print(f"\n📸 Image: {Path(image_path).name}")
    print(f"{'-'*60}")

    # Line 109: Extract and display AGE
    if 'age' in result:
        age = result['age']
        print(f"\n👤 AGE: {age:.1f} years")

    # Line 114: Extract and display GENDER
    if 'gender' in result:
        gender_scores = result['gender']
        dominant_gender = result.get('dominant_gender', 'Unknown')
        print("\n⚧️  GENDER:")
        print(f"   Dominant: {dominant_gender}")
        for gender, score in gender_scores.items():
            print(f"   - {gender}: {score:.2f}%")

    # Line 123: Extract and display RACE/ETHNICITY
    if 'race' in result:
        race_scores = result['race']
        dominant_race = result.get('dominant_race', 'Unknown')
        print("\n🌍 RACE/ETHNICITY:")
        print(f"   Dominant: {dominant_race}")
        for race, score in race_scores.items():
            print(f"   - {race}: {score:.2f}%")

    # Line 132: Extract and display EMOTION
    if 'emotion' in result:
        emotion_scores = result['emotion']
        dominant_emotion = result.get('dominant_emotion', 'Unknown')
        print("\n😊 EMOTION:")
        print(f"   Dominant: {dominant_emotion}")
        for emotion, score in emotion_scores.items():
            print(f"   - {emotion}: {score:.2f}%")

    # Line 141: Display face region coordinates
    if 'region' in result:
        region = result['region']
        print("\n📍 FACE REGION:")
        print(f"   Position: (x={region['x']}, y={region['y']})")
        print(f"   Size: {region['w']}x{region['h']} pixels")
        print(f"   Confidence: {region.get('confidence', 'N/A')}")


def main():
    """Main function demonstrating DeepFace attribute extraction."""

    # Line 152: Print header
    print("\n" + "="*60)
    print("DeepFace Attribute Extraction Demo")
    print("="*60)
    print("\nDeepFace can extract the following attributes:")
    print("  • Age estimation")
    print("  • Gender classification")
    print("  • Race/ethnicity detection")
    print("  • Emotion recognition")
    print("  • Face region coordinates")

    # Line 163: Create sample images for demonstration
    print("\n" + "="*60)
    print("Creating sample images...")
    print("="*60)

    sample_images = [
        create_sample_face_image('lightblue', 'sample1'),
        create_sample_face_image('lightgreen', 'sample2'),
    ]

    # Line 173: Analyze each sample image
    print("\n" + "="*60)
    print("Analyzing facial attributes...")
    print("="*60)

    all_results = []
    for img_path in sample_images:
        result = analyze_face_attributes(img_path)
        if result:
            display_attributes(result, img_path)
            all_results.append({
                'image': Path(img_path).name,
                'attributes': result
            })

    # Line 188: Summary section
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"\nTotal images analyzed: {len(sample_images)}")
    print(f"Successful analyses: {len(all_results)}")

    # Line 195: Show JSON output example
    if all_results:
        print("\n" + "="*60)
        print("Sample JSON Output (first result):")
        print("="*60)
        first_result = all_results[0]['attributes']
        # Show simplified version for clarity
        simplified = {
            'age': first_result.get('age'),
            'dominant_gender': first_result.get('dominant_gender'),
            'dominant_race': first_result.get('dominant_race'),
            'dominant_emotion': first_result.get('dominant_emotion'),
        }
        print(json.dumps(simplified, indent=2))

    # Line 210: Cleanup
    print("\n" + "="*60)
    print("Cleaning up temporary files...")
    print("="*60)
    for img_path in sample_images:
        Path(img_path).unlink(missing_ok=True)
        print(f"Deleted: {Path(img_path).name}")

    print("\n✅ Demo completed successfully!")


if __name__ == "__main__":
    # Line 222: Entry point
    main()
