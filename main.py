import decimal 

def pi(n):
    decimal.getcontext().prec = n + 1
    C = 426880 * decimal.Decimal(1005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L 

    for i in range(1,n):
        M= M * (K ** 3 - 16 * K)/ ((i+1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M*L) / X
    num_pi = C / sqrtreturn num_pi 
