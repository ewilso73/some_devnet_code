import sys
def doubler(number):
	"""
	Given a number, double it and return the value.
	"""
	result = number * 2
	return result

if __name__ == '__main__':
	try:
		input = float(sys.argv[1])
	except (IndexError, ValueError) as e:
		print("++++++++++++++++++++++++++++++++++++++++++++")
		print("+++++++++ Welcome to the Doubler! ++++++++++")
		print("you must provide a number as a parameter to")
		print("           use this script.")
		print("Example: ")
		print("	python example1.py 100")
		print("++++++++++++++++++++++++++++++++++++++++++++")
		sys.exit(1)

	answer = doubler(input)
	print(answer)
	
