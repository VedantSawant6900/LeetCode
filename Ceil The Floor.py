def getFloorAndCeil(a, n, x):
    lb=0
    ub=n-1
    fl=0
    cl=0
    while lb<=ub:
        mid = int((lb+ub)/2)
        if a[mid]>x:
            ub=mid-1
        elif a[mid]<x:
            lb=lb+1
        else:
            return [a[mid],a[mid]]
    print(mid)
    if mid==0 and x<a[mid]:
        return [-1,a[mid]]
    if mid==n-1 and x>a[mid]:
        return [a[mid],-1]
    if a[mid]>x:
        return [a[mid-1],a[mid]]
    else:
        return [a[mid],a[mid-1]]
print(getFloorAndCeil([2], 1, 23))
