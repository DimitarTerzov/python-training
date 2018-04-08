Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> outer = ['Li', 'Na', 'K']
>>> inner = ['F', 'Cl', 'Br']
>>> for metals in outer:
	for halogen in inner:
		print(metal + halogen]
		
SyntaxError: invalid syntax
>>> for metals in outer:
	for halogen in inner:
		print(metal + halogen)

		
Traceback (most recent call last):
  File "<pyshell#6>", line 3, in <module>
    print(metal + halogen)
NameError: name 'metal' is not defined
>>> for metal in outer:
	for halogen in inner:
		print(metal + halogen)

		
LiF
LiCl
LiBr
NaF
NaCl
NaBr
KF
KCl
KBr
>>> def print_table(n):
	""" (int) -> NoneType

	Print the multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
		1	2	3	4	5
	1	1	2	3	4	5
	2	2	4	6	8	10
	3	3	6	9	12	15
	4	4	8	12	16	20
	5	5	10	15	20	25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))
	# Print the header row.
	for i in numbers:
		print('\t' + str(i), end='')

		
>>> def print_table(n):
	""" (int) -> NoneType

	Print the multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
		1	2	3	4	5
	1	1	2	3	4	5
	2	2	4	6	8	10
	3	3	6	9	12	15
	4	4	8	12	16	20
	5	5	10	15	20	25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))
	# Print the header row.
	for i in numbers:
		print('\t' + str(i), end='')
	# End the header row.
	print()

	
>>> def print_table(n):
	""" (int) -> NoneType

	Print the multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
		1	2	3	4	5
	1	1	2	3	4	5
	2	2	4	6	8	10
	3	3	6	9	12	15
	4	4	8	12	16	20
	5	5	10	15	20	25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))
	# Print the header row.
	for i in numbers:
		print('\t' + str(i), end='')
	# End the header row.
	print()
	# Print each row number and the contents of each row.
	for i in numbers:
		print(i, end='')
		for j in numbers:
			print('\t' + str(i * j), end='')
		# End the current row.
		print()

		
>>> print_table(5)
	1	2	3	4	5
1	1	2	3	4	5
2	2	4	6	8	10
3	3	6	9	12	15
4	4	8	12	16	20
5	5	10	15	20	25
>>> def print_table(n):
	for i in numbers:
		print(i, end='')
		for j in numbers:
			print('\t' + str(i * J), end='')
		print()

		
>>> print_table(5)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print_table(5)
  File "<pyshell#48>", line 2, in print_table
    for i in numbers:
NameError: name 'numbers' is not defined
>>> def print_table(n):
	""" (int) -> NoneType

	Print the multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
		1	2	3	4	5
	1	1	2	3	4	5
	2	2	4	6	8	10
	3	3	6	9	12	15
	4	4	8	12	16	20
	5	5	10	15	20	25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))
	# Print the header row.
	for i in numbers:
		print('\t' + str(i), end='')
	# End the header row.
	print()
	# Print each row number and the contents of each row.
	for i in numbers:
		print(i, end='')
		for j in numbers:
			print('\t' + str(i * j), end='')
		# End the current row.
		print()

		
>>> print_table(6)
	1	2	3	4	5	6
1	1	2	3	4	5	6
2	2	4	6	8	10	12
3	3	6	9	12	15	18
4	4	8	12	16	20	24
5	5	10	15	20	25	30
6	6	12	18	24	30	36
>>> elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
>>> for inner_list in elements:
	print(inner_list)

	
['Li', 'Na', 'K']
['F', 'Cl', 'Br']
>>> elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
>>> for inner_list in elements:
	for item in inner_list:
		print(item)

		
Li
Na
K
F
Cl
Br
>>> inner_list
['F', 'Cl', 'Br']
>>> 
>>> 
>>> info = [['Isaac Newton', 1643, 1727],
		['Charles Darwin', 1809, 1882],
		['Alan Turing', 1912, 1954, 'alan@bletchley.uk']]
>>> for item in info:
	print(len(item))

	
3
3
4
>>> drinking_times_by_day = [["9:02", "10:17", "13:52", "18:23", "21:31"],
			 ["8:45", "12:44", "14:52", "22:17"],
			 ["8:55", "11:11", "12:34", "13:46",
			  "15:52", "17:08", "21:15"],
			 ["9:15", "11:44", "16:28"],
			 ["10:01", "13:33", "16:45", "19:00"],
			 ["9:34", "11:16", "15:52", "20:37"],
			 ["9:01", "12:24", "18:51", "23:13"]]
>>> for day in drinking_time_by_day:
	for drinking_time in day:
		print(drinking_time, end='')
	print()

	
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    for day in drinking_time_by_day:
NameError: name 'drinking_time_by_day' is not defined
>>> for day in drinking_times_by_day:
	for drinking_time in day:
		print(drinking_time, end='')
	print()

	
9:0210:1713:5218:2321:31
8:4512:4414:5222:17
8:5511:1112:3413:4615:5217:0821:15
9:1511:4416:28
10:0113:3316:4519:00
9:3411:1615:5220:37
9:0112:2418:5123:13
>>> for day in drinking_times_by_day:
	for drinking_time in day:
		print(drinking_time, end='	')
	print()

	
9:02	10:17	13:52	18:23	21:31	
8:45	12:44	14:52	22:17	
8:55	11:11	12:34	13:46	15:52	17:08	21:15	
9:15	11:44	16:28	
10:01	13:33	16:45	19:00	
9:34	11:16	15:52	20:37	
9:01	12:24	18:51	23:13	
>>> 
