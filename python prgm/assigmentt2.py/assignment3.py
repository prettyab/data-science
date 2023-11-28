# 1.
# sum=int(input("enter the number"))
# if sum>0:
#     print('postive')
# else:
#     print('negative')

# 2.
# num=int(input("enter the number"))
# if (num%2==0):
#     print(" is even")
# else:
#     print("is odd")

# 3.
# n=int(input("enter the number"))
# factorial=1
# if n<0:
#     print("factorial is does not exit for negative number")
# elif n==0:
#     print("factorial 0 is 1")
# else:
#     for i in range(1,n+1 ):
#         factorial=factorial*i
#         print("the factorial",n,"is",factorial)

# 4.
# num_1=10
# num_2=11
# # num_3=num_1%num_2
# # print(num_3)
# # num_4=num_1-num_2
# # print(num_4)
# num_5=num_1*num_2
# print(num_5)

# rows=5
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end= '')
#     print()

# 5.
# asciii_n=65
# rows=4
# for i in range(0,rows):
#     for j in range(0,i+1):
#         char=chr(asciii_n)
#         print(char,end= '')
#         asciii_n+=1
#     print("")

# 6.
# str=input()
# if str==str[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# # 7.
# list=[1,2,3,4,5]
# result=sum(list)
# print(result)

# 8.
# n=51
# for i in range(1,51):
#     print(i,end='')

# 9.
lower = int(input("enter lower limit >1 :"))
upper = int(input("enter upper limit :"))
for i in range(lower, upper+1):
    if i >1:
        for num in range(2,i):
            if i%num==0:
             break
        else:
            print(i)
