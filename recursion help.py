#def countWays will take 3 arguments n,i,j. it will return an integer of how many distinct ways there is to count to n using the integers i and j and i is less than j
def countWays(n,i,j):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return countWays((n-i),i,j)+countWays((n-j),i,j)

#countWays1 will take 2 arguments n,i.
# n will be an integer and i will be a tuple of distince integers
# will return how many distinct ways ther is to count to n using the integers in i
def countWays1(n,i):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return sum([countWays1(n-j,(i)) for j in i])
# a girl has to take n steps
# she can take them 1,2, or 3 at a time
# how many distinct ways there is to tak e the steps

def stepWays(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return stepWays(n-1)+stepWays(n-2)+stepWays(n-3)
