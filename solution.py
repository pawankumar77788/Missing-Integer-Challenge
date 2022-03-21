def Solution (A):
    A = [ele for ele in A if ele > 0]
    if len (A) != 0:
        A = list(set(A))
        A.sort()
        for i in range (len(A)):
            try:
                if A[i+1] - A[i] > 1:
                    if A[i]> and i == 0:
                        return 1
                    else:
                        return A[i]
            except:
                if A[0] > 1:
                    return 1
                else:
                    return A[i]+1
        else:
            return 1
