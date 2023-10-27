class Student:
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []

    def display_info(self):
        return f"Student name is {self.name} and age is {self.age}"

    def enroll(self, course):
        course = course.capitalize()  # Capitalize the first letter for consistency
        if course in Student.available_courses:
            if course not in self.courses:
                self.courses.append(course)
                return f"{course} added successfully!"
            else:
                return f"{course} is already enrolled."
        else:
            return f"{course} is not available. Please try again."

    def list_courses(self):
        if self.courses:
            return f"{self.name} is enrolled in: {', '.join(self.courses)}"
        else:
            return f"{self.name} is not enrolled in any courses."

    def list_available_courses(self):
        available_courses = set(Student.available_courses) - set(self.courses)
        return f"Available courses for {self.name} are: {', '.join(available_courses)}"


def main():
    # Get student information
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student1 = Student(name, age)

    # Get the user input for the course
    course_name = input("Enter the course name: ")

    while course_name.lower() != "exit":
        result = student1.enroll(course_name)
        print(result)

        # Get the next course name from the user
        course_name = input("Enter the course name (or 'exit' to quit): ")

    # Display the list of enrolled courses
    print(student1.list_courses())

if __name__ == "__main__":
    main()
