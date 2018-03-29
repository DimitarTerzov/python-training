Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> PracProg2loop
Repeating Code Using Loops
SyntaxError: multiple statements found while compiling a single statement
>>> 4. In this exercise, you’ll create a nested list and then write code that performs operations on that list.
a. Create a nested list where each element of the outer list contains the atomic number and atomic weight for an alkaline earth metal. The values are beryllium (4 and 9.012), magnesium (12 and 24.305), calcium (20 and 40.078), strontium (38 and 87.62), barium (56 and 137.327), and radium (88 and 226). Assign the list to variable alkaline_earth_metals.
SyntaxError: invalid syntax
>>> 
>>> 
>>> metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
>>> alkaline_earth_metals = [[4, 9.012], [12, 24.305],
			     [20, 40.078], [38, 87.62],
			     [56, 137.327], [88, 226]]
>>> range(metals)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    range(metals)
TypeError: 'list' object cannot be interpreted as an integer
>>> for i in range(len(metals)):
	print(metals[i], alkaline_earth_metals[i])

	
Beryllium [4, 9.012]
Magnesium [12, 24.305]
Calcium [20, 40.078]
Strontium [38, 87.62]
Barium [56, 137.327]
Radium [88, 226]
>>> for i in range(len(metals)):
	# Element [Atomic Number, Atomic weight]
	print(metals[i], alkaline_earth_metals[i])

	
Beryllium [4, 9.012]
Magnesium [12, 24.305]
Calcium [20, 40.078]
Strontium [38, 87.62]
Barium [56, 137.327]
Radium [88, 226]
>>> for i in range(len(metals)):
	# Element [Atomic Number, Atomic weight]
	print(metals[i], alkaline_earth_metals[i])

	
Beryllium [4, 9.012]
Magnesium [12, 24.305]
Calcium [20, 40.078]
Strontium [38, 87.62]
Barium [56, 137.327]
Radium [88, 226]
>>> for inner_list in alkaline_earth_metals:
	print(inner_list[0])
	print(inner_list[1])

	
4
9.012
12
24.305
20
40.078
38
87.62
56
137.327
88
226
>>> for inner_list in alkaline_earth_metals:
	print(metals[0])
	print(inner_list[0])
	print(inner_list[1])

	
Beryllium
4
9.012
Beryllium
12
24.305
Beryllium
20
40.078
Beryllium
38
87.62
Beryllium
56
137.327
Beryllium
88
226
>>> for inner_list in alkaline_earth_metals:
	print(metals)
	print(inner_list[0])
	print(inner_list[1])

	
['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
4
9.012
['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
12
24.305
['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
20
40.078
['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
38
87.62
['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
56
137.327
['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
88
226
>>> for inner_list in alkaline_earth_metals:
	print(metals[0])
	print(inner_list[0])
	print(inner_list[1])

	
Beryllium
4
9.012
Beryllium
12
24.305
Beryllium
20
40.078
Beryllium
38
87.62
Beryllium
56
137.327
Beryllium
88
226
>>> for inner_list in alkaline_earth_metals:
	print(inner_list[0])
	print(inner_list[1])
	print(metals[0])

	
4
9.012
Beryllium
12
24.305
Beryllium
20
40.078
Beryllium
38
87.62
Beryllium
56
137.327
Beryllium
88
226
Beryllium
>>> al
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    al
NameError: name 'al' is not defined
>>> alkaline_earth_metals
[[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]
>>> 
>>> 
>>> alkaline_earth_metals = [[4, 9.012,'Beryllium'], [12, 24.305,'Magnesium'],
			     [20, 40.078,'Calcium'], [38, 87.62,'Strontium'],
			     [56, 137.327,'Barium'], [88, 226,'Radium']]
>>> 
>>> alkaline_earth_metals
[[4, 9.012, 'Beryllium'], [12, 24.305, 'Magnesium'], [20, 40.078, 'Calcium'], [38, 87.62, 'Strontium'], [56, 137.327, 'Barium'], [88, 226, 'Radium']]
>>> for inner_list in alkaline_earth_metals:
	# Atomic number, Atomic weight, Element
	print(inner_list[0])
	print(inner_list[1])
	print(inner_list[2])

	
4
9.012
Beryllium
12
24.305
Magnesium
20
40.078
Calcium
38
87.62
Strontium
56
137.327
Barium
88
226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0], inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0],	 inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0],       inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0    ], inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0: ], inner_list[1])
	print(inner_list[2])

	
[4, 9.012, 'Beryllium'] 9.012
Beryllium
[12, 24.305, 'Magnesium'] 24.305
Magnesium
[20, 40.078, 'Calcium'] 40.078
Calcium
[38, 87.62, 'Strontium'] 87.62
Strontium
[56, 137.327, 'Barium'] 137.327
Barium
[88, 226, 'Radium'] 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0], inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0], (inner_list[1]))
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0],      (inner_list[1]))
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0]    , inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0]    ,     inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0];, inner_list[1])
	print(inner_list[2])
	
SyntaxError: invalid syntax
>>> 
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0], inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0]'', inner_list[1])
	print(inner_list[2])
	
SyntaxError: invalid syntax
>>> 
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0]' ', inner_list[1])
	print(inner_list[2])
	
SyntaxError: invalid syntax
>>> 
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0] + str' ', inner_list[1])
	print(inner_list[2])
	
SyntaxError: invalid syntax
>>> 
>>> alkaline_earth_metals
[[4, 9.012, 'Beryllium'], [12, 24.305, 'Magnesium'], [20, 40.078, 'Calcium'], [38, 87.62, 'Strontium'], [56, 137.327, 'Barium'], [88, 226, 'Radium']]
>>> alkaline_earth_metals = [[4,     9.012,'Beryllium'], [12, 24.305,'Magnesium'],
			     [20, 40.078,'Calcium'], [38, 87.62,'Strontium'],
			     [56, 137.327,'Barium'], [88, 226,'Radium']]
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0], inner_list[1])
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0] + '\t', inner_list[1])
	print(inner_list[2])

	
Traceback (most recent call last):
  File "<pyshell#77>", line 3, in <module>
    print(inner_list[0] + '\t', inner_list[1])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(inner_list[0] + str'\t', inner_list[1])
	print(inner_list[2])
	
SyntaxError: invalid syntax
>>> 
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]) + str'\t', (inner_list[1]))
	print(inner_list[2])
	
SyntaxError: invalid syntax
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]) + '\t', (inner_list[1]))
	print(inner_list[2])

	
Traceback (most recent call last):
  File "<pyshell#82>", line 3, in <module>
    print((inner_list[0]) + '\t', (inner_list[1]))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]) + "\t", (inner_list[1]))
	print(inner_list[2])

	
Traceback (most recent call last):
  File "<pyshell#84>", line 3, in <module>
    print((inner_list[0]) + "\t", (inner_list[1]))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print "\t".join([str(i) for i in alkaline_earth_metals])
	
SyntaxError: invalid syntax
>>> alkaline_earth_metals
[[4, 9.012, 'Beryllium'], [12, 24.305, 'Magnesium'], [20, 40.078, 'Calcium'], [38, 87.62, 'Strontium'], [56, 137.327, 'Barium'], [88, 226, 'Radium']]
>>> for a in alkaline_earth_metals:
	print "\t".joim([str(i) for i in alkaline_earth_metals])
	
SyntaxError: invalid syntax
>>> for a in alkaline_earth_metals:
	print ("\t".joim([str(i) for i in alkaline_earth_metals]))

	
Traceback (most recent call last):
  File "<pyshell#90>", line 2, in <module>
    print ("\t".joim([str(i) for i in alkaline_earth_metals]))
AttributeError: 'str' object has no attribute 'joim'
>>> for a in alkaline_earth_metals:
	print ("\t".join([str(i) for i in alkaline_earth_metals]))

	
[4, 9.012, 'Beryllium']	[12, 24.305, 'Magnesium']	[20, 40.078, 'Calcium']	[38, 87.62, 'Strontium']	[56, 137.327, 'Barium']	[88, 226, 'Radium']
[4, 9.012, 'Beryllium']	[12, 24.305, 'Magnesium']	[20, 40.078, 'Calcium']	[38, 87.62, 'Strontium']	[56, 137.327, 'Barium']	[88, 226, 'Radium']
[4, 9.012, 'Beryllium']	[12, 24.305, 'Magnesium']	[20, 40.078, 'Calcium']	[38, 87.62, 'Strontium']	[56, 137.327, 'Barium']	[88, 226, 'Radium']
[4, 9.012, 'Beryllium']	[12, 24.305, 'Magnesium']	[20, 40.078, 'Calcium']	[38, 87.62, 'Strontium']	[56, 137.327, 'Barium']	[88, 226, 'Radium']
[4, 9.012, 'Beryllium']	[12, 24.305, 'Magnesium']	[20, 40.078, 'Calcium']	[38, 87.62, 'Strontium']	[56, 137.327, 'Barium']	[88, 226, 'Radium']
[4, 9.012, 'Beryllium']	[12, 24.305, 'Magnesium']	[20, 40.078, 'Calcium']	[38, 87.62, 'Strontium']	[56, 137.327, 'Barium']	[88, 226, 'Radium']
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]), (inner_list[1]))
	print(inner_list[2])

	
4 9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]""), (inner_list[1]))
	print(inner_list[2])
	
SyntaxError: invalid syntax
>>> inner_list
[88, 226, 'Radium']
>>> alkaline_earth_metals = [['4    ', 9.012,'Beryllium'], [12, 24.305,'Magnesium'],
			     [20, 40.078,'Calcium'], [38, 87.62,'Strontium'],
			     [56, 137.327,'Barium'], [88, 226,'Radium']]
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]), (inner_list[1]))
	print(inner_list[2])

	
4     9.012
Beryllium
12 24.305
Magnesium
20 40.078
Calcium
38 87.62
Strontium
56 137.327
Barium
88 226
Radium
>>> alkaline_earth_metals = [['4    ', 9.012,'Beryllium'], ['12    ', 24.305,'Magnesium'],
			     ['20    ', 40.078,'Calcium'], ['38    ', 87.62,'Strontium'],
			     ['56    ', 137.327,'Barium'], ['88    ', 226,'Radium']]
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]), (inner_list[1]))
	print(inner_list[2])

	
4     9.012
Beryllium
12     24.305
Magnesium
20     40.078
Calcium
38     87.62
Strontium
56     137.327
Barium
88     226
Radium
>>> alkaline_earth_metals = [[' 4    ', 9.012,'Beryllium'], ['12    ', 24.305,'Magnesium'],
			     ['20    ', 40.078,'Calcium'], ['38    ', 87.62,'Strontium'],
			     ['56    ', 137.327,'Barium'], ['88    ', 226,'Radium']]
>>> 
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]), (inner_list[1]))
	print(inner_list[2])

	
 4     9.012
Beryllium
12     24.305
Magnesium
20     40.078
Calcium
38     87.62
Strontium
56     137.327
Barium
88     226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]), (inner_list[1]))
	
	print(inner_list[2])

	
 4     9.012
Beryllium
12     24.305
Magnesium
20     40.078
Calcium
38     87.62
Strontium
56     137.327
Barium
88     226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]), (inner_list[1]))
	print("\n" inner_list[2])
	
SyntaxError: invalid syntax
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]), (inner_list[1]))
	print("\n", inner_list[2])

	
 4     9.012

 Beryllium
12     24.305

 Magnesium
20     40.078

 Calcium
38     87.62

 Strontium
56     137.327

 Barium
88     226

 Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(("\n", inner_list[0]), (inner_list[1]))
	print("\n", inner_list[2])

	
('\n', ' 4    ') 9.012

 Beryllium
('\n', '12    ') 24.305

 Magnesium
('\n', '20    ') 40.078

 Calcium
('\n', '38    ') 87.62

 Strontium
('\n', '56    ') 137.327

 Barium
('\n', '88    ') 226

 Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(( inner_list[0]) + (inner_list[1]))
	print("\n", inner_list[2])

	
Traceback (most recent call last):
  File "<pyshell#115>", line 3, in <module>
    print(( inner_list[0]) + (inner_list[1]))
TypeError: Can't convert 'float' object to str implicitly
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(( inner_list[0]), (inner_list[1]))
	print("\n", inner_list[2])

	
 4     9.012

 Beryllium
12     24.305

 Magnesium
20     40.078

 Calcium
38     87.62

 Strontium
56     137.327

 Barium
88     226

 Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print(("\n", inner_list[0]), (inner_list[1]))
	print(inner_list[2])

	
('\n', ' 4    ') 9.012
Beryllium
('\n', '12    ') 24.305
Magnesium
('\n', '20    ') 40.078
Calcium
('\n', '38    ') 87.62
Strontium
('\n', '56    ') 137.327
Barium
('\n', '88    ') 226
Radium
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print("\n"(inner_list[0]), (inner_list[1]))
	print(inner_list[2])

	
Traceback (most recent call last):
  File "<pyshell#121>", line 3, in <module>
    print("\n"(inner_list[0]), (inner_list[1]))
TypeError: 'str' object is not callable
>>> for inner_list in alkaline_earth_metals:
	# Atomic number and Atomic weight, Element
	print((inner_list[0]), (inner_list[1]))
	print(inner_list[2])

	
 4     9.012
Beryllium
12     24.305
Magnesium
20     40.078
Calcium
38     87.62
Strontium
56     137.327
Barium
88     226
Radium
>>> number_and_weight = []
>>> for inner_list in alkaline_earth_metals:
	number_and_weight.append(inner_list[0])
	number_and_weight.append(inner_list[1])

	
>>> number_and_weight
[' 4    ', 9.012, '12    ', 24.305, '20    ', 40.078, '38    ', 87.62, '56    ', 137.327, '88    ', 226]
>>> for inner_list in alkaline_earth_metals:
	print(number_and_weight.append(inner_list[0]))
	print(number_and_weight.append(inner_list[1]))

	
None
None
None
None
None
None
None
None
None
None
None
None
>>> for inner_list in alkaline_earth_metals:
	number_and_weight.append(inner_list[0])
	number_and_weight.append(inner_list[1])
    print(number_and_weight)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> for inner_list in alkaline_earth_metals:
	number_and_weight.append(inner_list[0])
	number_and_weight.append(inner_list[1])
		print(number_and_weight)
		
SyntaxError: unexpected indent
>>> alkaline_earth_metals = [[4, 9.012,'Beryllium'], [12, 24.305,'Magnesium'],
			     [20, 40.078,'Calcium'], [38, 87.62,'Strontium'],
			     [56, 137.327,'Barium'], [88, 226,'Radium']]
>>> for inner_list in alkaline_earth_metals:
	number_and_weight.append(inner_list[0])
	number_and_weight.append(inner_list[1])
	number_and_weight.append(inner_list[2])

	
>>> number_and_weight
[' 4    ', 9.012, '12    ', 24.305, '20    ', 40.078, '38    ', 87.62, '56    ', 137.327, '88    ', 226, ' 4    ', 9.012, '12    ', 24.305, '20    ', 40.078, '38    ', 87.62, '56    ', 137.327, '88    ', 226, 4, 9.012, 'Beryllium', 12, 24.305, 'Magnesium', 20, 40.078, 'Calcium', 38, 87.62, 'Strontium', 56, 137.327, 'Barium', 88, 226, 'Radium']
>>> alkaline_earth_metals
[[4, 9.012, 'Beryllium'], [12, 24.305, 'Magnesium'], [20, 40.078, 'Calcium'], [38, 87.62, 'Strontium'], [56, 137.327, 'Barium'], [88, 226, 'Radium']]
>>> number_and_weight = []
>>> for inner_list in alkaline_earth_metals:
	number_and_weight.append(inner_list[0])
	number_and_weight.append(inner_list[1])
	number_and_weight.append(inner_list[2])

	
>>> number_and_weight
[4, 9.012, 'Beryllium', 12, 24.305, 'Magnesium', 20, 40.078, 'Calcium', 38, 87.62, 'Strontium', 56, 137.327, 'Barium', 88, 226, 'Radium']
>>> alkaline_earth_metals = [[4, 9.012,Beryllium], [12, 24.305,'Magnesium'],
			     [20, 40.078,'Calcium'], [38, 87.62,'Strontium'],
			     [56, 137.327,'Barium'], [88, 226,'Radium']]
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    alkaline_earth_metals = [[4, 9.012,Beryllium], [12, 24.305,'Magnesium'],
NameError: name 'Beryllium' is not defined
>>> alkaline_earth_metals = [[4, 9.012, Beryllium], [12, 24.305,'Magnesium'],
			     [20, 40.078,'Calcium'], [38, 87.62,'Strontium'],
			     [56, 137.327,'Barium'], [88, 226,'Radium']]
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    alkaline_earth_metals = [[4, 9.012, Beryllium], [12, 24.305,'Magnesium'],
NameError: name 'Beryllium' is not defined
>>> alkaline_earth_metals = [[4, 9.012, str(Beryllium)], [12, 24.305,'Magnesium'],
			     [20, 40.078,'Calcium'], [38, 87.62,'Strontium'],
			     [56, 137.327,'Barium'], [88, 226,'Radium']]
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    alkaline_earth_metals = [[4, 9.012, str(Beryllium)], [12, 24.305,'Magnesium'],
NameError: name 'Beryllium' is not defined
>>> alkaline_earth_metals = [[4, 9.012,'Beryllium'], [12, 24.305,'Magnesium'],
			     [20, 40.078,'Calcium'], [38, 87.62,'Strontium'],
			     [56, 137.327,'Barium'], [88, 226,'Radium']]
>>> def mystery_function(values):
	result = []
	for sublist in values:
		result.append([sublist[0]])
		for i in sublist[1:]:
			result[-1].insert(0, i)

			
>>> def mystery_function(values):
	result = []
	for sublist in values:
		result.append([sublist[0]])
		for i in sublist[1:]:
			result[-1].insert(0, i)
	return result

>>> mystery_function(15)
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    mystery_function(15)
  File "<pyshell#163>", line 3, in mystery_function
    for sublist in values:
TypeError: 'int' object is not iterable
>>> mystery_function([1, 2, 3], [9, 8, 7])
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    mystery_function([1, 2, 3], [9, 8, 7])
TypeError: mystery_function() takes 1 positional argument but 2 were given
>>> mystery_function([9, 8, 7])
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    mystery_function([9, 8, 7])
  File "<pyshell#163>", line 4, in mystery_function
    result.append([sublist[0]])
TypeError: 'int' object is not subscriptable
>>> mystery_function([[1, 2, 3], [9, 8, 7]])
[[3, 2, 1], [7, 8, 9]]
>>> def stupid_function(List_and_sublist):
	""" (list) -> list

	Return reversed values. [SubList1[55, 13, 7, 2], Sublist2[4, 14, 24, 64]]
	-> reversed values in sublists: [Sublist1[2, 7, 13, 55], Sublist2[64, 24, 14, 4]

	>>> stupid_function([[!, ?], [F, T, W]])
	[[?, !], [W, T, F]]
	"""
	r.list = []
	for sublist in List_and_sublist:
		# Sublist in reverse order by inserting the last
		# element to the front of the new sublist.
		r.list.append([sublist[0]])
		for i in sublist[1:]:
			r.list[-1].insert(0, i)
	return r.list

>>> stupid_function([[2018, 03, 28], [Year, Month, Day]])
SyntaxError: invalid token
>>> stupid_function([[2018, '03', 28], [Year, Month, Day]])
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    stupid_function([[2018, '03', 28], [Year, Month, Day]])
NameError: name 'Year' is not defined
>>> stupid_function([[2018, '03', 28], ['Year', 'Month', 'Day']])
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    stupid_function([[2018, '03', 28], ['Year', 'Month', 'Day']])
  File "<pyshell#184>", line 10, in stupid_function
    r.list = []
NameError: name 'r' is not defined
>>> def stupid_function(List_and_sublist):
	""" (list) -> list

	Return reversed values. [SubList1[55, 13, 7, 2], Sublist2[4, 14, 24, 64]]
	-> reversed values in sublists: [Sublist1[2, 7, 13, 55], Sublist2[64, 24, 14, 4]

	>>> stupid_function([[!, ?], [F, T, W]])
	[[?, !], [W, T, F]]
	"""
	REVlist = []
	for sublist in List_and_sublist:
		# Sublist in reverse order by inserting the last
		# element to the front of the new sublist.
		REVlist.append([sublist[0]])
		for i in sublist[1:]:
			REVlist[-1].insert(0, i)
	return REVlist

>>> stupid_function([[2018, '03', 28], ['Year', 'Month', 'Day']])
[[28, '03', 2018], ['Day', 'Month', 'Year']]
>>> stupid_function([[2018, 03, 28], ['Year', 'Month', 'Day']])
SyntaxError: invalid token
>>> stupid_function([[2018, 'Mar', 28], ['Year', 'Month', 'Day']])
[[28, 'Mar', 2018], ['Day', 'Month', 'Year']]
>>> 
>>> 
>>> 
>>> country_population = [1295, 23, 7, 3, 47, 21]
>>> total = []
>>> total
[]
>>> total = 0
>>> for population in country_population:
	total += population

	
>>> total
1396
>>> for population in country_population:
	total = population

	
>>> total
21
>>> for population in country_population:
	total -= population

	
>>> total
-1375
>>> population
21
>>> country_population
[1295, 23, 7, 3, 47, 21]
>>> total = 0
>>> for population in country_population:
	total += population

	
>>> for population in country_population:
	total += population
	print(total)

	
2691
2714
2721
2724
2771
2792
>>> total
2792
>>> country_population
[1295, 23, 7, 3, 47, 21]
>>> total = 0
>>> for population in country_population:
	total += population

	
>>> total
1396
>>> print(total)
1396
>>> for population in country_population:
	total += population
    print(total)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> for population in country_population:
	total += population
        print(total)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for population in country_population:
	total += population
	print(total)

	
2691
2714
2721
2724
2771
2792
>>> total
2792
>>> total = 0
>>> total
0
>>> for population in country_population:
	total += population
    print(total)
    
SyntaxError: unindent does not match any outer indentation level
>>> total
0
>>> country_population
[1295, 23, 7, 3, 47, 21]
>>> for population in country_population:
	total += population

	
>>> print(total)
1396
>>> rat_1 = 105
>>> rat_2 = 120
>>> if rat_1 > rat_2:
	print("Rat 1 weight more than rat 2 on day 1.")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if rat_1 > rat_2:
	print("Rat 1 weight more than rat 2 on day 1.")
        else:
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> 
>>> print range(33, 50)
SyntaxError: invalid syntax
>>> print(range(33, 50))
range(33, 50)
>>> range(33, 50)
range(33, 50)
>>> for numbers in range(33, 50):
	print(numbers)

	
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
>>> for numbers in range(len(33, 50)):
	print(numbers)

	
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    for numbers in range(len(33, 50)):
TypeError: len() takes exactly one argument (2 given)
>>> for numbers in range(len([33, 50])):
	print(numbers)

	
0
1
>>> for numbers in range(33, 50):
	print(numbers).list

	
33
Traceback (most recent call last):
  File "<pyshell#262>", line 2, in <module>
    print(numbers).list
AttributeError: 'NoneType' object has no attribute 'list'
>>> for numbers in range(33, 50):
	print(list(numbers))

	
Traceback (most recent call last):
  File "<pyshell#264>", line 2, in <module>
    print(list(numbers))
TypeError: 'int' object is not iterable
>>> list(range(33, 50))
[33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> print(list(range(33, 50)))
[33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> print(range(1, 11))
range(1, 11)
>>> print(list(range(1, 11)))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for ave in list(range(2, 23)):
	new_list += ave

	
Traceback (most recent call last):
  File "<pyshell#271>", line 2, in <module>
    new_list += ave
NameError: name 'new_list' is not defined
>>> new_list = 0
>>> for ave in list(range(2, 23)):
	new_list += ave

	
>>> new_list
252
>>> new_list = 0
>>> for ave in list(range(2, 23)):
	new_list += ave
	return new_list / 2
SyntaxError: 'return' outside function
>>> for ave in list(range(2, 23)):
	new_list += ave
    return new_list / 2
SyntaxError: unindent does not match any outer indentation level
>>> for ave in list(range(2, 23)):
	new_list += ave
        new_list / 2
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for ave in list(range(2, 23)):
	new_list += ave
	new_list / 2

	
1.0
2.5
4.5
7.0
10.0
13.5
17.5
22.0
27.0
32.5
38.5
45.0
52.0
59.5
67.5
76.0
85.0
94.5
104.5
115.0
126.0
>>> new_list
252
>>> for ave in list(range(2, 23)):
	new_list += ave
	(new_list / 2)

	
127.0
128.5
130.5
133.0
136.0
139.5
143.5
148.0
153.0
158.5
164.5
171.0
178.0
185.5
193.5
202.0
211.0
220.5
230.5
241.0
252.0
>>> for ave in list(range(2, 23)):
	new_list += ave
	print(new_list / 2)

	
253.0
254.5
256.5
259.0
262.0
265.5
269.5
274.0
279.0
284.5
290.5
297.0
304.0
311.5
319.5
328.0
337.0
346.5
356.5
367.0
378.0
>>> for ave in list(range(2, 23)):
	new_list += ave
	print(new_list / 2)

	
379.0
380.5
382.5
385.0
388.0
391.5
395.5
400.0
405.0
410.5
416.5
423.0
430.0
437.5
445.5
454.0
463.0
472.5
482.5
493.0
504.0
>>> for ave in list(range(2, 23)):
	new_list += ave
	print(new_list / 2)

	
505.0
506.5
508.5
511.0
514.0
517.5
521.5
526.0
531.0
536.5
542.5
549.0
556.0
563.5
571.5
580.0
589.0
598.5
608.5
619.0
630.0
>>> new_list = 0
>>> for ave in list(range(2, 23)):
	new_list += ave

	
>>> new_list
252
>>> 
>>> 
>>> sum = 0
>>> sum
0
>>> count = 0
>>> for number in range(2, 23):
	sum += number
	count += 1
    average = sum / count
    
SyntaxError: unindent does not match any outer indentation level
>>> for number in range(2, 23):
	sum += number
	count += 1
        average = sum / count
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for number in range(2, 23):
	sum += number
	count += 1

	
>>> count
21
>>> sum
252
>>> average = sum / count
>>> average
12.0
>>> number
22
>>> 
>>> 
>>> def remove_neg(num_list):
	""" list of number) -> NoneType

	Remove the negative numbers from list num_list.

	>>> numbers = [-5, 1, -3, 2]
	>>> remove_neg(numbers)
	[1, 2]
	"""
	for item in num_list:
		if item < 0:
		    num_list.remove(item)

		    
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 1])
>>> 
>>> list11 = [1, 2, 3, -3, 6, -1, -3, 1]
>>> list11
[1, 2, 3, -3, 6, -1, -3, 1]
>>> remove_neg(list11)
>>> list11
[1, 2, 3, 6, -3, 1]
>>> def remove_neg(num_list):
	""" list of number) -> NoneType

	Remove the negative numbers from list num_list.

	>>> numbers = [-5, 1, -3, 2]
	>>> remove_neg(numbers)
	[1, 2]
	"""
	for item in num_list:
		if item < 0:
		    num_list.remove(item)
		    num_list.remove(item)

		    
>>> list11 = [1, 2, 3, -3, 6, -1, -3, 1]
>>> remove_neg(list11)
Traceback (most recent call last):
  File "<pyshell#343>", line 1, in <module>
    remove_neg(list11)
  File "<pyshell#341>", line 13, in remove_neg
    num_list.remove(item)
ValueError: list.remove(x): x not in list
>>> list11
[1, 2, 3, 6, 1]
>>> list11 = [1, 2, 3, -3, 6, -1, -3, 1]
>>> def remove_neg(num_list):
	index = 0
	while index < len(num_list):
		if num_list[index] < 0:
			del num_list[index]
		else:
			index += 1

			
>>> list11
[1, 2, 3, -3, 6, -1, -3, 1]
>>> remove_neg(list11)
>>> list11
[1, 2, 3, 6, 1]
>>> for width in range(1, 8):
	print('T' * width)

	
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
>>> for width in range(1, 8):
	print('T' * width)

	
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
>>> for width in range(1, 8):
	print(' ' * (7 - width), 'T' * width, sep='')

	
      T
     TT
    TTT
   TTTT
  TTTTT
 TTTTTT
TTTTTTT
>>> for width in range(1, 8):
	print(' ' * (7 - width), 'T' * width)

	
       T
      TT
     TTT
    TTTT
   TTTTT
  TTTTTT
 TTTTTTT
>>> for width in range(1, 8):
	print(' ' * (8 - width), 'T' * width)

	
        T
       TT
      TTT
     TTTT
    TTTTT
   TTTTTT
  TTTTTTT
>>> for width in range(1, 8):
	print(' ' * (6 - width), 'T' * width)

	
      T
     TT
    TTT
   TTTT
  TTTTT
 TTTTTT
 TTTTTTT
>>> for width in range(1, 8):
	print(' ' * (7 - width), 'T' * width, sep='')

	
      T
     TT
    TTT
   TTTT
  TTTTT
 TTTTTT
TTTTTTT
>>> 
>>> 
>>> 
>>> width = 1
>>> while width < 8:
	print(' ' * (7 - width), 'T' * width, sep='')
	width += 1

	
      T
     TT
    TTT
   TTTT
  TTTTT
 TTTTTT
TTTTTTT
>>> width = 1
>>> while width < 8:
	print('T' * width)
	width += 1

	
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
>>> while width < 8:
	print('T' * width)

	
>>> while width < 8:
	print('T' * width)

	
>>> while width < 8:
	print('T' * width)
	width += 8

	
>>> while width < 8:
	print('T' * width)
	width += 1

	
>>> width
8
>>> width = 1
>>> while width < 8:
	print('T' * width)
	width += 8

	
T
>>> width = 1
>>> while width < 8:
	print('T' * width)

	
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
kT
T
T
Tl
T
T
T
sT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
dT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
Tc
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
lT
T
T
T
T
Tk
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
aT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
nT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
Tk
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
hT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
eT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
wT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
hT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
Td
T
T
T
T
T
T
T
T
T
wT
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T

=============================== RESTART: Shell ===============================
>>> width = 1
>>> while width < 8:
	print('T' * width)
	width += 1

	
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
>>> width = 1
>>> while width < 8:
	print(' ' * (7 - width), 'T' * width, sep='')
	width += 1

	
      T
     TT
    TTT
   TTTT
  TTTTT
 TTTTTT
TTTTTTT
>>> 
>>> 
>>> week = 1
>>> while rat_1_weight[week] / rat_1_weigth[0] - 1 < .25:
	week += 1

	
Traceback (most recent call last):
  File "<pyshell#416>", line 1, in <module>
    while rat_1_weight[week] / rat_1_weigth[0] - 1 < .25:
NameError: name 'rat_1_weight' is not defined
>>> while rat_1_weight[week] / rat_1_weigth[0] - 1 < .25:
	week += 1
    print(week)
    
SyntaxError: unindent does not match any outer indentation level
>>> week
1
>>> 
>>> 
>>> 
>>> 
