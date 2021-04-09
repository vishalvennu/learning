x = 10
start = 0
end = x


while (int(start) != int(end)):
    mid = (start + end)/2
    if (mid*mid == x):
        print (mid)
    elif (mid*mid > x):
        end = mid
    elif (mid*mid < x):
        start = mid
print(start)