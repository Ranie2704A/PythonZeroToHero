age = int(input('Give me your age:\n'))
print(type(age))
name = input('Give me your name:\n')

print(f"Your name is {name} and you're {age} years old.")

#When we use the 'input' function, always the data is taken as a string by default
#We can change it using the data type at the beginning -> int(input('blabla'))
"""

On the print function, the data will be cast as a string,
if we have for ex: 
    print('Your age is: ' + age + ' years old.')
we will have an error, because age -> int(input())
so, we can make the cast of the variable:
    print('Your age is: ' + str(age) + ' years old.')
or, we can use the fstring:
    print(f'Your age is: {age} years old.')

"""