# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronicnumber(n):
    f=0
    for i in range(1,n):
        if n==i*(i+1):
            f=1
            break
    return f==1

def nthpronicnumber(n):
    f=1
    g=0
    while(f<=abs(n)):
        g=g+1
        if(pronicnumber(g)):
            f=f+1
    return g