# syntax_example_2
def area_triangle(length, height):
  area = length * height * 0.5
  print(f"Area of the triangle is {area}")


area_triangle(10, 10)


# syntax of arguments

def sum(a, b, c):
  print(a + b + c)


sum(10, 10, 5)

sum(7, 8, 100)

def introduce(student_name, age):
  print("Hi. My name is " + student_name)
  print("I am " + str(age) + " years old.")

introduce("Abhirath", 50)


def print_shopping_list(list_of_items):
  print(list_of_items)


fruits = ['apple', 'banana', 'orange']
print_shopping_list(fruits)

print_shopping_list(['plastic', 'steel', 'rubber'])