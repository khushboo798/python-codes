# def calculateGmean(a,b):
#   mean = (a*b)/(a+b)
#   print(mean)

# def isGreater(a,b):
#   if(a>b):
#    print("first number is greater")
#   else :
#    print("second number is greater or equal")

# def isLesser(a,b):
#   pass
# a = 9
# b=8
# isGreater(a,b)
# calculateGmean(a,b)

# a = 9
# b=8
# if(a>b):
#   print("first number is greater")
# else :
#   print("second number is greater or equal")
# calculateGmean(a,b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)


# c = 8
# d =7
# isGreater(c,d)
# if(c>d):
#   print("first number is greater")
# else :
#   print("second number is greater or equal")
# calculateGmean(c,d)
# gmean2 = (c*d)/(c+d)
# print (gmean2)


# def average(a=9,b=1):
# def average(a,b):
#   print("the average is" ,(a+b)/2)
#  average(1,5)
#  average()
# average(5)
# average(b=9)
# average(4,6)
# average(b=9,a=21)

# def average(a,b,c=1):
#  print("the average is" ,(a+b+c)/2)
# average(5,6)

def average(*numbers):
#  print(type(numbers))
 sum= 0
 for i in numbers :
  sum = sum + i
#   print("average is:" ,sum/len(numbers))
 return sum/len(numbers)
c= average(5,6,7,1)
print (c)