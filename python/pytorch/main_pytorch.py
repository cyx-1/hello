#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "torch>=2.0.0",
#     "numpy>=1.24.0",
# ]
# ///

"""
Comprehensive PyTorch Demonstration
This script demonstrates key PyTorch features including:
- Tensor operations
- Neural network creation
- Model training
- Saving and loading models
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


def print_section(title):
    """Print formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print(f"{'=' * 60}")


def demonstrate_tensors():
    """Demonstrate basic tensor operations."""
    print_section("1. TENSOR BASICS")

    # Create tensors
    print("\n[Line 35] Creating tensors from Python lists:")
    t1 = torch.tensor([[1, 2], [3, 4]])
    print(f"t1 = {t1}")
    print(f"Shape: {t1.shape}, dtype: {t1.dtype}")

    print("\n[Line 41] Creating tensors with specific functions:")
    zeros = torch.zeros(2, 3)
    ones = torch.ones(2, 3)
    random = torch.rand(2, 3)
    print(f"Zeros:\n{zeros}")
    print(f"Ones:\n{ones}")
    print(f"Random:\n{random}")

    # Tensor operations
    print("\n[Line 51] Tensor arithmetic operations:")
    a = torch.tensor([1.0, 2.0, 3.0])
    b = torch.tensor([4.0, 5.0, 6.0])
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a + b = {a + b}")
    print(f"a * b = {a * b}")
    print(f"a @ b (dot product) = {a @ b}")

    # Matrix operations
    print("\n[Line 62] Matrix multiplication:")
    m1 = torch.randn(2, 3)
    m2 = torch.randn(3, 4)
    result = torch.matmul(m1, m2)
    print(f"m1 shape: {m1.shape}")
    print(f"m2 shape: {m2.shape}")
    print(f"m1 @ m2 shape: {result.shape}")

    # Reshaping
    print("\n[Line 72] Reshaping tensors:")
    original = torch.arange(12)
    reshaped = original.view(3, 4)
    print(f"Original: {original}")
    print(f"Reshaped to 3x4:\n{reshaped}")

    # Device management
    print("\n[Line 80] Device management:")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    tensor_on_device = torch.ones(2, 2).to(device)
    print(f"Tensor on {device}: {tensor_on_device}")


def demonstrate_autograd():
    """Demonstrate automatic differentiation."""
    print_section("2. AUTOMATIC DIFFERENTIATION (AUTOGRAD)")

    print("\n[Line 92] Computing gradients:")
    x = torch.tensor([2.0], requires_grad=True)
    y = torch.tensor([3.0], requires_grad=True)

    # Compute z = x^2 + y^3
    z = x**2 + y**3
    print(f"x = {x.item()}, y = {y.item()}")
    print(f"z = x^2 + y^3 = {z.item()}")

    # Compute gradients
    z.backward()
    print(f"dz/dx = 2x = {x.grad.item()}")
    print(f"dz/dy = 3y^2 = {y.grad.item()}")

    # More complex example
    print("\n[Line 108] Gradient descent example:")
    x = torch.tensor([1.0], requires_grad=True)
    learning_rate = 0.1

    for i in range(5):
        # Function: f(x) = (x - 3)^2
        loss = (x - 3) ** 2

        # Compute gradient
        loss.backward()

        # Update x
        with torch.no_grad():
            x -= learning_rate * x.grad
            x.grad.zero_()

        print(f"Step {i + 1}: x = {x.item():.4f}, loss = {loss.item():.4f}")


class SimpleNet(nn.Module):
    """Simple neural network for demonstration."""

    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


def demonstrate_neural_network():
    """Demonstrate neural network creation and usage."""
    print_section("3. NEURAL NETWORKS")

    print("\n[Line 148] Creating a simple neural network:")
    model = SimpleNet(input_size=10, hidden_size=20, output_size=2)
    print(model)

    print("\n[Line 153] Model parameters:")
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Total parameters: {total_params}")
    for name, param in model.named_parameters():
        print(f"{name}: {param.shape}")

    print("\n[Line 160] Forward pass:")
    x = torch.randn(5, 10)  # Batch of 5 samples, 10 features each
    output = model(x)
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Output:\n{output}")


def train_model():
    """Demonstrate model training on a simple dataset."""
    print_section("4. MODEL TRAINING")

    # Generate synthetic data for binary classification
    print("\n[Line 174] Generating synthetic dataset:")
    np.random.seed(42)
    torch.manual_seed(42)

    # Create data: y = 1 if x1 + x2 > 0, else 0
    n_samples = 100
    X = torch.randn(n_samples, 2)
    y = (X[:, 0] + X[:, 1] > 0).long()
    print(f"Dataset size: {n_samples} samples")
    print(f"Feature shape: {X.shape}")
    print(f"Label distribution: {torch.bincount(y)}")

    # Create model
    print("\n[Line 188] Creating model for binary classification:")
    model = SimpleNet(input_size=2, hidden_size=10, output_size=2)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Training loop
    print("\n[Line 195] Training for 100 epochs:")
    n_epochs = 100
    for epoch in range(n_epochs):
        # Forward pass
        outputs = model(X)
        loss = criterion(outputs, y)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Print progress
        if (epoch + 1) % 20 == 0:
            # Calculate accuracy
            _, predicted = torch.max(outputs, 1)
            accuracy = (predicted == y).float().mean()
            print(
                f"Epoch [{epoch + 1}/{n_epochs}], Loss: {loss.item():.4f}, Accuracy: {accuracy.item():.4f}"
            )

    # Final evaluation
    print("\n[Line 216] Final evaluation:")
    with torch.no_grad():
        outputs = model(X)
        _, predicted = torch.max(outputs, 1)
        accuracy = (predicted == y).float().mean()
        print(f"Final accuracy: {accuracy.item():.4f}")

    return model


def demonstrate_save_load(model):
    """Demonstrate saving and loading models."""
    print_section("5. SAVING AND LOADING MODELS")

    print("\n[Line 231] Saving model state:")
    save_path = "model_checkpoint.pth"
    torch.save(model.state_dict(), save_path)
    print(f"Model saved to {save_path}")

    print("\n[Line 236] Loading model state:")
    new_model = SimpleNet(input_size=2, hidden_size=10, output_size=2)
    new_model.load_state_dict(torch.load(save_path))
    new_model.eval()
    print("Model loaded successfully")

    print("\n[Line 242] Verifying loaded model:")
    test_input = torch.randn(3, 2)
    with torch.no_grad():
        original_output = model(test_input)
        loaded_output = new_model(test_input)
    print(f"Outputs match: {torch.allclose(original_output, loaded_output)}")


def demonstrate_advanced_features():
    """Demonstrate advanced PyTorch features."""
    print_section("6. ADVANCED FEATURES")

    print("\n[Line 254] Custom loss function:")

    class CustomMSELoss(nn.Module):
        def forward(self, pred, target):
            return torch.mean((pred - target) ** 2)

    custom_loss = CustomMSELoss()
    pred = torch.tensor([1.0, 2.0, 3.0])
    target = torch.tensor([1.5, 2.5, 3.5])
    loss_value = custom_loss(pred, target)
    print(f"Custom MSE Loss: {loss_value.item():.4f}")

    print("\n[Line 266] Using different optimizers:")
    model = SimpleNet(2, 10, 2)

    sgd = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    adam = optim.Adam(model.parameters(), lr=0.001)

    print(f"SGD optimizer: {sgd}")
    print(f"Adam optimizer: {adam}")

    print("\n[Line 276] Learning rate scheduler:")
    scheduler = optim.lr_scheduler.StepLR(sgd, step_size=10, gamma=0.1)
    print(f"Initial LR: {sgd.param_groups[0]['lr']}")
    for i in range(3):
        scheduler.step()
        print(f"After {(i + 1) * 10} steps: LR = {sgd.param_groups[0]['lr']}")


def main():
    """Run all demonstrations."""
    print("=" * 60)
    print("PyTorch Comprehensive Demonstration")
    print(f"PyTorch version: {torch.__version__}")
    print("=" * 60)

    demonstrate_tensors()
    demonstrate_autograd()
    demonstrate_neural_network()
    trained_model = train_model()
    demonstrate_save_load(trained_model)
    demonstrate_advanced_features()

    print("\n" + "=" * 60)
    print("Demonstration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
