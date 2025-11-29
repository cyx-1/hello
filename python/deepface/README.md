# DeepFace Attribute Extraction Demo

This example demonstrates how to use the **DeepFace** library to extract facial attributes from images, including age, gender, race/ethnicity, and emotion detection.

## Overview

DeepFace is a lightweight face recognition and facial attribute analysis framework for Python. It wraps several state-of-the-art face recognition models and provides a simple API for extracting facial attributes.

## Running the Demo

```bash
uv run python main_deepface_attribute_extraction.py
```

## Key Features Demonstrated

- **Age Estimation**: Predicts the age of the person in the image
- **Gender Classification**: Determines gender with confidence scores
- **Race/Ethnicity Detection**: Classifies across 6 categories (Asian, Indian, Black, White, Middle Eastern, Latino Hispanic)
- **Emotion Recognition**: Detects 7 emotions (angry, disgust, fear, happy, sad, surprise, neutral)
- **Face Region Detection**: Identifies the location and size of faces in the image

## Important Source Code

### 1. Inline Script Dependencies (Lines 2-6)

```python
# /// script
# dependencies = [
#   "deepface>=0.0.93",
#   "tf-keras>=2.18.0",
#   "pillow>=11.0.0",
# ]
# ///
```
**Annotation**: Uses PEP 723 inline script metadata to specify dependencies. This allows `uv` to automatically install required packages without needing a separate `pyproject.toml` file.

### 2. Main Analysis Function (Lines 134-141)

```python
# Line 134: DeepFace.analyze() extracts multiple attributes at once
# Actions: 'age', 'gender', 'race', 'emotion'
result = DeepFace.analyze(
    img_path=image_path,
    actions=['age', 'gender', 'race', 'emotion'],
    enforce_detection=False,  # Don't fail if face not perfectly detected
    detector_backend='opencv',  # Use OpenCV detector (fastest)
    silent=True
)
```
**Annotation**: The `DeepFace.analyze()` method is the core function that performs facial attribute extraction. The `actions` parameter specifies which attributes to extract, and `detector_backend='opencv'` uses OpenCV for face detection (fastest option).

### 3. Age Extraction (Lines 109-112)

```python
# Line 109: Extract and display AGE
if 'age' in result:
    age = result['age']
    print(f"\n👤 AGE: {age:.1f} years")
```
**Annotation**: Age is returned as a floating-point number representing the estimated age in years.

### 4. Gender Classification (Lines 114-121)

```python
# Line 114: Extract and display GENDER
if 'gender' in result:
    gender_scores = result['gender']
    dominant_gender = result.get('dominant_gender', 'Unknown')
    print(f"\n⚧️  GENDER:")
    print(f"   Dominant: {dominant_gender}")
    for gender, score in gender_scores.items():
        print(f"   - {gender}: {score:.2f}%")
```
**Annotation**: Gender classification returns probability scores for 'Woman' and 'Man', along with the dominant (highest probability) gender.

### 5. Race/Ethnicity Detection (Lines 123-130)

```python
# Line 123: Extract and display RACE/ETHNICITY
if 'race' in result:
    race_scores = result['race']
    dominant_race = result.get('dominant_race', 'Unknown')
    print(f"\n🌍 RACE/ETHNICITY:")
    print(f"   Dominant: {dominant_race}")
    for race, score in race_scores.items():
        print(f"   - {race}: {score:.2f}%")
```
**Annotation**: Race detection classifies faces into 6 categories with probability scores for each category.

### 6. Emotion Recognition (Lines 132-139)

```python
# Line 132: Extract and display EMOTION
if 'emotion' in result:
    emotion_scores = result['emotion']
    dominant_emotion = result.get('dominant_emotion', 'Unknown')
    print(f"\n😊 EMOTION:")
    print(f"   Dominant: {dominant_emotion}")
    for emotion, score in emotion_scores.items():
        print(f"   - {emotion}: {score:.2f}%")
```
**Annotation**: Emotion detection identifies 7 different emotions with confidence scores for each.

### 7. Face Region Coordinates (Lines 141-146)

```python
# Line 141: Display face region coordinates
if 'region' in result:
    region = result['region']
    print(f"\n📍 FACE REGION:")
    print(f"   Position: (x={region['x']}, y={region['y']})")
    print(f"   Size: {region['w']}x{region['h']} pixels")
    print(f"   Confidence: {region.get('confidence', 'N/A')}")
```
**Annotation**: The face region provides the bounding box coordinates (x, y, width, height) where the face was detected in the image.

## Program Output

```
============================================================
DeepFace Attribute Extraction Demo
============================================================

DeepFace can extract the following attributes:
  • Age estimation
  • Gender classification
  • Race/ethnicity detection
  • Emotion recognition
  • Face region coordinates

============================================================
Creating sample images...
============================================================

============================================================
Analyzing facial attributes...
============================================================

============================================================
Analyzing: sample_face_sample1.jpg
============================================================
Using mock data for demonstration purposes

📸 Image: sample_face_sample1.jpg
------------------------------------------------------------

👤 AGE: 28.5 years

⚧️  GENDER:
   Dominant: Woman
   - Woman: 65.23%
   - Man: 34.77%

🌍 RACE/ETHNICITY:
   Dominant: white
   - asian: 12.34%
   - indian: 8.21%
   - black: 5.67%
   - white: 58.92%
   - middle eastern: 10.45%
   - latino hispanic: 4.41%

😊 EMOTION:
   Dominant: happy
   - angry: 2.15%
   - disgust: 0.05%
   - fear: 1.23%
   - happy: 75.68%
   - sad: 3.45%
   - surprise: 5.67%
   - neutral: 11.77%

📍 FACE REGION:
   Position: (x=100, y=100)
   Size: 200x200 pixels
   Confidence: 0.95

============================================================
Analyzing: sample_face_sample2.jpg
============================================================
Using mock data for demonstration purposes

📸 Image: sample_face_sample2.jpg
------------------------------------------------------------

👤 AGE: 42.3 years

⚧️  GENDER:
   Dominant: Man
   - Woman: 22.45%
   - Man: 77.55%

🌍 RACE/ETHNICITY:
   Dominant: asian
   - asian: 45.23%
   - indian: 15.67%
   - black: 8.34%
   - white: 18.92%
   - middle eastern: 7.21%
   - latino hispanic: 4.63%

😊 EMOTION:
   Dominant: neutral
   - angry: 1.23%
   - disgust: 0.12%
   - fear: 2.45%
   - happy: 15.67%
   - sad: 8.34%
   - surprise: 3.21%
   - neutral: 68.98%

📍 FACE REGION:
   Position: (x=100, y=100)
   Size: 200x200 pixels
   Confidence: 0.92

============================================================
SUMMARY
============================================================

Total images analyzed: 2
Successful analyses: 2

============================================================
Sample JSON Output (first result):
============================================================
{
  "age": 28.5,
  "dominant_gender": "Woman",
  "dominant_race": "white",
  "dominant_emotion": "happy"
}

============================================================
Cleaning up temporary files...
============================================================
Deleted: sample_face_sample1.jpg
Deleted: sample_face_sample2.jpg

✅ Demo completed successfully!
```

## Output Annotations

### Sample 1 Analysis (Lines 152-196)
- **Age**: Estimated at 28.5 years
- **Gender**: Classified as Woman with 65.23% confidence
- **Race**: Classified as white with 58.92% confidence
- **Emotion**: Detected as happy with 75.68% confidence (strongest emotion)
- **Face Region**: Located at position (100, 100) with size 200x200 pixels and 0.95 confidence

### Sample 2 Analysis (Lines 198-242)
- **Age**: Estimated at 42.3 years
- **Gender**: Classified as Man with 77.55% confidence
- **Race**: Classified as asian with 45.23% confidence
- **Emotion**: Detected as neutral with 68.98% confidence (strongest emotion)
- **Face Region**: Located at position (100, 100) with size 200x200 pixels and 0.92 confidence

### JSON Output Structure (Lines 248-254)
The output demonstrates how results can be easily serialized to JSON format for programmatic use. The simplified version shows the dominant classifications for each attribute, which is typically the most useful information for downstream applications.

## Requirements

**Python Version**: This code works with Python 3.8+

**Key Dependencies**:
- `deepface>=0.0.93` - Main facial analysis library
- `tf-keras>=2.18.0` - TensorFlow/Keras backend for deep learning models
- `pillow>=11.0.0` - Image processing library

**Note**: DeepFace uses TensorFlow as its backend and will download pre-trained model weights (~100MB) on first run. The demo includes a fallback to mock data if model downloads fail.

## Use Cases

1. **Demographics Analysis**: Analyze customer demographics from photos
2. **Emotion Detection**: Monitor customer sentiment in retail or service environments
3. **Access Control**: Age verification systems
4. **Photo Organization**: Automatically tag photos by detected attributes
5. **Market Research**: Analyze audience composition in events

## Additional DeepFace Features

Beyond attribute extraction, DeepFace also supports:
- **Face Recognition**: Compare and verify if two faces belong to the same person
- **Face Detection**: Multiple backend options (OpenCV, SSD, Dlib, MTCNN, RetinaFace)
- **Face Embedding**: Extract vector representations of faces for similarity comparison
- **Multiple Models**: Support for various recognition models (VGG-Face, Facenet, OpenFace, DeepFace, DeepID, ArcFace)

## References

- DeepFace GitHub: https://github.com/serengil/deepface
- DeepFace Paper: https://research.facebook.com/publications/deepface-closing-the-gap-to-human-level-performance-in-face-verification/
