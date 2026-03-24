### 1. Core idea and features

**Main scenario:**  
You are building a small system for your academy to:

- **Manage students:** add, edit, list, search, delete.  
- **Manage courses:** add courses, set capacity, assign teachers.  
- **Enrollments:** enroll students in courses, list who is in which course.  
- **Progress tracking:** store grades, calculate averages, pass/fail.  
- **Reports & analytics:** simple stats (top students, course popularity, etc.).  
- **Data persistence:** save/load data using JSON files.

---

### 2. How each Python topic fits into the project

#### Basics and data handling

- **Python Syntax, Output, Comments:**  
  Use clean print statements, comments to explain each module, and consistent indentation.

- **Variables, Data Types, Numbers, Casting:**  
  - Store student age as `int`, GPA as `float`, names as `str`.  
  - Cast user input from `str` to `int`/`float` when needed.

- **Strings, Booleans, Operators:**  
  - String operations for names, course codes.  
  - Boolean flags like `is_active`, `has_passed`.  
  - Comparison and logical operators for validations and filters.

- **Lists, Tuples, Sets, Dictionaries:**  
  - **Lists:** list of students, list of courses.  
  - **Tuples:** immutable `(course_code, term)` keys.  
  - **Sets:** unique student IDs in a course, or unique skills.  
  - **Dictionaries:** student data:  
    ```python
    student = {
        "id": 1,
        "name": "Alice",
        "age": 20,
        "courses": ["PY101", "JS101"]
    }
    ```

---

#### Control flow and loops

- **If...Else, Match:**  
  - Menu choices:  
    ```python
    choice = input("Choose option: ")
    if choice == "1": ...
    ```
  - Use `match` for main menu routing:
    ```python
    match choice:
        case "1": add_student()
        case "2": list_students()
        case _: print("Invalid choice")
    ```

- **While Loops, For Loops, Range:**  
  - `while` loop for the main menu until user exits.  
  - `for` loops to iterate over students/courses.  
  - `range` for generating IDs or demo data.

- **Arrays, Iterators:**  
  - Treat Python lists as arrays of students.  
  - Create a custom iterator for paginating student lists (e.g., 10 per page).

---

#### Functions, modules, and organization

- **Functions:**  
  - `add_student()`, `remove_student()`, `enroll_student()`, `calculate_gpa()`, etc.

- **Modules:**  
  Split your project:
  - `students.py` – student-related functions/classes  
  - `courses.py` – course-related logic  
  - `enrollments.py` – enrollment logic  
  - `reports.py` – analytics and statistics  
  - `main.py` – entry point with the menu

- **Dates, Math:**  
  - Use `datetime` for enrollment date, course start/end dates.  
  - Use `math` for rounding GPAs, computing statistics.

---

#### Error handling, external tools, and utilities

- **Try...Except:**  
  - Handle invalid input (e.g., non-numeric age).  
  - Handle file read/write errors when loading/saving JSON.

- **Python PIP, VirtualEnv:**  
  - Create a virtual environment for the project.  
  - Use `pip` to install a package like `python-dateutil` or `rich` for nicer console output.

- **JSON:**  
  - Save all data to `students.json`, `courses.json`, `enrollments.json`.  
  - Load them at startup.

- **RegEx:**  
  - Validate email format for students.  
  - Validate course codes like `PY101`, `DS201`.

- **String Formatting, None, User Input:**  
  - Use f-strings for clean messages:
    ```python
    print(f"Student {student['name']} has GPA {gpa:.2f}")
    ```
  - Use `None` for optional fields (e.g., `graduation_date = None`).  
  - Use `input()` for menu and data entry.

---

#### OOP and classes

Create a small OOP model:

- **Python OOP, Classes/Objects:**
  - `Student`, `Course`, `Enrollment` classes.

- **__init__ Method, self Parameter:**
  ```python
  class Student:
      def __init__(self, student_id, name, age, email):
          self.id = student_id
          self.name = name
          self.age = age
          self.email = email
          self.courses = []
  ```

- **Class Properties (using @property):**
  ```python
  class Student:
      @property
      def is_adult(self):
          return self.age >= 18
  ```

- **Class Methods (and static methods):**
  ```python
  class Student:
      students = []

      @classmethod
      def from_dict(cls, data):
          return cls(data["id"], data["name"], data["age"], data["email"])
  ```

- **Code Challenge idea:**  
  - Add a feature: “Recommend top 3 courses for a student based on their grades and interests.”  
  - Or: “Implement search with filters (by name, min GPA, enrolled course) using list comprehensions and OOP methods.”