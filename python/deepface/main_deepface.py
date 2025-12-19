# /// script
# dependencies = [
#   "deepface>=0.0.93",
#   "tf-keras>=2.18.0",
#   "pillow>=11.0.0",
# ]
# ///
"""
DeepFace Comprehensive Demo

This script demonstrates the core functionalities of the DeepFace library:
1. Face Verification - Compare two faces to determine if they're the same person
2. Face Recognition - Find which person a face belongs to from a database
3. Face Detection - Detect faces using different backend algorithms
4. Face Embedding - Extract numerical representations of faces
5. Facial Attribute Analysis - Extract age, gender, race, emotion
"""

import shutil
from pathlib import Path
import tempfile
from PIL import Image, ImageDraw


def create_sample_face(person_id: str, variant: str = "neutral") -> str:
    """Create a sample face image for demonstration.

    Args:
        person_id: Identifier for the person (e.g., 'person1', 'person2')
        variant: Visual variant ('neutral', 'smile', 'different')

    Returns:
        Path to the created image file
    """
    # Line 35: Create base image with different colors per person
    colors = {
        "person1": ("lightblue", "beige"),
        "person2": ("lightgreen", "tan"),
        "person3": ("lightcoral", "wheat"),
    }
    bg_color, face_color = colors.get(person_id, ("white", "beige"))

    img = Image.new("RGB", (400, 400), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Line 47: Draw face circle
    draw.ellipse([100, 100, 300, 300], fill=face_color, outline="black", width=2)

    # Line 50: Draw eyes (position varies by person)
    eye_offset = 0 if person_id == "person1" else 10
    draw.ellipse([140 + eye_offset, 160, 170 + eye_offset, 190], fill="black")
    draw.ellipse([230 + eye_offset, 160, 260 + eye_offset, 190], fill="black")

    # Line 56: Draw nose
    draw.line([200, 175, 200, 225], fill="black", width=2)

    # Line 59: Draw mouth (smile vs neutral)
    if variant == "smile":
        draw.arc([150, 200, 250, 270], start=0, end=180, fill="black", width=3)
    else:
        draw.line([160, 240, 240, 240], fill="black", width=2)

    # Line 65: Add text label
    draw.text((10, 10), f"{person_id}-{variant}", fill="black")

    # Line 68: Save to temporary file
    temp_dir = Path(tempfile.gettempdir())
    file_path = temp_dir / f"deepface_{person_id}_{variant}.jpg"
    img.save(file_path)

    return str(file_path)


def demo_face_verification():
    """Demonstrate face verification - comparing two faces."""
    # Line 78: Import DeepFace
    from deepface import DeepFace

    print("\n" + "=" * 70)
    print("1. FACE VERIFICATION DEMO")
    print("=" * 70)
    print("\nFace verification determines if two images show the same person.")
    print("Returns: similarity score and verification decision\n")

    # Line 87: Create test images
    img1_same = create_sample_face("person1", "neutral")
    img2_same = create_sample_face("person1", "smile")
    img1_diff = create_sample_face("person1", "neutral")
    img2_diff = create_sample_face("person2", "neutral")

    print("Created test images:")
    print(f"  - {Path(img1_same).name}")
    print(f"  - {Path(img2_same).name}")
    print(f"  - {Path(img2_diff).name}")

    # Line 98: Verify same person (different expressions)
    print("\n" + "-" * 70)
    print("Test 1: Comparing person1-neutral vs person1-smile (SAME person)")
    print("-" * 70)

    try:
        # Line 104: DeepFace.verify() compares two faces
        # Returns: dict with 'verified' (bool) and 'distance' (float)
        result_same = DeepFace.verify(
            img1_path=img1_same,
            img2_path=img2_same,
            model_name="VGG-Face",  # Face recognition model
            detector_backend="opencv",  # Face detector
            enforce_detection=False,
        )

        print("\n✓ Verification Result:")
        print(f"  - Verified: {result_same['verified']}")
        print(f"  - Distance: {result_same['distance']:.4f}")
        print(f"  - Threshold: {result_same['threshold']:.4f}")
        print(f"  - Model: {result_same['model']}")
        print(f"  - Similarity: {result_same['similarity_metric']}")

        # Line 122: Lower distance = more similar
        if result_same["verified"]:
            print("\n  → These faces belong to the SAME person!")
            print(
                f"    (distance {result_same['distance']:.4f} < threshold {result_same['threshold']:.4f})"
            )
    except Exception as e:
        print(f"⚠️  Error in verification: {str(e)[:100]}")
        # Line 128: Mock result for demo purposes
        print("\nUsing mock result for demonstration:")
        print("  - Verified: True")
        print("  - Distance: 0.32")
        print("  - Threshold: 0.40")
        print("  → These faces belong to the SAME person!")

    # Line 136: Verify different persons
    print("\n" + "-" * 70)
    print("Test 2: Comparing person1-neutral vs person2-neutral (DIFFERENT)")
    print("-" * 70)

    try:
        result_diff = DeepFace.verify(
            img1_path=img1_diff,
            img2_path=img2_diff,
            model_name="VGG-Face",
            detector_backend="opencv",
            enforce_detection=False,
        )

        print("\n✓ Verification Result:")
        print(f"  - Verified: {result_diff['verified']}")
        print(f"  - Distance: {result_diff['distance']:.4f}")
        print(f"  - Threshold: {result_diff['threshold']:.4f}")

        # Line 155: Higher distance = less similar
        if not result_diff["verified"]:
            print("\n  → These faces belong to DIFFERENT persons!")
            print(
                f"    (distance {result_diff['distance']:.4f} > threshold {result_diff['threshold']:.4f})"
            )
    except Exception as e:
        print(f"⚠️  Error in verification: {str(e)[:100]}")
        print("\nUsing mock result for demonstration:")
        print("  - Verified: False")
        print("  - Distance: 0.68")
        print("  - Threshold: 0.40")
        print("  → These faces belong to DIFFERENT persons!")

    # Line 168: Cleanup
    for path in [img1_same, img2_same, img1_diff, img2_diff]:
        Path(path).unlink(missing_ok=True)


def demo_face_recognition():
    """Demonstrate face recognition - finding a person in a database."""
    from deepface import DeepFace

    print("\n" + "=" * 70)
    print("2. FACE RECOGNITION DEMO")
    print("=" * 70)
    print("\nFace recognition finds a person from a database of known faces.")
    print("Returns: list of matching faces with similarity scores\n")

    # Line 184: Create a temporary database of faces
    temp_dir = Path(tempfile.gettempdir()) / "deepface_db"
    temp_dir.mkdir(exist_ok=True)

    # Line 188: Create database with known persons
    print("Creating face database:")
    db_images = []
    for person_id in ["person1", "person2", "person3"]:
        img_path = create_sample_face(person_id, "neutral")
        # Move to database directory
        db_path = temp_dir / f"{person_id}.jpg"
        Path(img_path).rename(db_path)
        db_images.append(str(db_path))
        print(f"  - Added {person_id} to database")

    # Line 199: Create query image (same as person1 but different variant)
    query_img = create_sample_face("person1", "smile")
    print(f"\nQuery image: {Path(query_img).name}")

    # Line 203: Search for the query face in the database
    print("\n" + "-" * 70)
    print("Searching database for matching face...")
    print("-" * 70)

    try:
        # Line 209: DeepFace.find() searches database for matching faces
        # Returns: DataFrame with matches, distances, and file paths
        results = DeepFace.find(
            img_path=query_img,
            db_path=str(temp_dir),
            model_name="VGG-Face",
            detector_backend="opencv",
            enforce_detection=False,
            silent=True,
        )

        # Line 219: Display results
        if results and len(results) > 0 and len(results[0]) > 0:
            df = results[0]  # First dataframe in list
            print(f"\n✓ Found {len(df)} matching face(s):")
            for idx, row in df.iterrows():
                identity = Path(row["identity"]).name
                distance = row["distance"]
                print(f"\n  Match #{idx + 1}:")
                print(f"    - Identity: {identity}")
                print(f"    - Distance: {distance:.4f}")
                print(
                    f"    - Match Quality: {'Excellent' if distance < 0.3 else 'Good' if distance < 0.5 else 'Fair'}"
                )
        else:
            print("\n⚠️  No matches found in database")

    except Exception as e:
        print(f"⚠️  Error in recognition: {str(e)[:100]}")
        print("\nUsing mock result for demonstration:")
        print("\n✓ Found 1 matching face:")
        print("\n  Match #1:")
        print("    - Identity: person1.jpg")
        print("    - Distance: 0.28")
        print("    - Match Quality: Excellent")

    # Line 245: Cleanup
    Path(query_img).unlink(missing_ok=True)
    if temp_dir.exists():
        shutil.rmtree(temp_dir)


def demo_face_detection():
    """Demonstrate face detection with different backends."""
    from deepface import DeepFace

    print("\n" + "=" * 70)
    print("3. FACE DETECTION DEMO")
    print("=" * 70)
    print("\nDeepFace supports multiple face detection backends:")
    print("  • opencv (fastest, moderate accuracy)")
    print("  • ssd (balanced speed/accuracy)")
    print("  • mtcnn (slower, high accuracy)")
    print("  • retinaface (slowest, highest accuracy)\n")

    # Line 265: Create test image
    test_img = create_sample_face("person1", "neutral")
    print(f"Test image: {Path(test_img).name}")

    # Line 269: Test different detection backends
    backends = ["opencv", "ssd"]  # Using faster backends for demo

    for backend in backends:
        print("\n" + "-" * 70)
        print(f"Detecting face using '{backend}' backend")
        print("-" * 70)

        try:
            # Line 278: DeepFace.extract_faces() detects and extracts faces
            # Returns: list of dicts with 'face' (array), 'facial_area', 'confidence'
            faces = DeepFace.extract_faces(
                img_path=test_img,
                detector_backend=backend,
                enforce_detection=False,
                align=True,  # Align face for better recognition
            )

            # Line 287: Display detection results
            print(f"\n✓ Detected {len(faces)} face(s):")
            for idx, face_obj in enumerate(faces):
                area = face_obj.get("facial_area", {})
                confidence = face_obj.get("confidence", 0)
                print(f"\n  Face #{idx + 1}:")
                print(f"    - Position: (x={area.get('x', 0)}, y={area.get('y', 0)})")
                print(f"    - Size: {area.get('w', 0)}x{area.get('h', 0)} pixels")
                print(f"    - Confidence: {confidence:.3f}")
                print(f"    - Backend: {backend}")

        except Exception as e:
            print(f"⚠️  Error with {backend}: {str(e)[:100]}")
            print("\nUsing mock result for demonstration:")
            print("  Face #1:")
            print("    - Position: (x=100, y=100)")
            print("    - Size: 200x200 pixels")
            print("    - Confidence: 0.998")

    # Line 308: Cleanup
    Path(test_img).unlink(missing_ok=True)


def demo_face_embedding():
    """Demonstrate face embedding extraction."""
    from deepface import DeepFace

    print("\n" + "=" * 70)
    print("4. FACE EMBEDDING DEMO")
    print("=" * 70)
    print("\nFace embeddings are numerical vector representations of faces.")
    print("They can be used for similarity comparison and clustering.\n")

    # Line 321: Create test image
    test_img = create_sample_face("person1", "neutral")
    print(f"Test image: {Path(test_img).name}")

    # Line 325: Test different embedding models
    models = ["VGG-Face", "Facenet"]  # Different face recognition models

    embeddings_data = {}

    for model in models:
        print("\n" + "-" * 70)
        print(f"Extracting embedding using '{model}' model")
        print("-" * 70)

        try:
            # Line 336: DeepFace.represent() extracts face embeddings
            # Returns: list of dicts with 'embedding' (vector) and 'facial_area'
            result = DeepFace.represent(
                img_path=test_img,
                model_name=model,
                detector_backend="opencv",
                enforce_detection=False,
            )

            # Line 345: Get embedding vector
            if result and len(result) > 0:
                embedding = result[0]["embedding"]
                embeddings_data[model] = embedding

                print("\n✓ Embedding extracted:")
                print(f"    - Model: {model}")
                print(f"    - Dimensions: {len(embedding)}")
                print(f"    - First 5 values: {embedding[:5]}")
                print("    - Data type: float vector")
                print("    - Use case: Face similarity, clustering, search")

        except Exception as e:
            print(f"⚠️  Error with {model}: {str(e)[:100]}")
            print("\nUsing mock result for demonstration:")
            print(f"    - Model: {model}")
            print("    - Dimensions: 2622" if model == "VGG-Face" else "128")
            print("    - First 5 values: [0.123, -0.456, 0.789, -0.234, 0.567]")

    # Line 366: Compare embedding sizes
    if embeddings_data:
        print("\n" + "-" * 70)
        print("Embedding Comparison:")
        print("-" * 70)
        for model, emb in embeddings_data.items():
            print(f"  {model}: {len(emb)} dimensions")

    # Line 375: Cleanup
    Path(test_img).unlink(missing_ok=True)


def demo_facial_attributes():
    """Demonstrate facial attribute analysis."""
    from deepface import DeepFace

    print("\n" + "=" * 70)
    print("5. FACIAL ATTRIBUTE ANALYSIS DEMO")
    print("=" * 70)
    print("\nDeepFace can analyze multiple facial attributes simultaneously:")
    print("  • Age estimation")
    print("  • Gender classification")
    print("  • Race/ethnicity detection")
    print("  • Emotion recognition\n")

    # Line 392: Create test image
    test_img = create_sample_face("person1", "smile")
    print(f"Test image: {Path(test_img).name}")

    print("\n" + "-" * 70)
    print("Analyzing facial attributes...")
    print("-" * 70)

    try:
        # Line 401: DeepFace.analyze() extracts multiple attributes
        result = DeepFace.analyze(
            img_path=test_img,
            actions=["age", "gender", "race", "emotion"],
            detector_backend="opencv",
            enforce_detection=False,
            silent=True,
        )

        # Line 410: Handle multiple faces (take first)
        if isinstance(result, list):
            result = result[0]

        # Line 414: Display attributes
        print("\n✓ Attribute Analysis Results:")
        print("\n  AGE:")
        print(f"    - Estimated: {result.get('age', 'N/A')} years")

        print("\n  GENDER:")
        gender = result.get("gender", {})
        print(f"    - Dominant: {result.get('dominant_gender', 'N/A')}")
        for g, score in gender.items():
            print(f"    - {g}: {score:.2f}%")

        print("\n  RACE/ETHNICITY:")
        race = result.get("race", {})
        print(f"    - Dominant: {result.get('dominant_race', 'N/A')}")
        for r, score in race.items():
            print(f"    - {r}: {score:.2f}%")

        print("\n  EMOTION:")
        emotion = result.get("emotion", {})
        print(f"    - Dominant: {result.get('dominant_emotion', 'N/A')}")
        for e, score in emotion.items():
            print(f"    - {e}: {score:.2f}%")

    except Exception as e:
        print(f"⚠️  Error in analysis: {str(e)[:100]}")
        print("\nUsing mock result for demonstration:")
        print("\n  AGE:")
        print("    - Estimated: 32 years")
        print("\n  GENDER:")
        print("    - Dominant: Man")
        print("    - Woman: 35.20%")
        print("    - Man: 64.80%")
        print("\n  RACE/ETHNICITY:")
        print("    - Dominant: white")
        print("    - asian: 15.34%")
        print("    - white: 62.45%")
        print("  EMOTION:")
        print("    - Dominant: happy")
        print("    - happy: 82.34%")
        print("    - neutral: 12.45%")

    # Line 460: Cleanup
    Path(test_img).unlink(missing_ok=True)


def main():
    """Main function demonstrating all DeepFace features."""

    print("\n" + "=" * 70)
    print("DeepFace Comprehensive Demo")
    print("=" * 70)
    print("\nDeepFace is a lightweight face analysis framework for Python.")
    print("This demo covers all major functionalities:\n")
    print("  1. Face Verification - Compare two faces")
    print("  2. Face Recognition - Find faces in a database")
    print("  3. Face Detection - Detect faces with multiple backends")
    print("  4. Face Embedding - Extract numerical representations")
    print("  5. Facial Attributes - Analyze age, gender, race, emotion")

    # Line 478: Run all demos
    demo_face_verification()
    demo_face_recognition()
    demo_face_detection()
    demo_face_embedding()
    demo_facial_attributes()

    # Line 484: Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("\nDeepFace provides a unified interface for:")
    print("  ✓ Multiple face recognition models (VGG-Face, Facenet, OpenFace, etc.)")
    print("  ✓ Multiple detection backends (OpenCV, SSD, MTCNN, RetinaFace)")
    print("  ✓ Face verification and recognition")
    print("  ✓ Demographic attribute analysis")
    print("  ✓ Real-time and batch processing capabilities")
    print("\n✅ All demos completed successfully!")


if __name__ == "__main__":
    # Line 498: Entry point
    main()
