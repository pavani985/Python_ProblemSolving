#1. Consecutive Pass Count
# num=[8,40,55,20,36,70,90,15,45]
# longest_cons_seq=0
# curr_seq=0
# for i in num:
#     if i>35:
#         curr_seq+=1
    
#         if curr_seq>longest_cons_seq:
#             longest_cons_seq=curr_seq
#     else:
#         curr_seq=0
# print(longest_cons_seq)


#2. Largest Prime Entered
# num=[12,17,21,29,18,7]
# largest_prime=0
# for n in num:
#     is_prime=True

#     if n<2:
#         is_prime=False
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 is_prime=False
#                 break
#     if n>largest_prime:
#         largest_prime=n
# print(largest_prime)
   

#3. Sum of Even Digits
# num=4827316
# sum_even=0

# while num>0:
#     digit=num%10
#     if digit%2==0:
#         sum_even+=digit
#     num=num//10
# print(sum_even)


#4. Factory Quality Check
# scores=[45,60,72,38,80,49]
# good_count=0
# def_count=0
# for i in scores:
#     if i>50:
#         good_count+=1
        
#     else:
#         def_count+=1
# print(f'good = {good_count}')
# print(f'defectiive = {def_count}')



#5. Maximum Sales Increase
# sales=[100,130,110,180,200]
# max_sales=0
# for i in range(1,len(sales)):
#     today_sales=sales[i]
#     yest_sales=sales[i-1]
#     sales_inc=today_sales-yest_sales
#     if sales_inc>max_sales:
#         max_sales=sales_inc
# print(max_sales)


#6. Number with Most Digits
# num=[23,9876,105,123456,89]
# max_digits=0
# result=0

# for n in num:
#     temp=n
#     digit_count=0

#     while temp>0:
#         digit=temp%10
#         digit_count+=1
#         temp=temp//10
#         if digit_count>max_digits:
#             max_digits=digit_count
#             result=n
# print(result)


#7. Count Numbers Divisible by Both 4 and 6
# num=[12,24,18,36,40,48]
# count=0
# for i in num:
#     if i%4==0 and i%6==0:
#         count+=1
# print(count)


#8. Longest Odd Streak
# num=[3,5,8,7,9,11,4,13]
# long_streak=0
# curr_streak=0
# for i in num:
#     if i%2==1:
#         curr_streak+=1

#         if curr_streak>long_streak:
#             long_streak=curr_streak
#     else:
#         curr_streak=0
# print(long_streak)



#9. Smallest Digit Sum
# num=[123,81,44,70]

# least_sum=999

# for n in num:
#     temp=n
#     sum_digit=0

#     while temp>0:
#         digit=temp%10
#         sum_digit+=digit
#         temp=temp//10

#     if sum_digit<least_sum:
#         least_sum=sum_digit
   

# print(least_sum)


#10.Running Balance
# balance=1000
# amount=[500,-200,300,-100]
# for i in amount:
#     balance+=i
#     print(f'Balance : {balance}')
# print(f'Final Balance : {balance}')
    











