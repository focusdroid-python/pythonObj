def test(number):
	def test_in(test_number):
		print(number + test_number)

	return test_in




b = test(100)
b(100)