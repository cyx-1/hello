# TensorFlow Python Example

A comprehensive demonstration of TensorFlow, the leading deep learning framework developed by Google. This example showcases core concepts including tensor operations, neural network creation, model training, and deployment.

## Requirements

**Python Version**: >= 3.9
**TensorFlow Version**: >= 2.15.0 (This example uses TensorFlow 2.20.0 with Keras 3.12.0)

## Running the Example

```bash
uv run main_tensorflow.py
```

## Overview

This example demonstrates 10 key TensorFlow concepts:

1. **Basic Tensor Operations** - Creating and manipulating tensors
2. **Dataset Creation** - Generating synthetic data for classification
3. **Sequential API** - Building neural networks with simple architecture
4. **Model Training** - Training with callbacks and early stopping
5. **Model Evaluation** - Evaluating performance and making predictions
6. **Functional API** - Creating complex models with dropout layers
7. **Multi-class Classification** - Working with Fashion MNIST dataset
8. **Custom Training Loop** - Low-level training with GradientTape
9. **Model Persistence** - Saving and loading models
10. **Layer Types** - Different layer types and their purposes

---

## Example 1: Basic Tensor Operations

### Source Code (Lines 46-74)

```python
# Create tensors
tensor_a = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
tensor_b = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)

print("\nTensor A:")
print(tensor_a)
print(f"Shape: {tensor_a.shape}, Dtype: {tensor_a.dtype}")

print("\nTensor B:")
print(tensor_b)

# Basic operations
print("\nTensor Addition (A + B):")
print(tf.add(tensor_a, tensor_b))

print("\nTensor Multiplication (A * B, element-wise):")
print(tf.multiply(tensor_a, tensor_b))

print("\nMatrix Multiplication (A @ B):")
print(tf.matmul(tensor_a, tensor_b))
```

### Output

```
Tensor A:
tf.Tensor(
[[1. 2.]
 [3. 4.]], shape=(2, 2), dtype=float32)
Shape: (2, 2), Dtype: <dtype: 'float32'>

Tensor Addition (A + B):
tf.Tensor(
[[ 6.  8.]
 [10. 12.]], shape=(2, 2), dtype=float32)

Matrix Multiplication (A @ B):
tf.Tensor(
[[19. 22.]
 [43. 50.]], shape=(2, 2), dtype=float32)
```

### Annotations

- **Line 46-47**: Creates 2x2 tensors with float32 data type
- **Line 61**: Demonstrates element-wise addition using `tf.add()`
- **Line 67**: Shows element-wise multiplication (Hadamard product)
- **Line 70**: Performs matrix multiplication (dot product) - notice how [[1,2],[3,4]] @ [[5,6],[7,8]] = [[19,22],[43,50]]

---

## Example 2: Creating a Dataset for Classification

### Source Code (Lines 82-105)

```python
# Generate synthetic data for binary classification
np.random.seed(42)
n_samples = 1000

# Create two classes with different distributions
class_0 = np.random.randn(n_samples // 2, 2) + np.array([2, 2])
class_1 = np.random.randn(n_samples // 2, 2) + np.array([-2, -2])

X = np.vstack([class_0, class_1]).astype(np.float32)
y = np.hstack([np.zeros(n_samples // 2), np.ones(n_samples // 2)]).astype(np.float32)

# Shuffle the data
indices = np.random.permutation(n_samples)
X = X[indices]
y = y[indices]

# Split into train and test sets
split_idx = int(0.8 * n_samples)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]
```

### Output

```
Training set: 800 samples
Test set: 200 samples
Features: 2
First 5 training samples:
[[-0.9759375  -1.4074731 ]
 [-0.3387408  -2.4570963 ]
 [ 0.39251676  2.184634  ]
 [-0.9239929  -1.9786884 ]
 [ 1.2436492   0.5777463 ]]
First 5 training labels: [1. 1. 0. 1. 0.]
```

### Annotations

- **Lines 87-88**: Creates two Gaussian distributions centered at (2,2) and (-2,-2) for binary classification
- **Line 90**: Stacks both classes vertically to create feature matrix X
- **Line 94-95**: Shuffles data to ensure random distribution across batches
- **Output**: Shows the 80/20 train-test split with 2 features per sample

---

## Example 3: Building a Neural Network (Sequential API)

### Source Code (Lines 112-121)

```python
model = keras.Sequential([
    layers.Input(shape=(2,)),
    layers.Dense(16, activation='relu', name='hidden_1'),
    layers.Dense(8, activation='relu', name='hidden_2'),
    layers.Dense(1, activation='sigmoid', name='output')
], name='binary_classifier')

print("\nModel Architecture:")
model.summary()
```

### Output

```
Model Architecture:
Model: "binary_classifier"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ hidden_1 (Dense)                │ (None, 16)             │            48 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ hidden_2 (Dense)                │ (None, 8)              │           136 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ output (Dense)                  │ (None, 1)              │             9 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 193 (772.00 B)
 Trainable params: 193 (772.00 B)
 Non-trainable params: 0 (0.00 B)

Layer details:
  Layer 0: hidden_1 - Dense
    Units: 16
    Activation: relu
  Layer 1: hidden_2 - Dense
    Units: 8
    Activation: relu
  Layer 2: output - Dense
    Units: 1
    Activation: sigmoid
```

### Annotations

- **Line 113**: Input layer expects 2 features (our X,Y coordinates)
- **Line 114**: First hidden layer with 16 neurons and ReLU activation (2 inputs × 16 neurons + 16 biases = 48 params)
- **Line 115**: Second hidden layer with 8 neurons (16 inputs × 8 neurons + 8 biases = 136 params)
- **Line 116**: Output layer with sigmoid activation for binary classification (8 inputs × 1 neuron + 1 bias = 9 params)
- **Output**: Total of 193 trainable parameters - very lightweight network!

---

## Example 4: Compiling and Training the Model

### Source Code (Lines 138-156)

```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.01),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Create callbacks
early_stopping = keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True,
    verbose=1
)

reduce_lr = keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=5,
    verbose=1,
    min_lr=0.0001
)

history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping, reduce_lr],
    verbose=0
)
```

### Output

```
Model compiled with:
  Optimizer: Adam (lr=0.01)
  Loss: binary_crossentropy
  Metrics: accuracy

Training the model...

Epoch 26: ReduceLROnPlateau reducing learning rate to 0.004999999888241291.

Epoch 32: ReduceLROnPlateau reducing learning rate to 0.0024999999441206455.

Epoch 37: ReduceLROnPlateau reducing learning rate to 0.0012499999720603228.

Epoch 45: ReduceLROnPlateau reducing learning rate to 0.0006249999860301614.

Epoch 50: ReduceLROnPlateau reducing learning rate to 0.0003124999930150807.
Restoring model weights from the end of the best epoch: 50.

Training completed!
  Total epochs run: 50
  Final training loss: 0.0018
  Final training accuracy: 1.0000
  Final validation loss: 0.0002
  Final validation accuracy: 1.0000
```

### Annotations

- **Line 139**: Adam optimizer with initial learning rate of 0.01
- **Line 145-147**: Early stopping monitors validation loss and stops if no improvement after 10 epochs
- **Line 153-155**: Learning rate reduction cuts LR in half when validation loss plateaus
- **Output**: The learning rate was automatically reduced 5 times (at epochs 26, 32, 37, 45, 50) as training converged
- **Output**: Perfect accuracy (1.0000) achieved on both training and validation sets, indicating the problem is linearly separable

---

## Example 5: Model Evaluation and Prediction

### Source Code (Lines 175-189)

```python
# Evaluate on test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTest Set Evaluation:")
print(f"  Test Loss: {test_loss:.4f}")
print(f"  Test Accuracy: {test_accuracy:.4f}")

# Make predictions
predictions = model.predict(X_test[:5], verbose=0)
print(f"\nPredictions for first 5 test samples:")
for i in range(5):
    predicted_class = 1 if predictions[i][0] > 0.5 else 0
    actual_class = int(y_test[i])
    confidence = predictions[i][0] if predicted_class == 1 else 1 - predictions[i][0]
    print(f"  Sample {i+1}: Predicted={predicted_class} (confidence={confidence:.3f}), Actual={actual_class}")
```

### Output

```
Test Set Evaluation:
  Test Loss: 0.0000
  Test Accuracy: 1.0000

Predictions for first 5 test samples:
  Sample 1: Predicted=1 (confidence=1.000), Actual=1
  Sample 2: Predicted=1 (confidence=1.000), Actual=1
  Sample 3: Predicted=1 (confidence=1.000), Actual=1
  Sample 4: Predicted=0 (confidence=1.000), Actual=0
  Sample 5: Predicted=1 (confidence=1.000), Actual=1
```

### Annotations

- **Line 176**: `evaluate()` returns both loss and accuracy metrics on the test set
- **Line 182**: `predict()` returns raw probabilities from the sigmoid output layer
- **Line 185**: Confidence is calculated from the probability - for class 1, it's the raw value; for class 0, it's 1 - probability
- **Output**: All 5 predictions are correct with 100% confidence, demonstrating the model's strong performance

---

## Example 6: Building a Model with Functional API

### Source Code (Lines 197-209)

```python
# Functional API allows for more complex architectures
inputs = keras.Input(shape=(2,), name='input')
x = layers.Dense(16, activation='relu', name='dense_1')(inputs)
x = layers.Dropout(0.3, name='dropout_1')(x)
x = layers.Dense(8, activation='relu', name='dense_2')(x)
x = layers.Dropout(0.2, name='dropout_2')(x)
outputs = layers.Dense(1, activation='sigmoid', name='output')(x)

functional_model = keras.Model(inputs=inputs, outputs=outputs, name='functional_classifier')
```

### Output

```
Functional Model Architecture:
Model: "functional_classifier"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ input (InputLayer)              │ (None, 2)              │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_1 (Dense)                 │ (None, 16)             │            48 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_1 (Dropout)             │ (None, 16)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 8)              │           136 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_2 (Dropout)             │ (None, 8)              │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ output (Dense)                  │ (None, 1)              │             9 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 193 (772.00 B)
 Trainable params: 193 (772.00 B)
 Non-trainable params: 0 (0.00 B)

Training functional model (with dropout)...

Functional Model Test Accuracy: 1.0000
```

### Annotations

- **Lines 198-203**: Functional API connects layers explicitly using function call syntax: `layer(input_tensor)`
- **Line 200, 202**: Dropout layers randomly zero out 30% and 20% of neurons during training to prevent overfitting
- **Line 205**: `keras.Model()` creates a model by specifying inputs and outputs
- **Output**: Dropout layers have 0 parameters - they only modify training behavior
- **Advantage**: Functional API allows for complex architectures like multi-input/output models, skip connections, etc.

---

## Example 7: Multi-class Classification with Fashion MNIST

### Source Code (Lines 231-241)

```python
# Load Fashion MNIST dataset
print("\nLoading Fashion MNIST dataset...")
(X_train_mnist, y_train_mnist), (X_test_mnist, y_test_mnist) = keras.datasets.fashion_mnist.load_data()

# Normalize pixel values to [0, 1]
X_train_mnist = X_train_mnist.astype('float32') / 255.0
X_test_mnist = X_test_mnist.astype('float32') / 255.0

# Reshape for dense layers (flatten)
X_train_mnist_flat = X_train_mnist.reshape(-1, 28 * 28)
X_test_mnist_flat = X_test_mnist.reshape(-1, 28 * 28)
```

### Source Code - Model (Lines 254-261)

```python
# Build multi-class classification model
mnist_model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')  # 10 classes
], name='fashion_mnist_classifier')
```

### Output

```
Dataset loaded:
  Training samples: 60000
  Test samples: 10000
  Image shape: (28, 28) (28x28 pixels)
  Number of classes: 10
  Flattened input shape: 784 features

Fashion MNIST Model Architecture:
Model: "fashion_mnist_classifier"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ dense (Dense)                   │ (None, 128)            │       100,480 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout (Dropout)               │ (None, 128)            │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_1 (Dense)                 │ (None, 64)             │         8,256 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_1 (Dropout)             │ (None, 64)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 10)             │           650 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 109,386 (427.29 KB)
 Trainable params: 109,386 (427.29 KB)
 Non-trainable params: 0 (0.00 B)

Fashion MNIST Test Accuracy: 0.8182

Predictions for first 5 test images:
  Image 1: Predicted=Ankle boot (confidence=0.811), Actual=Ankle boot
  Image 2: Predicted=Pullover (confidence=0.982), Actual=Pullover
  Image 3: Predicted=Trouser (confidence=1.000), Actual=Trouser
  Image 4: Predicted=Trouser (confidence=0.999), Actual=Trouser
  Image 5: Predicted=Shirt (confidence=0.468), Actual=Shirt
```

### Annotations

- **Line 237**: Normalizes pixel values from [0, 255] to [0, 1] for better training
- **Line 241**: Flattens 28×28 images into 784-dimensional vectors
- **Line 261**: Softmax activation for multi-class classification - outputs sum to 1.0
- **Line 269**: Uses `sparse_categorical_crossentropy` for integer labels (vs one-hot encoded)
- **Output**: 109K parameters - much larger than binary classifier due to 784 input features
- **Output**: Achieves 81.82% accuracy on Fashion MNIST, a realistic performance for this simple architecture

---

## Example 8: Custom Training Loop

### Source Code (Lines 338-368)

```python
# Custom training loop
epochs = 5
batch_size = 32

for epoch in range(epochs):
    # Shuffle training data
    indices = np.random.permutation(len(X_train))
    X_train_shuffled = X_train[indices]
    y_train_shuffled = y_train[indices]

    # Iterate over batches
    for step in range(0, len(X_train), batch_size):
        X_batch = X_train_shuffled[step:step + batch_size]
        y_batch = y_train_shuffled[step:step + batch_size]

        # Forward pass and compute loss
        with tf.GradientTape() as tape:
            predictions = custom_model(X_batch, training=True)
            loss_value = loss_fn(y_batch, predictions)

        # Backward pass
        gradients = tape.gradient(loss_value, custom_model.trainable_weights)
        optimizer.apply_gradients(zip(gradients, custom_model.trainable_weights))

        # Update metrics
        train_acc_metric.update_state(y_batch, predictions)

    # Display metrics at the end of each epoch
    train_acc = train_acc_metric.result()
    print(f"  Epoch {epoch + 1}/{epochs} - Loss: {loss_value:.4f}, Accuracy: {train_acc:.4f}")

    # Reset metrics
    train_acc_metric.reset_state()
```

### Output

```
Running custom training loop (5 epochs)...
  Epoch 1/5 - Loss: 0.4319, Accuracy: 0.6687
  Epoch 2/5 - Loss: 0.2917, Accuracy: 0.9975
  Epoch 3/5 - Loss: 0.2371, Accuracy: 0.9975
  Epoch 4/5 - Loss: 0.2201, Accuracy: 0.9987
  Epoch 5/5 - Loss: 0.1292, Accuracy: 0.9987
```

### Annotations

- **Line 344**: Shuffles data each epoch for better training
- **Line 354**: `GradientTape` records operations for automatic differentiation
- **Line 359**: Computes gradients of loss with respect to model weights
- **Line 360**: Applies gradients using the optimizer
- **Output**: Shows rapid improvement from 66.87% to 99.87% accuracy over 5 epochs
- **Output**: Loss decreases from 0.4319 to 0.1292, indicating effective learning
- **Use case**: Custom training loops are essential for advanced techniques like GANs, meta-learning, or research

---

## Example 9: Model Saving and Loading

### Source Code (Lines 375-402)

```python
# Save model in Keras format
save_path = '/tmp/my_model.keras'
model.save(save_path)
print(f"\nModel saved to: {save_path}")

# Load the model
loaded_model = keras.models.load_model(save_path)
print(f"Model loaded successfully!")

# Verify loaded model works
loaded_predictions = loaded_model.predict(X_test[:3], verbose=0)
original_predictions = model.predict(X_test[:3], verbose=0)

print("\nVerifying loaded model predictions match original:")
for i in range(3):
    print(f"  Sample {i+1}: Original={original_predictions[i][0]:.4f}, "
          f"Loaded={loaded_predictions[i][0]:.4f}, "
          f"Match={np.allclose(original_predictions[i], loaded_predictions[i])}")

# Save weights only
weights_path = '/tmp/my_model_weights.weights.h5'
model.save_weights(weights_path)

# Also demonstrate export for TFLite/TFServing
export_path = '/tmp/my_model_export'
model.export(export_path)
```

### Output

```
Model saved to: /tmp/my_model.keras
Model loaded successfully!

Verifying loaded model predictions match original:
  Sample 1: Original=1.0000, Loaded=1.0000, Match=True
  Sample 2: Original=1.0000, Loaded=1.0000, Match=True
  Sample 3: Original=0.9996, Loaded=0.9996, Match=True

Model weights saved to: /tmp/my_model_weights.weights.h5
Model exported for TFLite/TFServing to: /tmp/my_model_export
```

### Annotations

- **Line 377**: `.keras` format is the native Keras 3 format (recommended over `.h5`)
- **Line 381**: `load_model()` reconstructs the entire model including architecture, weights, and optimizer state
- **Line 385-392**: Verification confirms loaded model produces identical predictions
- **Line 396**: Saving weights only (useful when you want to reuse architecture with different weights)
- **Line 401**: `export()` creates a SavedModel format compatible with TensorFlow Serving, TFLite, and TensorFlow.js
- **Use case**: SavedModel format is production-ready for deployment in various environments

---

## Example 10: Working with Different Layer Types

### Source Code (Lines 410-421)

```python
# Demonstrate various layer types
demo_model = keras.Sequential([
    layers.Input(shape=(10,)),
    layers.Dense(64, activation='relu', name='dense_layer'),
    layers.BatchNormalization(name='batch_norm'),
    layers.Dropout(0.5, name='dropout'),
    layers.Dense(32, activation='relu', name='dense_2'),
    layers.Dense(1, activation='sigmoid', name='output')
], name='layer_demo_model')
```

### Output

```
Model with various layer types:
Model: "layer_demo_model"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ dense_layer (Dense)             │ (None, 64)             │           704 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_norm (BatchNormalization) │ (None, 64)             │           256 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout (Dropout)               │ (None, 64)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 32)             │         2,080 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ output (Dense)                  │ (None, 1)              │            33 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 3,073 (12.00 KB)
 Trainable params: 2,945 (11.50 KB)
 Non-trainable params: 128 (512.00 B)

Layer type descriptions:
  Dense: Fully connected layer with weights and biases
  BatchNormalization: Normalizes activations for faster training
  Dropout: Randomly drops units during training to prevent overfitting
```

### Annotations

- **Line 414**: `BatchNormalization` normalizes the activations and has 256 parameters (64 × 4: gamma, beta, moving_mean, moving_variance)
- **Line 415**: `Dropout(0.5)` randomly zeros out 50% of neurons during training
- **Output**: Notice 128 non-trainable params - these are BatchNorm's moving statistics
- **Output**: Total trainable params = 2,945 (excludes the 128 non-trainable BatchNorm statistics)
- **Key insight**: BatchNorm accelerates training and can improve generalization; Dropout prevents overfitting

---

## Summary

This example demonstrates TensorFlow's comprehensive capabilities:

### Core Features Covered
- ✅ Tensor operations and manipulations
- ✅ Binary and multi-class classification
- ✅ Sequential and Functional API
- ✅ Training callbacks (EarlyStopping, ReduceLROnPlateau)
- ✅ Custom training loops with GradientTape
- ✅ Model persistence (.keras, weights, SavedModel)
- ✅ Various layer types (Dense, Dropout, BatchNormalization)

### Performance Highlights
- Binary classifier: 100% test accuracy (simple linearly separable data)
- Fashion MNIST: 81.82% test accuracy with basic architecture
- Custom training loop: 99.87% accuracy after 5 epochs

### Production Ready
- Multiple save formats for different deployment scenarios
- TensorFlow Serving export for production APIs
- Comprehensive evaluation and prediction capabilities

### Version Information
**TensorFlow**: 2.20.0
**Keras**: 3.12.0
**Python**: 3.11+

---

## Key Takeaways

1. **High-level API (Keras)**: Provides quick model development with Sequential and Functional APIs
2. **Low-level API (GradientTape)**: Enables custom training loops for research and advanced use cases
3. **Callbacks**: Built-in tools like early stopping and learning rate scheduling improve training
4. **Model Persistence**: Multiple formats (.keras, weights, SavedModel) for different use cases
5. **Performance**: Excellent on CPUs, with GPU/TPU support for larger workloads
6. **Ecosystem**: Extensive support for deployment (TF Serving, TFLite, TF.js)

TensorFlow remains one of the most comprehensive deep learning frameworks, suitable for both research and production environments.
