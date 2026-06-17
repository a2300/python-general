import time
 
class MockPyTorchModel:
    def __init__(self):
        self.training = True
    def __call__(self, x):
        return [val * 1.5 for val in x]
 
class InferenceProfiler:
    def __init__(self, model):
        self.model = model
        
    def __enter__(self):
        self.start_time = time.perf_counter()
        self.original_mode = self.model.training
        # Set model to evaluation mode
        self.model.training = False
        print("[Enter] Switched model to eval mode, started timer.")
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore the original training state
        self.model.training = self.original_mode
        elapsed = time.perf_counter() - self.start_time
        print(f"[Exit] Block latency: {elapsed:.6f} seconds")
        print("[Exit] Restored training state. Simulating CUDA cache clean.")
        # Returning False ensures any exception that occurred is not suppressed
        return False
 
 
# Execution becomes incredibly clean and robust
model = MockPyTorchModel()
with InferenceProfiler(model):
    res = model([1.0, 2.0, 3.0])
    print(f"Prediction inside context: {res}")