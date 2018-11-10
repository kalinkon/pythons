numberlist1 = [1, 2, 3, 4, 5]
numberlist2 = [10, 20, 30, 40, 50, 51]
testtuplelist = list(zip(numberlist1, numberlist2))

print(testtuplelist)
print(testtuplelist[0][1])

testtupleZipObject = zip(numberlist1, numberlist2)
