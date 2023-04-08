'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

n=int(input("Enter the number"))
for i in range(n):
    for j in range(n,i,-1):
        print("#",end=" ")
    print(" ")
for i in range(n-1):
    for j in range(i+1):
        print("#",end=" ")
    print(" ")
