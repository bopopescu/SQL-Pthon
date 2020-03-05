# the from is the name of th efile with the class definition and import the name of the class
from span import Student

# we make a instance of the class while also passing arguments to use the init method and assigning values
student1 = Student("Jim", "Business", 2.1, False)
student2 = Student
student2.name = "Pam"

print(student2.name)

print(student1.gpa)
print(student1.checkGpa())
print(student2.gpa)

prices = [10, 20, 30]
total = 0;
for items in prices:
    total += items
print(total)

# co-ordinates using nested loops

for x in range(4):
    for y in range(3):
        # this is a formatted string
        print(f'({x},{y})')

numbers = [5, 2, 5, 2, 2]

for i in numbers:
    print('x' * i)

numberz = [2, 2, 2, 2, 5]
# proper way of doing the above example

for x_count in numberz:
    # makes a string which we append
    output = ''
    # for the number started in x_count the range loop will go that number of times each time adding a x
    for count in range(x_count):
        output += 'x'
    print(output)

ints = list(range(51))
biggest = ints[0]
for i in ints:
    if i > biggest:
        biggest = i

print(biggest)

# 2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# to access the single number
print(matrix[0][0])

for i in matrix:
    for j in i:
        print(j)

# list methods
# appedn adds to the end of the list
numbers.append(20)
print(numbers)
# inser you can choose location of insertion the first number us the index second is the number
numbers.insert(0, 30)
