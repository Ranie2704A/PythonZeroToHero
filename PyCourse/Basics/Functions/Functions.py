def greeting(name, age):
    print(f"Hello {name}! You are {age} years old.")


greeting("Abad", 22)
greeting("Abril", 1)

name = "Sharon"
age = 25
greeting(name, age)

def force(weight):
    g = 9.81
    return weight * g

print(force(100))

force_newtons = force(100)
print(force_newtons)

def mid(num1, num2):
    middle = (num1 + num2) / 2
    return middle

middle_value = mid(100, 50)
print(middle_value)