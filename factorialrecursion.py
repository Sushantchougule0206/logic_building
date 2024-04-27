def factorial(fact):
    if fact==0:
        return 1
    else:
        return fact*factorial(fact-1)

num=int(input("Enter the number:"))
result=factorial(num)
print(result)