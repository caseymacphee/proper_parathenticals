import pytest

from proper_paren import *

def test_open():
	newstring = """
	This is a string with ((((()))))(((( four more opening parens
		"""
	output = proper_parentheticals(newstring)
	assert output == 1
	newstring = """
	This is a string with ((((()))))( only one more opening paren
		"""
	output = proper_parentheticals(newstring)
	assert output == 1

def test_balanced():
	newstring = """
	This is a string with ((((((((())))))))) and even number of parens
		"""
	output = proper_parentheticals(newstring)
	assert output == 0

	newstring = """
	This is a string with no parens
	"""
	output = proper_parentheticals(newstring)
	assert output == 0

def test_broken():
	newstring = """
	This is a string with ((((((((()))))))))))))))))) more closing parens
		"""
	output = proper_parentheticals(newstring)
	assert output == -1
	newstring = """
	This is a string with only ) one closing paren 
		"""

	output = proper_parentheticals(newstring)
	assert output == -1
