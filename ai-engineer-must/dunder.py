class CustomDatasetPythonic:
    def __init__(self, data_list):
        self.data = data_list
        
    def __len__(self) -> int:
        return len(self.data)
        
    def __getitem__(self, idx: int):
        return self.data[idx]
 
class PredictionPipeline:
    def __init__(self, step_value: float):
        self.step_value = step_value
        
    def __call__(self, x: float) -> float:
        # Implementing __call__ makes instances callable like functions
        return x * self.step_value
 
 
# Instantiating the protocol-compatible dataset
dataset = CustomDatasetPythonic(["Sample A", "Sample B", "Sample C"])
print(f"Dataset length: {len(dataset)}")
print(f"Index access [1]: {dataset[1]}")
 
# Instantiating the callable pipeline
pipeline = PredictionPipeline(step_value=2.5)
 
# Call the object directly
result = pipeline(10.0)
print(f"Pipeline call execution result: {result}")
