def w1(func):
	def inner():
		print('---verification-----')
		func()
	return inner

@w1
def f1():
	print('-----f1-----')
@w1
def f2():
	print('-----f2-----')


# innerFun = w1(f1)
# innerFun = w1(f2)
# innerFun()

f1()
