# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "tensorflow>=2.15.0",
#     "numpy>=1.24.0",
# ]
# ///
"""
TensorFlow Example: Comprehensive Deep Learning Framework Demonstration

This example showcases key TensorFlow concepts:
1. Tensor operations and manipulation
2. Building neural networks with Sequential and Functional API
3. Model training with callbacks
4. Model evaluation and prediction
5. Working with different layer types
6. Custom training loops
7. Model saving and loading
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

# Set random seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Suppress TensorFlow warnings for cleaner output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print(f"TensorFlow Version: {tf.__version__}")
print(f"Keras Version: {keras.__version__}")
print(f"GPU Available: {len(tf.config.list_physical_devices('GPU')) > 0}")
print()


# Example 1: Basic Tensor Operations
print("=" * 70)
print("Example 1: Basic Tensor Operations")
print("=" * 70)

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

print("\nTensor Transpose:")
print(tf.transpose(tensor_a))

# Reshaping
tensor_c = tf.constant([1, 2, 3, 4, 5, 6])
print(f"\nOriginal tensor: {tensor_c}")
print(f"Reshaped to (2, 3):\n{tf.reshape(tensor_c, (2, 3))}")
print(f"Reshaped to (3, 2):\n{tf.reshape(tensor_c, (3, 2))}")


# Example 2: Creating a Simple Dataset
print("\n" + "=" * 70)
print("Example 2: Creating a Dataset for Classification")
print("=" * 70)

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

print(f"\nTraining set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")
print(f"Features: {X_train.shape[1]}")
print(f"First 5 training samples:\n{X_train[:5]}")
print(f"First 5 training labels: {y_train[:5]}")


# Example 3: Building a Neural Network with Sequential API
print("\n" + "=" * 70)
print("Example 3: Building a Neural Network (Sequential API)")
print("=" * 70)

model = keras.Sequential([
    layers.Input(shape=(2,)),
    layers.Dense(16, activation='relu', name='hidden_1'),
    layers.Dense(8, activation='relu', name='hidden_2'),
    layers.Dense(1, activation='sigmoid', name='output')
], name='binary_classifier')

print("\nModel Architecture:")
model.summary()

print("\nLayer details:")
for i, layer in enumerate(model.layers):
    print(f"  Layer {i}: {layer.name} - {layer.__class__.__name__}")
    if hasattr(layer, 'units'):
        print(f"    Units: {layer.units}")
    if hasattr(layer, 'activation') and layer.activation is not None:
        print(f"    Activation: {layer.activation.__name__}")


# Example 4: Compiling and Training the Model
print("\n" + "=" * 70)
print("Example 4: Compiling and Training the Model")
print("=" * 70)

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.01),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("\nModel compiled with:")
print("  Optimizer: Adam (lr=0.01)")
print("  Loss: binary_crossentropy")
print("  Metrics: accuracy")

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

print("\nTraining the model...")
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping, reduce_lr],
    verbose=0  # Set to 1 to see training progress
)

print("\nTraining completed!")
print(f"  Total epochs run: {len(history.history['loss'])}")
print(f"  Final training loss: {history.history['loss'][-1]:.4f}")
print(f"  Final training accuracy: {history.history['accuracy'][-1]:.4f}")
print(f"  Final validation loss: {history.history['val_loss'][-1]:.4f}")
print(f"  Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")


# Example 5: Model Evaluation and Prediction
print("\n" + "=" * 70)
print("Example 5: Model Evaluation and Prediction")
print("=" * 70)

# Evaluate on test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print("\nTest Set Evaluation:")
print(f"  Test Loss: {test_loss:.4f}")
print(f"  Test Accuracy: {test_accuracy:.4f}")

# Make predictions
predictions = model.predict(X_test[:5], verbose=0)
print("\nPredictions for first 5 test samples:")
for i in range(5):
    predicted_class = 1 if predictions[i][0] > 0.5 else 0
    actual_class = int(y_test[i])
    confidence = predictions[i][0] if predicted_class == 1 else 1 - predictions[i][0]
    print(f"  Sample {i+1}: Predicted={predicted_class} (confidence={confidence:.3f}), Actual={actual_class}")


# Example 6: Building a Model with Functional API
print("\n" + "=" * 70)
print("Example 6: Building a Model with Functional API")
print("=" * 70)

# Functional API allows for more complex architectures
inputs = keras.Input(shape=(2,), name='input')
x = layers.Dense(16, activation='relu', name='dense_1')(inputs)
x = layers.Dropout(0.3, name='dropout_1')(x)
x = layers.Dense(8, activation='relu', name='dense_2')(x)
x = layers.Dropout(0.2, name='dropout_2')(x)
outputs = layers.Dense(1, activation='sigmoid', name='output')(x)

functional_model = keras.Model(inputs=inputs, outputs=outputs, name='functional_classifier')

print("\nFunctional Model Architecture:")
functional_model.summary()

functional_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("\nTraining functional model (with dropout)...")
history_func = functional_model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=32,
    validation_split=0.2,
    verbose=0
)

test_loss_func, test_accuracy_func = functional_model.evaluate(X_test, y_test, verbose=0)
print(f"\nFunctional Model Test Accuracy: {test_accuracy_func:.4f}")


# Example 7: Working with Multi-class Classification
print("\n" + "=" * 70)
print("Example 7: Multi-class Classification with Fashion MNIST")
print("=" * 70)

# Load Fashion MNIST dataset
print("\nLoading Fashion MNIST dataset...")
(X_train_mnist, y_train_mnist), (X_test_mnist, y_test_mnist) = keras.datasets.fashion_mnist.load_data()

# Normalize pixel values to [0, 1]
X_train_mnist = X_train_mnist.astype('float32') / 255.0
X_test_mnist = X_test_mnist.astype('float32') / 255.0

# Reshape for dense layers (flatten)
X_train_mnist_flat = X_train_mnist.reshape(-1, 28 * 28)
X_test_mnist_flat = X_test_mnist.reshape(-1, 28 * 28)

print("\nDataset loaded:")
print(f"  Training samples: {X_train_mnist.shape[0]}")
print(f"  Test samples: {X_test_mnist.shape[0]}")
print(f"  Image shape: {X_train_mnist.shape[1:]} (28x28 pixels)")
print(f"  Number of classes: {len(np.unique(y_train_mnist))}")
print(f"  Flattened input shape: {X_train_mnist_flat.shape[1]} features")

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Build multi-class classification model
mnist_model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')  # 10 classes
], name='fashion_mnist_classifier')

print("\nFashion MNIST Model Architecture:")
mnist_model.summary()

mnist_model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',  # For integer labels
    metrics=['accuracy']
)

print("\nTraining on Fashion MNIST (5 epochs for demonstration)...")
# Using only a subset for faster demonstration
mnist_history = mnist_model.fit(
    X_train_mnist_flat[:10000],
    y_train_mnist[:10000],
    epochs=5,
    batch_size=128,
    validation_split=0.2,
    verbose=1
)

# Evaluate
test_loss_mnist, test_accuracy_mnist = mnist_model.evaluate(
    X_test_mnist_flat, y_test_mnist, verbose=0
)
print(f"\nFashion MNIST Test Accuracy: {test_accuracy_mnist:.4f}")

# Make predictions
predictions_mnist = mnist_model.predict(X_test_mnist_flat[:5], verbose=0)
print("\nPredictions for first 5 test images:")
for i in range(5):
    predicted_class = np.argmax(predictions_mnist[i])
    actual_class = y_test_mnist[i]
    confidence = predictions_mnist[i][predicted_class]
    print(f"  Image {i+1}: Predicted={class_names[predicted_class]} (confidence={confidence:.3f}), "
          f"Actual={class_names[actual_class]}")


# Example 8: Custom Training Loop
print("\n" + "=" * 70)
print("Example 8: Custom Training Loop")
print("=" * 70)

# Create a simple model
custom_model = keras.Sequential([
    layers.Dense(16, activation='relu', input_shape=(2,)),
    layers.Dense(1, activation='sigmoid')
])

# Define optimizer and loss
optimizer = keras.optimizers.SGD(learning_rate=0.01)
loss_fn = keras.losses.BinaryCrossentropy()

# Metrics
train_acc_metric = keras.metrics.BinaryAccuracy()

print("\nRunning custom training loop (5 epochs)...")

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


# Example 9: Model Saving and Loading
print("\n" + "=" * 70)
print("Example 9: Model Saving and Loading")
print("=" * 70)

# Save model in Keras format
save_path = '/tmp/my_model.keras'
model.save(save_path)
print(f"\nModel saved to: {save_path}")

# Load the model
loaded_model = keras.models.load_model(save_path)
print("Model loaded successfully!")

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
print(f"\nModel weights saved to: {weights_path}")

# Also demonstrate export for TFLite/TFServing
export_path = '/tmp/my_model_export'
model.export(export_path)
print(f"Model exported for TFLite/TFServing to: {export_path}")


# Example 10: Working with Different Layer Types
print("\n" + "=" * 70)
print("Example 10: Working with Different Layer Types")
print("=" * 70)

# Demonstrate various layer types
demo_model = keras.Sequential([
    layers.Input(shape=(10,)),
    layers.Dense(64, activation='relu', name='dense_layer'),
    layers.BatchNormalization(name='batch_norm'),
    layers.Dropout(0.5, name='dropout'),
    layers.Dense(32, activation='relu', name='dense_2'),
    layers.Dense(1, activation='sigmoid', name='output')
], name='layer_demo_model')

print("\nModel with various layer types:")
demo_model.summary()

print("\nLayer type descriptions:")
print("  Dense: Fully connected layer with weights and biases")
print("  BatchNormalization: Normalizes activations for faster training")
print("  Dropout: Randomly drops units during training to prevent overfitting")


# Summary
print("\n" + "=" * 70)
print("Summary: TensorFlow Key Features Demonstrated")
print("=" * 70)
print("""
1. Tensor Operations: Created and manipulated tensors with various operations
2. Dataset Creation: Generated synthetic data for classification tasks
3. Sequential API: Built neural networks with simple sequential architecture
4. Model Training: Trained models with callbacks (early stopping, learning rate reduction)
5. Model Evaluation: Evaluated model performance and made predictions
6. Functional API: Created more complex models with dropout layers
7. Multi-class Classification: Worked with Fashion MNIST dataset (10 classes)
8. Custom Training Loop: Implemented custom training with GradientTape
9. Model Persistence: Saved and loaded models in SavedModel format
10. Layer Types: Demonstrated Dense, Dropout, and BatchNormalization layers

TensorFlow is a comprehensive deep learning framework that provides:
- High-level APIs (Keras) for quick model development
- Low-level APIs for custom implementations
- Excellent performance on CPUs, GPUs, and TPUs
- Production-ready deployment capabilities
- Extensive ecosystem and community support

Note: This example requires TensorFlow >= 2.15.0
""")
