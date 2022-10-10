#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	c = 0
	try:
		for i, v in enumerate(my_list):
			if i < x:
				print(v, end="")
				c += 1
	except IndexError:
		pass
	print()
	return (c)
