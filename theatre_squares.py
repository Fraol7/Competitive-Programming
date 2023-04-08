def theatre_square(n,m,a):
    if n%a != 0:
        quo1 = (n//a) + 1
    else:
        quo1 = n//a
    if m%a != 0:
        quo2 = (m//a) + 1
    else:
        quo2 = m//a
    return quo1 * quo2
