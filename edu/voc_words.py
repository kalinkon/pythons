file = open("/home/linkon/Desktop/python/edu/voc_words.txt","r")

wordlist = file.readlines()

print(wordlist)

length = len(wordlist)

print(length)
# for word in wordlist:
# 	word


for i in range(length):
	wordlist[i] = wordlist[i].replace("\n","")

new_file = open("/home/linkon/Desktop/python/edu/new_voc_words.txt","w+")

for word in wordlist:
	new_file.write(word+",")




