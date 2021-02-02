def countApplesAndOranges(s, t, a, b, apples, oranges):
    applescount = 0
    orangescount = 0
    for i in range (len(apples)):
        if apples[i]+a >= s and apples[i]+a<=t:
            applescount += 1
    for j in range(len(oranges)):
        if oranges[j]+b >= s and oranges[j]+b <= t:
            orangescount += 1
    print(applescount)
    print (orangescount)
print(countApplesAndOranges(s=7,t=10,a=4,b=12,apples=[2,3,-4],oranges=[3,-2,-4]))