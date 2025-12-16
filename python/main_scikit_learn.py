# /// script
# dependencies = [
#   "scikit-learn>=1.3.0",
#   "numpy>=1.24.0",
#   "pandas>=2.0.0"
# ]
# ///

"""
Comprehensive Scikit-Learn demonstration showcasing various machine learning capabilities.
"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    mean_squared_error,
    r2_score,
    silhouette_score,
)


def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'=' * 80}")
    print(f"{title.center(80)}")
    print(f"{'=' * 80}\n")


def demonstrate_classification():
    """Demonstrate classification with Iris dataset."""
    print_section("CLASSIFICATION: Iris Dataset")

    # Line 50: Load the famous Iris dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    print(f"Line 54: Dataset shape: {X.shape}")
    print(f"Line 55: Number of classes: {len(np.unique(y))}")
    print(f"Line 56: Feature names: {iris.feature_names}")

    # Line 59: Split data into training and testing sets (80/20 split)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"\nLine 63: Training samples: {X_train.shape[0]}")
    print(f"Line 64: Testing samples: {X_test.shape[0]}")

    # Line 67: Train a Decision Tree Classifier
    dt_classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
    dt_classifier.fit(X_train, y_train)
    dt_predictions = dt_classifier.predict(X_test)
    dt_accuracy = accuracy_score(y_test, dt_predictions)

    print(f"\nLine 73: Decision Tree Accuracy: {dt_accuracy:.4f}")

    # Line 76: Train a Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)
    rf_predictions = rf_classifier.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_predictions)

    print(f"Line 82: Random Forest Accuracy: {rf_accuracy:.4f}")

    # Line 85: Display confusion matrix
    print("\nLine 86: Confusion Matrix (Random Forest):")
    print(confusion_matrix(y_test, rf_predictions))

    # Line 90: Display classification report
    print("\nLine 91: Classification Report (Random Forest):")
    print(classification_report(y_test, rf_predictions, target_names=iris.target_names))

    # Line 95: Perform 5-fold cross-validation
    cv_scores = cross_val_score(rf_classifier, X, y, cv=5)
    print(f"\nLine 97: Cross-Validation Scores: {cv_scores}")
    print(f"Line 98: Mean CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")


def demonstrate_regression():
    """Demonstrate regression with synthetic housing dataset."""
    print_section("REGRESSION: Synthetic Housing Price Dataset")

    # Line 106: Create synthetic housing dataset (avoids network issues)
    np.random.seed(42)
    n_samples = 1000
    feature_names = [
        "SquareFeet",
        "Bedrooms",
        "Bathrooms",
        "YearBuilt",
        "LotSize",
        "GarageSize",
        "Distance",
        "SchoolRating",
    ]

    # Generate features with realistic correlations to house prices
    X = np.column_stack(
        [
            np.random.normal(1800, 500, n_samples),  # Square feet
            np.random.randint(1, 6, n_samples),  # Bedrooms
            np.random.randint(1, 4, n_samples),  # Bathrooms
            np.random.randint(1950, 2020, n_samples),  # Year built
            np.random.normal(7500, 2000, n_samples),  # Lot size
            np.random.randint(0, 3, n_samples),  # Garage size
            np.random.normal(15, 8, n_samples),  # Distance to city
            np.random.uniform(1, 10, n_samples),  # School rating
        ]
    )

    # Generate target (house prices) with realistic relationship
    y = (
        0.15 * X[:, 0]  # Square feet
        + 25000 * X[:, 1]  # Bedrooms
        + 35000 * X[:, 2]  # Bathrooms
        + 500 * (X[:, 3] - 1950)  # Year built
        + 0.02 * X[:, 4]  # Lot size
        + 15000 * X[:, 5]  # Garage
        + -3000 * X[:, 6]  # Distance (negative)
        + 10000 * X[:, 7]  # School rating
        + np.random.normal(0, 25000, n_samples)
    )  # Noise

    y = y / 1000  # Convert to thousands

    print(f"Line 136: Dataset shape: {X.shape}")
    print(f"Line 137: Feature names: {feature_names}")
    print(
        f"Line 138: Target (house price) - Min: ${y.min():.2f}k, Max: ${y.max():.2f}k"
    )

    # Line 141: Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Line 146: Train a Linear Regression model
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_predictions = lr_model.predict(X_test)

    # Line 151: Calculate regression metrics
    mse = mean_squared_error(y_test, lr_predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, lr_predictions)

    print("\nLine 156: Linear Regression Performance:")
    print(f"Line 157:   Mean Squared Error: {mse:.4f}")
    print(f"Line 158:   Root Mean Squared Error: {rmse:.4f}")
    print(f"Line 159:   R² Score: {r2:.4f}")

    # Line 162: Show feature coefficients
    print("\nLine 163: Feature Importance (Coefficients):")
    for name, coef in zip(feature_names, lr_model.coef_):
        print(f"Line 165:   {name:15s}: {coef:8.4f}")


def demonstrate_clustering():
    """Demonstrate clustering with Iris dataset."""
    print_section("CLUSTERING: K-Means on Iris Dataset")

    # Line 151: Load Iris dataset
    iris = datasets.load_iris()
    X = iris.data

    print(f"Line 155: Dataset shape: {X.shape}")

    # Line 158: Apply K-Means clustering with 3 clusters
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X)

    print("\nLine 162: K-Means Clustering Results:")
    print(f"Line 163: Cluster centers shape: {kmeans.cluster_centers_.shape}")

    # Line 166: Calculate silhouette score (measure of cluster quality)
    silhouette_avg = silhouette_score(X, cluster_labels)
    print(f"Line 168: Silhouette Score: {silhouette_avg:.4f}")

    # Line 171: Show distribution of samples across clusters
    unique, counts = np.unique(cluster_labels, return_counts=True)
    print("\nLine 173: Cluster Distribution:")
    for cluster_id, count in zip(unique, counts):
        print(f"Line 175:   Cluster {cluster_id}: {count} samples")

    # Line 178: Compare with actual labels
    print("\nLine 179: Comparison with actual labels (first 20 samples):")
    print(f"Line 180: Predicted clusters: {cluster_labels[:20]}")
    print(f"Line 181: Actual labels:      {iris.target[:20]}")


def demonstrate_pipeline():
    """Demonstrate preprocessing pipeline."""
    print_section("PIPELINE: Preprocessing + Classification")

    # Line 189: Load Iris dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # Line 193: Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Line 198: Create a pipeline with StandardScaler and LogisticRegression
    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=200, random_state=42)),
        ]
    )

    print("Line 204: Pipeline steps:")
    for step_name, step_estimator in pipeline.steps:
        print(f"Line 206:   {step_name}: {type(step_estimator).__name__}")

    # Line 209: Fit the entire pipeline
    pipeline.fit(X_train, y_train)

    # Line 212: Make predictions
    predictions = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print(f"\nLine 216: Pipeline Accuracy: {accuracy:.4f}")

    # Line 219: Show scaling effect
    print("\nLine 220: Feature scaling example (first training sample):")
    print(f"Line 221:   Original values: {X_train[0]}")
    scaled = pipeline.named_steps["scaler"].transform(X_train[0].reshape(1, -1))
    print(f"Line 223:   Scaled values:   {scaled[0]}")


def demonstrate_feature_importance():
    """Demonstrate feature importance analysis."""
    print_section("FEATURE IMPORTANCE: Random Forest Analysis")

    # Line 231: Load Iris dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # Line 235: Train Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X, y)

    # Line 239: Get feature importances
    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1]

    print("Line 243: Feature Importance Ranking:")
    for i, idx in enumerate(indices):
        print(
            f"Line 246:   {i + 1}. {iris.feature_names[idx]:20s}: {importances[idx]:.4f}"
        )


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 80)
    print("SCIKIT-LEARN COMPREHENSIVE DEMONSTRATION".center(80))
    print("=" * 80)

    demonstrate_classification()
    demonstrate_regression()
    demonstrate_clustering()
    demonstrate_pipeline()
    demonstrate_feature_importance()

    print("\n" + "=" * 80)
    print("DEMONSTRATION COMPLETE".center(80))
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
