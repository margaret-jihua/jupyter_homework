def primeRangeSum(num1, num2):
    # check if a number is prime
    def isPrime(n):
        if n < 1:
            return False
        for i in range(2, n-1):
            # check if n is not divisible by i
            if n % i == 0:
                return False
        else:
            return True
    sum = 0
    if num1 < num2:
        for i in range(num1, num2+1):
            if isPrime(i):
                sum += i
    else:
        for i in range(num2, num1+1):
            if isPrime(i):
                sum += i

    print(sum)


primeRangeSum(10,20)
primeRangeSum(20,29)
primeRangeSum(20,10)
primeRangeSum(50,41)