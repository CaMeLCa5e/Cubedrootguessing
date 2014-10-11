#finding a cubed root by guess and check 

x = int(raw_input("Enter an integer"))

#changed to if loop.
for ans in range(0, abs(x)+1):
	if ans**3 == abs(x):
		break

	#ans = 0
	#while ans**3 < abs(x):
	#	ans = ans +1  #Iterloop 


if ans**3!=abs(x):
	print(str(x)+ "is not a perfect cube")
else:
	if x < 0:
		ans = -ans
	print('Cube root of' + str(x)+ " is " + str(ans))