# Fundamentals of Computer Science Program

This program is a representation of courses that are provided, with a specific focus on OOP (Object-Oriented Programming) courses. The program includes a parent class named `Course` that provides basic course details and a derived class named `OOPCourse` which offers details specific to an OOP course.

### Classes and Methods:

- **Course (Parent Class)**:
    - `contact_details()`: Provides a contact hyperlink.
    - `head_office()`: Shares the head office location.
    
- **OOPCourse (Derived Class)**:
    - `__init__()`: Initializes constants for the OOPCourse.
    - `trainer_details()`: Displays course's name and instructor.
    - `show_course_id()`: Displays course's ID number.

### Usage:

When you run the program, it instantiates an OOPCourse object and displays relevant details about the course, including contact information, head office location, course name, instructor details, and the course ID.

### Sample Output:

```
Welcome to the Fundamentals of Computer Science program
The head office location is Cape Town
Please contact us by visiting www.hyperiondev.com

This is the OOP Fundamentals course and your trainer is Mr Anon A. Mouse

The ID number of the course is # 12345
```
