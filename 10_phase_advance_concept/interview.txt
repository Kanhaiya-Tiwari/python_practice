Phase 10 — Advanced Python Concepts: Interview Questions and Answers

Basic

Q: What is an iterator?
A: An iterator is an object that implements the iterator 
protocol: it has an `__iter__()` method that returns the 
iterator itself and a `__next__()` method that returns the next
 item or raises `StopIteration` when exhausted.

Q: What is the difference between an iterator and a generator?
A: A generator is a specific, convenient way to create iterators
\ using a function with `yield` or a generator expression. All
 generators are iterators, but not all iterators are generators.

Q: Why are generators memory efficient?
A: Generators produce items lazily, yielding one item at a time 
on demand instead of building and storing the entire sequence in
 memory.

Q: What is a decorator?
A: A decorator is a callable that takes a function (or class) 
and returns a new function (or class), often used to wrap or 
modify behavior (e.g., `@decorator`).

Q: What is a closure?
A: A closure is a function that captures and retains access to
 variables from its lexical enclosing scope, even when the outer 
 function has finished execution.

Q: What is a context manager?
A: A context manager defines `__enter__()` and `__exit__()`
 methods and is used with the `with` statement to set up and 
 tear down resources reliably.

Intermediate

Q: What are list comprehensions?
A: List comprehensions provide a concise syntax to create lists
 from iterables using an expression and optional `for`/`if` 
 clauses: `[expr for item in iterable if cond]`.

Q: Difference between list comprehension and map()?
A: Both can transform iterables. List comprehensions are usually
 more pythonic and readable and can include conditional logic. `
 map()` applies a function to each item and returns an iterator 
 in Python 3.

Q: Difference between filter() and map()?
A: `map()` transforms each item using a function; `filter()` 
selects items for which a predicate returns True. Both return 
iterators in Python 3.

Q: Difference between zip() and enumerate()?
A: `zip()` pairs items from multiple iterables into tuples. 
`enumerate()` pairs each item with its index: it yields 
`(index, item)` from a single iterable.

Advanced

Q: Why use generators instead of lists?
A: Generators save memory and can represent infinite sequences; 
they start producing results immediately and are suitable when
 you need items lazily or the full list would be large.

Q: What is yield?
A: `yield` turns a function into a generator by pausing its 
state and returning a value to the caller; subsequent calls 
resume execution after the `yield`.

Q: Why use decorators?
A: Decorators enable reusable cross-cutting behavior (logging,
 caching, access control, timing) without modifying the 
 decorated function's code.

Q: What does reduce() do?
A: `functools.reduce()` applies a binary function cumulatively
 to the items of an iterable, reducing it to a single value 
 (e.g., summing or combining elements).

Q: When should you use a context manager?
A: Use a context manager whenever you need deterministic setup 
and teardown of resources (files, locks, network connections, 
transactions). `with` ensures cleanup runs even if exceptions 
occur.

End of Phase 10 interview notes.

