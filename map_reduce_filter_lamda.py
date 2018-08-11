# >>>>>>>>>>>>>>>>>>>>>>>>>>>lamda<<<<<<<<<<<<<<<<<<<<<<

function = lambda x,y:x+y
# possible
functionBool = lambda x,y:x==y 
# possible

testCalculation=function(2,3)
testboolCheck = functionBool(2,2)
print(testCalculation)
print(testboolCheck)




numberlist1=[1,2,3,4,5]
numberlist2=[10,20,30,40,50,51] 
testtuplelist=list(zip(numberlist1,numberlist2))

print(testtuplelist)
print(testtuplelist[0][1])

testtupleZipObject=zip(numberlist1,numberlist2)




result = map(lambda x,y:x+y,numberlist1,numberlist2)

print(list(result))


# [11, 22, 33, 44, 55]







#>>>>>>>>>>>>>>>>MAP<<<<<<<<<<<<<<<<<
# def fahrenheit(T):
#     return ((float(9)/5)*T + 32)
# def celsius(T):
#     return (float(5)/9)*(T-32)


someTemperature = [39.2,38.0,41.0,30]


resultlist=map(lambda x:(float(9)/5)*x + 32,someTemperature)

print(list(resultlist))


# 5
# True
# [102.56, 100.4, 105.8, 86.0]




#>>>>>>>>>>FILTER<<<<<<<<<<<<<<

somenumbers = [2,7,11,13,19,20]

oddnumberlist=filter(lambda x: x%2==0,somenumbers)

print(list(oddnumberlist))

# output
# [2, 20]

#>>>>>>>>>>>REDUCE<<<<<<<<<<<<<

some_numbers_to_add = [2,7,13,100]
import functools
summation = functools.reduce(lambda x,y:x+y,some_numbers_to_add)

print(summation)

# output
# 122






