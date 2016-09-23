def game(n,a,b,c):
	if n==1:
		print a + '->' + c
	else :
		game(n-1,a,c,b)
		print a + '->' + c
		game(n-1,b,a,c)

number = raw_input('please chooes how many plates you want: ')

game (int(number),'a','b','c')	
