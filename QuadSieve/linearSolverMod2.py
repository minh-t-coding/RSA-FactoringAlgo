
def dimensions(a):
    assert(len(a)>0)
    return len(a),len(a[0])

def triangulate(a):
    """
    Algorithm taken from https://www.cs.umd.edu/~gasarch/TOPICS/factoring/fastgauss.pdf
    Solves an nxm matrix for combinations that sum to 0
    """
    n,m=dimensions(a)
    mark=[None]*n
    
    for j in range(m):
        for i in range(n):
            if a[i][j]==1:
                mark[i]=j
                for k in range(m):
                    if j!=k and a[i][k]==1:
                        for l in range(n):
                            a[l][k]=(a[l][k]+a[l][j])%2
                break
    return mark

def solve(a):
    n,m=dimensions(a)
    mark=triangulate(a)

    marked=[]
    unmarked=[]
    for i in range(len(mark)):
        if mark[i]!=None:
            marked.append(i)
        else:
            unmarked.append(i)

    result=[]
    for i in unmarked:
        ones={j for j in range(m) if a[i][j]}
        dependencies={j for j in marked if mark[j] in ones}
        dependencies.add(i)
        result.append(dependencies)

    return result


def printMatrix(a):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in a]))



