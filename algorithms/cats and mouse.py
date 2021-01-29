def catAndMouse(x, y, z):
    a=abs(x-z)
    b=abs(y-z)
    if a > b:
        return 'Cat B'
    if a==b:
        return 'Mouse C'
    else:
        return 'Cat A'
print(catAndMouse(x=1,y=2,z=3))