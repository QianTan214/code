def nats(n):
    yield n
    yield from nats(n+1)


def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n != 0)

g = sieve(nats(2)) # g is generator object


