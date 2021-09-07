# Python does not require a key word to declare a value as a variable.
first_name = 'Guido'
print(first_name)
# Strings can be set with single or double quotes.
middle_name = 'Van'
print(middle_name)
last_name = 'Rossum'
print(last_name)
# Note, like JavaScript, Python variables can change type.
age = 'eighty-five'
age = 85
print(age)
# age = 17
# Use the type function to see the type of a given value.
print(type(first_name))
print(type(age)) # type of age
print('Hello %s %s %s' % (first_name, middle_name, last_name))

# Comments are set with the octothorpe (pound, hashtag).

# # If Statements
# if age >= 23:
#   print('I am ancient')

# # If-else Statements
# if age >= 23:
#   print('I am an adult')
# else:
#   print('I am still growing')

# #If-elif-else
# if age >= 23:
#   print('i can legally drink')
# elif age < 15:
#   print('i got a lot of growing up to do')
# else:
#   print('I am groot')

## Note: above code would break if you had two blank lines in between code.

# For-In-Loop (similar to JavaScript for-loop)
# my_list = [1,2,3,4,5,6,7,8,'Guido','has','stepped','down']

# for x in my_list:
#   print(x)

# Another example of for-in loop, also demonstrating creation of array and use of a built in method, just like you would do in JavaScript.
developers = ['jake','spencer','stu','kim','stephen','bryson']

# for devs in developers:
#   print(devs.capitalize())

# Handling Data with Python
open_file = open("FinalGrades.csv")

# for row in open_file:
#   print(row)

open_file.seek(0)
# A more complicated look at what we can do with the data.
# grades = open('FinalGrades.csv')
total_a = 0
total_b = 0
total_c = 0

for line in open_file:
  line = line.rstrip('\n').split(',')
  for value in line:
    if value == "A":
      total_a += 1
    elif value == "B":
      total_b += 1
    elif value == "C":
      total_c += 1

print("A's:", total_a)
print("B's:", total_b)
print("C's:", total_c)

open_file.close()

from statistics import mean
data1 = [21,23,25,76,98,102,24,22]
print(mean(data1))


