# class 10
from datetime import date, datetime
class Employee:
    # Ye class variable hai or ye sirf or sirf class ke name se accessible hoga na ke self ke through or iske liye (instance ya object bhi nahi banana parta hai direct class ke name ke through access kiya jasakta hai (print(Employee.employee)))
    __employee = 0
    def __init__(self, fname, lname, salary, age, joining_date):
        self.fname = fname
        self.lname = lname
        # Private Variable (It cannot be accesible outside the class but inside it can be accessible in the class). It is called name mangaling and it is denoted by __. or ye use nahi karna normal way mein. normal way mein sirf or sirf _ use karte hain
        # Python mein private ya protected ka koi concept hi nahi hai ye jo hum kar rahe hain ye sirf ek hack hai na ke ek genuine way
        # __ is a keyword to prevent overlapping of same name properties existing in the different classes it will attach the name of class with that variable
        self.__salary = self.validate(salary)
        self._age = age
        self.experience = self.calculate_years_of_service(joining_date)
    #PYTHONIC WAY OF GETTER AND SETTER
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        self._age = new_age
    
    # Normal / Traditional way of getting and setting
    def get_salary(self):
        return self.__salary
    # Getter and setter to access the private element (Encapsulation)
    def set_salary(self, salary):
        self.__salary = self.validate(salary)

    def validate(self, salary):
        if salary <= 0:
            raise Exception("Salary cannot be zero")
        else:
            return salary

    @classmethod
    # ye method bhi same class variable ki tarha hi access hoga no need to create any instance of the class or iske argument mein (cls) pass karte hain while instance method ke liye (self) use karte hain use to kuch bhi karsakte hain lekin python ki convention ye kehti hai ke is tarah code likha jaye or static method ke argument mein kuch bhi pass nahi karte nothing...
    def create_instance(cls):
        # __ ke sath hai class variable ka name to sirf of sirf ye class ke andar hi call ya access hosakta hai 
        # print("Creating Instance of", cls.__employee)
        return cls(
            "Muhammad",
            "Owais",
            100,
            21,
            "2023-01-21",
        )
    @classmethod
    def get_total_employees(cls):
        return cls.__employee
    
    # Utility function wo function hota hai jismein ek esi logic likhi jaati hai jo cheez baar baar repeat horahi hoti hai ye helper function bhi kehlata hai jese ke hamare pass different jagah par string mein date arahi hai or hamen use date object mein convert krna hai to bar bar alag jagah code karne ke bajae hum ek function banaenge jiske through wo kaam ek line mein hi hojayega or code bhi optimize hojayega
    @staticmethod # ((@static ya whatever)decorator kehlata hai or ye function se pehle call hota hai)
    # Esa method jismein na apko instance na hi class method ki zaroorat pare tab hum ye static method use karte hain
    def calculate_years_of_service(joining_date):
        current_date = datetime.now()
        join = datetime.fromisoformat(joining_date)
        return (current_date - join).days

# emp1 = Employee(
#     "Muhammad",
#     "Owais",
#     20000000,
#     21
# )

# print(emp1.__dict__)

# # Normal / Traditional way of setting the so called private variable through set method
# emp1.set_salary(340000000)
# print(emp1.__dict__)

# # ye wala python ka way hai getting and setting wala ismein method ke aage parenthesis nahi lagate
# emp1.age = 45
# print(emp1.__dict__)

# ye jo instance create kiya hai mene ye mein class method ke through kiya hai
emp1 = Employee.create_instance()
print(emp1.__dict__)

print(emp1.calculate_years_of_service("2023-01-21"))

help(Employee)
