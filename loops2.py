# 1. Highest Profit Month
# Definition: Find the maximum value and its position while reading inputs.

# profits=[12000,15000,9800,17500,16000]
# highest_profit=profits[0]
# for profit in range(len(profits)) :
#     if profits[profit]>highest_profit:
#         highest_profit=profits[profit]
# print(f'Highest Profit : {highest_profit}')
# print(f'Month : {profit}')


#2. Perfect Square Counter
# Definition: A perfect square is the square of an integer.
# num=[16,20,25,18,49]
# count=0
# for i in num:
#     j=1
#     while j*j<=i:
#         if j*j==i:
#             count+=1
#             break
#         j+=1
# print(count)


#3.3. Sum of Multiples of 7
# Definition: Multiples of 7 are numbers divisible by 7
# number=7
# sum=0
# for i in range(10,36):
#     if i%number==0:
#         sum+=i
# print(sum)

        
    
#4. Longest Positive Streak
# num=[5,7,-2,4,9,10,12,-5]
# curr_streak=0
# longest_streak=1
# for i in num:
#     if i>0:
#        curr_streak+=1
#        if curr_streak>longest_streak:
#             longest_streak=curr_streak
#     else:
#             curr_streak=0
# print(longest_streak)



#5. Count Numbers with Exactly Three Divisors
# num=[4,9,8,16,25]
# count=0
# for n in num:
#     divisors_count=0

#     for i in range(1,n+1):
#         if n%i==0:
#             divisors_count+=1

#     if divisors_count==3:
#         print(n)


#6.6. Largest Difference
# num=[10,25,18,40,32]
# larg_diff=0
# for i in range(len(num)-1):
#     diff=num[i+1]-num[i]
#     if diff>larg_diff:
#         larg_diff=diff
# print(larg_diff)


#7. Salary Bonus
# sal=[25000,40000,18000,32000,29000]
# count=0
# for salary in sal:
#     if salary<30000:
#         count+=1
# print(count)



#8. Largest Digit Sum
# num=[123,98,555,71]
# result=0
# largest_digit_sum=0

# for n in num:
#     temp=n
#     sum1=0

#     while temp>0:
#         digit=temp%10
#         sum1+=digit
#         temp=temp//10

#     if sum1>largest_digit_sum:
#         largest_digit_sum=sum1
#         result=n
# print(result)


#9. Average Until Zero
# num=[8,12,20,0]
# total=0
# count=0
# for i in num:
#     if i==0:
#         break
#     else:
#         total+=i
#         count+=1
# avg=total/count
# print(f'{avg:.2f}')


#10. Count Numbers Greater Than Average
# num=[10,20,30,40,50]
# total=0
# count=0
# result=0

# for i in num:
#     total+=i
#     count+=1
# avg=total/count

# for i in num:
#  if i>avg:
#     result+=1
# print(result)



    

    




    




