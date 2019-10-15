# https://app.codesignal.com/challenge/2cnGDhLAdiShkfdNn

def primeFactors2(n):
    root = get_root(n)
    primes = set()
    for i in range(1, root + 1):
        if not n % i and i not in primes:
            opp = n // i
            i_root = get_root(i)
            opp_root = get_root(opp)
            j, k = 2, 2
            while j <= i_root:
                if not i % j:
                    break
                j += 1
            if j > i_root and i != 1:
                primes.add(i)
                
            while k <= opp_root:
                if not opp % k:
                    break
                k += 1
            if k > opp_root and opp != 1:
                primes.add(opp)
                    
                  
    primes_list = list(primes)
    primes_list.sort()
    return primes_list

def get_root(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
    
    

