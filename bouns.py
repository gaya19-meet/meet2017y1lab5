def draw (n, m ,border , fill):
	print(border * (m))
	for i in range (n-2):
		print (border + fill*(m-2) + border )
	print(border * (m))

draw (5 , 12 , '@' , 'x')