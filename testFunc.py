def getValue():
	integerInput = input("Input an integer: ")
	return int(integerInput)

def validateValue(value):
	if isinstance(value, int):
		return True
	else:
		return False

def findArea(var1, var2):
	return var1 * var2
