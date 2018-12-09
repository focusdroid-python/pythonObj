def line_conf(a, b):
	def line(x):
		print(a*x + b)

	return line

line1 = line_conf(1,1)

line1(0)