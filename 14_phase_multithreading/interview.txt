Phase 14 — Multithreading Interview Questions and Answers

Basic

Q: What is multithreading?
A: Multithreading is a way to run multiple threads in the same process so different tasks can execute concurrently.

Q: What is a thread?
A: A thread is the smallest unit of execution within a process. Threads share memory space and resources of the same process.

Q: What is a lock?
A: A lock is a synchronization primitive used to prevent multiple threads from accessing the same resource at the same time.

Q: What is a semaphore?
A: A semaphore is a synchronization object that controls access to a shared resource by limiting how many threads can use it at once.

Q: What is a queue?
A: A queue is a data structure used for communication between threads. It helps safely pass tasks or messages between producers and consumers.

Intermediate

Q: Why do we use threads?
A: Threads are useful for performing tasks concurrently, especially when operations involve waiting, such as file I/O, web requests, or background jobs.

Q: What is the difference between a thread and a process?
A: A process is an independent program with its own memory, while threads share memory within the same process.

Q: What is ThreadPoolExecutor?
A: ThreadPoolExecutor is a high-level API that manages a pool of worker threads and executes tasks efficiently.

Q: Why do we need locks?
A: Without locks, multiple threads may modify the same data simultaneously and cause race conditions or inconsistent states.

Q: What is a race condition?
A: A race condition occurs when two or more threads access shared data concurrently and the final result depends on the timing of execution.

Advanced

Q: What is the purpose of a semaphore?
A: A semaphore restricts access to a limited number of resources, helpful when only a fixed number of threads should access a critical section at a time.

Q: How does a queue help in multithreading?
A: It provides thread-safe communication and helps coordinate work distribution between multiple threads.

Q: Why is ThreadPoolExecutor preferred over manually creating threads?
A: It reduces boilerplate, manages thread lifecycle automatically, and is easier to use for tasks that need parallel execution.

Q: What are the disadvantages of multithreading?
A: It can introduce complexity, debugging difficulty, and synchronization issues such as deadlocks or race conditions.

Q: When should you avoid multithreading?
A: Avoid it when tasks are CPU-bound and not waiting on I/O, because Python threads are limited by the GIL for CPU-heavy work.

End of Phase 14 interview notes.
