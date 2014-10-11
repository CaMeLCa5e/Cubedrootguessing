#finding a cubed root by guess and check 

x = int(raw_input("Enter an integer"))
ans = 0
while ans**3 < abs(x):
	ans = ans +1  #Iterloop 
if ans**3!=abs(x):
	print(str(x)+ "is not a perfect cube")
else:
	print('Cube root of' + str(x)+ "is" + str(ans))