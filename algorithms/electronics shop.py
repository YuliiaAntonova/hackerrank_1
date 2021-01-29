def getMoneySpent(keyboards, drives, b):
    '''
    1. Create an empty list a from the sum of elements
    2. If not a return -1, else return max(a)
    '''
    a = []
    for i in keyboards:
        for j in drives:
            if i+j <= b:
                a.append(i+j)
    if not a:
        return -1
    else:
        return max(a)

print(getMoneySpent([40,50,60],[5,8,12],b=60))