# ---------------------------------------- for loop ---------------------------------
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
n = int(input("Enter your number :"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
# 1 
# 1 1 
# 1 1 1 
# 1 1 1 1 
# 1 1 1 1 1
# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     x =1
#     for j in range(1,i+1):
#         print(x,end=' ')
#     print()


# 3 
# 3 6 
# 3 6 9 
# 3 6 9 12 
# 3 6 9 12 15 

# n = int(input("Enter your number :"))
# for i in range(1,n+1):
#     x = 3
#     for i in range(1,i + 1):
#         print(x,end=' ')
#         x = x+3
#     print()
