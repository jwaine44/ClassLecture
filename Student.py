class Grade:
    def __init__(self, topic, mark, student_name):
        self.topic = topic
        self.mark = mark
        self.student_name = student_name

    def print_info(self):
        print("Topic", self.topic)
        print("Grade", self.mark)
        print("Student", self.student_name)
        return self

    def extra_points(self, percentage):
        current_grade = self.mark
        final_grade = current_grade * (percentage / 100) + current_grade
        self.mark = final_grade
        return self

class Student:
    bootcamp = "Coding Dojo"
    list_students = []
    # Constructor - constructing objects; written like a function
    def __init__(self, first_name, last_name, instructor, current_stack, mark):
        # Setting attributes, the variables that all instances of class will take on; accessible in the entire class
        self.first_name = first_name
        self.last_name = last_name
        self.instructor = instructor
        self.current_stack = current_stack
        self.grade = Grade(current_stack, mark, first_name)
    # Self is reference to the class itself
    
    # Creating a method; functions inside class, actions that object can perform
    def print_student_info(self):
        print("First name", self.first_name)
        print("Last name", self. last_name)
        print("Instructor", self.instructor)
        print("Current stack", self.current_stack)
        print("Grade", self.grade)
        Student.list_students.append(self)

    def full_name(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def print_all_students(cls):           # Refers to the entire class, cls has access to class attributes
        for student in cls.list_students:
            print(student.full_name(), student.current_stack)

    @classmethod
    def change_stack_name(cls, new_stack):
        for student in cls.list_students:
            student.current_stack = new_stack
        # for i in range(0, len(cls.list_students)):
        #     cls.list_students[i].current_stack = new_stack

    @staticmethod                           # Functions defined within class that have no instance to instance/class attributes
    def add_two_numbers(num1, num2):
        return num1 + num2

alexander = Student("Alexander", "Miller", "Alfredo", "Python/Flask", 8.2)
martha = Student("Martha", "Smith", "Amanda", "Web Fundamentals", 9.2)
roger = Student("Roger", "Smith", "Tyler", "C#", 7.6)
anna = Student("Anna", "Smith", "Nichole", "Java", 10.0)

Student.print_all_students()
Student.change_stack_name("MERN")
Student.print_all_students()

print(Student.add_two_numbers(20,30))

alexander.print_student_info()



# Student.bootcamp = "The Coding Dojo"

# print(alexander.bootcamp)

# alexander = Student("Alexander", "Miller", "Alfredo", "Python/Flask")         # Putting Student calls the constructor like a function
# alexander.print_student_info()
# print(f"{alexander.first_name}'s instructor is {alexander.instructor}")

# martha = Student("Martha", "Smith", "Amanda", "Web Fundamentals")
# martha.print_student_info()
# print(f"{martha.first_name}'s instructor is {martha.instructor}")

# name = alexander.full_name()
# print(name)