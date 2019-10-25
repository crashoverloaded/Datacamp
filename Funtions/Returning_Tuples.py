#!/usr/bin/python3

def raise_both(value1,value2):
	""" Raise Value1 to the power of value2 """
	new_value1 = value1 ** value2
	new_value2 = value2 ** value1
	
	new_tuple=(new_value1,new_value2)
	return new_tuple
a=raise_both(int(input("ENter VAlue 1:-")),int(input("ENter Value 2:-")))
print(a)
