# tests.py
from functions.run_python_file import run_python_file

def test_1():
    test = run_python_file("calculator", "main.py")
    print(f"Test 1:\n{test}")

def test_2():
    test = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Test 2:\n{test}")

def test_3():
    test = run_python_file("calculator", "tests.py")
    print(f"Test 3:\n{test}")

def test_4():
    test = run_python_file("calculator", "../main.py")
    print(f"Test 4:\n{test}")

def test_5():
    test = run_python_file("calculator", "nonexistent.py")
    print(f"Test 5:\n{test}")

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()