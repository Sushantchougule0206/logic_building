#Perfect sqaure WAP to check if a number is perfect square ot not.
def perfectsqrt(num):
    demo=num**0.5
    demo1=int(demo)
    if demo==demo1:
        return True
    else:
        return False

sqrt=int(input("Enter the number:"))
print(perfectsqrt(sqrt))