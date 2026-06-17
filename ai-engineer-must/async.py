import time
import asyncio

# Mocking a synchronous external API call to an LLM
def query_llm_sync(prompt: str) -> str:
    time.sleep(0.1)  # Simulate 100ms network latency
    return f"Response to '{prompt}'"
 
def run_sequential(prompts):
    start = time.perf_counter()
    results = []
    for p in prompts:
        results.append(query_llm_sync(p))
    elapsed = time.perf_counter() - start
    print(f"Sequential processing took {elapsed:.4f} seconds.")
    return results
 
# Mocking an asynchronous external API call to an LLM
async def query_llm_async(prompt: str) -> str:
    await asyncio.sleep(0.1)  # Non-blocking sleep simulates async network I/O
    return f"Response to '{prompt}'"
 
async def run_concurrent(prompts):
    start = time.perf_counter()
    # Schedule all LLM calls to execute concurrently
    tasks = [query_llm_async(p) for p in prompts]
    results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    print(f"Concurrent processing took {elapsed:.4f} seconds.")
    return results
 

# Executing the synchronous runner
prompts = [f"Explain topic {i}" for i in range(20)]
_ = run_sequential(prompts)

# Executing the async runner
prompts = [f"Explain topic {i}" for i in range(20)]
_ = asyncio.run(run_concurrent(prompts))

# Output:
# Sequential processing took 2.0768 seconds.
# Concurrent processing took 0.1016 seconds.