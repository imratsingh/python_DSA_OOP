# ---------------------------------------- for loop ---------------------------------5
# *
# * *
# * * *
# * * * *
# * * * * *
# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# * * * *
# * * * *
# * * * *
# * * * *

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *
# n = int(input("Enter your number :"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     print(' '*(n-i),end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     print(' '*(n-i),end="")
#     for i in range(i):
#         print('*',end="")
#     print()

# 1 
# 1 1 
# 1 1 1 
# 1 1 1 1 
# 1 1 1 1 1

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     for i in range(1,i+1):
#         print("1",end=" ")
#     print()

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     x = 1
#     for j in range(1,i+1):
#         print(x,end=" ")
#     print()

# 3 
# 3 6 
# 3 6 9 
# 3 6 9 12 
# 3 6 9 12 15 

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     x = 3
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x = x + 3
#     print()
# -----------------------------------------------------------------------
# ✔ ord() → character to integer
# ✔ chr() → integer to character

# A
# A B 
# A B C 
# A B C D 
# A B C D E

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     ch = "A"
#     for j in range(i):
#         print(ch,end=" ")
#         ch = chr(ord(ch)+1)
#     print()

# A
# A B 
# A B C
# A B C D
# A B C D E 

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     ch = "A"
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch = chr(ord(ch)+ 1)
#     print()

# A 
# A C 
# A C E 
# A C E G 
# A C E G i 

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     ch = "A"
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch = chr(ord(ch)+2)
#     print()


n= int(input("enter your number :"))
for i in range(1,n+1):
    ch="A"
    for j in range(1,n+1):
        print(ch,end=" ")
        ch = chr(ord(ch)+1)
    print()
