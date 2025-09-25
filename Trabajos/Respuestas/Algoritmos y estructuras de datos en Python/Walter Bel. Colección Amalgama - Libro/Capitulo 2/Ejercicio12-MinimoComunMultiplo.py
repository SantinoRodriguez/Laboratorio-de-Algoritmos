def MCD(n,m):
    if m == 0:
        return n
    else:
        return MCD(n, n % m) 
    
print(MCD(270,192))