# Read marks of N students. Count how many scored 35 or more.
# marks=[5,45,20,67,35,18]
# count=0
# for mark in marks:
#     if mark>35:
#         count+=1
# print(count)


#Shop Profit Days
# Read profit for N days. Count days with profit greater than Rs.1000.
# profit=[5,800,1200,1500,950,2000]
# count=0
# for i in profit:
#     if i>1000:
#         count+=1
# print(count)/



#  Largest Multiple of 5
# Task: Read N numbers. Print the largest divisible by 5, else 'No Multiple of 5'.
# num1=[5,12,25,18,40,7]
# largest_multiple=1
# for i in num1:
#     if i%5==0:
#        if i>largest_multiple:
#              largest_multiple=i
# print(largest_multiple)
            

# . Average of Even Numbers
# Task: Read N numbers. Print average of even numbers, else 'No Even Numbers'.
# num1=[5,2,5,8,7,10]
# sum_even=0
# count=0
# for num in num1:
#     if num%2==0:
#         sum_even+=num
#         count+=1

# if count>0:
#     avg=sum_even/count
#     print(f'{avg:.2f}')
# else:
#     print("No even numbers")



#  Student Improvement
# Task: Read marks in N tests. Count how many times marks increased.

# marks=[5,50,55,52,60,70]

# count=0
# for i in range(1,len(marks)):
#     current_marks=marks[i]
#     previous_marks=marks[i-1]
#     if current_marks>previous_marks:
#         count+=1
# print(count)


#Divisors Count
# Task: Read a number and count its divisors.
# num=int(input("enter a number : "))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# print(count)


# Smallest Odd Number
# Task: Read N numbers. Print smallest odd number or 'No Odd Number'.
# num=[5,8,13,6,5,10]
# smallest_odd=5
# for i in num:
#     if i%2==1:
#         if i<smallest_odd:
#             smallest_odd=i
# print(smallest_odd)


# Count Numbers Ending with 7
# Task: Read N numbers. Count numbers ending with digit 7.
# num=[5,27,15,97,120,47]
# count=0
# for i in num:
#     if i%10==7:
#         count+=1
# print(count)


#  Multiplication Table
# Task: Read a number and print table from 1 to 15.
# num=int(input("enter a number : "))
# for i in range(1,16):
#    print(f'{num}x{i}={num*i}')


# #Sum Until Negative Number
# Task: Read numbers until a negative number is entered. Print sum of positive numbers.

# num=[5,10,8,2,-1]
# sum=0
# for i in num:
#     if i>0:
#         sum+=i
#     else:
#         break

# print(sum)

