def sol(e,l):
    e=int(input("Enter The Number of Heads:"))
    l=int(input("Enter The Number of Legs :"))
    for c in range(e+1):
        h=e-c
        if (h*2)+(c*4)==l:
            return h,c
    return None,None