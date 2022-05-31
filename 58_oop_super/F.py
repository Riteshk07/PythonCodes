class Employee:
    def __init__(self,name, age, email, designation, salary, experience):
        self.name = name
        self.age = age
        self.email = email 
        self.designation = designation
        self.salary = salary 
        self.experience = experience

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Email: {self.email}, Designation: {self.designation}, Salary: {self.salary}, Experience: {self.experience}'

class Student:
    def __init__(self, name, age, email, degree, branch, semester):
        self.name = name
        self.age = age
        self.email = email
        self.degree= degree
        self.branch = branch
        self.semester = semester

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Email: {self.email}, Degree: {self.degree}, Branch: {self.branch}, Semester: {self.semester}'


e = Employee('Mr.Sharma', 28, 'sh@gm.com', 'Manager', 34000, 10)

s = Student('Golu', 21, 'golu@gm.com', 'BTech', 'CS', '2nd')

print(e)
print(s)
