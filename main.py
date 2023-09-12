#1 implement a recursive function to calculate the factorial of a given number 
i=1
fact=1
n=int(input("Enter the number:"))
while(i<=n):
     fact=fact*i
     i=i+1
print(fact)