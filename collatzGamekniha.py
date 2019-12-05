print("This is colatz sequence")
user = int(input("please enter a number \n"))
           
def collatz(n):
    print(n)
           
    while n!= 1:
           
        if n % 2 == 0:
            n = n // 2
            print(n)
           
        else:
           n = n * 3 + 1
           print(n)


collatz(user)
           
