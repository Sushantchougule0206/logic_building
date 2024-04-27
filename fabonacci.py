def fibonacci(n):
    x=0
    y=1
    for i in range(1,n):
        z=y+x
        print(z,end=' ')
        x=y
        y=z

num=int(input("Enter the length for seris:"))
fibonacci(num)
    