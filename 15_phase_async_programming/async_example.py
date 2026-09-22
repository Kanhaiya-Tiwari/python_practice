"""
Phase 15: Async Programming - Basics
Covers: async, await, asyncio, Event Loop, Socket Programming
"""

import asyncio
import time

try:
    import aiohttp
    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False


# ============================================================================
# 1. BASIC ASYNC/AWAIT
# ============================================================================

async def greet(name: str) -> str:
    """Basic async function"""
    await asyncio.sleep(1)
    return f"Hello, {name}!"


async def basic_example():
    """Example 1: Run single async function"""
    print("\n=== 1. Basic Async/Await ===")
    result = await greet("Alice")
    print(result)


# ============================================================================
# 2. CONCURRENT EXECUTION WITH GATHER
# ============================================================================

async def task_a():
    print("Task A started")
    await asyncio.sleep(2)
    return "A done"


async def task_b():
    print("Task B started")
    await asyncio.sleep(1)
    return "B done"


async def task_c():
    print("Task C started")
    await asyncio.sleep(1)
    return "C done"


async def gather_example():
    """Example 2: Run multiple tasks concurrently"""
    print("\n=== 2. Concurrent Execution (gather) ===")
    start = time.time()
    results = await asyncio.gather(task_a(), task_b(), task_c())
    duration = time.time() - start
    print(f"Results: {results}")
    print(f"Time: {duration:.1f}s (serial would be ~4s)")


# ============================================================================
# 3. ASYNCIO TIMEOUT
# ============================================================================

async def slow_task():
    await asyncio.sleep(5)
    return "Done"


async def timeout_example():
    """Example 3: Timeout handling"""
    print("\n=== 3. Timeout ===")
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out!")


# ============================================================================
# 4. ASYNCIO LOCK (SYNCHRONIZATION)
# ============================================================================

counter = 0
lock = asyncio.Lock()


async def increment():
    """Increment counter safely with lock"""
    global counter
    async with lock:
        temp = counter
        await asyncio.sleep(0.1)
        counter = temp + 1


async def lock_example():
    """Example 4: Synchronization with locks"""
    print("\n=== 4. Asyncio Lock ===")
    global counter
    counter = 0
    await asyncio.gather(increment(), increment(), increment())
    print(f"Counter (with lock): {counter}")


# ============================================================================
# 5. ASYNCIO QUEUE (PRODUCER-CONSUMER)
# ============================================================================

async def producer(queue: asyncio.Queue):
    """Producer puts items in queue"""
    for i in range(1, 4):
        print(f"Producing {i}")
        await queue.put(i)
        await asyncio.sleep(0.2)
    await queue.put(None)  # Signal end


async def consumer(queue: asyncio.Queue, name: str):
    """Consumer takes items from queue"""
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        print(f"{name} consumed {item}")
        queue.task_done()


async def queue_example():
    """Example 5: Queue for producer-consumer"""
    print("\n=== 5. Asyncio Queue ===")
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue, "Consumer"),
    )


# ============================================================================
# 6. SOCKET PROGRAMMING (ASYNC TCP)
# ============================================================================

async def tcp_echo_server():
    """Simple async TCP echo server"""
    async def handle_client(reader, writer):
        addr = writer.get_extra_info('peername')
        print(f"Client connected: {addr}")
        try:
            data = await reader.read(100)
            msg = data.decode()
            print(f"Received: {msg}")
            writer.write(f"Echo: {msg}".encode())
            await writer.drain()
        finally:
            writer.close()
            await writer.wait_closed()
    
    server = await asyncio.start_server(handle_client, '127.0.0.1', 9999)
    addr = server.sockets[0].getsockname()
    print(f"Server listening on {addr}")
    
    async with server:
        await asyncio.sleep(3)  # Run for 3 seconds
        print("Server closing")


async def tcp_client():
    """Simple async TCP client"""
    try:
        await asyncio.sleep(0.5)  # Wait for server
        reader, writer = await asyncio.open_connection('127.0.0.1', 9999)
        print("Connected to server")
        
        writer.write(b"Hello Server!")
        await writer.drain()
        
        data = await reader.read(100)
        print(f"Received: {data.decode()}")
        
        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"Client error: {e}")


async def socket_example():
    """Example 6: Async socket programming"""
    print("\n=== 6. Async Socket (TCP) ===")
    await asyncio.gather(tcp_echo_server(), tcp_client())


# ============================================================================
# 7. HTTP REQUESTS (AIOHTTP)
# ============================================================================

async def http_example():
    """Example 7: HTTP requests with aiohttp"""
    if not HAS_AIOHTTP:
        print("\n=== 7. HTTP with aiohttp ===")
        print("Install aiohttp: pip install aiohttp")
        return
    
    print("\n=== 7. HTTP with aiohttp ===")
    
    async def fetch(session, url):
        try:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    return await response.json()
                return f"Status: {response.status}"
        except Exception as e:
            return f"Error: {e}"
    
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
    ]
    
    try:
        async with aiohttp.ClientSession() as session:
            results = await asyncio.gather(*[fetch(session, url) for url in urls])
            for i, result in enumerate(results, 1):
                print(f"Request {i}: {str(result)[:100]}...")
    except Exception as e:
        print(f"Error: {e}")


# ============================================================================
# MAIN
# ============================================================================

async def main():
    """Run all examples"""
    print("=" * 60)
    print("PHASE 15: ASYNC PROGRAMMING")
    print("=" * 60)
    
    await basic_example()
    await gather_example()
    await timeout_example()
    await lock_example()
    await queue_example()
    await socket_example()
    await http_example()
    
    print("\n" + "=" * 60)
    print("COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
