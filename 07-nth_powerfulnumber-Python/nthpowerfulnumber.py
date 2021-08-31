# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isPowerful(n):
    while (n % 2 == 0):
        a = 0
        while (n % 2 == 0):
            n = n // 2
            a = a + 1
        if ( a == 1):
            return False
    for power in range(3, int(math.sqrt(n))+1, 2):
        a = 0
        while (n % power == 0):
            n = n // power
            a = a + 1
        if (a == 1):
            return False
    return (n == 1)

def nthpowerfulnumber(n):
    found = 0
    guess = 0
    while (found <= abs(n)):
        guess += 1
        if(isPowerful(guess)):
            found += 1
    return guess
