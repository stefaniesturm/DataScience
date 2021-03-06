
# coding: utf-8

# ##Sieve of Eratosthenes


import argparse

def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    # Code adaptedfrom: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)

    return [2] + [el for el in sieve if el]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="return primes until n using sieve of Eratosthenes")
    parser.add_argument("n", help="return primes until n",type=int)
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
    args = parser.parse_args()
    n = args.n
    answer = sieveOfEratosthenes(n)
    if args.verbose:
        print ("List of primes numbers below {} is: \n{}".format(args.n, answer))
    else:
        print (answer)
