import sys

n = int(sys.argv[1]) + 1

def is_prime(n):
    i = 2
    while i < n and n % i != 0:
       i = i + 1

    return n == i


print('Multiples of 3: {}'.format([num for num in range(1, n) if not num % 3]))

print ('Multiples of 3 squared: {}'.format([num * num for num in range(1, n) if not num % 3]))

print ('Multiples of 4 doubled: {}'.format([num * 2 for num in range(1, n) if not num % 4]))

print ('Multiples of 3 or 4: {}'.format([num for num in range(1, n) if not num % 3 or not num % 4]))

print ('Multiples of 3 and 4: {}'.format([num for num in range(1, n) if not num % 3 and not num % 4]))

print ('Multiples of 3 replaced: {}'.format(['X' if not num % 3 else num for num in range(1, n)]))

print ('Primes: {}'.format([num for num in range(1, n) if is_prime(num)]))


