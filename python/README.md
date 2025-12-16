# Scikit-Learn Comprehensive Demonstration

This project demonstrates various machine learning capabilities of **Scikit-Learn**, the popular Python machine learning library.

## Running the Program

```bash
uv run main_scikit_learn.py
```

## Requirements

This demonstration requires:
- **Python**: 3.11 or later
- **scikit-learn**: >= 1.3.0
- **numpy**: >= 1.24.0
- **pandas**: >= 2.0.0

Dependencies are specified using inline script metadata and will be automatically installed by `uv`.

---

## What This Demonstration Covers

1. **Classification** - Using Decision Trees and Random Forests on the Iris dataset
2. **Regression** - Linear regression with synthetic housing price data
3. **Clustering** - K-Means clustering on the Iris dataset
4. **Pipelines** - Combining preprocessing and classification
5. **Feature Importance** - Analyzing which features matter most

---

## Section 1: Classification with Iris Dataset

### Key Source Code (Lines 41-98)

```python
50:     # Line 50: Load the famous Iris dataset
51:     iris = datasets.load_iris()
52:     X, y = iris.data, iris.target
...
59:     # Line 59: Split data into training and testing sets (80/20 split)
60:     X_train, X_test, y_train, y_test = train_test_split(
61:         X, y, test_size=0.2, random_state=42
62:     )
...
67:     # Line 67: Train a Decision Tree Classifier
68:     dt_classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
69:     dt_classifier.fit(X_train, y_train)
...
76:     # Line 76: Train a Random Forest Classifier
77:     rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
78:     rf_classifier.fit(X_train, y_train)
...
95:     # Line 95: Perform 5-fold cross-validation
96:     cv_scores = cross_val_score(rf_classifier, X, y, cv=5)
```

### Program Output

```
================================================================================
                          CLASSIFICATION: Iris Dataset
================================================================================

Line 54: Dataset shape: (150, 4)
Line 55: Number of classes: 3
Line 56: Feature names: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

Line 63: Training samples: 120
Line 64: Testing samples: 30

Line 73: Decision Tree Accuracy: 1.0000
Line 82: Random Forest Accuracy: 1.0000

Line 86: Confusion Matrix (Random Forest):
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]

Line 91: Classification Report (Random Forest):
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30


Line 97: Cross-Validation Scores: [0.96666667 0.96666667 0.93333333 0.96666667 1.        ]
Line 98: Mean CV Score: 0.9667 (+/- 0.0211)
```

### Analysis

- **Lines 50-52**: The Iris dataset contains 150 samples of iris flowers with 4 features each (sepal/petal dimensions)
- **Lines 59-62**: Data is split 80/20 for training and testing (120 train, 30 test samples)
- **Lines 67-69**: A Decision Tree with max depth of 3 achieves **100% accuracy** on the test set
- **Lines 76-78**: Random Forest with 100 trees also achieves **100% accuracy**
- **Line 86**: The confusion matrix shows perfect classification - no misclassifications
- **Line 91**: The classification report confirms precision, recall, and f1-scores of 1.00 for all three iris species
- **Lines 95-98**: Cross-validation scores show the model is robust with mean accuracy of **96.67%**

---

## Section 2: Regression with Housing Price Data

### Key Source Code (Lines 89-151)

```python
93:     # Line 106: Create synthetic housing dataset (avoids network issues)
94:     np.random.seed(42)
95:     n_samples = 1000
96:     feature_names = ['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt',
97:                      'LotSize', 'GarageSize', 'Distance', 'SchoolRating']
...
100:    X = np.column_stack([
101:        np.random.normal(1800, 500, n_samples),    # Square feet
102:        np.random.randint(1, 6, n_samples),        # Bedrooms
103:        np.random.randint(1, 4, n_samples),        # Bathrooms
104:        np.random.randint(1950, 2020, n_samples),  # Year built
...
112:    y = (0.15 * X[:, 0] +                          # Square feet
113:         25000 * X[:, 1] +                         # Bedrooms
114:         35000 * X[:, 2] +                         # Bathrooms
115:         500 * (X[:, 3] - 1950) +                  # Year built
...
134:    lr_model = LinearRegression()
135:    lr_model.fit(X_train, y_train)
136:    lr_predictions = lr_model.predict(X_test)
```

### Program Output

```
================================================================================
                  REGRESSION: Synthetic Housing Price Dataset
================================================================================

Line 136: Dataset shape: (1000, 8)
Line 137: Feature names: ['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt', 'LotSize', 'GarageSize', 'Distance', 'SchoolRating']
Line 138: Target (house price) - Min: $15.82k, Max: $364.47k

Line 156: Linear Regression Performance:
Line 157:   Mean Squared Error: 545.9762
Line 158:   Root Mean Squared Error: 23.3661
Line 159:   R² Score: 0.8422

Line 163: Feature Importance (Coefficients):
Line 165:   SquareFeet     :   0.0019
Line 165:   Bedrooms       :  25.3437
Line 165:   Bathrooms      :  33.9307
Line 165:   YearBuilt      :   0.4842
Line 165:   LotSize        :  -0.0007
Line 165:   GarageSize     :  14.9382
Line 165:   Distance       :  -3.0938
Line 165:   SchoolRating   :  10.1450
```

### Analysis

- **Lines 93-108**: Synthetic housing data is generated with 8 realistic features affecting house prices
- **Lines 112-120**: Target prices are computed using a known linear relationship plus noise
- **Lines 134-136**: Linear Regression model is trained to learn the relationship
- **Line 157**: RMSE of 23.37k means predictions are typically off by about $23,370
- **Line 159**: R² score of **0.8422** means the model explains 84.22% of variance in house prices
- **Line 163-165**: Coefficients reveal feature importance:
  - **Bathrooms** ($33.93k) and **Bedrooms** ($25.34k) have the largest positive impact
  - **Distance** (-$3.09k) has a negative impact (farther from city = lower price)
  - **SchoolRating** ($10.15k per point) significantly affects prices

---

## Section 3: Clustering with K-Means

### Key Source Code (Lines 154-186)

```python
158:    # Line 158: Apply K-Means clustering with 3 clusters
159:    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
160:    cluster_labels = kmeans.fit_predict(X)
...
166:    # Line 166: Calculate silhouette score (measure of cluster quality)
167:    silhouette_avg = silhouette_score(X, cluster_labels)
...
171:    # Line 171: Show distribution of samples across clusters
172:    unique, counts = np.unique(cluster_labels, return_counts=True)
```

### Program Output

```
================================================================================
                      CLUSTERING: K-Means on Iris Dataset
================================================================================

Line 155: Dataset shape: (150, 4)

Line 162: K-Means Clustering Results:
Line 163: Cluster centers shape: (3, 4)
Line 168: Silhouette Score: 0.5528

Line 173: Cluster Distribution:
Line 175:   Cluster 0: 62 samples
Line 175:   Cluster 1: 50 samples
Line 175:   Cluster 2: 38 samples

Line 179: Comparison with actual labels (first 20 samples):
Line 180: Predicted clusters: [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
Line 181: Actual labels:      [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
```

### Analysis

- **Lines 158-160**: K-Means algorithm finds 3 cluster centers in the 4-dimensional feature space
- **Line 168**: Silhouette score of **0.5528** indicates reasonably good cluster separation (range: -1 to 1)
- **Lines 173-175**: Clusters are somewhat balanced (62, 50, 38 samples)
- **Lines 180-181**: Note that cluster IDs (0,1,2) don't directly map to species labels - K-Means is unsupervised and assigns arbitrary cluster numbers

---

## Section 4: Pipeline with Preprocessing

### Key Source Code (Lines 188-227)

```python
198:    # Line 198: Create a pipeline with StandardScaler and LogisticRegression
199:    pipeline = Pipeline([
200:        ('scaler', StandardScaler()),
201:        ('classifier', LogisticRegression(max_iter=200, random_state=42))
202:    ])
...
209:    # Line 209: Fit the entire pipeline
210:    pipeline.fit(X_train, y_train)
...
212:    # Line 212: Make predictions
213:    predictions = pipeline.predict(X_test)
```

### Program Output

```
================================================================================
                    PIPELINE: Preprocessing + Classification
================================================================================

Line 204: Pipeline steps:
Line 206:   scaler: StandardScaler
Line 206:   classifier: LogisticRegression

Line 216: Pipeline Accuracy: 1.0000

Line 220: Feature scaling example (first training sample):
Line 221:   Original values: [4.6 3.6 1.  0.2]
Line 223:   Scaled values:   [-1.47393679  1.20365799 -1.56253475 -1.31260282]
```

### Analysis

- **Lines 198-202**: A Pipeline chains StandardScaler (normalization) with LogisticRegression
- **Line 210**: Calling `fit()` on the pipeline trains both steps in sequence
- **Line 216**: The pipeline achieves **100% accuracy** on the test set
- **Lines 221-223**: StandardScaler transforms features to have mean=0 and std=1, which helps many ML algorithms perform better

---

## Section 5: Feature Importance Analysis

### Key Source Code (Lines 230-251)

```python
235:    # Line 235: Train Random Forest
236:    rf = RandomForestClassifier(n_estimators=100, random_state=42)
237:    rf.fit(X, y)
...
239:    # Line 239: Get feature importances
240:    importances = rf.feature_importances_
241:    indices = np.argsort(importances)[::-1]
```

### Program Output

```
================================================================================
                   FEATURE IMPORTANCE: Random Forest Analysis
================================================================================

Line 243: Feature Importance Ranking:
Line 246:   1. petal length (cm)   : 0.4361
Line 246:   2. petal width (cm)    : 0.4361
Line 246:   3. sepal length (cm)   : 0.1061
Line 246:   4. sepal width (cm)    : 0.0217
```

### Analysis

- **Lines 235-237**: Random Forest is trained on the full Iris dataset
- **Lines 239-241**: Feature importances are extracted and sorted
- **Line 246**: Results show that **petal dimensions** (length and width) are far more important (43.61% each) than sepal dimensions for classifying iris species
- This insight could be used for dimensionality reduction - we could potentially use just petal measurements for classification

---

## Key Takeaways

1. **Classification**: Scikit-learn makes it easy to train multiple classifiers and compare their performance
2. **Metrics**: Built-in functions provide comprehensive evaluation (accuracy, confusion matrix, classification report)
3. **Regression**: Linear models can effectively learn relationships between features and continuous targets
4. **Clustering**: Unsupervised learning algorithms like K-Means can discover patterns without labeled data
5. **Pipelines**: Chaining preprocessing and modeling steps ensures consistent data transformation
6. **Feature Analysis**: Tree-based models can reveal which features are most important for predictions

---

## Version Information

This code requires **Python 3.11+** for optimal compatibility with the inline script metadata format used for dependency management with `uv`.

**Last Updated**: December 2025
