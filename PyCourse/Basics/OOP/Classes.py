from Student import Student

student1 = Student('John', 'Doe', 'Engineer', 8)
print(student1)

student2 = Student('Alex', 'Doe', 'Engineer', 4)
print(student2)

print(student1.is_approved())
print(student2.is_approved())