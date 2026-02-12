#------------------------------------------conditional statement---------------------------
# (1).question is trafic light

# light =input("Enter the light :")
# if(light == "red"):
#     print("stop")
# elif(light == "yello"):
#     print("look")
# elif(light == "green"):
#     print("go")
# else:
#     print("light is break :")

#(2) print marks with grade

# marks = int(input("enter the marks"))
# if(marks >= 90 and marks <100):
#     print("he wont A grade")
# elif(marks >= 80 and marks < 90):
#     print("he wont b grade")
# elif(marks >= 70 and marks <80):
#     print("he wont c grade")
# else:
#     print("he wont d grade")

# single line if / ternary operator
# food = input("Enter you food :")
# eat = "yes" if food == "cake" else "no"
# print(eat)


# food = input("Enter your food :")
# print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

#------------------------------------type conversion-----------------------------------------

# a = "2"
# b = 4.5
# print(type(a))  # it give error because it is not posible string add into the float values
# print(a + b)

# a = int("2")
# b = 4.5
# print(type(a))
# print(a + b)

 # -----------------------------------------how to get input----------------------------------------------

# num1 = int(input("Enter your frist number :"))
# num2 = int(input("Etner your second number :"))
# sum = num1 + num2
# print("it is the sum of two number :",sum)

# side = float(input("Enter your side :"))
# aria = side ** side
# print("it is the area of the squres :",aria)

# num1 = float(input("Enter your number :"))
# num2 = float(input("Enter your number :"))
# avg = (num1 + num2)/2
# print(avg)

# num1 = int(input("Enter your frist number :"))
# num2 = int(input("Enter your second number :"))

# print(num1 >= num2)

#---------------------------------------------string ---------------------------------------

# str1 = "imrat"
# len1 = len(str1)
# print(len1)

# str2 = "singh"
# len2 = len(str2)
# print(len2)

# final_string = str1 +" " + str2
# print(final_string)
# print(len(final_string))

# str = "imrat singh"
# print(str[3])
# print(str[5])
# print(str[9])

#---------------------------------------slicing--------------------------------------------
# str = "imrat singh"
# print(str[5:len(str)])
# print(str[5:])
# print(str[0:4])
# print(str[-5:-2])
# print(str.endswith("ngh"))
# print(str.capitalize()) # it makes copy then change string it is not change orignal string
# print(str)
# print(str.replace("a","o"))
# print(str.find("i")) # it is find charecter in string where 1 cqurence
# print(str.count("i")) # it count number how many time ocure

# write the program to input user name and print its length
# name = input("Enter your name :")
# print(len(name))

# write the program to find the occurrence of "s" in a string
# str = input("Enter your str :")
# print(str.count("n"))

#         -------------------- conditional statement ------------------------

# Q1. Take a number as input and check whether it is:
# Positive
# Negative
# Zero

# number = int(input("Enter your number :"))
# if(number >0):
#     print("it is positive :")
# elif(number < 0):
#     print("it is nagetive :")
# else:
#     print("it is zero :")
# --------------------------------------------------------------------------------------------------
# Q2. Take marks of a student as input and print the grade:

# 90–100 → Grade A

# 75–89 → Grade B

# 60–74 → Grade C

# 40–59 → Grade D

# Below 40 → Fail

# marks = float(input("Enter your marks :"))

# if(marks<=100 and marks>=90):
#     print("grade A")
# elif(marks >75 and marks <=89):
#     print("grade B")
# elif(marks >60 and marks <= 74):
#     print("grade C")
# elif(marks >40 and marks <59):
#     print("grade D")
# else:
#     print("fail")
#--------------------------------------------------------------------------------------------------

# Q3. Take a number as input and check whether it is:

# Even

# Odd

# num = int(input("Enter your number :"))
# if(num % 2 == 0):
#     print("even",num)
# else:
#     print("odd",num)
#--------------------------------------------------------------------------------------------------------
# Q4. Take three numbers as input and print the largest number.
# num1 = int(input("Enter your num1 :"))
# num2 = int(input("Enter your num2 :"))
# num3 = int(input("Enter your num3 :"))
# if(num1 > num2 and num1 > num3):
#     print("num1 is grater :",num1)
# elif(num2 > num1 and num2 > num3):
#     print("num2 is grater :",num2)
# else:
#     print("num3 is grater :",num3)
# ----------------------------------------------------------------------------------------------------
# Q5. Take a year as input and check whether it is a leap year or not.
# year = int(input("Enter your year :"))
# if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
#     print("it is a leap year :",year)
# else:
#     print("it is not a leap year :",year)
#---------------------------------------------------------------------------------------------------
# Q6. Take a character as input and check whether it is:
# A vowel (a, e, i, o, u)
# Or a consonant

# char = input("Enter your char :")
# if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
#     print("it is a vowel",char)
# else:
#     print("it is a consonant :",char)
# ------------------------------------------------------------------------------------------------

# Q7. Take age as input and classify:
# Child (0–12)
# Teenager (13–19)
# Adult (20–59)
# Senior Citizen (60 and above)
# age = float(input("Enter your age :"))
# if(age >0 and age <=12):
#     print("child",age)
# elif(age >=13 and age <=19):
#     print("teenager :",age)
# elif(age >=20 and age <=59):
#     print("adult :",age)
# else:
#     print("senior citizen :",age)
#----------------------------------------------------------------------------------------------------
# Q8. Take two numbers and one operator (+, −, *, /) as input and perform a calculator operation.
# num1 = float(input("Enter your number frist :"))
# num2 = float(input("Enter your number second :"))
# operatar = input("Enter your operatur like ,+,-,*,/ = :")

# if (operatar == "+"):
#     print("result = ",num1 + num2)
# elif(operatar == "-"):
#     print("result = ",num1 - num2)
# elif(operatar == "*"):
#     print("result = ",num1 * num2)
# elif(operatar == "/"):
#     if(num2 != 0):
#         print("result = ",num1 / num2)
#     else:
#         print("error : we can not perform operation :")
# else:
#     print("you are Enter invalid operatar")
# ------------------------------------------------------------------------------------------------
# Q9. Take temperature (in °C) as input and print:
# Below 0 → Freezing
# 0–20 → Cold
# 21–35 → Normal
# Above 35 → Hot

# tem = int(input("Enter your temprature :"))
# if(tem <= 0):
#     print("freezing")
# elif(tem > 0 and tem <= 20):
#     print("it is cold temprature :")
# elif(tem >= 21 and tem <=35):
#     print("normal temprature :")
# else:
#     print("very hot :")
#----------------------------------------------------------------------------------------------------
# Q10. Take salary as input and calculate bonus:
# Salary ≥ 50,000 → 20% bonus
# Salary ≥ 30,000 → 10% bonus
# Salary < 30,000 → 5% bonus

#----------------------------------------------------------------------------------


#------------------------------------------list ----------------------------------

#  a built-in data type that store set of values
# list is mutable data types 
#  it can store elements of different types (integer,float,string,etc)

# list = [32,34,45,45,56]
# print(list)
# print(list[4])
# list[0]=77
# print(list)
# print(list[1:3])

# list = [1,2,3,4]
# list.append(100) # it is used to add one element at the end
# print(list)
# list.insert(1,200) # insert element at index
# print(list)
# list.reverse() # it is used to reverses list
# print(list)
# list.sort() # it is used sorts list in asending order
# print(list)
# list.sort(reverse=True) # it is used sorts list in decending order
# print(list)

#-------------------------------- list slicing --------------------------
# marks = [45,67,78,90,57]
# print(marks[:4])
# print(marks[-4:-1])
# print(marks[-1:])
# print(marks[1:])
# print(marks[2:-1])

#--------------------------------------- practices Question for list-----------------------------
#(1).Write a program to remove duplicate elements from a list.
# number = [45,34,2,7,2]
# unique_number = list(set(number))
# print("list after removing duplicate elements :",unique_number)
#(2)Write a program to sort a list in ascending order.
# list = [65,2,57,3,90]
# list.sort()
# print(list)
# (3) write the program ask the user to enter names of movies and store them in a list
# movies = []
# mov1 = input("Enter your 1st movies :")
# mov2 = input("Enter your 2st movies :")
# mov3 = input("Enter your 3st movies :")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# (4) write to chceck if a list contains apalindrome of elements.
# list1 = [1,2,4]
# list_copy = list1.copy()
# list_copy.reverse()
# if(list_copy == list1):
#     print("it is palindrome :")
# else:
#     print("Not a palindrome :")

# dixnary



