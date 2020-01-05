#! python3

# Find the largest prime factor of a given number

def largestPrimeFactor(number):
    allFactors = []
    allPrimes = []
    print(len(allPrimes))
    largestPrimeFactor = 0
# If the number is 2, go no further
    if number == 2:
        return 2
            
#Step 1: Find primes between 3 and number, checking only odd numbers
    for i in range(3, number, 2):
        isPrime = True
        if number % i == 0: #If i is a factor of number
            for j in range(2, i):
                if i % j == 0: # Check whether i is prime
                    isPrime = False
                    print('%s was divisible by %s' % (i, j))
                    break #break out of current j
                else:
                    continue #try the next j
            if isPrime == True: #If it is prime, put it in the prime factors 
                allPrimes.append(i)
    print(allPrimes)


    largestPrimeFactor = allPrimes[-1]

    return largestPrimeFactor


print('largestPrimeFactor(13195) should return 29:')                
print(largestPrimeFactor(13195))

print('largestPrimeFactor(600851475143) should return 6857:')                
print(largestPrimeFactor(600851475143))

