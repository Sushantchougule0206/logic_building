n=int(input("Enter the number:"))
sum=0
a=n
length=len(str(n))
while n>0:
    arm=n%10
    sum=sum+arm**length
    n=n//10
if a == sum:
    print("Yes,It is armstrong number")






