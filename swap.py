# This program is for simple swapping of two numbers or strings
#Here we are taking inputs from the user:

x=input("Enter the value of X:")
y=input("Enter the value of Y:")

#this is the main logic for swapping:

temp=x
x=y
y=temp

#output:

print(f"Value of X after swapping is : {x}")
print(f"Value of Y after swapping is : {y}")