'''
Q.1 Write a Python function to sum all the numbers in a list.

Sample List : (8, 2, 3, 0, 7)

Expected Output : 20'''


def addition(): 
    num=int(input("Enter the numbers : ")) 
    lst1=[]
    for i in range(num):
        num1=int(input("Enter the numbers : "))
        lst1.append(num1)
    add=sum(lst1)
    return add
data=addition()
print(data)





