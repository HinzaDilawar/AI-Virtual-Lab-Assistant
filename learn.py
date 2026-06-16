# frontend/pages/learn.py
import streamlit as st
from backend.progress import add_progress

# -------------------------------
# 1. TOPICS LISTS (Python & C++)
# -------------------------------
PY_TOPICS = [
    "Hello World", "Variables", "Data Types", "Input/Output", "Arithmetic Operators",
    "If-Else", "For Loop", "While Loop", "Lists", "Tuples", "Dictionaries",
    "Functions", "Lambda Functions", "Map/Filter/Reduce", "List Comprehension",
    "File I/O", "Exception Handling", "Classes & Objects", "Inheritance", "Polymorphism",
    "Encapsulation", "Recursion", "Factorial", "Fibonacci", "Prime Check",
    "Linear Search", "Binary Search", "Bubble Sort", "Selection Sort", "Insertion Sort",
    "Merge Sort", "Quick Sort", "Stack", "Queue", "Linked List",
    "Palindrome", "Anagram", "JSON Read/Write", "HTTP Request", "Regex Example",
    "Decorators", "Generators", "Context Managers", "Unit Test", "Matrix Multiplication",
    "Sparse Matrix", "CSV Processing", "Datetime Example", "Threading", "Multiprocessing"
]

CPP_TOPICS = [
    "Hello World","Variables & Constants","Data Types","Input/Output","Arithmetic Operators",
    "Relational Operators","Logical Operators","If-Else","Switch Case","For Loop","While Loop",
    "Do-While Loop","Break & Continue","Arrays","2D Arrays","Strings","Pointers","References",
    "Functions","Function Overloading","Default Arguments","Recursion","Inline Functions","Structures",
    "Unions","Enumerations (Enums)","Classes & Objects","Constructors","Destructors","Encapsulation",
    "Inheritance","Multilevel Inheritance","Multiple Inheritance","Hierarchical Inheritance","Polymorphism",
    "Function Overriding","Virtual Functions","Abstract Classes","Friend Function","Static Members",
    "Dynamic Memory","Exception Handling","Function Templates","Class Templates","Namespaces","File Writing",
    "File Reading","STL Vector","STL Stack","STL Queue",
]

JS_TOPICS = [
    "Hello World","Variables (var, let, const)","Data Types","Type Conversion","Template Literals",
    "Arithmetic Operators","Comparison Operators","Logical Operators","If-Else","Switch Case",
    "For Loop","While Loop","Do-While Loop","Break & Continue","Functions","Arrow Functions",
    "Default Parameters","Rest & Spread Operator","Arrays","Array Methods","Objects",
    "Object Destructuring","Array Destructuring","Spread with Arrays & Objects","String Methods",
    "Math Object","Date Object","Null & Undefined","Typeof Operator","Ternary Operator",
    "Short Circuit Evaluation","Callbacks","Promises","Async & Await","Try-Catch-Finally","DOM Selection",
    "DOM Manipulation","Event Listeners","Classes & Objects (OOP)","Constructor Functions","Inheritance (extends)",
    "Getters & Setters","Modules (import/export)","JSON Parse & Stringify","LocalStorage & SessionStorage",
    "Fetch API","Map & Set","Higher Order Functions","Closures","Regular Expressions (Regex)",
]

# -------------------------------
# 2. COMPLETE LEARN CONTENT DICTIONARY
# -------------------------------
LEARN_CONTENT = {
    "Python": {
        "Hello World": {

            "explanation": "Prints a message to the screen. Introduces Python syntax and output.",

            "example": """print("Hello, world!")""",

            "output": "Hello, world!"

        },

        "Variables": {

            "explanation": "Variables store data in memory for later use.",

            "example": """name = "Ali"

age = 20

print(name, age)""",

            "output": "Ali 20"

        },

       "Data Types": {

            "explanation": "Python supports int, float, str, list, tuple, dict, bool.",

            "example": """x = 10

y = 3.14

z = "Hello"

print(type(x), type(y), type(z))""",

            "output": "<class 'int'> <class 'float'> <class 'str'>"

        },

        "Input/Output": {

            "explanation": "Input allows user data; output displays data.",

            "example": """name = "Ali"

print(f"Hello {name}")""",

            "output": "Hello Ali"

        },

        "Arithmetic Operators": {

            "explanation": "Perform calculations with +, -, , /, %, //, *.",

            "example": """a=10

b=3

print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)""",

            "output": "13 7 30 3.3333333333333335 3 1 1000"

        },

        "If-Else": {

            "explanation": "Conditional statements execute code based on True/False.",

            "example": """age=18

if age>=18:

    print("Adult")

else:

    print("Minor")""",

            "output": "Adult"

        },

        "For Loop": {

            "explanation": "Repeat code over sequences or ranges.",

            "example": """for i in range(3):

    print(i)""",

            "output": "0\n1\n2"

        },

        "While Loop": {

            "explanation": "Repeat code while condition is True.",

            "example": """i=0

while i<3:

    print(i)

    i+=1""",

            "output": "0\n1\n2"

        },

        "Lists": {

            "explanation": "Ordered, mutable collection of items.",

            "example": """fruits = ["apple", "banana"]

fruits.append("cherry")

print(fruits)""",

            "output": "['apple', 'banana', 'cherry']"

        },

        "Tuples": {

            "explanation": "Ordered, immutable collection of items.",

            "example": """t = (1,2,3)

print(t[1])""",

            "output": "2"

        },

        "Dictionaries": {

            "explanation": "Key-value pairs for fast lookup.",

            "example": """student = {"name":"Ali","age":20}

print(student["name"])""",

            "output": "Ali"

        },

        "Functions": {

            "explanation": "Reusable blocks of code with optional inputs/outputs.",

            "example": """def greet(name):

    print(f"Hello {name}")



greet("Ali")""",

            "output": "Hello Ali"

        },

        "Lambda Functions": {

            "explanation": "Anonymous one-line functions.",

            "example": """square = lambda x: x**2

print(square(5))""",

            "output": "25"

        },

        "Map/Filter/Reduce": {

            "explanation": "Functional tools: map applies, filter selects, reduce accumulates.",

            "example": """nums = [1,2,3,4]

squared = list(map(lambda x: x**2, nums))

evens = list(filter(lambda x: x%2==0, nums))

print(squared, evens)""",

            "output": "[1, 4, 9, 16] [2, 4]"

        },

        "List Comprehension": {

            "explanation": "Create lists concisely in one line.",

            "example": """squares = [x**2 for x in range(5)]

print(squares)""",

            "output": "[0, 1, 4, 9, 16]"

        },

        "File I/O": {

            "explanation": "Read/write files using open() and with statement.",

            "example": 'with open("file.txt","w") as f:\n    f.write("Hello")\nwith open("file.txt") as f:\n    print(f.read())',

            "output": "Hello"

        },

        "Exception Handling": {

            "explanation": "Catch errors with try-except to prevent crashes.",

            "example": 'try:\n    print(10/0)\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")',

            "output": "Cannot divide by zero"

        },

        "Classes & Objects": {

            "explanation": "Classes define objects; objects are instances with attributes/methods.",

            "example": 'class Person:\n    def __init__(self):\n        self.name=name\np=Person("Ali")\nprint(p.name)',

            "output": "Ali"

        },

        "Inheritance": {

            "explanation": "Child class inherits attributes/methods from parent class.",

            "example": 'class Student(Person):\n    def __init__(self):\n        super().init_(name)\n        self.roll=roll\ns=Student("Ali",1)\nprint(s.name,s.roll)',

            "output": "Ali 1"

        },

        "Polymorphism": {

            "explanation": "Same operation can work on different types or classes.",

            "example": 'print(len("Hello"))\nprint(len([1,2,3]))',

            "output": "5 3"

        },

        "Encapsulation": {

            "explanation": "Restrict access to attributes for data protection.",

            "example": 'class Test:\n    def _init_(self):\n        self._x=0\n    def get_x(self):\n        return self._x\nt=Test()\nprint(t.get_x())',

            "output": "0"

        },

        "Recursion": {

            "explanation": "Function calling itself to solve problems.",

            "example": 'def rec(n):\n    return 1 if n<=1 else n*rec(n-1)\nprint(rec(5))',

            "output": "120"

        },

        "Factorial": {

            "explanation": "Calculates factorial of n using recursion.",

            "example": 'def factorial(n):\n    return 1 if n<=1 else n*factorial(n-1)\nprint(factorial(5))',

            "output": "120"

        },

        "Fibonacci": {

            "explanation": "Prints first n numbers of Fibonacci sequence.",

            "example": 'a,b=0,1\nfor _ in range(5):\n    print(a,end=" ")\n    a,b=b,a+b',

            "output": "0 1 1 2 3"

        },

        "Prime Check": {

            "explanation": "Check if a number is prime by testing divisibility.",

            "example": 'n=7\nfor i in range(2,n):\n    if n%i==0:\n        print("Not Prime")\n        break\nelse:\n    print("Prime")',

            "output": "Prime"

        },

        "Linear Search": {

            "explanation": "Search element sequentially in a list until found.",

            "example": 'arr=[1,2,3,4]\nfor x in arr:\n    if x==3:\n        print("Found")',

            "output": "Found"

        },

        "Binary Search": {

            "explanation": "Efficient search in sorted list by dividing search space.",

            "example": 'arr=[1,3,5,7,9]\nlow,high=0,len(arr)-1\nkey=5\nwhile low<=high:\n    mid=(low+high)//2\n    if arr[mid]==key:\n        print("Found")\n        break\n    elif arr[mid]<key:\n        low=mid+1\n    else:\n        high=mid-1',

            "output": "Found"

        },

        "Bubble Sort": {

            "explanation": "Compare adjacent elements and swap to sort list.",

            "example": 'arr=[5,2,4,1]\nn=len(arr)\nfor i in range(n):\n    for j in range(0,n-i-1):\n        if arr[j]>arr[j+1]: arr[j],arr[j+1]=arr[j+1],arr[j]\nprint(arr)',

            "output": "[1, 2, 4, 5]"

        },

        "Selection Sort": {

            "explanation": "Select min element repeatedly and place it in correct position.",

            "example": 'arr=[5,2,4,1]\nn=len(arr)\nfor i in range(n):\n    min_idx=i\n    for j in range(i+1,n):\n        if arr[j]<arr[min_idx]: min_idx=j\n    arr[i],arr[min_idx]=arr[min_idx],arr[i]\nprint(arr)',

            "output": "[1, 2, 4, 5]"

        },

        "Insertion Sort": {

            "explanation": "Insert each element at correct position in sorted part.",

            "example": 'arr=[5,2,4,1]\nfor i in range(1,len(arr)):\n    key=arr[i]\n    j=i-1\n    while j>=0 and arr[j]>key:\n        arr[j+1]=arr[j]\n        j-=1\n    arr[j+1]=key\nprint(arr)',

            "output": "[1, 2, 4, 5]"

        },

        "Merge Sort": {

            "explanation": "Divide array, sort halves, merge them.",

            "example": 'def merge_sort(arr):\n    if len(arr)>1:\n        mid=len(arr)//2\n        L,R=arr[:mid],arr[mid:]\n        merge_sort(L)\n        merge_sort(R)\n        i=j=k=0\n        while i<len(L) and j<len(R):\n            if L[i]<R[j]: arr[k]=L[i]; i+=1\n            else: arr[k]=R[j]; j+=1\n            k+=1\n        while i<len(L): arr[k]=L[i]; i+=1; k+=1\n        while j<len(R): arr[k]=R[j]; j+=1; k+=1\narr=[5,2,4,1]\nmerge_sort(arr)\nprint(arr)',

            "output": "[1, 2, 4, 5]"

        },

        "Quick Sort": {

            "explanation": "Divide and conquer sorting using pivot element.",

            "example": 'def quick_sort(arr):\n    if len(arr)<=1: return arr\n    pivot=arr[0]\n    less=[x for x in arr[1:] if x<=pivot]\n    greater=[x for x in arr[1:] if x>pivot]\n    return quick_sort(less)+[pivot]+quick_sort(greater)\nprint(quick_sort([5,2,4,1]))',

            "output": "[1, 2, 4, 5]"

        },

        "Stack": {

            "explanation": "LIFO structure using list append/pop.",

            "example": 'stack=[]\nstack.append(1)\nstack.append(2)\nprint(stack.pop())',

            "output": "2"

        },

        "Queue": {

            "explanation": "FIFO structure using deque for efficiency.",

            "example": 'from collections import deque\nq=deque()\nq.append(1)\nq.append(2)\nprint(q.popleft())',

            "output": "1"

        },

        "Linked List": {

            "explanation": "Basic linked list with nodes and pointers.",

            "example": 'class Node:\n    def _init_(self,data): self.data=data; self.next=None\nhead=Node(1)\nhead.next=Node(2)\nprint(head.data,head.next.data)',

            "output": "1 2"

        },

        "Palindrome": {

            "explanation": "Check if string/number reads same forwards/backwards.",

            "example": 's="radar"\nprint("Palindrome" if s==s[::-1] else "Not Palindrome")',

            "output": "Palindrome"

        },

        "Anagram": {

            "explanation": "Check if two strings have same letters.",

            "example": 's1="listen"; s2="silent"\nprint("Anagram" if sorted(s1)==sorted(s2) else "Not Anagram")',

            "output": "Anagram"

        },

        "JSON Read/Write": {

            "explanation": "Read/write JSON files with json module.",

            "example": 'import json\ndata={"name":"Ali"}\nwith open("data.json","w") as f: json.dump(data,f)\nwith open("data.json") as f: print(json.load(f))',

            "output": "{'name': 'Ali'}"

        },

        "HTTP Request": {

            "explanation": "Make HTTP calls using requests library.",

            "example": 'import requests\nres=requests.get("https://api.github.com")\nprint(res.status_code)',

            "output": "200"

        },

        "Regex Example": {

            "explanation": "Use regex patterns to match strings.",

            "example": 'import re\npattern="a.b"\nprint(bool(re.match(pattern,"acb")))',

            "output": "True"

        },

        "Decorators": {

            "explanation": "Wrap functions to extend behavior.",

            "example": 'def deco(func):\n    def wrapper():\n        print("Before")\n        func()\n        print("After")\n    return wrapper\n@deco\ndef say(): print("Hello")\nsay()',

            "output": "Before\nHello\nAfter"

        },

        "Generators": {

            "explanation": "Yield values lazily to save memory.",

            "example": 'def gen():\n    for i in range(3): yield i\nfor x in gen(): print(x)',

            "output": "0\n1\n2"

        },

        "Context Managers": {

            "explanation": "Use 'with' for resource management like files.",

            "example": 'with open("file.txt","w") as f:\n    f.write("Hello")',

            "output": "(writes Hello to file)"

        },

        "Unit Test": {

            "explanation": "Test functions/classes with unittest module.",

            "example": 'import unittest\nclass Test(unittest.TestCase):\n    def test_add(self): self.assertEqual(2+3,5)',

            "output": "(No direct output; passes test)"

        },

        "Matrix Multiplication": {

            "explanation": "Multiply two matrices using nested loops.",

            "example": 'a=[[1,2],[3,4]]\nb=[[5,6],[7,8]]\nresult=[[0,0],[0,0]]\nfor i in range(2):\n    for j in range(2):\n        for k in range(2): result[i][j]+=a[i][k]*b[k][j]\nprint(result)',

            "output": "[[19, 22], [43, 50]]"

        },

        "Sparse Matrix": {

            "explanation": "Store only non-zero elements efficiently using dict.",

            "example": 'sparse={(0,1):5,(2,3):10}\nprint(sparse.get((0,1),0))',

            "output": "5"

        },

        "CSV Processing": {

            "explanation": "Read/write CSV files with csv module.",

            "example": 'import csv\nwith open("data.csv","w") as f:\n    writer=csv.writer(f)\n    writer.writerow(["Name","Age"])',

            "output": "(CSV file created)"

        },

        "Datetime Example": {

            "explanation": "Work with dates and times using datetime module.",

            "example": 'from datetime import datetime\nnow=datetime.now()\nprint(now)',

            "output": "(Current datetime)"

        },

        "Threading": {

            "explanation": "Run multiple threads concurrently for I/O tasks.",

            "example": 'import threading\ndef f(): print("Thread running")\nt=threading.Thread(target=f)\nt.start()',

            "output": "Thread running"

        },

        "Multiprocessing": {

            "explanation": "Run multiple processes concurrently for CPU-bound tasks.",

            "example": 'from multiprocessing import Process\ndef f(): print("Process running")\np=Process(target=f)\np.start(); p.join()',

            "output": "Process running"
        }

    },

    "C++": {
        "Hello World": {
        "explanation": "The basic skeleton of every C++ program. It uses the iostream library and the cout object to print text to the console. Every C++ program must have a main() function as the entry point.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << "Hello, World!";\n    return 0;\n}',
        "output": "Hello, World!"
    },
    "Variables & Constants": {
        "explanation": "Variables store data values that can change during program execution. Constants are declared with the 'const' keyword and cannot be changed after initialization.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int age = 21;\n    const double PI = 3.14;\n    cout << "Age: " << age << endl;\n    cout << "PI: " << PI;\n    return 0;\n}',
        "output": "Age: 21\nPI: 3.14"
    },
    "Data Types": {
        "explanation": "Data types define what kind of value a variable can hold. Common types: int (whole numbers), double/float (decimals), char (single character), bool (true/false), string (text).",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 10;\n    double y = 3.14;\n    char ch = \'A\';\n    bool flag = true;\n    cout << x << " " << y << " " << ch << " " << flag;\n    return 0;\n}',
        "output": "10 3.14 A 1"
    },
    "Input/Output": {
        "explanation": "'cout' is used to display output to the screen. 'cin' is used to take input from the user via keyboard. Both require the iostream header file.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int num;\n    cout << "Enter a number: ";\n    // cin >> num;  // Takes input at runtime\n    num = 42;     // Simulated input\n    cout << "You entered: " << num;\n    return 0;\n}',
        "output": "Enter a number: You entered: 42"
    },
    "Arithmetic Operators": {
        "explanation": "Used to perform mathematical calculations: + (addition), - (subtraction), * (multiplication), / (division), % (modulus/remainder).",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 10, b = 3;\n    cout << "Add: " << a+b << endl;\n    cout << "Sub: " << a-b << endl;\n    cout << "Mul: " << a*b << endl;\n    cout << "Div: " << a/b << endl;\n    cout << "Mod: " << a%b << endl;\n    return 0;\n}',
        "output": "Add: 13\nSub: 7\nMul: 30\nDiv: 3\nMod: 1"
    },
    "Relational Operators": {
        "explanation": "Used to compare two values. They return a boolean result — true (1) or false (0). Operators: == (equal), != (not equal), < (less than), > (greater than), <= , >=.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 10, b = 20;\n    cout << (a == b) << endl;  // 0 (false)\n    cout << (a != b) << endl;  // 1 (true)\n    cout << (a < b)  << endl;  // 1 (true)\n    return 0;\n}',
        "output": "0\n1\n1"
    },
    "Logical Operators": {
        "explanation": "Used to combine multiple conditions. && (AND) returns true if both conditions are true. || (OR) returns true if at least one is true. ! (NOT) reverses the result.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int age = 20;\n    bool hasID = true;\n    if (age >= 18 && hasID) {\n        cout << "Entry Allowed";\n    } else {\n        cout << "Entry Denied";\n    }\n    return 0;\n}',
        "output": "Entry Allowed"
    },
    "If-Else": {
        "explanation": "Executes a block of code based on a condition. If the condition is true, the 'if' block runs. Otherwise, the 'else' block runs. 'else if' handles multiple conditions.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int marks = 75;\n    if (marks >= 90) {\n        cout << "Grade A";\n    } else if (marks >= 50) {\n        cout << "Grade B";\n    } else {\n        cout << "Fail";\n    }\n    return 0;\n}',
        "output": "Grade B"
    },
    "Switch Case": {
        "explanation": "Selects one block of code to execute from multiple options based on a variable's value. 'break' exits the switch. 'default' runs when no case matches.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int day = 3;\n    switch (day) {\n        case 1: cout << "Monday"; break;\n        case 2: cout << "Tuesday"; break;\n        case 3: cout << "Wednesday"; break;\n        default: cout << "Other Day";\n    }\n    return 0;\n}',
        "output": "Wednesday"
    },
    "For Loop": {
        "explanation": "Used when you know exactly how many times to repeat a block. It has three parts in one line: initialization, condition check, and increment/decrement.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    for (int i = 1; i <= 5; i++) {\n        cout << i << " ";\n    }\n    return 0;\n}',
        "output": "1 2 3 4 5"
    },
    "While Loop": {
        "explanation": "Repeats a block of code as long as the condition remains true. The condition is checked before each iteration. If false from the start, the loop never executes.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int i = 1;\n    while (i <= 5) {\n        cout << i << " ";\n        i++;\n    }\n    return 0;\n}',
        "output": "1 2 3 4 5"
    },
    "Do-While Loop": {
        "explanation": "Similar to while loop, but the condition is checked AFTER executing the body. This guarantees the loop runs at least once, even if the condition is false.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int i = 1;\n    do {\n        cout << i << " ";\n        i++;\n    } while (i <= 5);\n    return 0;\n}',
        "output": "1 2 3 4 5"
    },
    "Break & Continue": {
        "explanation": "'break' immediately exits the loop. 'continue' skips the rest of the current iteration and jumps to the next one. Both are used to control loop flow.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    for (int i = 1; i <= 5; i++) {\n        if (i == 3) continue;  // Skip 3\n        if (i == 5) break;     // Stop at 5\n        cout << i << " ";\n    }\n    return 0;\n}',
        "output": "1 2 4"
    },
    "Arrays": {
        "explanation": "A collection of variables of the same type stored in contiguous memory. Elements are accessed using an index starting from 0.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int marks[5] = {90, 85, 78, 92, 88};\n    for (int i = 0; i < 5; i++) {\n        cout << marks[i] << " ";\n    }\n    return 0;\n}',
        "output": "90 85 78 92 88"
    },
    "2D Arrays": {
        "explanation": "An array of arrays that stores data in rows and columns (like a table or matrix). Accessed using two indices: row and column.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};\n    for (int i = 0; i < 2; i++) {\n        for (int j = 0; j < 3; j++) {\n            cout << matrix[i][j] << " ";\n        }\n        cout << endl;\n    }\n    return 0;\n}',
        "output": "1 2 3\n4 5 6"
    },
    "Strings": {
        "explanation": "The string class from the <string> header stores text. Supports concatenation with '+', and useful methods like length(), substr(), find(), etc.",
        "example": '#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string name = "Ali";\n    string greeting = "Hello, " + name + "!";\n    cout << greeting << endl;\n    cout << "Length: " << name.length();\n    return 0;\n}',
        "output": "Hello, Ali!\nLength: 3"
    },
    "Pointers": {
        "explanation": "A pointer stores the memory address of another variable. Use '&' to get the address and '*' to dereference (access the value at that address).",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int num = 42;\n    int* ptr = &num;   // ptr stores address of num\n    cout << "Value: " << *ptr << endl;  // Dereference\n    cout << "Address: " << ptr;\n    return 0;\n}',
        "output": "Value: 42\nAddress: 0x61ff08 (example)"
    },
    "References": {
        "explanation": "A reference is an alias (another name) for an existing variable. Created with '&'. Any change to the reference also changes the original variable.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int original = 10;\n    int& ref = original;  // ref is an alias for original\n    ref = 50;             // original also becomes 50\n    cout << "Original: " << original;\n    return 0;\n}',
        "output": "Original: 50"
    },
    "Functions": {
        "explanation": "A reusable block of code that performs a specific task. Functions have a return type, a name, and optional parameters. They help avoid code repetition.",
        "example": '#include <iostream>\nusing namespace std;\n\nint add(int a, int b) {\n    return a + b;\n}\n\nint main() {\n    int result = add(5, 3);\n    cout << "Sum: " << result;\n    return 0;\n}',
        "output": "Sum: 8"
    },
    "Function Overloading": {
        "explanation": "Multiple functions can share the same name but must have different parameters (type or count). The compiler picks the correct version based on the arguments passed.",
        "example": '#include <iostream>\nusing namespace std;\n\nint area(int side) { return side * side; }\nint area(int l, int b) { return l * b; }\n\nint main() {\n    cout << area(5) << endl;   // Square\n    cout << area(4, 6);         // Rectangle\n    return 0;\n}',
        "output": "25\n24"
    },
    "Default Arguments": {
        "explanation": "Function parameters can be assigned default values. If a caller omits that argument, the default value is used automatically.",
        "example": '#include <iostream>\nusing namespace std;\n\nvoid greet(string name, string msg = "Hello") {\n    cout << msg << ", " << name << "!";\n}\n\nint main() {\n    greet("Ali");           // Uses default msg\n    cout << endl;\n    greet("Sara", "Hi");    // Uses custom msg\n    return 0;\n}',
        "output": "Hello, Ali!\nHi, Sara!"
    },
    "Recursion": {
        "explanation": "A function that calls itself to solve a smaller version of the same problem. Must have a base case to stop, otherwise it causes infinite recursion (stack overflow).",
        "example": '#include <iostream>\nusing namespace std;\n\nint factorial(int n) {\n    if (n <= 1) return 1;        // Base case\n    return n * factorial(n - 1); // Recursive call\n}\n\nint main() {\n    cout << "5! = " << factorial(5);\n    return 0;\n}',
        "output": "5! = 120"
    },
    "Inline Functions": {
        "explanation": "A hint to the compiler to replace the function call with the actual function body at compile time. Reduces overhead for small, frequently called functions.",
        "example": '#include <iostream>\nusing namespace std;\n\ninline int square(int x) {\n    return x * x;\n}\n\nint main() {\n    cout << square(5) << endl;\n    cout << square(9);\n    return 0;\n}',
        "output": "25\n81"
    },
    "Structures": {
        "explanation": "A struct groups related variables of different data types under one name. All members are public by default, unlike classes.",
        "example": '#include <iostream>\nusing namespace std;\n\nstruct Student {\n    int roll;\n    string name;\n    float gpa;\n};\n\nint main() {\n    Student s1 = {101, "Ali", 3.8};\n    cout << s1.name << " GPA: " << s1.gpa;\n    return 0;\n}',
        "output": "Ali GPA: 3.8"
    },
    "Unions": {
        "explanation": "All members of a union share the same memory location. Only one member can hold a value at a time. Useful for memory-efficient storage.",
        "example": '#include <iostream>\nusing namespace std;\n\nunion Data {\n    int i;\n    float f;\n};\n\nint main() {\n    Data d;\n    d.i = 42;\n    cout << "Int: " << d.i << endl;\n    d.f = 3.14;  // Overwrites i in memory\n    cout << "Float: " << d.f;\n    return 0;\n}',
        "output": "Int: 42\nFloat: 3.14"
    },
    "Enumerations (Enums)": {
        "explanation": "An enum defines a set of named integer constants. Makes code more readable and easier to manage than raw numbers.",
        "example": '#include <iostream>\nusing namespace std;\n\nenum Day { MON=1, TUE, WED, THU, FRI, SAT, SUN };\n\nint main() {\n    Day today = WED;\n    cout << "Day number: " << today;\n    if (today == WED) cout << endl << "It is Wednesday!";\n    return 0;\n}',
        "output": "Day number: 3\nIt is Wednesday!"
    },
    "Classes & Objects": {
        "explanation": "A class is a blueprint/template for creating objects. It contains data members (attributes) and member functions (methods). An object is an instance of a class.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Car {\npublic:\n    string brand;\n    int speed;\n    void show() {\n        cout << brand << " - " << speed << " km/h";\n    }\n};\n\nint main() {\n    Car c;\n    c.brand = "Toyota";\n    c.speed = 180;\n    c.show();\n    return 0;\n}',
        "output": "Toyota - 180 km/h"
    },
    "Constructors": {
        "explanation": "A special member function automatically called when an object is created. It has the same name as the class and no return type. Used to initialize data members.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Person {\npublic:\n    string name;\n    Person(string n) {  // Constructor\n        name = n;\n        cout << "Object created for: " << name;\n    }\n};\n\nint main() {\n    Person p("Ali");\n    return 0;\n}',
        "output": "Object created for: Ali"
    },
    "Destructors": {
        "explanation": "A special function automatically called when an object goes out of scope or is deleted. Starts with '~'. Used to release resources and clean up memory.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Demo {\npublic:\n    Demo()  { cout << "Object Created\\n"; }\n    ~Demo() { cout << "Object Destroyed"; }  // Destructor\n};\n\nint main() {\n    Demo d;\n    return 0;  // Destructor called here automatically\n}',
        "output": "Object Created\nObject Destroyed"
    },
    "Encapsulation": {
        "explanation": "Bundling data and methods together, and restricting direct access to data using private members. Public getter/setter methods provide controlled access.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass BankAccount {\nprivate:\n    double balance;  // Cannot be accessed directly\npublic:\n    BankAccount(double b) { balance = b; }\n    void deposit(double amt) { balance += amt; }\n    double getBalance() { return balance; }\n};\n\nint main() {\n    BankAccount acc(1000);\n    acc.deposit(500);\n    cout << "Balance: " << acc.getBalance();\n    return 0;\n}',
        "output": "Balance: 1500"
    },
    "Inheritance": {
        "explanation": "A child class inherits the properties and methods of a parent class. Promotes code reuse. The child class can also add its own members.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Animal {\npublic:\n    void eat() { cout << "Eating\\n"; }\n};\n\nclass Dog : public Animal {  // Dog inherits Animal\npublic:\n    void bark() { cout << "Barking"; }\n};\n\nint main() {\n    Dog d;\n    d.eat();   // Inherited from Animal\n    d.bark();  // Dog\'s own method\n    return 0;\n}',
        "output": "Eating\nBarking"
    },
    "Multilevel Inheritance": {
        "explanation": "A chain of inheritance: Class C inherits from Class B, which inherits from Class A. Class C gets access to members of both A and B.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass A {\npublic:\n    void showA() { cout << "Class A\\n"; }\n};\nclass B : public A {\npublic:\n    void showB() { cout << "Class B\\n"; }\n};\nclass C : public B {\npublic:\n    void showC() { cout << "Class C"; }\n};\n\nint main() {\n    C obj;\n    obj.showA();\n    obj.showB();\n    obj.showC();\n    return 0;\n}',
        "output": "Class A\nClass B\nClass C"
    },
    "Multiple Inheritance": {
        "explanation": "A class inherits from two or more parent classes simultaneously. The child class gets features from all parents. Use a comma to separate base classes.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Father {\npublic:\n    void work() { cout << "Father works\\n"; }\n};\nclass Mother {\npublic:\n    void cook() { cout << "Mother cooks\\n"; }\n};\nclass Child : public Father, public Mother {};\n\nint main() {\n    Child c;\n    c.work();\n    c.cook();\n    return 0;\n}',
        "output": "Father works\nMother cooks"
    },
    "Hierarchical Inheritance": {
        "explanation": "Multiple child classes inherit from a single parent class. All children share the parent's properties but can have their own unique methods.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Shape {\npublic:\n    void color() { cout << "Color: Red\\n"; }\n};\nclass Circle : public Shape {\npublic:\n    void draw() { cout << "Drawing Circle\\n"; }\n};\nclass Square : public Shape {\npublic:\n    void draw() { cout << "Drawing Square"; }\n};\n\nint main() {\n    Circle c; c.color(); c.draw();\n    Square s; s.draw();\n    return 0;\n}',
        "output": "Color: Red\nDrawing Circle\nDrawing Square"
    },
    "Polymorphism": {
        "explanation": "The ability of one entity to behave differently in different contexts. Achieved through function overloading (compile-time) and virtual functions (runtime).",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Shape {\npublic:\n    virtual void area() {\n        cout << "Shape area\\n";\n    }\n};\nclass Circle : public Shape {\npublic:\n    void area() override {\n        cout << "Circle area = pi * r^2";\n    }\n};\n\nint main() {\n    Shape* s = new Circle();\n    s->area();  // Calls Circle\'s area at runtime\n    delete s;\n    return 0;\n}',
        "output": "Circle area = pi * r^2"
    },
    "Function Overriding": {
        "explanation": "A derived class provides its own implementation of a function already defined in the base class. The child's version replaces the parent's version for that object.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Parent {\npublic:\n    void greet() { cout << "Hello from Parent\\n"; }\n};\nclass Child : public Parent {\npublic:\n    void greet() { cout << "Hello from Child"; }  // Override\n};\n\nint main() {\n    Child c;\n    c.greet();  // Child\'s version is called\n    return 0;\n}',
        "output": "Hello from Child"
    },
    "Virtual Functions": {
        "explanation": "Declared with 'virtual' in the base class. Enables runtime polymorphism — the correct overridden function is called based on the actual object type, not the pointer type.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Animal {\npublic:\n    virtual void sound() { cout << "Some sound\\n"; }\n};\nclass Cat : public Animal {\npublic:\n    void sound() override { cout << "Meow"; }\n};\n\nint main() {\n    Animal* a = new Cat();\n    a->sound();  // Calls Cat::sound() at runtime\n    delete a;\n    return 0;\n}',
        "output": "Meow"
    },
    "Abstract Classes": {
        "explanation": "A class with at least one pure virtual function (= 0). Cannot be instantiated directly. Serves as a base class that forces derived classes to implement certain methods.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Shape {\npublic:\n    virtual void area() = 0;  // Pure virtual — makes class abstract\n};\nclass Rectangle : public Shape {\npublic:\n    void area() override {\n        cout << "Area = length x width";\n    }\n};\n\nint main() {\n    Rectangle r;\n    r.area();\n    return 0;\n}',
        "output": "Area = length x width"
    },
    "Friend Function": {
        "explanation": "A function declared with the 'friend' keyword inside a class. It is NOT a member of the class but can access its private and protected members.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Box {\nprivate:\n    int width = 10;\npublic:\n    friend void printWidth(Box b);  // Friend declaration\n};\n\nvoid printWidth(Box b) {\n    cout << "Width: " << b.width;  // Accessing private member\n}\n\nint main() {\n    Box b;\n    printWidth(b);\n    return 0;\n}',
        "output": "Width: 10"
    },
    "Static Members": {
        "explanation": "Static members belong to the class itself, not to any specific object. Only one copy is shared among all instances. Accessed using the class name with '::'.",
        "example": '#include <iostream>\nusing namespace std;\n\nclass Counter {\npublic:\n    static int count;  // Shared by all objects\n    Counter() { count++; }\n};\nint Counter::count = 0;  // Initialize outside class\n\nint main() {\n    Counter c1, c2, c3;\n    cout << "Total objects: " << Counter::count;\n    return 0;\n}',
        "output": "Total objects: 3"
    },
    "Dynamic Memory": {
        "explanation": "Memory allocated at runtime using 'new' (on the heap). Must be manually released using 'delete' to prevent memory leaks. Set pointer to nullptr after deletion.",
        "example": '#include <iostream>\nusing namespace std;\n\nint main() {\n    int* p = new int(100);  // Allocate on heap\n    cout << "Value: " << *p << endl;\n    delete p;               // Free the memory\n    p = nullptr;            // Avoid dangling pointer\n    cout << "Memory freed!";\n    return 0;\n}',
        "output": "Value: 100\nMemory freed!"
    },
    "Exception Handling": {
        "explanation": "Handles runtime errors gracefully using try-catch blocks. Code that might throw an error goes in 'try'. The 'catch' block handles the error and prevents crashes.",
        "example": '#include <iostream>\nusing namespace std;\n\nint divide(int a, int b) {\n    if (b == 0) throw runtime_error("Division by zero!");\n    return a / b;\n}\n\nint main() {\n    try {\n        cout << divide(10, 2) << endl;\n        cout << divide(5, 0);   // Throws exception\n    } catch (runtime_error& e) {\n        cout << "Error: " << e.what();\n    }\n    return 0;\n}',
        "output": "5\nError: Division by zero!"
    },
    "Function Templates": {
        "explanation": "Write a single generic function that works with any data type. The compiler generates the appropriate version based on the argument type passed.",
        "example": '#include <iostream>\nusing namespace std;\n\ntemplate <typename T>\nT maxValue(T a, T b) {\n    return (a > b) ? a : b;\n}\n\nint main() {\n    cout << maxValue(10, 20) << endl;    // int\n    cout << maxValue(3.5, 2.1) << endl;  // double\n    cout << maxValue(\'z\', \'a\');         // char\n    return 0;\n}',
        "output": "20\n3.5\nz"
    },
    "Class Templates": {
        "explanation": "Create a generic class that can work with any data type. The STL containers like vector, stack, and queue are all class templates.",
        "example": '#include <iostream>\nusing namespace std;\n\ntemplate <class T>\nclass Box {\nprivate:\n    T value;\npublic:\n    Box(T v) : value(v) {}\n    void show() { cout << "Value: " << value; }\n};\n\nint main() {\n    Box<int> b1(42);\n    Box<string> b2("Hello");\n    b1.show(); cout << endl;\n    b2.show();\n    return 0;\n}',
        "output": "Value: 42\nValue: Hello"
    },
    "Namespaces": {
        "explanation": "Namespaces organize code into logical groups and prevent naming conflicts between different libraries or modules. Use '::' to access members.",
        "example": '#include <iostream>\nusing namespace std;\n\nnamespace Math {\n    int add(int a, int b) { return a + b; }\n}\nnamespace Science {\n    int add(int a, int b) { return a + b + 10; }\n}\n\nint main() {\n    cout << Math::add(5, 3) << endl;    // 8\n    cout << Science::add(5, 3);         // 18\n    return 0;\n}',
        "output": "8\n18"
    },
    "File Writing": {
        "explanation": "The 'ofstream' class creates or opens a file for writing. Requires the <fstream> header. Always close the file after writing.",
        "example": '#include <iostream>\n#include <fstream>\nusing namespace std;\n\nint main() {\n    ofstream file("output.txt");  // Create file\n    if (file.is_open()) {\n        file << "Hello, File!" << endl;\n        file << "Second line";\n        file.close();\n        cout << "File written successfully!";\n    }\n    return 0;\n}',
        "output": "File written successfully!"
    },
    "File Reading": {
        "explanation": "The 'ifstream' class opens an existing file for reading. Use getline() to read line by line. Always close the file after reading.",
        "example": '#include <iostream>\n#include <fstream>\n#include <string>\nusing namespace std;\n\nint main() {\n    ifstream file("output.txt");  // Open file\n    string line;\n    while (getline(file, line)) {\n        cout << line << endl;  // Print each line\n    }\n    file.close();\n    return 0;\n}',
        "output": "Hello, File!\nSecond line"
    },
    "STL Vector": {
        "explanation": "A dynamic array from the Standard Template Library that resizes automatically. Requires <vector>. Common methods: push_back(), pop_back(), size(), at().",
        "example": '#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<int> v = {1, 2, 3};\n    v.push_back(4);  // Add to end\n    v.push_back(5);\n    \n    cout << "Size: " << v.size() << endl;\n    for (int x : v) {\n        cout << x << " ";\n    }\n    return 0;\n}',
        "output": "Size: 5\n1 2 3 4 5"
    },
    "STL Stack": {
        "explanation": "A Last-In-First-Out (LIFO) container from the STL. Requires <stack>. Key methods: push() (add), pop() (remove top), top() (view top).",
        "example": '#include <iostream>\n#include <stack>\nusing namespace std;\n\nint main() {\n    stack<int> s;\n    s.push(10);\n    s.push(20);\n    s.push(30);\n    \n    cout << "Top: " << s.top() << endl;  // 30\n    s.pop();\n    cout << "After pop: " << s.top();    // 20\n    return 0;\n}',
        "output": "Top: 30\nAfter pop: 20"
    },
    "STL Queue": {
        "explanation": "A First-In-First-Out (FIFO) container from the STL. Requires <queue>. Key methods: push() (add to back), pop() (remove front), front() (view front).",
        "example": '#include <iostream>\n#include <queue>\nusing namespace std;\n\nint main() {\n    queue<string> q;\n    q.push("Ali");\n    q.push("Sara");\n    q.push("Usman");\n    \n    cout << "Front: " << q.front() << endl;  // Ali\n    q.pop();\n    cout << "After pop: " << q.front();      // Sara\n    return 0;\n}',
        "output": "Front: Ali\nAfter pop: Sara"
    },
      },
    "JavaScript" : {
    "Hello World": {
        "explanation": "The simplest JavaScript program. Use console.log() to print output to the browser console or terminal. It is the starting point of every JavaScript developer.",
        "example": '// Run in browser console or Node.js\nconsole.log("Hello, World!");',
        "output": "Hello, World!"
    },
    "Variables (var, let, const)": {
        "explanation": "'var' is function-scoped and old-style. 'let' is block-scoped and can be reassigned. 'const' is block-scoped and cannot be reassigned after declaration. Prefer let and const in modern JS.",
        "example": 'var name = "Ali";       // Old way\nlet age = 20;           // Can be reassigned\nconst PI = 3.14;        // Cannot be reassigned\n\nconsole.log(name);\nconsole.log(age);\nconsole.log(PI);',
        "output": "Ali\n20\n3.14"
    },
    "Data Types": {
        "explanation": "JavaScript has 7 primitive types: String, Number, Boolean, Null, Undefined, Symbol, BigInt. Everything else (arrays, functions, objects) is of type Object.",
        "example": 'let str = "Hello";         // String\nlet num = 42;             // Number\nlet bool = true;          // Boolean\nlet nothing = null;       // Null\nlet undef;                // Undefined\n\nconsole.log(typeof str);\nconsole.log(typeof num);\nconsole.log(typeof bool);',
        "output": "string\nnumber\nboolean"
    },
    "Type Conversion": {
        "explanation": "JavaScript can convert between types explicitly (manual) or implicitly (automatic/coercion). Use Number(), String(), Boolean() for explicit conversion.",
        "example": 'let str = "42";\nlet num = Number(str);    // String to Number\nlet back = String(num);   // Number to String\nlet bool = Boolean(0);    // 0 is falsy -> false\n\nconsole.log(num + 8);\nconsole.log(typeof back);\nconsole.log(bool);',
        "output": "50\nstring\nfalse"
    },
    "Template Literals": {
        "explanation": "Template literals use backticks (`) instead of quotes. They allow embedding expressions with ${} and support multi-line strings without escape characters.",
        "example": 'let name = "Sara";\nlet age = 22;\n\nlet message = `My name is ${name} and I am ${age} years old.`;\nconsole.log(message);\n\n// Multi-line\nlet multiLine = `Line 1\nLine 2`;\nconsole.log(multiLine);',
        "output": "My name is Sara and I am 22 years old.\nLine 1\nLine 2"
    },
    "Arithmetic Operators": {
        "explanation": "Standard math operators: + (addition), - (subtraction), * (multiplication), / (division), % (modulus), ** (exponentiation). The + operator also concatenates strings.",
        "example": 'let a = 10, b = 3;\nconsole.log(a + b);   // 13\nconsole.log(a - b);   // 7\nconsole.log(a * b);   // 30\nconsole.log(a / b);   // 3.333\nconsole.log(a % b);   // 1\nconsole.log(a ** b);  // 1000',
        "output": "13\n7\n30\n3.3333333333333335\n1\n1000"
    },
    "Comparison Operators": {
        "explanation": "== checks value only (loose). === checks both value AND type (strict — always preferred). != and !== are their negations. <, >, <=, >= compare numbers and strings.",
        "example": 'console.log(5 == "5");   // true  (loose)\nconsole.log(5 === "5");  // false (strict)\nconsole.log(5 !== "5");  // true\nconsole.log(10 > 3);     // true\nconsole.log(10 <= 10);   // true',
        "output": "true\nfalse\ntrue\ntrue\ntrue"
    },
    "Logical Operators": {
        "explanation": "&& (AND) returns true only if both sides are true. || (OR) returns true if at least one side is true. ! (NOT) reverses a boolean. Often used in conditions.",
        "example": 'let age = 20;\nlet hasID = true;\n\nconsole.log(age >= 18 && hasID);  // true\nconsole.log(age < 18 || hasID);   // true\nconsole.log(!hasID);               // false',
        "output": "true\ntrue\nfalse"
    },
    "If-Else": {
        "explanation": "Executes code conditionally. 'if' runs when condition is true. 'else if' checks another condition. 'else' runs when all conditions are false.",
        "example": 'let score = 75;\n\nif (score >= 90) {\n    console.log("Grade A");\n} else if (score >= 60) {\n    console.log("Grade B");\n} else {\n    console.log("Fail");\n}',
        "output": "Grade B"
    },
    "Switch Case": {
        "explanation": "Evaluates an expression and matches it against multiple 'case' values. 'break' exits the switch. 'default' handles unmatched values.",
        "example": 'let day = 3;\n\nswitch (day) {\n    case 1: console.log("Monday"); break;\n    case 2: console.log("Tuesday"); break;\n    case 3: console.log("Wednesday"); break;\n    default: console.log("Other");\n}',
        "output": "Wednesday"
    },
    "For Loop": {
        "explanation": "Runs a block of code a fixed number of times. Has three parts: initialization, condition, and update. Also includes for...of (iterates values) and for...in (iterates keys).",
        "example": '// Classic for loop\nfor (let i = 1; i <= 5; i++) {\n    process.stdout.write(i + " ");\n}\nconsole.log();\n\n// for...of loop\nlet fruits = ["apple", "banana", "cherry"];\nfor (let fruit of fruits) {\n    console.log(fruit);\n}',
        "output": "1 2 3 4 5\napple\nbanana\ncherry"
    },
    "While Loop": {
        "explanation": "Repeats code while a condition is true. The condition is checked before each iteration. If the condition is false initially, the loop body never executes.",
        "example": 'let i = 1;\nwhile (i <= 5) {\n    process.stdout.write(i + " ");\n    i++;\n}\nconsole.log();\nconsole.log("Loop finished");',
        "output": "1 2 3 4 5\nLoop finished"
    },
    "Do-While Loop": {
        "explanation": "Executes the body first, then checks the condition. Guarantees the loop runs at least once regardless of the condition.",
        "example": 'let i = 1;\ndo {\n    process.stdout.write(i + " ");\n    i++;\n} while (i <= 5);\nconsole.log();\nconsole.log("Done");',
        "output": "1 2 3 4 5\nDone"
    },
    "Break & Continue": {
        "explanation": "'break' stops the loop entirely. 'continue' skips the current iteration and moves to the next one.",
        "example": 'for (let i = 1; i <= 6; i++) {\n    if (i === 3) continue;  // Skip 3\n    if (i === 6) break;     // Stop at 6\n    console.log(i);\n}',
        "output": "1\n2\n4\n5"
    },
    "Functions": {
        "explanation": "Reusable blocks of code. Defined with the 'function' keyword. Can accept parameters and return values. Functions are first-class citizens in JavaScript.",
        "example": 'function greet(name) {\n    return `Hello, ${name}!`;\n}\n\nfunction add(a, b) {\n    return a + b;\n}\n\nconsole.log(greet("Ali"));\nconsole.log(add(5, 3));',
        "output": "Hello, Ali!\n8"
    },
    "Arrow Functions": {
        "explanation": "A shorter syntax for writing functions using '=>'. They do NOT have their own 'this' context. Great for callbacks and short operations.",
        "example": '// Regular function\nfunction square(x) { return x * x; }\n\n// Arrow function\nconst cube = (x) => x * x * x;\n\n// Arrow with multiple lines\nconst add = (a, b) => {\n    let sum = a + b;\n    return sum;\n};\n\nconsole.log(square(4));\nconsole.log(cube(3));\nconsole.log(add(5, 7));',
        "output": "16\n27\n12"
    },
    "Default Parameters": {
        "explanation": "Function parameters can have default values. If the caller does not pass an argument, the default value is used automatically.",
        "example": 'function greet(name = "Guest", msg = "Hello") {\n    console.log(`${msg}, ${name}!`);\n}\n\ngreet();                  // Uses both defaults\ngreet("Ali");             // Uses default msg\ngreet("Sara", "Hi");      // No defaults used',
        "output": "Hello, Guest!\nHello, Ali!\nHi, Sara!"
    },
    "Rest & Spread Operator": {
        "explanation": "Both use '...'. REST collects multiple arguments into an array inside a function. SPREAD expands an array or object into individual elements.",
        "example": '// REST — collects remaining args\nfunction sum(...nums) {\n    return nums.reduce((a, b) => a + b, 0);\n}\nconsole.log(sum(1, 2, 3, 4));  // 10\n\n// SPREAD — expands array\nlet arr1 = [1, 2, 3];\nlet arr2 = [...arr1, 4, 5];\nconsole.log(arr2);',
        "output": "10\n[1, 2, 3, 4, 5]"
    },
    "Arrays": {
        "explanation": "Ordered collections of values. Arrays can hold any type. Indexed from 0. Created with [] syntax.",
        "example": 'let fruits = ["apple", "banana", "cherry"];\n\nconsole.log(fruits[0]);          // First element\nconsole.log(fruits.length);      // Length\nfruits.push("mango");            // Add to end\nconsole.log(fruits);',
        "output": "apple\n3\n['apple', 'banana', 'cherry', 'mango']"
    },
    "Array Methods": {
        "explanation": "JavaScript arrays have powerful built-in methods. push/pop (add/remove end), shift/unshift (remove/add start), map (transform), filter (select), reduce (accumulate), find, includes, indexOf.",
        "example": 'let nums = [1, 2, 3, 4, 5];\n\nlet doubled = nums.map(n => n * 2);\nconsole.log(doubled);\n\nlet evens = nums.filter(n => n % 2 === 0);\nconsole.log(evens);\n\nlet total = nums.reduce((sum, n) => sum + n, 0);\nconsole.log(total);',
        "output": "[2, 4, 6, 8, 10]\n[2, 4]\n15"
    },
    "Objects": {
        "explanation": "Objects store data as key-value pairs. Keys are strings (or Symbols). Values can be any type including functions (called methods). Created with {} syntax.",
        "example": 'let person = {\n    name: "Ali",\n    age: 25,\n    greet() {\n        return `Hi, I am ${this.name}`;\n    }\n};\n\nconsole.log(person.name);\nconsole.log(person["age"]);\nconsole.log(person.greet());',
        "output": "Ali\n25\nHi, I am Ali"
    },
    "Object Destructuring": {
        "explanation": "Extract values from objects into variables in a clean, readable way. Can rename variables and set default values during destructuring.",
        "example": 'let person = { name: "Sara", age: 22, city: "Lahore" };\n\n// Destructure\nlet { name, age, city } = person;\nconsole.log(name, age, city);\n\n// Rename + default\nlet { name: fullName, country = "Pakistan" } = person;\nconsole.log(fullName, country);',
        "output": "Sara 22 Lahore\nSara Pakistan"
    },
    "Array Destructuring": {
        "explanation": "Extract values from arrays into variables by position. You can skip elements using commas and collect remaining items with the rest operator.",
        "example": 'let colors = ["red", "green", "blue", "yellow"];\n\nlet [first, second, ...rest] = colors;\nconsole.log(first);   // red\nconsole.log(second);  // green\nconsole.log(rest);    // [\'blue\', \'yellow\']\n\n// Swap variables\nlet a = 1, b = 2;\n[a, b] = [b, a];\nconsole.log(a, b);',
        "output": "red\ngreen\n['blue', 'yellow']\n2 1"
    },
    "Spread with Arrays & Objects": {
        "explanation": "The spread operator (...) copies and merges arrays or objects. It creates a shallow copy — nested objects are still referenced.",
        "example": '// Merge arrays\nlet arr1 = [1, 2, 3];\nlet arr2 = [4, 5, 6];\nlet merged = [...arr1, ...arr2];\nconsole.log(merged);\n\n// Merge objects\nlet obj1 = { a: 1, b: 2 };\nlet obj2 = { c: 3, d: 4 };\nlet combined = { ...obj1, ...obj2 };\nconsole.log(combined);',
        "output": "[1, 2, 3, 4, 5, 6]\n{ a: 1, b: 2, c: 3, d: 4 }"
    },
    "String Methods": {
        "explanation": "JavaScript strings have many built-in methods: toUpperCase(), toLowerCase(), trim(), includes(), startsWith(), endsWith(), slice(), replace(), split(), repeat().",
        "example": 'let str = "  Hello, World!  ";\n\nconsole.log(str.trim());                    // Remove spaces\nconsole.log(str.trim().toUpperCase());      // Uppercase\nconsole.log(str.includes("World"));         // true\nconsole.log(str.trim().slice(0, 5));        // Hello\nconsole.log(str.trim().replace("World", "JS"));',
        "output": "Hello, World!\nHELLO, WORLD!\ntrue\nHello\nHello, JS!"
    },
    "Math Object": {
        "explanation": "The built-in Math object provides mathematical constants and functions like Math.PI, Math.round(), Math.floor(), Math.ceil(), Math.sqrt(), Math.pow(), Math.random(), Math.max(), Math.min().",
        "example": 'console.log(Math.PI);              // 3.14159...\nconsole.log(Math.round(4.6));      // 5\nconsole.log(Math.floor(4.9));      // 4\nconsole.log(Math.ceil(4.1));       // 5\nconsole.log(Math.sqrt(16));        // 4\nconsole.log(Math.max(1, 9, 5));    // 9\nconsole.log(Math.pow(2, 10));      // 1024',
        "output": "3.141592653589793\n5\n4\n5\n4\n9\n1024"
    },
    "Date Object": {
        "explanation": "The Date object handles dates and times. Create with new Date(). Methods: getFullYear(), getMonth() (0-indexed), getDate(), getDay(), getHours(), toLocaleDateString().",
        "example": 'let now = new Date();\n\nconsole.log(now.getFullYear());        // e.g. 2026\nconsole.log(now.getMonth() + 1);      // Month (1-12)\nconsole.log(now.getDate());           // Day of month\n\nlet specific = new Date("2024-01-15");\nconsole.log(specific.toLocaleDateString());',
        "output": "2026\n4\n28\n1/15/2024"
    },
    "Null & Undefined": {
        "explanation": "'undefined' means a variable has been declared but not assigned a value. 'null' is an intentional absence of value — it must be explicitly set. They are loosely equal but not strictly equal.",
        "example": 'let a;                  // undefined (not assigned)\nlet b = null;           // null (intentionally empty)\n\nconsole.log(a);         // undefined\nconsole.log(b);         // null\nconsole.log(a == b);    // true  (loose)\nconsole.log(a === b);   // false (strict)',
        "output": "undefined\nnull\ntrue\nfalse"
    },
    "Typeof Operator": {
        "explanation": "The typeof operator returns a string indicating the data type of a value. Useful for type-checking before performing operations.",
        "example": 'console.log(typeof "hello");      // string\nconsole.log(typeof 42);           // number\nconsole.log(typeof true);         // boolean\nconsole.log(typeof undefined);    // undefined\nconsole.log(typeof null);         // object (known JS quirk!)\nconsole.log(typeof []);           // object\nconsole.log(typeof function(){});  // function',
        "output": "string\nnumber\nboolean\nundefined\nobject\nobject\nfunction"
    },
    "Ternary Operator": {
        "explanation": "A shorthand for if-else. Syntax: condition ? valueIfTrue : valueIfFalse. Great for simple inline conditions. Can be nested but avoid over-nesting for readability.",
        "example": 'let age = 20;\nlet status = age >= 18 ? "Adult" : "Minor";\nconsole.log(status);\n\nlet score = 85;\nlet grade = score >= 90 ? "A" : score >= 60 ? "B" : "F";\nconsole.log(grade);',
        "output": "Adult\nB"
    },
    "Short Circuit Evaluation": {
        "explanation": "&& returns the first falsy value or the last value. || returns the first truthy value or the last value. Used for default values and conditional execution. ?? (nullish coalescing) returns right side only for null/undefined.",
        "example": 'let name = "";\nlet display = name || "Anonymous";    // name is falsy\nconsole.log(display);\n\nlet user = { isAdmin: true };\nuser.isAdmin && console.log("Access Granted");\n\nlet val = null ?? "Default";           // ?? only for null/undefined\nconsole.log(val);',
        "output": "Anonymous\nAccess Granted\nDefault"
    },
    "Callbacks": {
        "explanation": "A callback is a function passed as an argument to another function, to be called later. Fundamental to JavaScript's asynchronous programming model.",
        "example": 'function greet(name, callback) {\n    console.log(`Hello, ${name}!`);\n    callback();\n}\n\nfunction sayBye() {\n    console.log("Goodbye!");\n}\n\ngreet("Ali", sayBye);\n\n// Common use: setTimeout\nsetTimeout(() => console.log("Runs after 0ms"), 0);',
        "output": "Hello, Ali!\nGoodbye!\nRuns after 0ms"
    },
    "Promises": {
        "explanation": "A Promise represents a value that may be available now, later, or never. States: pending, fulfilled, rejected. Use .then() for success, .catch() for errors, .finally() for cleanup.",
        "example": 'let promise = new Promise((resolve, reject) => {\n    let success = true;\n    if (success) {\n        resolve("Data loaded!");\n    } else {\n        reject("Error occurred!");\n    }\n});\n\npromise\n    .then(result => console.log(result))\n    .catch(err => console.log(err))\n    .finally(() => console.log("Done"));',
        "output": "Data loaded!\nDone"
    },
    "Async & Await": {
        "explanation": "async/await is syntactic sugar over Promises. An 'async' function always returns a Promise. 'await' pauses execution until the Promise resolves. Makes async code look synchronous.",
        "example": 'function fetchData() {\n    return new Promise(resolve => {\n        setTimeout(() => resolve("Data received!"), 100);\n    });\n}\n\nasync function main() {\n    console.log("Fetching...");\n    let data = await fetchData();\n    console.log(data);\n    console.log("Finished");\n}\n\nmain();',
        "output": "Fetching...\nData received!\nFinished"
    },
    "Try-Catch-Finally": {
        "explanation": "Handles runtime errors gracefully. 'try' contains the risky code. 'catch' handles any error thrown. 'finally' always runs regardless of success or failure.",
        "example": 'function divide(a, b) {\n    if (b === 0) throw new Error("Cannot divide by zero!");\n    return a / b;\n}\n\ntry {\n    console.log(divide(10, 2));\n    console.log(divide(5, 0));     // Throws error\n} catch (error) {\n    console.log("Error:", error.message);\n} finally {\n    console.log("Execution complete");\n}',
        "output": "5\nError: Cannot divide by zero!\nExecution complete"
    },
    "DOM Selection": {
        "explanation": "The DOM (Document Object Model) represents the HTML page. Use JavaScript to select elements: getElementById(), querySelector() (first match), querySelectorAll() (all matches), getElementsByClassName().",
        "example": '// In a browser environment:\n// <h1 id="title">Hello</h1>\n// <p class="text">World</p>\n\nconst title = document.getElementById("title");\nconst firstText = document.querySelector(".text");\nconst allTexts = document.querySelectorAll("p");\n\nconsole.log(title.textContent);      // Hello\nconsole.log(allTexts.length);        // Number of <p> elements',
        "output": "Hello\n1"
    },
    "DOM Manipulation": {
        "explanation": "After selecting elements, you can change their content, style, attributes, or structure. Key properties/methods: textContent, innerHTML, style, setAttribute, classList, appendChild, remove().",
        "example": '// In a browser environment:\nconst box = document.querySelector("#box");\n\nbox.textContent = "Updated Text";          // Change text\nbox.style.color = "red";                   // Change style\nbox.classList.add("active");               // Add class\nbox.setAttribute("data-id", "42");         // Set attribute\n\n// Create and append new element\nconst newEl = document.createElement("p");\nnewEl.textContent = "New paragraph";\ndocument.body.appendChild(newEl);',
        "output": "(DOM updated in browser)"
    },
    "Event Listeners": {
        "explanation": "addEventListener() attaches an event handler to an element. Common events: click, mouseover, keydown, submit, load, change. removeEventListener() removes them.",
        "example": '// In a browser environment:\nconst btn = document.querySelector("#myBtn");\n\nbtn.addEventListener("click", function(event) {\n    console.log("Button clicked!");\n    console.log("Target:", event.target);\n});\n\n// Arrow function version\nbtn.addEventListener("mouseover", () => {\n    console.log("Mouse is over the button");\n});',
        "output": "Button clicked!\nMouse is over the button"
    },
    "Classes & Objects (OOP)": {
        "explanation": "ES6 classes provide a cleaner syntax for OOP. A class is a blueprint; objects are instances. Contains a constructor() for initialization and methods for behavior.",
        "example": 'class Animal {\n    constructor(name, sound) {\n        this.name = name;\n        this.sound = sound;\n    }\n\n    speak() {\n        return `${this.name} says ${this.sound}`;\n    }\n}\n\nconst dog = new Animal("Dog", "Woof");\nconst cat = new Animal("Cat", "Meow");\n\nconsole.log(dog.speak());\nconsole.log(cat.speak());',
        "output": "Dog says Woof\nCat says Meow"
    },
    "Constructor Functions": {
        "explanation": "Before ES6 classes, constructor functions were used to create objects. Called with 'new'. 'this' refers to the new object being created.",
        "example": 'function Person(name, age) {\n    this.name = name;\n    this.age = age;\n    this.greet = function() {\n        return `Hi, I am ${this.name}`;\n    };\n}\n\nconst p1 = new Person("Ali", 25);\nconst p2 = new Person("Sara", 22);\n\nconsole.log(p1.greet());\nconsole.log(p2.age);',
        "output": "Hi, I am Ali\n22"
    },
    "Inheritance (extends)": {
        "explanation": "A child class inherits from a parent using 'extends'. 'super()' calls the parent constructor. The child can override parent methods or add new ones.",
        "example": 'class Vehicle {\n    constructor(brand) {\n        this.brand = brand;\n    }\n    describe() {\n        return `This is a ${this.brand}`;\n    }\n}\n\nclass Car extends Vehicle {\n    constructor(brand, doors) {\n        super(brand);         // Call parent constructor\n        this.doors = doors;\n    }\n    describe() {\n        return `${super.describe()} with ${this.doors} doors`;\n    }\n}\n\nconst myCar = new Car("Toyota", 4);\nconsole.log(myCar.describe());',
        "output": "This is a Toyota with 4 doors"
    },
    "Getters & Setters": {
        "explanation": "Getters and setters let you define computed properties and add validation logic. 'get' runs when accessing a property. 'set' runs when assigning to it.",
        "example": 'class Circle {\n    constructor(radius) {\n        this._radius = radius;\n    }\n\n    get radius() {\n        return this._radius;\n    }\n\n    set radius(value) {\n        if (value < 0) throw new Error("Radius cannot be negative");\n        this._radius = value;\n    }\n\n    get area() {\n        return (Math.PI * this._radius ** 2).toFixed(2);\n    }\n}\n\nconst c = new Circle(5);\nconsole.log(c.radius);    // 5\nconsole.log(c.area);      // 78.54\nc.radius = 10;\nconsole.log(c.area);      // 314.16',
        "output": "5\n78.54\n314.16"
    },
    "Modules (import/export)": {
        "explanation": "ES6 modules let you split code into separate files. 'export' makes items available. 'import' brings them in. Named exports use {}, default export has no braces.",
        "example": '// math.js (exporting)\nexport const PI = 3.14159;\nexport function add(a, b) { return a + b; }\nexport default function multiply(a, b) { return a * b; }\n\n// main.js (importing)\nimport multiply, { PI, add } from "./math.js";\n\nconsole.log(PI);            // 3.14159\nconsole.log(add(3, 4));     // 7\nconsole.log(multiply(3, 4)); // 12',
        "output": "3.14159\n7\n12"
    },
    "JSON Parse & Stringify": {
        "explanation": "JSON (JavaScript Object Notation) is a data format for storing/exchanging data. JSON.stringify() converts object to JSON string. JSON.parse() converts JSON string back to object.",
        "example": 'let user = {\n    name: "Ali",\n    age: 25,\n    skills: ["JS", "Python"]\n};\n\n// Object to JSON string\nlet jsonString = JSON.stringify(user);\nconsole.log(jsonString);\nconsole.log(typeof jsonString);\n\n// JSON string to Object\nlet parsed = JSON.parse(jsonString);\nconsole.log(parsed.name);\nconsole.log(parsed.skills[0]);',
        "output": '{"name":"Ali","age":25,"skills":["JS","Python"]}\nstring\nAli\nJS'
    },
    "LocalStorage & SessionStorage": {
        "explanation": "Browser storage APIs. localStorage persists until manually cleared. sessionStorage clears when the tab closes. Both store string key-value pairs. Use JSON for objects.",
        "example": '// In a browser environment:\n\n// Store data\nlocalStorage.setItem("username", "Ali");\nlocalStorage.setItem("user", JSON.stringify({ age: 25 }));\n\n// Retrieve data\nlet name = localStorage.getItem("username");\nlet user = JSON.parse(localStorage.getItem("user"));\nconsole.log(name);        // Ali\nconsole.log(user.age);    // 25\n\n// Remove data\nlocalStorage.removeItem("username");\nlocalStorage.clear();     // Remove all',
        "output": "Ali\n25"
    },
    "Fetch API": {
        "explanation": "The Fetch API makes HTTP requests to servers. Returns a Promise. Use .json() to parse the response. Always handle errors with try-catch or .catch().",
        "example": '// Fetch data from an API\nasync function getData() {\n    try {\n        const response = await fetch("https://jsonplaceholder.typicode.com/posts/1");\n\n        if (!response.ok) throw new Error("Request failed!");\n\n        const data = await response.json();\n        console.log(data.title);\n        console.log(data.id);\n    } catch (error) {\n        console.log("Error:", error.message);\n    }\n}\n\ngetData();',
        "output": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit\n1"
    },
    "Map & Set": {
        "explanation": "Map stores key-value pairs where keys can be ANY type (unlike objects). Set stores unique values only — no duplicates allowed. Both are iterable.",
        "example": '// MAP\nlet map = new Map();\nmap.set("name", "Ali");\nmap.set(1, "one");\nconsole.log(map.get("name"));   // Ali\nconsole.log(map.size);          // 2\n\n// SET\nlet set = new Set([1, 2, 2, 3, 3, 4]);\nconsole.log(set);               // {1, 2, 3, 4} — no duplicates\nset.add(5);\nconsole.log(set.has(3));        // true\nconsole.log(set.size);          // 5',
        "output": "Ali\n2\nSet(4) { 1, 2, 3, 4 }\ntrue\n5"
    },
    "Higher Order Functions": {
        "explanation": "Functions that take other functions as arguments OR return functions. Examples: map(), filter(), reduce(), forEach(). They enable functional programming style.",
        "example": 'let numbers = [1, 2, 3, 4, 5, 6];\n\n// map — transform each element\nlet squares = numbers.map(n => n ** 2);\nconsole.log(squares);\n\n// filter — keep matching elements\nlet evens = numbers.filter(n => n % 2 === 0);\nconsole.log(evens);\n\n// reduce — accumulate to single value\nlet sum = numbers.reduce((acc, n) => acc + n, 0);\nconsole.log(sum);\n\n// forEach — iterate (no return value)\nnumbers.forEach(n => process.stdout.write(n + " "));',
        "output": "[1, 4, 9, 16, 25, 36]\n[2, 4, 6]\n21\n1 2 3 4 5 6"
    },
    "Closures": {
        "explanation": "A closure is a function that remembers variables from its outer scope even after the outer function has finished executing. Used for data privacy and factory functions.",
        "example": 'function makeCounter() {\n    let count = 0;     // Private variable\n\n    return {\n        increment() { count++; },\n        decrement() { count--; },\n        getCount()  { return count; }\n    };\n}\n\nconst counter = makeCounter();\ncounter.increment();\ncounter.increment();\ncounter.increment();\ncounter.decrement();\nconsole.log(counter.getCount());   // 2\n// count is not accessible from outside',
        "output": "2"
    },
    "Regular Expressions (Regex)": {
        "explanation": "Regular expressions define search patterns for strings. Created with /pattern/flags or new RegExp(). Methods: test() (returns boolean), match(), replace(), split(). Flags: g (global), i (case-insensitive).",
        "example": 'let email = "user@example.com";\nlet emailPattern = /^[\\w.-]+@[\\w.-]+\\.\\w{2,}$/;\n\nconsole.log(emailPattern.test(email));       // true\nconsole.log(emailPattern.test("invalid"));   // false\n\n// Replace\nlet text = "Hello World Hello JS";\nconsole.log(text.replace(/Hello/g, "Hi"));\n\n// Extract matches\nlet nums = "Phone: 123-456-7890";\nlet found = nums.match(/\\d+/g);\nconsole.log(found);',
        "output": "true\nfalse\nHi World Hi JS\n['123', '456', '7890']"
    } 
  }
}
# -------------------------------
# 3. HELPER FUNCTION
# -------------------------------
def get_content(language, topic):
    # LEARN_CONTENT se specific language ka data nikaalna
    lang_data = LEARN_CONTENT.get(language, {})
    
    if topic in lang_data:
        explanation = lang_data[topic].get("explanation", "No explanation available.")
        example = lang_data[topic].get("example", "// No example code available.")
        output = lang_data[topic].get("output", "No output available.")
        return explanation, example, output
    
    # Agar topic nahi milta to fallback message
    return "Details for this topic are being updated.", "// Example pending...", "Output pending..."
# 4. UNIFIED APP FUNCTION (Corrected Routing)
# -------------------------------
def app():
    st.title("📚 Learn — Programming Topics")
    st.write("Select a language and a topic to study its explanation and code.")

    # 1. Available languages list
    languages_list = ["Python", "C++", "JavaScript"]
    
    # 2. Dashboard se aane wali value check karein. Agar kuch na mile toh default "Python"
    coming_lang = st.session_state.get("learn_lang", "Python")
    
    # 3. Dynamic Index find karein ke selectbox kis language par load ho
    if coming_lang in languages_list:
        default_idx = languages_list.index(coming_lang)
    else:
        default_idx = 0

    # 4. Select language with dynamic default index
    language = st.selectbox("Choose Language", languages_list, index=default_idx)
    
    # Sync update: Agar user manually drop-down badle, toh session state bhi change ho jaye
    st.session_state["learn_lang"] = language
    
    # Assign topics list based on language selection
    if language == "Python":
        topics = PY_TOPICS
    elif language == "C++":
        topics = CPP_TOPICS
    elif language == "JavaScript":
        topics = JS_TOPICS

    # Searchable topic dropdown
    selected_topic = st.selectbox(f"Search {language} Topic", topics)

    if selected_topic:
        explanation, example, output = get_content(language, selected_topic)
        
        with st.container():
            st.markdown(f"### {selected_topic} ({language})")
            st.info(f"**📖 Explanation:** {explanation}")
            
            st.markdown("**💻 Code Example:**")
            # C++ ke liye 'cpp' syntax highlighting activate hogi
            syntax_lang = language.lower().replace("++", "pp")
            st.code(example, language=syntax_lang)
            
            st.markdown("**📤 Expected Output:**")
            st.code(output)

            # Button ke liye unique key taaki state conflict na ho
            btn_key = f"run_{language}_{selected_topic.replace(' ', '_')}"
            
            if st.button("Run Code Simulation", key=btn_key):
                st.success(f"Execution Successful in {language} Environment!")
                st.markdown("**Output Window:**")
                st.code(output)
                
                # Progress update logic
                if st.session_state.get("username"):
                    add_progress(st.session_state["username"], f"{language}: {selected_topic}", status="Completed")

    st.markdown("---")
    st.caption("© 2026 AI Virtual Lab Assistant | Unified Learning Module")