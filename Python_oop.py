# ----------------------function----------------
# -----> block of statements that perform a specific task.
# def calc_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum
# calc_sum(3,5)
# calc_sum(5,6)
# calc_sum(3,9)


# we have two types of function bilt_in function and user define function
# built_in function
# print()
# len()
# type()
# range()

# practices question

# write a program to print the length of a list
# cities = ["imrat","singh","lodhi","thakur"]
# heros = ["ram","syam","viru","varun"]

# def print_list(list):
#     print(len(list))

# print_list(cities)
# print_list(heros)

# write a program to print the elements of a lsit in a single line
# list = ["imrat","singh","lodhi","thakur"]

# def print_element(list):
#     for item in list:
#         print(item,end=" ")
# print_element(list)

# n = 5

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     return fact

# print(factorial(n))

# def converter(usd_val):
#     inr_val = usd_val * 90
#     return inr_val
# print(converter(4))

# Write a function to find the maximum of two numbers.

# num1 = 20
# num2 = 30

# def maximum(num1,num2):
#     if(num1 > num2):
#         print("num1 is maximum :",num1)
#     else:
#         print("num2 is maximum :",num2)

# maximum(num1,num2)
# Write a function to find the factorial of a number.
# num = 5
# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *= i
#     return fact
# print(factorial(num))
# Write a function to check whether a number is prime.
# def prime(num):
#     if(num<=1):
#         return False
#     for i in range(2,num):
#         if(num % i == 0):
#             return False
#     return True
# num =  7

# if prime(num):
#     print("prime number :")
# else:
#     print("not a prime number :")


# Write a function to reverse a string.
# str = "imratsingh"
# def reverse(str):
#     revers = ""
#     for char in str:
#         revers = char + revers
#     return revers
# print(reverse(str))

# Write a function to count vowels in a string.
# str = "imratsingh"
# def count_vowels(str):
#     count = 0
#     for char in str:
#         if(char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
#             count = count + 1 
#     return count
# print(count_vowels(str))


# Write a function to print numbers from 1 to N.
# num = int(input("Enter your number :"))
# def print_n(num):
#     for i in range(1,num):
#         print(i)
# print_n(num)
# Write a function to calculate the sum of all numbers in a list.
# list = [21,2,1,3,4,5]
# def sum_cal(list):
#     sum = 0
#     for i in list:
#         sum = sum + i
#     return sum
# print(sum_cal(list))
# Write a function to find the largest number in a list.
# list = [2,4,5,2,6]
# def  largest_num(list):
#     largest = list[0]
#     for i in list:
#         if(i > largest):
#             largest =  i
#     return largest
# print(largest_num(list))
# Write a function to print the Fibonacci series up to N terms.
# num = 10
# def fibonacci(num):
#     a = 0
#     b = 1
#     if(num<=0):
#         print("Enter positive number:")
#     elif(num == 1):
#         print(a)
#     else:
#         print(a,b,end=" ")
#         for i in range(2,num):
#             c = a + b
#             print(c,end=" ")
#             a = b
#             b = c
# fibonacci(num)

# ----------------------- recursion ----------------------------
# -----> when a function calls itself repeatedly
# n = 5
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(n)
# write a program to find factorial using recursion

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(5))

# write a program to find the  sum of n natural number
# n = 10
# def sum_cal (n):
#     if (n == 0):
#         return 0
#     return sum_cal(n - 1) + n
# print(sum_cal(4))

# write a program  to print all elements in a list using Recursion
# def print_list(list,idx):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# list = ["imrat","singh","lodhi","thakur"]
# print_list(list,idx=0)

# -------------------------- object oriented programing ------------------------
#class is a blue print 
# object is a real world entity 

class car:
    color = "blue"
    brand = "merch"
car1 = car()
print(car1.color)
 




