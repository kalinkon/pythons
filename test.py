# astring = "Hello world!"
# print(astring.index("o"))

# astring = "Hello world!"
# print(astring[3:7])



# lista= ["dsd",0,[1,2,3]]

# print (lista[2][2])

file = open("/home/linkon/Desktop/hello.txt","r")

# print (file.read())

string = file.readlines()
# print(string)

newList = list()
for each in string:
	if each.find("www") == -1 and each.find(" ") == -1: 
		newList.append(each.replace("\n",""))

print (newList)
# data = list()
# for line in string:
# 	data.append(line.split("/n"))


# print(data)

# alist = string.split(" ")

# # print(alist)



aset = set(newList)

counter = dict()

for a in aset:
	counter[a]=0

for a in newList:
	if a in aset:
		count = counter.get(a) +1
		counter[a]=count

print(counter)





filew = open("/home/linkon/Desktop/out.txt","w+")
filew.write("Unique Words"+"\n")

for words in aset:
	filew.write(words+'\n')


filew.write("Repeated Words"+"\n")


for key, value in counter.items():
	if value > 1 :
		filew.write(key+' '+str(value)+" times" +"\n")



