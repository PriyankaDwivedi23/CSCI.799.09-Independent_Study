def turan(n,r):
    quotient,modulo=divmod(n,r)
    if modulo:
        return modulo * (modulo-1)//2+(2 * modulo + r * quotient)*(r-1)* quotient //2
    return n * quotient*(r-1)//2

def findSmallClique(n,m):
    low = 1
    high = 3*n*n//(n*n-2*m)
    while low < high :
        mid =(low+high)//2
        if turan(n,mid)>=m:
            high = mid
        else:
            low = mid+1
    return high

if __name__ == '__main__':
    testcase = int(input())
    for _  in range(testcase):
        n,m = [int(i) for i in input().split()]
        result = findSmallClique(n,m)
        print(result)
