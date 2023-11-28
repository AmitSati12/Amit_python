# tuples >>>> it is same as string but are immutable .
tuple1=("hero",1,11,123444)
print(tuple1)
print(tuple1[0:3])
print(len(tuple1))

# tuple inside tuple 
# tuple NESTING
tuple2=("hii",15,(12,1234),"hello")
print(tuple2[2][1])


# List .>>>>>are same as tuples but are muatable 
list1=["herry bhai",12,]
print(list1[0])
# we can do nesting in list also and add tuples inside list
list2=["sorry",12,[123,1234],("amit",15),987654321]


# ADD ELEMENT IN LIST 
# list=list2+["add kr diya "]
list=[14,334,344]

# ADD SINGLE ELEMENT 
# list.extend([1000])
list.append([10,20])


#  how to change element in list 
# list[0]="amit"
# print(list)
# # Splite
# list1.split(",")
# print(list1)


# how to make copies of list 
A=["abcd","efgh"]
b=A[:]    #>>>>>>we use "":"" for there is no change in second list  
A[1]=("ABCD")
print(A[1])
help(A)#>>> use to check operation which can perform in list 
print(b[1])
