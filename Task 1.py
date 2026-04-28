more = [x+1 for x in [1, 2, 3, 4,]]    # it takes in 1 then 2,. 3,. 4
print()            # more = [ 2, 3, 4, 5]

def square( n:int) -> int:
    return n*n

squares = [ square(x) for x in [1, 2, 3, 4,]]        # n = 1 returns 1, n = 2 returns 4
print()                                         #n = 3 returns 9, n = 4 returns 16
                                             # squares = [ 1, 4, 9, 16] this line of code
                                             #  returns a new list of the squared values

def check(n: int ) -> bool:
    return n > 2                            # n = 0 returns false, n = 1 returns false,n = 2 returns false,
                                            # n = 3 returns True, n = 4 returns True,
answer = [ x for x in range(5) if check(x)]     # answer = [3, 4]
print()

def inc ( m: int ) -> int:          #m = 3 returns 4 , 4 returns 5
    return m + 1


def check1( n: int) -> bool:        # n = 0 returns false, n = 1 returns false,n = 2 returns false,
                                            # n = 3 returns True, n = 4 returns True,
    return n > 2

answer1 = [inc(x) for x in range(5) if check1(x)]    # answer = [ 4,5 ]
print()
