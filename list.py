# Consider a list (list = []). You can perform the following commands:

#1 insert i e: Insert integer  at position .
# 2 print: Print the list.
#3 remove e: Delete the first occurrence of integer .
#4 append e: Insert integer  at the end of the list.
# 5sort: Sort the list.
#6 pop: Pop the last element from the list.
# 7 reverse: Reverse the list.



# solution 
if __name__ == '__main__':
    N = int(input())
List=[];

for i in range(N):

        command=input.split();

        if command[0] == "insert":
# 1.insert
            List.insert(int(command[1]),int(command[2]))

        elif command[0] == "append":
# 2. append
            List.append(int(command[1]))

        elif command[0] == "pop":
#   3.pop 
          List.pop();

        elif command[0] == "print":
# 4.print 
            print(List)
# 5. remove 
        elif command[0] == "remove":

# 6. remove         
         List.remove(int(command[1]))
# 7.sort 
        elif command[0] == "sort":

         List.sort();

        else:

            List.reverse();