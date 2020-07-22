iterations=100
num=[]

def getfibonacci(i):
    if i < len(num): # return the cached result
        return num[i]
    else: #  cached results
        if i == 0:
            num.append(0)
        elif i == 1 or i == 2:
            num.append(1)
        elif i == 3:
            num.append(2)
        else:
            num.append(getfibonacci(i-1) + getfibonacci(i-2))
    
        return num[len(num) -1]

for i in range(0, iterations):
    print(str(getfibonacci(i)))