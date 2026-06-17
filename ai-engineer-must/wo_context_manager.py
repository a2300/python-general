import time
 
class MockPyTorchModel:
    def __init__(self):
        self.training = True
    def __call__(self, x):
        return [val * 1.5 for val in x]
 
# Create model
model = MockPyTorchModel()
 
# Start manual setup and execution
start_time = time.perf_counter()
original_mode = model.training
 
# Manually set model to evaluation mode
model.training = False  
 
try:
    # Perform inference
    outputs = model([1.0, 2.0, 3.0])
    print(f"Inference outputs: {outputs}")
finally:
    # We must explicitly clean up and restore state
    model.training = original_mode
    elapsed = time.perf_counter() - start_time
    print(f"[Manual Profile] Inference took {elapsed:.6f}s")
    print("[Manual GPU] Simulating: torch.cuda.empty_cache()")

# 2. Context Managers (Hardware State & Resource Management)