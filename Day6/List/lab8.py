# Write a Python program to print a specified list after removing the 0th, 4th and 5th 
# elements
a=[0,1,2,3,4,5,6,7,8,9]
for i in a:
    if i!=a[0] and i!=a[4] and i!=a[5]:
        print(i)