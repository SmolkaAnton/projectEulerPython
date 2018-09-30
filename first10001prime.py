def main():
    num_prime = int(input("How many prime numbers do you want to check: "))
    prime_numbers = find_primes(num_prime)
    print("The first ", num_prime, " numbers are: ", prime_numbers)

def isPrime(num):
    x = True
    for i in range(2, num):
       if num%i == 0:
           x = False
           break
    return x

def find_primes(num):
    primes = [2]
    size = len(primes)
    test = 3

    while(size<num):
        if(isPrime(test)):
            primes.append(test)
            size+=1
        test+=2
    return primes

main()
