def gen_fact(n):
    a = 1
    for i in range(1, n+1):
        a *= i
        yield a


nf = 10
factorials = [x for x in gen_fact(nf)]
print(f"The factorials until {nf}: {factorials}")