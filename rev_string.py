# def reverse_string(str):  
#     str1 = ""   # Declaring empty string to store the reversed string  
#     for i in str:  
#         str1 = i + str1  
#     return str1    # It will return the reverse string to the caller function  
     
# str = "Java Tpoint"    # Given String       
# print("The original string is: ",str)  
# print("The reverse string is",reverse_string(str)) # Function call  


str="this is me bro "

# print(str.split(str[::-1]))

new_string=str.split()



# original_string = "hello world"
# words = original_string.split()  # Split the string into a list of words

reversed_words = ' '.join(word[::-1] for word in new_string)
print(reversed_words)

