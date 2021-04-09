A = ['a','b']
B = ['a','b']

if (len(A)!=len(B)):
    print ("False")
elif (A == B) and (len(A)==len(set(A))):
    print ("False")
elif (sorted(A) != sorted (B)):
    print ("False")
else:
    count = 0
    for i in range(len(A)):
        if(A[i] != B[i]):
            count += 1
        elif (count > 2):
            print ("False")
    print ("True")