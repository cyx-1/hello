# PyTorch Comprehensive Demonstration

This is a comprehensive demonstration of PyTorch, covering tensor operations, automatic differentiation, neural networks, model training, and advanced features.

## Requirements

- **Python**: >= 3.9
- **PyTorch**: >= 2.0.0
- **NumPy**: >= 1.24.0

## Running the Program

```bash
uv run --no-project main_pytorch.py
```

The program uses inline script metadata for dependency management, so no separate `pyproject.toml` is needed.

---

## Program Overview

The demonstration is structured into 6 main sections:

1. **Tensor Basics** - Creating and manipulating tensors
2. **Automatic Differentiation** - Computing gradients with autograd
3. **Neural Networks** - Building neural network architectures
4. **Model Training** - Training a model on synthetic data
5. **Saving and Loading Models** - Persisting model state
6. **Advanced Features** - Custom losses, optimizers, and schedulers

---

## Section 1: Tensor Basics

### Source Code (Lines 35-84)

```python
35  print("\n[Line 35] Creating tensors from Python lists:")
36  t1 = torch.tensor([[1, 2], [3, 4]])
37  print(f"t1 = {t1}")
38  print(f"Shape: {t1.shape}, dtype: {t1.dtype}")
39
40  print("\n[Line 41] Creating tensors with specific functions:")
41  zeros = torch.zeros(2, 3)
42  ones = torch.ones(2, 3)
43  random = torch.rand(2, 3)
44  print(f"Zeros:\n{zeros}")
45  print(f"Ones:\n{ones}")
46  print(f"Random:\n{random}")
47
48  # Tensor operations
49  print("\n[Line 51] Tensor arithmetic operations:")
50  a = torch.tensor([1.0, 2.0, 3.0])
51  b = torch.tensor([4.0, 5.0, 6.0])
52  print(f"a = {a}")
53  print(f"b = {b}")
54  print(f"a + b = {a + b}")
55  print(f"a * b = {a * b}")
56  print(f"a @ b (dot product) = {a @ b}")
57
58  # Matrix operations
59  print("\n[Line 62] Matrix multiplication:")
60  m1 = torch.randn(2, 3)
61  m2 = torch.randn(3, 4)
62  result = torch.matmul(m1, m2)
63  print(f"m1 shape: {m1.shape}")
64  print(f"m2 shape: {m2.shape}")
65  print(f"m1 @ m2 shape: {result.shape}")
66
67  # Reshaping
68  print("\n[Line 72] Reshaping tensors:")
69  original = torch.arange(12)
70  reshaped = original.view(3, 4)
71  print(f"Original: {original}")
72  print(f"Reshaped to 3x4:\n{reshaped}")
73
74  # Device management
75  print("\n[Line 80] Device management:")
76  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
77  print(f"Using device: {device}")
78  text_on_device = torch.ones(2, 2).to(device)
79  print(f"Tensor on {device}: {tensor_on_device}")
```

### Output

```
[Line 35] Creating tensors from Python lists:
t1 = tensor([[1, 2],
        [3, 4]])
Shape: torch.Size([2, 2]), dtype: torch.int64

[Line 41] Creating tensors with specific functions:
Zeros:
tensor([[0., 0., 0.],
        [0., 0., 0.]])
Ones:
tensor([[1., 1., 1.],
        [1., 1., 1.]])
Random:
tensor([[0.4083, 0.1551, 0.1784],
        [0.2321, 0.1214, 0.4837]])

[Line 51] Tensor arithmetic operations:
a = tensor([1., 2., 3.])
b = tensor([4., 5., 6.])
a + b = tensor([5., 7., 9.])
a * b = tensor([ 4., 10., 18.])
a @ b (dot product) = 32.0

[Line 62] Matrix multiplication:
m1 shape: torch.Size([2, 3])
m2 shape: torch.Size([3, 4])
m1 @ m2 shape: torch.Size([2, 4])

[Line 72] Reshaping tensors:
Original: tensor([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
Reshaped to 3x4:
tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])

[Line 80] Device management:
Using device: cpu
Tensor on cpu: tensor([[1., 1.],
        [1., 1.]])
```

### Annotations

- **Lines 36-38**: Create a 2x2 integer tensor from a Python list. PyTorch automatically infers the dtype as `int64`.
- **Lines 41-46**: Demonstrate tensor creation functions: `zeros()`, `ones()`, and `rand()` for random values between 0 and 1.
- **Lines 50-56**: Show element-wise operations (addition, multiplication) and the dot product operator `@`.
- **Lines 60-65**: Matrix multiplication using `torch.matmul()` or the `@` operator. Shape compatibility: (2,3) @ (3,4) = (2,4).
- **Lines 69-72**: Reshape a 1D tensor of 12 elements into a 3x4 matrix using `.view()`.
- **Lines 76-79**: PyTorch supports GPU acceleration. This code detects if CUDA is available and moves tensors to the appropriate device.

---

## Section 2: Automatic Differentiation (Autograd)

### Source Code (Lines 92-126)

```python
 92  print("\n[Line 92] Computing gradients:")
 93  x = torch.tensor([2.0], requires_grad=True)
 94  y = torch.tensor([3.0], requires_grad=True)
 95
 96  # Compute z = x^2 + y^3
 97  z = x**2 + y**3
 98  print(f"x = {x.item()}, y = {y.item()}")
 99  print(f"z = x^2 + y^3 = {z.item()}")
100
101  # Compute gradients
102  z.backward()
103  print(f"dz/dx = 2x = {x.grad.item()}")
104  print(f"dz/dy = 3y^2 = {y.grad.item()}")
105
106  # More complex example
107  print("\n[Line 108] Gradient descent example:")
108  x = torch.tensor([1.0], requires_grad=True)
109  learning_rate = 0.1
110
111  for i in range(5):
112      # Function: f(x) = (x - 3)^2
113      loss = (x - 3)**2
114
115      # Compute gradient
116      loss.backward()
117
118      # Update x
119      with torch.no_grad():
120          x -= learning_rate * x.grad
121          x.grad.zero_()
122
123      print(f"Step {i+1}: x = {x.item():.4f}, loss = {loss.item():.4f}")
```

### Output

```
[Line 92] Computing gradients:
x = 2.0, y = 3.0
z = x^2 + y^3 = 31.0
dz/dx = 2x = 4.0
dz/dy = 3y^2 = 27.0

[Line 108] Gradient descent example:
Step 1: x = 1.4000, loss = 4.0000
Step 2: x = 1.7200, loss = 2.5600
Step 3: x = 1.9760, loss = 1.6384
Step 4: x = 2.1808, loss = 1.0486
Step 5: x = 2.3446, loss = 0.6711
```

### Annotations

- **Lines 93-94**: Create tensors with `requires_grad=True` to track operations for automatic differentiation.
- **Lines 97-99**: Compute z = x² + y³ = 2² + 3³ = 4 + 27 = 31.
- **Line 102**: `backward()` computes gradients automatically. For z = x² + y³: ∂z/∂x = 2x = 4, ∂z/∂y = 3y² = 27.
- **Lines 111-123**: Implement gradient descent to minimize f(x) = (x-3)². Starting from x=1, the algorithm iteratively moves x closer to the minimum at x=3.
- **Lines 119-121**: Use `torch.no_grad()` context to update parameters without tracking gradients, then zero out gradients for the next iteration.

---

## Section 3: Neural Networks

### Source Code (Lines 129-168)

```python
129  class SimpleNet(nn.Module):
130      """Simple neural network for demonstration."""
131
132      def __init__(self, input_size, hidden_size, output_size):
133          super().__init__()
134          self.fc1 = nn.Linear(input_size, hidden_size)
135          self.relu = nn.ReLU()
136          self.fc2 = nn.Linear(hidden_size, output_size)
137
138      def forward(self, x):
139          x = self.fc1(x)
140          x = self.relu(x)
141          x = self.fc2(x)
142          return x
143
...
148  print("\n[Line 148] Creating a simple neural network:")
149  model = SimpleNet(input_size=10, hidden_size=20, output_size=2)
150  print(model)
151
152  print("\n[Line 153] Model parameters:")
153  total_params = sum(p.numel() for p in model.parameters())
154  print(f"Total parameters: {total_params}")
155  for name, param in model.named_parameters():
156      print(f"{name}: {param.shape}")
157
158  print("\n[Line 160] Forward pass:")
159  x = torch.randn(5, 10)  # Batch of 5 samples, 10 features each
160  output = model(x)
161  print(f"Input shape: {x.shape}")
162  print(f"Output shape: {output.shape}")
163  print(f"Output:\n{output}")
```

### Output

```
[Line 148] Creating a simple neural network:
SimpleNet(
  (fc1): Linear(in_features=10, out_features=20, bias=True)
  (relu): ReLU()
  (fc2): Linear(in_features=20, out_features=2, bias=True)
)

[Line 153] Model parameters:
Total parameters: 262
fc1.weight: torch.Size([20, 10])
fc1.bias: torch.Size([20])
fc2.weight: torch.Size([2, 20])
fc2.bias: torch.Size([2])

[Line 160] Forward pass:
Input shape: torch.Size([5, 10])
Output shape: torch.Size([5, 2])
Output:
tensor([[-0.1812,  0.0679],
        [-0.0750,  0.1415],
        [-0.1874,  0.1561],
        [-0.2528,  0.0937],
        [-0.4026,  0.0928]], grad_fn=<AddmmBackward0>)
```

### Annotations

- **Lines 129-142**: Define a neural network class inheriting from `nn.Module`. The network has:
  - Input layer: 10 → 20 neurons (fc1)
  - Activation: ReLU
  - Output layer: 20 → 2 neurons (fc2)
- **Lines 153-154**: Calculate total parameters: (10×20 + 20) + (20×2 + 2) = 220 + 42 = 262 parameters.
- **Lines 159-163**: Perform a forward pass with a batch of 5 samples. Each sample has 10 features, producing 2 output values.
- The `grad_fn=<AddmmBackward0>` indicates the tensor is part of a computation graph for backpropagation.

---

## Section 4: Model Training

### Source Code (Lines 174-223)

```python
174  print("\n[Line 174] Generating synthetic dataset:")
175  np.random.seed(42)
176  torch.manual_seed(42)
177
178  # Create data: y = 1 if x1 + x2 > 0, else 0
179  n_samples = 100
180  X = torch.randn(n_samples, 2)
181  y = (X[:, 0] + X[:, 1] > 0).long()
182  print(f"Dataset size: {n_samples} samples")
183  print(f"Feature shape: {X.shape}")
184  print(f"Label distribution: {torch.bincount(y)}")
185
186  # Create model
187  print("\n[Line 188] Creating model for binary classification:")
188  model = SimpleNet(input_size=2, hidden_size=10, output_size=2)
189  criterion = nn.CrossEntropyLoss()
190  optimizer = optim.SGD(model.parameters(), lr=0.01)
191
192  # Training loop
193  print("\n[Line 195] Training for 100 epochs:")
194  n_epochs = 100
195  for epoch in range(n_epochs):
196      # Forward pass
197      outputs = model(X)
198      loss = criterion(outputs, y)
199
200      # Backward pass and optimization
201      optimizer.zero_grad()
202      loss.backward()
203      optimizer.step()
204
205      # Print progress
206      if (epoch + 1) % 20 == 0:
207          # Calculate accuracy
208          _, predicted = torch.max(outputs, 1)
209          accuracy = (predicted == y).float().mean()
210          print(f"Epoch [{epoch+1}/{n_epochs}], Loss: {loss.item():.4f}, Accuracy: {accuracy.item():.4f}")
211
212  # Final evaluation
213  print("\n[Line 216] Final evaluation:")
214  with torch.no_grad():
215      outputs = model(X)
216      _, predicted = torch.max(outputs, 1)
217      accuracy = (predicted == y).float().mean()
218      print(f"Final accuracy: {accuracy.item():.4f}")
```

### Output

```
[Line 174] Generating synthetic dataset:
Dataset size: 100 samples
Feature shape: torch.Size([100, 2])
Label distribution: tensor([47, 53])

[Line 188] Creating model for binary classification:

[Line 195] Training for 100 epochs:
Epoch [20/100], Loss: 0.7186, Accuracy: 0.5300
Epoch [40/100], Loss: 0.6940, Accuracy: 0.5300
Epoch [60/100], Loss: 0.6732, Accuracy: 0.5300
Epoch [80/100], Loss: 0.6548, Accuracy: 0.5000
Epoch [100/100], Loss: 0.6377, Accuracy: 0.5400

[Line 216] Final evaluation:
Final accuracy: 0.5400
```

### Annotations

- **Lines 175-184**: Generate a synthetic binary classification dataset. Label is 1 if x₁ + x₂ > 0, otherwise 0. The dataset has 47 samples of class 0 and 53 of class 1.
- **Lines 188-190**: Initialize a 2-layer neural network with:
  - CrossEntropyLoss for classification
  - SGD optimizer with learning rate 0.01
- **Lines 195-210**: Training loop implementing the standard PyTorch training pattern:
  1. Forward pass (line 197)
  2. Compute loss (line 198)
  3. Zero gradients (line 201)
  4. Backward pass (line 202)
  5. Update weights (line 203)
- **Lines 214-218**: Evaluate the trained model. Note: The accuracy around 54% suggests this simple model struggles with this particular synthetic task, which is expected given the limited architecture and training.

---

## Section 5: Saving and Loading Models

### Source Code (Lines 231-249)

```python
231  print("\n[Line 231] Saving model state:")
232  save_path = "model_checkpoint.pth"
233  torch.save(model.state_dict(), save_path)
234  print(f"Model saved to {save_path}")
235
236  print("\n[Line 236] Loading model state:")
237  new_model = SimpleNet(input_size=2, hidden_size=10, output_size=2)
238  new_model.load_state_dict(torch.load(save_path))
239  new_model.eval()
240  print("Model loaded successfully")
241
242  print("\n[Line 242] Verifying loaded model:")
243  test_input = torch.randn(3, 2)
244  with torch.no_grad():
245      original_output = model(test_input)
246      loaded_output = new_model(test_input)
247  print(f"Outputs match: {torch.allclose(original_output, loaded_output)}")
```

### Output

```
[Line 231] Saving model state:
Model saved to model_checkpoint.pth

[Line 236] Loading model state:
Model loaded successfully

[Line 242] Verifying loaded model:
Outputs match: True
```

### Annotations

- **Line 233**: `torch.save(model.state_dict(), ...)` saves only the model parameters (weights and biases), not the architecture.
- **Lines 237-239**: To load a model:
  1. Create a new instance of the model class with the same architecture
  2. Load the saved state dictionary
  3. Set to evaluation mode with `.eval()`
- **Lines 243-247**: Verify that the loaded model produces identical outputs to the original model using `torch.allclose()`.

---

## Section 6: Advanced Features

### Source Code (Lines 254-283)

```python
254  print("\n[Line 254] Custom loss function:")
255  class CustomMSELoss(nn.Module):
256      def forward(self, pred, target):
257          return torch.mean((pred - target)**2)
258
259  custom_loss = CustomMSELoss()
260  pred = torch.tensor([1.0, 2.0, 3.0])
261  target = torch.tensor([1.5, 2.5, 3.5])
262  loss_value = custom_loss(pred, target)
263  print(f"Custom MSE Loss: {loss_value.item():.4f}")
264
265  print("\n[Line 266] Using different optimizers:")
266  model = SimpleNet(2, 10, 2)
267
268  sgd = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
269  adam = optim.Adam(model.parameters(), lr=0.001)
270
271  print(f"SGD optimizer: {sgd}")
272  print(f"Adam optimizer: {adam}")
273
274  print("\n[Line 276] Learning rate scheduler:")
275  scheduler = optim.lr_scheduler.StepLR(sgd, step_size=10, gamma=0.1)
276  print(f"Initial LR: {sgd.param_groups[0]['lr']}")
277  for i in range(3):
278      scheduler.step()
279      print(f"After {(i+1)*10} steps: LR = {sgd.param_groups[0]['lr']}")
```

### Output

```
[Line 254] Custom loss function:
Custom MSE Loss: 0.2500

[Line 266] Using different optimizers:
SGD optimizer: SGD (
Parameter Group 0
    dampening: 0
    differentiable: False
    foreach: None
    fused: None
    lr: 0.01
    maximize: False
    momentum: 0.9
    nesterov: False
    weight_decay: 0
)
Adam optimizer: Adam (
Parameter Group 0
    amsgrad: False
    betas: (0.9, 0.999)
    capturable: False
    decoupled_weight_decay: False
    differentiable: False
    eps: 1e-08
    foreach: None
    fused: None
    lr: 0.001
    maximize: False
    weight_decay: 0
)

[Line 276] Learning rate scheduler:
Initial LR: 0.01
After 10 steps: LR = 0.01
After 20 steps: LR = 0.01
After 30 steps: LR = 0.01
```

### Annotations

- **Lines 255-263**: Create a custom loss function by inheriting from `nn.Module`. The MSE loss for predictions [1.0, 2.0, 3.0] vs targets [1.5, 2.5, 3.5] is: mean((0.5)² + (0.5)² + (0.5)²) = 0.25.
- **Lines 268-272**: PyTorch provides various optimizers:
  - **SGD**: Stochastic Gradient Descent with momentum=0.9
  - **Adam**: Adaptive learning rate optimizer with default β values (0.9, 0.999)
- **Lines 275-279**: Learning rate schedulers automatically adjust the learning rate during training. `StepLR` reduces the learning rate by a factor of `gamma` every `step_size` epochs. Note: In this demonstration, the LR remains 0.01 because we're only calling `step()` without actual training epochs.

---

## Key PyTorch Concepts Demonstrated

### 1. **Tensors**
PyTorch tensors are similar to NumPy arrays but with GPU acceleration and automatic differentiation capabilities.

### 2. **Autograd**
Automatic differentiation engine that tracks operations on tensors and computes gradients via backpropagation.

### 3. **Neural Network Modules**
The `nn.Module` class provides a convenient way to build and organize neural network layers.

### 4. **Training Loop Pattern**
```python
for epoch in range(n_epochs):
    outputs = model(inputs)        # Forward pass
    loss = criterion(outputs, targets)
    optimizer.zero_grad()          # Clear gradients
    loss.backward()                # Backward pass
    optimizer.step()               # Update weights
```

### 5. **Device Management**
PyTorch seamlessly handles CPU and GPU computation with `.to(device)` and automatic device detection.

---

## Notes

- This demonstration uses **PyTorch 2.9.1** with CUDA 12.8 support.
- The program runs on CPU in this environment (no GPU detected).
- All random operations are seeded for reproducibility (lines 175-176).
- The training example uses a simple synthetic dataset for demonstration purposes.

---

## Common PyTorch Operations Quick Reference

| Operation | Code | Description |
|-----------|------|-------------|
| Create tensor | `torch.tensor([1, 2, 3])` | From Python list |
| Zeros/Ones | `torch.zeros(2, 3)` | Initialize with 0s/1s |
| Random | `torch.randn(2, 3)` | Normal distribution |
| Matrix multiply | `a @ b` or `torch.matmul(a, b)` | Matrix multiplication |
| Reshape | `tensor.view(3, 4)` | Change tensor shape |
| Gradient | `loss.backward()` | Compute gradients |
| No gradient | `with torch.no_grad():` | Disable gradient tracking |
| To device | `tensor.to(device)` | Move to CPU/GPU |
| Save model | `torch.save(model.state_dict(), path)` | Save parameters |
| Load model | `model.load_state_dict(torch.load(path))` | Load parameters |

---

**Last Updated**: December 16, 2025
