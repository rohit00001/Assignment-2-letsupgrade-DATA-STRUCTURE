#Question 2
#Write a program to print the following pattern
#    1
#   22
#  333
# 4444
#55555
#Program

for x in range(1,6):
    for y in range(5,x,-1):
        print(" ", end="")
    for z in range(0,x):
            print(x,end="")
    print()
