# print(" enter your number /n")

fact_input = int(input("Inter your number:"))

def fact(fact_input):
	if fact_input != 1:
		return fact_input * fact(fact_input-1)
	else:
		return 1 

while True:
	if fact_input > -1: 
		result = fact(fact_input)
		print(result)
		break
	else:
		fact_input = int(input("Inter your number:"))
	


