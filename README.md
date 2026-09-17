# Python Practice Repository

A comprehensive, hands-on Python learning project with 8 progressive phases covering foundational programming concepts, interview preparation, and best practices.

**Perfect for:** Beginners learning Python, interview prep, and building coding confidence.

---

## 📚 Learning Phases

Each phase has its own detailed README with learning objectives, examples, and practice exercises.

### Phase 1: Introduction
📖 [Phase 1 README](1_PHASE_INTRODUCTION_README.md)
- Variables and data types
- Basic operations and type casting
- Input/output with print() and input()

### Phase 2: Loops & Control Flow
📖 [Phase 2 README](2_PHASE_LOOPS_README.md)
- if-elif-else statements
- for and while loops
- Loop control: break, continue, pass

### Phase 3: Strings
📖 [Phase 3 README](3_PHASE_STRINGS_README.md)
- String indexing and slicing
- String methods and manipulation
- String formatting (f-strings, .format())
- Unicode and encoding

### Phase 4: Collections
📖 [Phase 4 README](4_PHASE_COLLECTIONS_README.md)
- Lists (mutable sequences)
- Tuples (immutable sequences)
- Dictionaries (key-value pairs)
- Sets (unique values)

### Phase 5: Functions
📖 [Phase 5 README](5_PHASE_FUNCTIONS_README.md)
- Function definition and calling
- Parameters and arguments
- Return values and scope
- *args and **kwargs
- Lambda functions and recursion

### Phase 6: Exception Handling
📖 [Phase 6 README](6_PHASE_EXCEPTION_HANDLING_README.md)
- try-except-else-finally blocks
- Raising and handling exceptions
- Custom exceptions
- Assertions and validation

### Phase 7: Modules & Packages
📖 [Phase 7 README](7_PHASE_MODULES_PACKAGES_README.md)
- Modules and packages
- import statements
- Built-in modules (os, sys, json, logging)
- Third-party packages and pip

### Phase 8: File Handling
📖 [Phase 8 README](8_PHASE_FILE_HANDLING_README.md)
- Reading and writing files
- File modes and context managers
- Text and binary files
- File operations and error handling

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ installed
- Basic text editor or VS Code

### Setup

1. Navigate to the project directory:
```bash
cd /Users/kanha/DevOps/python-practice/python_practice
```

2. Activate the virtual environment:
```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

3. Run a phase file:
```bash
python 1_phase_introduction.py
python 2_phase_loops.py
# ... continue through all phases
```

---

## 📁 Project Structure

```
python_practice/
├── README.md                           # Main README (you are here)
├── 1_PHASE_INTRODUCTION_README.md
├── 2_PHASE_LOOPS_README.md
├── 3_PHASE_STRINGS_README.md
├── 4_PHASE_COLLECTIONS_README.md
├── 5_PHASE_FUNCTIONS_README.md
├── 6_PHASE_EXCEPTION_HANDLING_README.md
├── 7_PHASE_MODULES_PACKAGES_README.md
├── 8_PHASE_FILE_HANDLING_README.md
├── 1_phase_introduction.py
├── 2_phase_loops.py
├── phase3-string.py                    # Phase 3 main file
├── 4_phase_Collections.py
├── 5_phase_functions.py
├── 6_phase_Exception Handling.py
├── 7_phase_Modules & Packages.py
├── 8_phase_file_handing/
│   └── 8_phase_filehandling.py
├── .venv/                              # Virtual environment
└── ... (other practice files)
```

---

## 💡 Key Features

✅ **8 Progressive Phases** - Learn from basics to advanced concepts
✅ **Interview Questions** - Each phase includes common interview Q&A
✅ **Practical Examples** - Real-world code examples and use cases
✅ **Best Practices** - Python conventions and optimization tips
✅ **Modern Python** - Uses Python 3.7+ features (f-strings, type hints, etc.)
✅ **Clear Explanations** - Each concept explained with examples

---

## 🎯 Recommended Learning Path

1. **Day 1-2**: Phase 1 (Introduction)
2. **Day 3-4**: Phase 2 (Loops)
3. **Day 5-6**: Phase 3 (Strings)
4. **Day 7-8**: Phase 4 (Collections)
5. **Day 9-10**: Phase 5 (Functions)
6. **Day 11-12**: Phase 6 (Exceptions)
7. **Day 13-14**: Phase 7 (Modules)
8. **Day 15-16**: Phase 8 (File Handling)

**Total:** 2-4 weeks depending on practice intensity

---

## 📝 How to Use

1. **Read the Phase README** - Understand learning objectives
2. **Study the Examples** - Review code examples in the README
3. **Run the Phase File** - Execute the Python file to see it in action
4. **Practice Exercises** - Complete exercises listed in the README
5. **Review Q&A** - Read interview questions at the end of each phase
6. **Move to Next Phase** - Progress when confident

---

## 🔧 Installing Additional Packages

For some examples, you might need additional packages:

```bash
# Ensure you're in the virtual environment
source .venv/bin/activate

# Install packages as needed
pip install requests      # For HTTP requests
pip install boto3         # For AWS services
pip install numpy         # For numerical computing
pip install pandas        # For data analysis

# List installed packages
pip list

# Save requirements
pip freeze > requirements.txt
```

---

## 🎓 Interview Preparation

Each phase file contains real interview questions and answers:
- **Basic Questions** - Foundation level
- **Intermediate Questions** - Practical scenarios
- **Advanced Questions** - Problem-solving and optimization

Use the interview Q&A sections for:
- Preparing for technical interviews
- Refreshing your Python knowledge
- Understanding practical applications

---

## 💻 Running Scripts

### Single Phase
```bash
python 3_phase-string.py
```

### With Arguments (Phase 7+)
```bash
python script.py arg1 arg2 --option value
```

### Check Python Version
```bash
python --version
```

### Run in Debug Mode
```bash
python -m pdb 5_phase_functions.py
```

---

## 📚 Additional Resources

- **Official Python Docs:** https://docs.python.org/3/
- **Python Tips:** https://book.pythontips.com/
- **PEP 8 Style Guide:** https://www.python.org/dev/peps/pep-0008/
- **Python FAQ:** https://docs.python.org/3/faq/

---

## 🐛 Troubleshooting

### Module Not Found
```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Install the module
pip install module-name
```

### Python or Python3 Not Found
```bash
# Use full path
/usr/bin/python3 phase1.py

# Or create alias
alias python=/usr/bin/python3
```

### Permission Denied
```bash
# Make file executable
chmod +x script.py
```

---

## ✅ Checklist for Completion

- [ ] Phase 1 - Introduction (variables, types, I/O)
- [ ] Phase 2 - Loops (control flow, loops)
- [ ] Phase 3 - Strings (indexing, methods, formatting)
- [ ] Phase 4 - Collections (lists, tuples, dicts, sets)
- [ ] Phase 5 - Functions (definition, scope, lambda)
- [ ] Phase 6 - Exceptions (try-except, custom errors)
- [ ] Phase 7 - Modules (imports, built-in modules)
- [ ] Phase 8 - File Handling (reading, writing files)
- [ ] Review all interview questions
- [ ] Complete practice exercises for each phase

---

## 🤝 Contributing

Found a bug or have a suggestion? Feel free to improve this repository!

---

## 📄 License

This project is for learning and personal practice purposes.

---

## 🎉 Next Steps After Completion

Once you finish all 8 phases:

1. **Build Projects** - Create real applications using these concepts
2. **Contribute to Open Source** - Apply your skills in real projects
3. **Advanced Topics** - Learn OOP, decorators, generators, async/await
4. **Web Development** - Explore Flask/Django
5. **Data Science** - Study NumPy, Pandas, scikit-learn
6. **Interview Prep** - Practice on LeetCode, HackerRank

---

**Happy Learning! 🚀**

For phase-specific details, click on each phase README above.
