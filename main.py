#print("hello Amit hoe are you ")

# input value in program 


#val = input("Enter your value: ")
#print(val)
 
 # enter value with data type 
#input1 =int(input('enter the integer value '))
#print(input1)
#input2 =float(input("enter the num value" ))
#print(input2)
#input3 =String(input("enter your name plz "))
#print(input3)

#enter multiple value  in same time 
#x,y =input("Enter the value :").split()
#print("number of girls ",x)
#print("number of boys",y)#

# taking two inputs at a time

#a,b =input("Enter the two values ").split()
#print("first number is {} and second number is {}".format(b,a))
 
# taking multiple inputs at a time
# and type casting using list() function
#x = list(map(int, input("Enter multiple values: ").split()))
#print("List of students: ", x)



# how to create message in simple way
#name = input("enter your name bro  : ")#"Alice"
#age = input ("enter your age bro  :" )#25

#print("Hello, my name is", name, "and I am", age, "years old.")


# string value 
import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>')
		time.sleep(1)
	else:
		print('Start')
