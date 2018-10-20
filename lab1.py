import itertools
import collections

# #1.1
# print("Hello world")

# #1.2
# def function(number1, number2):
# 	if number1 < 0 or number2 < 0:
# 		print("Exception")   #!!!!!
# 		return False
# 	elif number1%number2==0:
# 		return True

# print(function(4, 2))
	
# #1.3

# def isComposite(n):
# 	temp = False
# 	for i in range(2,n):
# 		if function(n % i):
# 		   temp = True
# 		   break
# 	return temp

# def simpleRange(a, b):
# 	l = []
# 	for i in range(a, b):
# 		if not isComposite(i):
# 			l.append(i)
# 	return l	

# print simpleRange(1, 10)

# #1.4
# arr = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]

arr = []
arr1 = []
for sublist in arr:
	for item in sublist:
		if isinstance(item, list):
			for i in item:
				arr1.append(i)
		else:
			arr1.append(item)
print(arr1)
	