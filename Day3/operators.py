age=23
height=5.7
complex_number=3+3j
#Area of triangle
base=int(input("Enter base:"))
print("base",base)
Height=int(input("Enter height:"))
print(Height)
area=(0.5*base*Height)
print(area)
#Perimeter of triangle
side_a=int(input("Enter side a:"))
side_b=int(input("Enter side b:"))
side_c=int(input("Enter side c:"))
perimeter=(side_a+side_b+side_c)
print(perimeter)
#Area of rectangle
length=int(input("ENter legnth:"))
breadth=int(input("enter breadth:"))
area_rect=length*breadth
print(area_rect)
#Perimeter of rectangle
perimeter_rect=(2*(length+breadth))
print(perimeter_rect)
#Circle
radius=int(input("Radius of circle:"))
print(radius)
#area
area_circle=(3.14*radius*radius)
print(area_circle)
#circumference
circumference=(2*3.14*radius)
print(circumference)
# 1. Find the length of 'python' and 'dragon' and make a falsy comparison statement
word1 = 'python'
word2 = 'dragon'

# Find lengths
len_python = len(word1)
len_dragon = len(word2)

# Print lengths
print("Length of 'python':", len_python)
print("Length of 'dragon':", len_dragon)

# Falsy comparison statement
print(len_python == len_dragon)  

# 2. Use `and` operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in word1 and 'on' in word2)  

# 3. Use `in` operator to check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)  

# 4. There is no 'on' in both 'dragon' and 'python' (false statement)
print('on' not in word1 and 'on' not in word2)  

# 5. Find the length of the text "python", convert to float, and then to string
len_python_float = float(len(word1))
len_python_str = str(len_python_float)

print(len_python_str)  

# 6. Check if a number is even using Python
number = 4  # Change this to test different numbers
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 7. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 == int(2.7))  

# 8. Check if type of '10' is equal to type of 10
print(type('10') == type(10))  

# 9. Check if int('9.8') is equal to 10
print(int(9.8) == 10)  

# 10. Script to calculate pay based on hours and rate per hour
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

# Calculate weekly pay
pay = hours * rate
print("Your weekly earning is", pay)

# 11. Script to calculate the number of seconds a person has lived assuming 100 years
years = int(input("Enter number of years you have lived: "))

# Assuming a person lives for 100 years
seconds_per_year = 31536000 

# Calculate the total number of seconds
seconds_lived = years * seconds_per_year
print("You have lived for", seconds_lived, "seconds.")

# 12. Write a script to display a table
for i in range(1, 6):
    print(i, i**0, i**1, i**2, i**3)
