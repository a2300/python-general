import json
import io
import tracemalloc
 
# A mock JSONL file stream of raw text payloads
def get_dataset_stream():
    data = "\n".join([json.dumps({"id": i, "text": f"User query raw text payload {i}"}) for i in range(50000)])
    return io.StringIO(data)
 
# Naive list function processing all records at once
def load_all_records_naive(stream):
    records = []
    for line in stream:
        payload = json.loads(line)
 
        # Process data immediately and append to a list
        processed = {
            "id": payload["id"],
            "text": payload["text"].lower(),
            "length": len(payload["text"])
        }
        records.append(processed)
 
    return records
 
# Generator function yielding preprocessed records one-by-one
def stream_records_generator(stream):
    for line in stream:
        payload = json.loads(line)
        yield {
            "id": payload["id"],
            "text": payload["text"].lower(),
            "length": len(payload["text"])
        }
 
 
# Measure the naive implementation
tracemalloc.start()
stream_naive = get_dataset_stream()
records_list = load_all_records_naive(stream_naive)
for r in records_list:
    pass  # Simulate a training loop step
_, peak_naive = tracemalloc.get_traced_memory()
tracemalloc.stop()
 
# Measure the generator implementation
tracemalloc.start()
stream_gen = get_dataset_stream()
records_generator = stream_records_generator(stream_gen)
for r in records_generator:
    pass  # Simulate a training loop step
_, peak_gen = tracemalloc.get_traced_memory()
tracemalloc.stop()
 
# Output results
print(f"Naive peak RAM: {peak_naive / 1024 / 1024:.4f} MB")
print(f"Generator peak RAM: {peak_gen / 1024 / 1024:.4f} MB")

# Output:
# Naive peak RAM: 25.2127 MB
# Generator peak RAM: 13.9610 MB

# Generators solve this with lazy evaluation. By using the yield keyword, a generator returns an iterator that computes and yields elements on demand, one at a time. This keeps your RAM usage flat, whether you are streaming 100 samples or 100 million.
# By using generators, the peak RAM consumption dropped to nearly half. When working with multi-gigabyte text datasets for large language models or batching images for vision models, streaming data ensures that memory consumption remains flat and predictable, avoiding the worry of running out of RAM in production.