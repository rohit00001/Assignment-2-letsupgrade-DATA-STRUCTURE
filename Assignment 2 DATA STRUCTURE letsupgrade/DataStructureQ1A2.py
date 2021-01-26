#Write a Python program to print even numbers in a list.
#Sample:
#Input: list1 = [12, 3, 55, 6, 144]
#Output: [12, 6, 144]
#Input: list2 = [2, 10, 9, 37]
#Output: [2, 10]
#PROGRAM


list1 = [12, 3, 55, 6, 144]
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")
