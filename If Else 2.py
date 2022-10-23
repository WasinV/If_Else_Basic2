friend = ['A','B','C','D','E','F']

friend2 = {'A':'เอ', 'B':'บี', 'C':'ซี'}

visitor = 'b'

if visitor in friend or visitor.title() in friend:
	print('our team')
	if visitor in friend2 or visitor.title() in friend2:
		print('Hello Khun '+ friend2[visitor.title()])
	else:
		print('Hello customer')
else:
	print('stranger')





