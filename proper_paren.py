from node import *
from stack import *

def proper_parentheticals(string):
	parenstack = Stack()

	if type(string) != str:
		return ValueError('Function takes type string')
	try:
		for char in string:
			if char == '(':
				parenstack.push(char)
			if char == ')':
				parenstack.pop()
	except:
		return -1

	if parenstack.size == 0:
		return 0
	if parenstack.size > 0:
		return 1

