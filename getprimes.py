def isPrime(n, d = 2):
    if (n == 1):
        return False
    if (n == 2):
        return True
    if (n % d == 0): #its not prime if no remainder
        return False
    if ( d ** 2 > n): #when divisor squared is greater than number it must be prime
        return True
        
    return isPrime(n, d + 1)


x=1
y=100
for i in range(x,y):
    if (isPrime(i)):
        print(str(i) + ": Is Prime")
