import random

test_list = list()


for x in range(10):
	test_list.append(random.randint(1,20))


print('list before sortining:',test_list)
i = 0
j=0
for x in range (len(test_list)-1):

	for y in range(len(test_list)-(1+j)):
		i=i+1
		if test_list[y] >test_list[y+1]:
			test_list[y],test_list[y+1]=test_list[y+1],test_list[y] 
	j=j+1
print('list after sortining:',test_list,i)