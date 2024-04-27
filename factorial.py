def factorial(num):
    fact=1
    while num>0:
        fact=fact*num
        num-=1
    print(fact)
Num=int(input("Enter the number:"))
factorial(Num)
    


