# num1 =20
# print(type(num1))

# num1= 9.44
# print(type(num1))

# num1 = "imrat"
# print(type(num1))

# num1 = []
# print(type(num1))

# num1 = ()
# print(type(num1))

# num1 = True
# print(type(num1))

# num1 = None
# print(type(num1))

# num1 = ''' imrat singh lodhi
# student in cybrom'''
# print(type(num1))

                                     # coperision operature

# chek the numnber is even and odd 
# check the person is eligiable for vote or not
# check the number negetive or positive
# check the numebr is divisible by 5 or not
# chek the pon is correct or not
# check the number is above 50 or not 
# check the email is correct or not


# age = int(input("Enter your age :"))
# print(age >= 18)

# num = int(input("enter the number :"))
# print(num >= 1)

# num = int(input("Enter your number :"))
# print(num % 5 == 0)

# pin = int(input("Enter your pin :"))
# print(pin == 1234)

# num = int(input("Enter your numebr :"))
# print(num > 50)

# email = input("Enter your Email :")
# print(email == "imratsingh02@gmail.com")

                                 # logical opreture5


# check the email and passwoed is correct or not 
# check the number is divible b 5 and 10 or not 
# check th given character is vowel or constent
#check the number is above 50 and dicisible by 2 or not

# email = input("enter your email :")
# password = int(input("enter your password"))
# print(email == "imratsingh" and password == 1234)

# num = int(input("Enter the number :"))
# print(num % 5 ==0  and num % 10==0)

# char = input("enter your char :")
# print(char == "a" or char =="e" or char =="i" or char == "o" or char == "u")


# num = int(input("Enter your number :"))
# print(num > 50 and num % 2 == 0)

                                #membership operator
# tow types of membership operator
# in , not in 

# print("puthon" in "python program world coding")
# print('z' not in "python")

# # vowel consonent
# ch = input("Enter your number")
# print(ch in "aeiou")

# # identity operator 
# # it check the memory address
# # immutable -> int float complex string
# # is , is not 
# # id(variable) -> checks memory address 
# a = (1,2,3)
# b = (1,2,3)
# print(id(a))
# print(id(b))
# print(a is b)


                                     # ternary operator

# ontrue if condition else onfalse

# eligiable for vote
# age = int(input("Enter your age :"))
# print("Eligiable")if age>18 else print("not Eligiable")

# a = 100
# b = 20

# print("Grater") if a>b else print("not grater")



# # check the email correct or not 
# email = input("Enter your email :")
# print("Email is correct")if email == "imratsingh2@gamil.com" else print("email is not correct")


# check the number above 50 or not

# num = int(input("Enter your number :"))
# print("above")if num > 50 else print("blow")


# check the pin is correct or not

# pin = int(input("Enter your pin :"))
# print("correct")if pin == 1234 else print("not correct")


# check the number negative or positive 
# num = int(input("Enter your number :"))
# print("positive")if num > 0 else print("nagative")


# check the number is dicisible by 5 or not

# num = int(input("Enter your number :"))
# print("divisible")if num % 2 == 0 else print("not divisible")

# chek the person is eligiable for vote or not 
# age= int(input("Enter your age :"))
# print("eligiable for vote")if age > 18 else print("not eligiable for vote")


# chek the number is even or not 
# num = int(input("Enter your number :"))
# print("even")if num % 2 == 0 else print("odd")


# # check the number is above 50 and dicisibele by 2 ot not 
# num = int(input("Enter your number :"))
# print("above 50 and dicisibele by 2")if num >50 and num % 2 == 0 else print("not above 50 and dicisibele by 2")

# check the given charater is vowal or consonet
# char = input("Enter your charecter :")
# print("vowal")if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' else print("consonent")

# check the number is divisible by 5 and 10 or not 
# num = int(input("Enter your number :"))
# print("divisible by 5 and 10")if num % 5 ==0 and num % 10 == 0 else print(" not divisible by 5 and 10")

# check the email and password is correct or not

# email = input("Enter your email :")
# password = int(input("Enter your password :"))
# print("both are correct")if email == "imrat02@gmail.com" and password == 1234 else print("email or password is not corerct")


#----------------------------------------------------------list -----------------------------------

# list = [1,2,3,4,5]
# list.drop()

# list tuple set dictionary

# list   mutable
# []

# data = []
# data = list()
# print(type(data))

# Heterogeneous -> which store differnet type of data
# list tuple set dictionary
# data = [10,6.7,"raj",True,6+7j, [1,4,52] ]
# print(data)

# it allows duplicate values
# data = [1,2,1,2,1,2,1,2,1,2]
# print(data)

#        0    1  2    3   4   5
# data = [ 12, 12, 34, 37, 23, 16]
#        -6  -5  -4  -3  -2  -1

# print(data[0])
# print(data[-1])
# print(data)   # variable_name[indexing]  []->subscript operator


# data = [10,50,35,20]
# data[0] = data[0] + 5
# data[1] = data[1]+10
# data[2] = data[0]+5
# data[0] = "rahul"
# data[0],data[1] = "raj","rahul"
# print(data)
# li = [5,46,2,5,6,3]

# common method/function of list tuple set dicitonary
# print(len(li))
# print(max(li))
# print(min(li))
# print(sum(li))
# li.reverse()
# li.sort()   # assending
# li.sort(reverse=True)  # dessending
# print(li)
# print(li.index(24))

# print(li.count(24))
# to remove element from a list
# li.pop()
# li.pop(1)
# li.remove(24)
# li.clear()
# del li
# print(li)
# to add elemment in a list
# li.append(100)
# li.insert(1,90)
# li.extend([1,4,1,32,4])   # iterable object  list tuple set
# print(li)



# -------------------------------------------tuple ----------------------------------------

# Tuple ()
# immutable
# same as list
# duplicate allowed
# indexing
# heterogenous
# insersion order presevered
# dynamic


# data = ()
# data = tuple()
# data = (10,)
# print(type(data))

# data = (1,6,43,6,5,3)
# ans = sorted(data)
# ans = tuple(ans)
# print(ans)

# data[0] = data[0]+1
# data[0]=100
# print(len(data))
# print(max(data))
# print(min(data))
# print(sum(data))
# print(data.count(1))
# print(data.index(43))
# print(data)

# print(data[0])
# print(data[-1])


# li = [1,3,2,3]
# li = tuple(li)
# li = list(li)

# int(input())


# data = 1,4,2,4,2  # packing of data
# a,b,c,d,e = data  # unpacking of data
# print(d)
# print(data)



# a=10
# b=20
# c=40

# data = a,b,c
# num1,num2,num3 = data
# print(data)


# QUIZ GAME

# questions = (
#     '1 - Python was developed in ',
#     '2 - Pyhton was developed by ',
#     '3 - which one is not a keyword in python '
# )

# options = (
#     'A 1991 B 1990 C 1992 D 1993',
#     'A bejerne lee  B Guido van rousum  C none  D both a b',
#     'A True  B False  C true  D None'
# )

# answers = ("A","B","C")

# points = 0

# print(questions[0])
# print(options[0])
# ans = input("Enter your option ").upper()
# points += 1 if ans==answers[0] else 0


# print(questions[1])
# print(options[1])
# ans = input("Enter your option ").upper()
# points += 1 if ans==answers[1] else 0

# print(questions[2])
# print(options[2])
# ans = input("Enter your option ").upper()
# points += 1 if ans==answers[2] else 0


# print("Your total scores are",points)

# ----------------------------------------------------------------------------------------------------

# remove duplicate from list
# li = [1,2,1,2,4,12,32,2,411,21,21,31]
# li = set(li)
# li = list(li)
# print(li)


# set
# {}
# unique
# unordered
# indexing not allowed
# mutable
# data = {1,13,15,73,15,5}
# print(data[0])
# print(type(data))


# data1 = {10,80,60,40}
# data2 = {20,80,10,90}

# set mathematic fubction
# union    # return all value of add duplicate value single time
# data1 = data1.union(data2)
# print(data1)
# intersection     # return common value
# data1 = data1.intersection(data2)
# print(data1)
# difference  # which persent in x but not in y
# data1 = data1.difference(data2)
# print(data1)
# symmentic_dufference  # only return unique values
# data1 = data1.symmetric_difference(data2)
# print(data1)


# to add data in a set
# data.add(100)
# data.update({1,3,6,43,3})    # iterable object

# to remove element from a set
# data.pop()
# data.remove(89)
# data.discard(89)
# data.clear()
# del data

# print(data)
#---------------------------------------------dictionary ---------------------------------------

# dictionary  {}
# key-value pair
# key -> unique
# value -> can be duplicate
# heterogenonus
# indexing not allowed

# data = {}
# data = dict()
# print(type(data))

# data ={
#     "name":"raj",
#     "rollno":10101,
#     1012 : 200,
#     "course":["python","numpy","pandas"]
# }

# print(data.get("age","value does not exist"))
# print(data["age"])

# print(data.keys())
# print(data.values())
# print(data.items())

# print(len(data))
# print(max(data))
# print(min(data))

# to remove element from a dictionary
# data.pop("name")
# data.popitem()
# data.clear()
# del data



# to add key-value pair in dictionary
# data.setdefault("age",24)
# data.update({"age":12,"fees":50000})

# print(data["name"])
# print(data["course"])


# to add key-value pair in dictionary
# variable_name[key] = value
# data["age"]=24        # new key value pair add    
# data[1012] += 300     # update value
# data["name"] = "rahul"   #  override value



# count the frequency of an element in a list
#li = [1,2,1,2,1,2,2]
#1:3   2:4

# li = [1,1,2,1]
# data = {}
# print(data)

# data[li[0]] = data.get(li[0],0)+1
# print(data)

# data[li[1]] = data.get(li[1],0)+1
# print(data)

# data[li[2]] = data.get(li[2],0)+1
# print(data)

# data[li[3]] = data.get(li[3],0)+1
# print(data)


# -------------------------------------------------- if else ----------------------


# n = int(input("Enter your number :"))
# if n:
#     print("give val is :{n}")
# else:
#     print("Empty data :")

# n =input("Enter your values :")
# print(n)
# print(type(n))
# x = list(n)
# print(x)
# print(type(x))

# n = int(input("Enter your number :"))
# if(n>0):
#     print("it is the posivite number :")
# elif(n<0):
#     print("it is negative number :")
# else:
#     print("it is not a number :")

# num1 = int(input("Enter your number 1 :"))
# num2 = int(input("Etner your number 2 :"))
# num3 = int(input("Enter your number 3 :"))
# if(num1 > num2 and num1 > num3):
#      print("num1 is grater :",num1)
# elif(num2 > num1 and num2 > num3):
#      print("num2 is grater :",num2)
# else:
#      print("num3 is grater :",num3)

# n = int(input("Enter your values :"))
# if (n % 2 == 0):
#     print("even number :",n)
# else:
#     print("odd number :",n)

# n = int(input("Etner your numebr :"))
# if(n % 2 != 0):
#     print("odd number :",n)

# while loop 
#---->
# n = int(input("Enter your number :"))
# a,b = 0,1
# while n > 0:
#     print(a)
#     c = a+b
#     a = b
#     b = c
#     n -= 1

# n = int(input("Enter your numberr :"))
# i = 1
# while i<=n:
#     print("*"*n)
#     i = i+1

# n = int(input("Enter your number :"))
# i = 1
# while i <=n:
#     print("*"*i+" " *(n-1))
#     i = i + 1

# n = int(input("Enter your number :"))
# i = 1
# while i <=n:
#     print(" " *(n-i) + "*" * i)
#     i = i + 1


# n = int(input("Enter your number :"))
# i = 1
# while i <=n:
#     print(' ' * (n-i) + "*" * i)
#     i = i + 1

# n = int(input("Enter your number :"))
# i = 0
# while i < n:
#     print('*' * (n-i) + ' ' * i)
#     i = i + 1

# n = int(input("Etner your number :"))
# i =0 
# while i < n:
#     print(' ' * i + '*' * (n-i))
#     i = i + 1

# n = int(input("Enter your number :"))
# i = 0
# while i < n:
#     print(' '*i +'* '*(n-i))
#     i = i+ 1


# ---> for loop 