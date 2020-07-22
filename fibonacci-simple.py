iterations=100
num=[]

def getfibonacci(n):
    if n <= 1:
        return 1
    else:
        return getfibonacci(n - 1) + getfibonacci(n - 2)

for i in range(1, iterations):
    print(getfibonacci(i))