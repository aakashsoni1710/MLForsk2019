#string handling

str1=input("Enter The full name:")
a = str1.find(" ")
print(str1[a+1:],str1[:a])