tup = (1,5,7,78,666,"green")
# tup[0] = 90 # we can't change tuple
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1])
if 7 in tup :
    print ("yes")
    tup = tup[ :3]
    print(tup)
    tup2 = tup[ 1:3]
    print(tup2)
