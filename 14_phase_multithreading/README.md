# Phase 14 — Multithreading

This phase explains how Python handles multiple threads and thread synchronization.

## Topics

- Thread
- Lock
- Semaphore
- Queue
- ThreadPoolExecutor

## Files

- `interview.txt` — Q&A notes
- `multithreading_example.py` — example code

## Example

```python
import threading
import time

lock = threading.Lock()

def worker(name):
    with lock:
        print(f"Thread {name} started")
        time.sleep(1)
        print(f"Thread {name} finished")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
```

## Key Concepts

- Threads run concurrently within the same process
- Locks protect shared resources
- Semaphores limit access to a resource pool
- Queues are useful for safe producer-consumer communication
- ThreadPoolExecutor simplifies task execution management

## References

- Python threading docs: https://docs.python.org/3/library/threading.html
- Python concurrent.futures: https://docs.python.org/3/library/concurrent.futures.html
