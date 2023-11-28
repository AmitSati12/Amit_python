# li =[3,5,234,"harry"]

# print(type(li))
# print(li)



# n=7
# for i in range (0,n):
#     print(i)

#drive 

age =int(input("enter the age "))
if(age>=18):
    print("you can drive ")
else:
    print("cant drive ")



#prime number 
num =int(input("enter the number ")) 
if num==1:
    print("the is not prime")
else:
    for i in range(2,num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")