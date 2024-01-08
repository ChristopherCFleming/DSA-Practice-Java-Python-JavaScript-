# is prime
# Write a function, is_prime, that takes in a number as an argument. The function should return a boolean indicating whether or not the given number is prime.

# A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

# For example, 7 is a prime because it is only divisible by 1 and 7. For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

# You can assume that the input number is a positive integer.

# is_prime(2) # -> True
# is_prime(3) # -> True
# is_prime(4) # -> False
# is_prime(5) # -> True
# is_prime(6) # -> False
# is_prime(7) # -> True
# is_prime(8) # -> False
# is_prime(25) # -> False
# is_prime(31) # -> True
# is_prime(2017) # -> True
# is_prime(2048) # -> False
# is_prime(1) # -> False
# is_prime(713) # -> False

import math


def is_prime(n):
    maximum_iteration = math.floor(math.sqrt(n))
    current_iteration = 2

    if n == 1:
        return False
    if n == 2:
        return True

    while current_iteration <= maximum_iteration:
        if n % current_iteration == 0:
            return False
        else:
            current_iteration += 1

    return True
