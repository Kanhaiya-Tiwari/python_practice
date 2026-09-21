import threading
import time
from concurrent.futures import ThreadPoolExecutor


# Example 1: basic thread with lock
lock = threading.Lock()


def worker(name):
    time.sleep(0.5)
    with lock:
        print(f"Thread {name} is running")


threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("\nThread example finished\n")

# Example 2: Queue example
queue = []


def producer():
    for i in range(5):
        queue.append(i)
        print(f"Produced: {i}")
        time.sleep(0.2)


def consumer():
    while queue:
        item = queue.pop(0)
        print(f"Consumed: {item}")
        time.sleep(0.3)


thread1 = threading.Thread(target=producer)
thread2 = threading.Thread(target=consumer)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("\nQueue example finished\n")

# Example 3: ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(square, [1, 2, 3, 4, 5]))

print("ThreadPoolExecutor results:", results)
