PHASE 15: ASYNC PROGRAMMING - INTERVIEW QUESTIONS
====================================================

1. FUNDAMENTALS OF ASYNC PROGRAMMING

Q1. What is the difference between synchronous and asynchronous programming?
A1. Synchronous: Code executes sequentially; each line waits for the previous to complete.
    Asynchronous: Code can suspend and resume; allows I/O operations to happen without blocking.
    
Q2. What does the 'async' keyword do?
A2. The 'async' keyword defines a coroutine function. It returns a coroutine object when called
    rather than executing immediately. It allows the use of 'await' inside the function.

Q3. What does the 'await' keyword do?
A3. 'await' pauses execution of a coroutine and yields control back to the event loop
    until the awaited operation is complete. It can only be used inside async functions.

Q4. What is a coroutine?
A4. A coroutine is a special type of function that can be paused and resumed.
    Created with 'async def', it returns a coroutine object that must be awaited
    to execute, or scheduled as a task.

Q5. Explain the difference between a coroutine and a regular function.
A5. Regular functions: Execute from start to finish, return when done
    Coroutines: Can pause execution with await, resume later, more flexible control flow


2. EVENT LOOP AND ASYNCIO

Q6. What is an event loop?
A6. The event loop is the core of asyncio that:
    - Manages and executes coroutines
    - Handles I/O operations efficiently
    - Runs callbacks and tasks
    - Creates a single-threaded concurrency model

Q7. How do you run a coroutine?
A7. Using asyncio.run() at the top level:
    asyncio.run(my_coroutine())
    
    Or using get_event_loop():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine())

Q8. What is asyncio.gather()?
A8. asyncio.gather() runs multiple coroutines concurrently and waits for all to complete.
    It returns results in the same order as input.
    Example: results = await asyncio.gather(coro1(), coro2(), coro3())

Q9. What is asyncio.create_task()?
A9. asyncio.create_task() wraps a coroutine in a Task and schedules it to run.
    It starts running immediately when called (in background).
    Useful for creating background tasks.

Q10. What is the difference between asyncio.gather() and asyncio.create_task()?
A10. gather(): Waits for all coroutines to complete before returning
     create_task(): Returns immediately, task runs in background
     gather() is blocking, create_task() is non-blocking


3. ASYNC/AWAIT PATTERNS

Q11. How do you handle multiple concurrent operations?
A11. Use asyncio.gather() to run multiple coroutines concurrently:
    results = await asyncio.gather(task1(), task2(), task3())

Q12. How do you handle exceptions in async code?
A12. Use try/except blocks within coroutines, or use gather() with return_exceptions=True
    to capture exceptions as results.

Q13. What is an async context manager?
A13. Defined with __aenter__ and __aexit__ methods, allowing resource management
    with async operations. Used with 'async with' statement.

Q14. What is an async iterator?
A14. Implements __aiter__ and __anext__ methods, allowing iteration with async operations.
    Used with 'async for' loops.

Q15. How do you implement a timeout in asyncio?
A15. Use asyncio.wait_for() with a timeout parameter:
    result = await asyncio.wait_for(coro(), timeout=5.0)
    Raises asyncio.TimeoutError if timeout exceeded


4. SYNCHRONIZATION AND THREAD SAFETY

Q16. What is asyncio.Lock?
A16. A lock for synchronizing access to shared resources in async code.
    Only one coroutine can acquire the lock at a time.
    Used with 'async with' statement.

Q17. What is asyncio.Semaphore?
A17. Similar to Lock but allows multiple coroutines (specified count) to access
    the resource concurrently. Useful for rate limiting.

Q18. What is asyncio.Event?
A18. A synchronization primitive that allows coroutines to wait for an event to be set.
    One coroutine sets the event, others wait for it.

Q19. What is asyncio.Condition?
A19. A combination of Lock and Event. Coroutines can wait for a condition while
    another holds the lock and notifies when condition is met.

Q20. Why don't you need threading locks in asyncio?
A20. Asyncio is single-threaded. Context switches only occur at 'await' points,
    preventing race conditions. True parallel locks are only needed with threads.


5. ASYNCIO QUEUES AND CHANNELS

Q21. What are asyncio.Queue() and asyncio.LifoQueue()?
A21. Queue(): FIFO queue for async producer-consumer patterns
     LifoQueue(): LIFO queue (stack-like) for async operations

Q22. How do you implement producer-consumer with asyncio?
A22. Producer: Puts items in queue, signals end with None or sentinel value
     Consumer: Gets items from queue, processes them
     Both run concurrently using asyncio.gather()

Q23. What is queue.get() vs queue.get_nowait()?
A23. get(): Async method, waits if queue is empty
     get_nowait(): Synchronous, raises QueueEmpty exception if empty


6. SOCKET PROGRAMMING WITH ASYNCIO

Q24. How do you create an async TCP server?
A24. Use asyncio.start_server(callback, host, port) to create a server.
    The callback handles each client connection asynchronously.

Q25. How do you create an async TCP client?
A25. Use asyncio.open_connection(host, port) which returns (reader, writer) pair.
    Use reader.read() to receive data, writer.write() to send.

Q26. What is the difference between socket and asyncio socket?
A26. socket: Blocking I/O, one connection per thread/process
     asyncio socket: Non-blocking I/O, many connections handled by event loop

Q27. How do you handle multiple client connections in async server?
A27. asyncio.start_server creates a new task for each client automatically.
    Each client connection runs its own handler coroutine concurrently.

Q28. How do you implement timeout for connections?
A28. Use asyncio.wait_for() around the client handler code:
    await asyncio.wait_for(some_operation(), timeout=30)


7. HTTP AND API REQUESTS

Q29. What is aiohttp?
A29. An async HTTP client/server library for Python.
    Allows making HTTP requests without blocking the event loop.

Q30. How do you make async HTTP requests?
A30. Using aiohttp.ClientSession:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

Q31. How do you make multiple concurrent HTTP requests?
A31. Create multiple fetch tasks and use asyncio.gather():
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

Q32. What are the benefits of async HTTP over requests library?
A32. - Non-blocking: Handles hundreds of requests concurrently
     - Efficient: Uses event loop, minimal resource usage
     - Scalable: Can handle many connections in single thread
     - Faster: No thread overhead

Q33. How do you handle HTTP errors in async code?
A33. Check response.status code, catch aiohttp exceptions (ClientError, etc)
    Use try/except blocks around request operations


8. ADVANCED ASYNC CONCEPTS

Q34. What is asyncio.wait()?
A34. Returns when first coroutine(s) complete. Useful for waiting on first result
    or handling timeouts. Returns (done, pending) set of tasks.

Q35. What is the difference between Task and Coroutine?
A35. Coroutine: An object returned by async function, defines computation
     Task: Wraps coroutine, schedules it to run, can monitor progress

Q36. How do you cancel an async task?
A36. Use task.cancel(). Inside the task, handle asyncio.CancelledError exception.

Q37. What is asyncio.shield()?
A37. Protects a coroutine from being cancelled. Useful for ensuring cleanup operations.

Q38. What are callbacks in asyncio?
A38. Functions that run when a task completes. Add with task.add_done_callback().
    Useful for post-processing results without blocking.

Q39. How do you run blocking code in async context?
A39. Use loop.run_in_executor():
    result = await loop.run_in_executor(None, blocking_function, arg)
    Runs blocking function in thread pool, doesn't block event loop


9. PERFORMANCE AND DEBUGGING

Q40. How many concurrent connections can asyncio handle?
A40. Easily thousands on modern systems. Limited by OS file descriptor limits
    and available memory, not threading constraints.

Q41. How do you debug async code?
A41. - Use asyncio debug mode: asyncio.run(main(), debug=True)
     - Print/logging with timestamps
     - Use asyncio.all_tasks() to see running tasks
     - Check for common issues: blocking calls, missing awaits

Q42. What are common async programming mistakes?
A42. - Forgetting to await a coroutine
     - Mixing blocking code with async
     - Not using asyncio.gather() for concurrent operations
     - Incorrect exception handling
     - Creating too many tasks without pooling

Q43. How do you avoid starving the event loop?
A43. - Break long-running computations into smaller chunks
     - Use loop.run_in_executor() for blocking operations
     - Avoid busy-waiting loops
     - Ensure all coroutines use await regularly

Q44. How do you measure async performance?
A44. Compare: serial execution vs concurrent with asyncio.gather()
    Serial: sum of all operation times
    Concurrent: max operation time (can be 10-100x faster for I/O)


10. REAL-WORLD SCENARIOS

Q45. How would you scrape multiple websites concurrently?
A45. Use aiohttp to fetch multiple URLs concurrently with asyncio.gather()
    Each fetch is an async coroutine, all run simultaneously

Q46. How would you implement rate limiting in async code?
A46. Use asyncio.Semaphore to limit concurrent requests:
    semaphore = asyncio.Semaphore(10)  # Max 10 concurrent
    async with semaphore:
        make_request()

Q47. How would you implement async database queries?
A47. Use async database drivers (asyncpg for PostgreSQL, motor for MongoDB)
    Similar pattern to aiohttp: async context manager, await queries

Q48. How do you combine asyncio with other async libraries?
A48. Most async libraries are compatible. Just use asyncio.gather() or create_task()
    to manage execution of coroutines from different libraries

Q49. When should you use asyncio vs threading?
A49. asyncio: I/O-bound operations (network, database, file operations)
     threading: CPU-bound work (computation, image processing)
     asyncio better for I/O, simpler synchronization, lower overhead

Q50. How do you handle graceful shutdown in async applications?
A50. Use signals (SIGINT, SIGTERM) to cancel tasks:
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_tasks, loop)
    Cancel all running tasks before shutdown
