x = 540
rev_Num = 0
neg = 0
if (x == 0):
    print (rev_Num)
else: 
    if (x < 0):
        x = x - (2*x)   
        neg = 1
    while(x > 0):
        rev_Num = (rev_Num*10) + (x%10)
        x=int(x/10)
if (neg ==1):
    rev_Num = rev_Num - (2*rev_Num)    
print (rev_Num)

