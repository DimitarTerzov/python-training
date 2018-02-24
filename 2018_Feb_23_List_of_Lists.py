Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Working with a List of Lists')
Working with a List of Lists
>>> colors = 'red orange yellow green blue purple'.split()
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>> sorted_colors = colors.sort()
>>> print(sorted_colors)
None
>>> colors
['blue', 'green', 'orange', 'purple', 'red', 'yellow']
>>> colors.sort()
>>> colors
['blue', 'green', 'orange', 'purple', 'red', 'yellow']
>>> colors.sort()
>>> colors
['blue', 'green', 'orange', 'purple', 'red', 'yellow']
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=0)
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> life[0]
['Canada', 76.5]
>>> life[1]
['United States', 75.5]
>>> life[2]
['Mexico', 72.0]
>>> life[1]
['United States', 75.5]
>>> life[1][0]
'United States'
>>> life[1][1]
75.5
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> canada = life[0]
>>> canada
['Canada', 76.5]
>>> canda[0]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    canda[0]
NameError: name 'canda' is not defined
>>> canada[0]
'Canada'
>>> canda[1]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    canda[1]
NameError: name 'canda' is not defined
>>> canada[1]
76.5
>>> life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]
>>> canada = life[0]
>>> canada[1]
76.5
>>> canada[1] = 80.0
>>> canada
['Canada', 80.0]
>>> life
[['Canada', 80.0], ['United States', 75.5], ['Mexico', 72.0]]
>>> print('8.9 Exercises')
8.9 Exercises
>>> kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms
['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[0]
'Bacteria'
>>> kingdoms[5]
'Animalia'
>>> kingdoms[0][1][3]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    kingdoms[0][1][3]
IndexError: string index out of range
>>> kingdoms[[0], [1], [2]]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    kingdoms[[0], [1], [2]]
TypeError: list indices must be integers or slices, not tuple
>>> kingdoms[0, 1, 2]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    kingdoms[0, 1, 2]
TypeError: list indices must be integers or slices, not tuple
>>> kingdoms[:3]
['Bacteria', 'Protozoa', 'Chromista']
>>> kingdoms[2:3]
['Chromista']
>>> kingdoms[1:3]
['Protozoa', 'Chromista']
>>> kingdoms[0,5]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    kingdoms[0,5]
TypeError: list indices must be integers or slices, not tuple
>>> from operator import itemgetter
>>> print(*itemgetter(1, 4)(kingdoms))
Protozoa Fungi
>>> return(*itemgetter(1, 4)(kingdoms))
SyntaxError: 'return' outside function
>>> kingdoms[(*itemgetter(1, 4)(kingdoms))]
SyntaxError: can't use starred expression here
>>> kingdoms[*itemgetter(1, 4)(kingdoms)]
SyntaxError: invalid syntax
>>> kingdoms(*itemgetter(1, 4)(kingdoms))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    kingdoms(*itemgetter(1, 4)(kingdoms))
TypeError: 'list' object is not callable
>>> list(kingdoms[x] for x in (0,3))
['Bacteria', 'Plantae']
>>> map(kingdoms.__getitem__, [0,3])
<map object at 0x000001E20E829828>
>>> map(kingdoms.__getitem__, [0, 3])
<map object at 0x000001E20E829748>
>>> map(kingdoms.__getitem__, [0, 3])
<map object at 0x000001E20E8297B8>
>>> print(kingdoms[1], kingdoms[4])
Protozoa Fungi
>>> list(kingdoms[x] for x in (1,4))
['Protozoa', 'Fungi']
>>> kingdoms[2:]
['Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[2:4]
['Chromista', 'Plantae']
>>> kingdoms[2:5]
['Chromista', 'Plantae', 'Fungi']
>>> kingdoms[4:]
['Fungi', 'Animalia']
>>> kingdoms.clear()
>>> kingdoms
[]
>>> kingdoms = ['Bacteria', 'Protozoa', 'Chomista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[0]
'Bacteria'
>>> kingdoms[-5]
'Protozoa'
>>> kingdoms[-6]
'Bacteria'
>>> kingdoms[-1]
'Animalia'
>>> kingdoms[-6:-3]
['Bacteria', 'Protozoa', 'Chomista']
>>> kingdoms[-4:-1]
['Chomista', 'Plantae', 'Fungi']
>>> kingdoms[-2:0]
[]
>>> kingdoms[-2:]
['Fungi', 'Animalia']
>>> kingdoms.clear()
>>> kingdoms
[]
>>> kingdoms.clear(-)
SyntaxError: invalid syntax
>>> 
>>> 
>>> appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments.append('16:30')
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> appointments.pop()
'16:30'
>>> app
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    app
NameError: name 'app' is not defined
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments = appointments + [16:00]
SyntaxError: invalid syntax
>>> appointments += ['16:30']
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> appointments = q
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    appointments = q
NameError: name 'q' is not defined
>>> app2 = appointments + ['10:45']
>>> app2
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30', '10:45']
>>> app2 = appointments
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> app2 = appointments[:]
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> app2
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> app2 = appointments + ['10:45']
>>> app2
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30', '10:45']
>>> appointments = app2[:]
>>> app2
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30', '10:45']
>>> print('c. ------------------')
c. ------------------
>>> print('4. Variable ids refers to the list [4353, 2314, 2956, 3382, 9362, 3900]. Using list methods, do the following: ')
4. Variable ids refers to the list [4353, 2314, 2956, 3382, 9362, 3900]. Using list methods, do the following: 
>>> ids = [4353, 2314, 2956, 3382, 9362, 3900]
>>> ids
[4353, 2314, 2956, 3382, 9362, 3900]
>>> ids = iqq[:]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    ids = iqq[:]
NameError: name 'iqq' is not defined
>>> ids = iqq
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    ids = iqq
NameError: name 'iqq' is not defined
>>> ids = iqq[]
SyntaxError: invalid syntax
>>> iqq = ids
>>> iqq
[4353, 2314, 2956, 3382, 9362, 3900]
>>> ids.remove(3382)
>>> ids
[4353, 2314, 2956, 9362, 3900]
>>> ids.index(9362)
3
>>> ids.insert(4, '4499')
>>> ids
[4353, 2314, 2956, 9362, '4499', 3900]
>>> ids.extend('5566', '1830')
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    ids.extend('5566', '1830')
TypeError: extend() takes exactly one argument (2 given)
>>> ids.extend([5566, 1830])
>>> ids
[4353, 2314, 2956, 9362, '4499', 3900, 5566, 1830]
>>> ids
[4353, 2314, 2956, 9362, '4499', 3900, 5566, 1830]
>>> ids.reverse()
>>> ids
[1830, 5566, 3900, '4499', 9362, 2956, 2314, 4353]
>>> ids.sort()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    ids.sort()
TypeError: unorderable types: str() < int()
>>> ids.sort()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    ids.sort()
TypeError: unorderable types: str() < int()
>>> ids
[1830, 3900, 5566, '4499', 9362, 2956, 2314, 4353]
>>> ids.remove('4455')
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    ids.remove('4455')
ValueError: list.remove(x): x not in list
>>> ids.remove('4499')
>>> ids
[1830, 3900, 5566, 9362, 2956, 2314, 4353]
>>> ids.insert(3, 4499)
>>> ids
[1830, 3900, 5566, 4499, 9362, 2956, 2314, 4353]
>>> sorted(ids)
[1830, 2314, 2956, 3900, 4353, 4499, 5566, 9362]
>>> ids.sort()
>>> ids
[1830, 2314, 2956, 3900, 4353, 4499, 5566, 9362]
>>> ids = [1830, 3900, 5566, 4499, 9362, 2956, 2314, 4353]
>>> ids
[1830, 3900, 5566, 4499, 9362, 2956, 2314, 4353]
>>> ids.sort(reverse=false)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    ids.sort(reverse=false)
NameError: name 'false' is not defined
>>> ids.sort(reverse=False)
>>> ids
[1830, 2314, 2956, 3900, 4353, 4499, 5566, 9362]
>>> ids.sort(reverse=True)
>>> ids
[9362, 5566, 4499, 4353, 3900, 2956, 2314, 1830]
>>> ids.sort(3, reverce=False)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    ids.sort(3, reverce=False)
TypeError: 'reverce' is an invalid keyword argument for this function
>>> ids.sort(3, reverse=False)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    ids.sort(3, reverse=False)
TypeError: must use keyword argument for key function
>>> ids.sert(K, reverse=False)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    ids.sert(K, reverse=False)
AttributeError: 'list' object has no attribute 'sert'
>>> ids.sort(K, reverse=False)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    ids.sort(K, reverse=False)
NameError: name 'K' is not defined
>>> ids
[9362, 5566, 4499, 4353, 3900, 2956, 2314, 1830]
>>> ids.sort(reverse=True)
>>> ids
[9362, 5566, 4499, 4353, 3900, 2956, 2314, 1830]
>>> ids.sort(reverse=False)
>>> ids
[1830, 2314, 2956, 3900, 4353, 4499, 5566, 9362]
>>> alkaline_earth_metals = [[Beryllium, 4], [Magnesium, 12], [Calcium, 20], [Strontium, 38], [Barium, 56], [Radium, 88]]
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    alkaline_earth_metals = [[Beryllium, 4], [Magnesium, 12], [Calcium, 20], [Strontium, 38], [Barium, 56], [Radium, 88]]
NameError: name 'Beryllium' is not defined
>>> alkaline_earth_metals = [['Beryllium', 4], [Magnesium, 12], [Calcium, 20], [Strontium, 38], [Barium, 56], [Radium, 88]]
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    alkaline_earth_metals = [['Beryllium', 4], [Magnesium, 12], [Calcium, 20], [Strontium, 38], [Barium, 56], [Radium, 88]]
NameError: name 'Magnesium' is not defined
>>> alkaline_earth_metals = [['Beryllium', 4], ['Magnesium', 12], ['Calcium', 20], ['Strontium', 38], ['Barium', 56], ['Radium', 88]]
>>> alkaline_earth_metals
[['Beryllium', 4], ['Magnesium', 12], ['Calcium', 20], ['Strontium', 38], ['Barium', 56], ['Radium', 88]]
>>> alkaline_earth_metals.index(['Radium', 88])
5
>>> radium = alkaline_earth_metals[5]
>>> radium
['Radium', 88]
>>> radium[1] = 88.0
>>> radium
['Radium', 88.0]
>>> radium.index(['Radium', 88])
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    radium.index(['Radium', 88])
ValueError: ['Radium', 88] is not in list
>>> radium.index([88])
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    radium.index([88])
ValueError: [88] is not in list
>>> radium.index(88)
1
>>> alkaline_earth_metals[5]
['Radium', 88.0]
>>> radium[1]
88.0
>>> alkaline_earth_metals.count()
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    alkaline_earth_metals.count()
TypeError: count() takes exactly one argument (0 given)
>>> alkaline_earth_metals.len()
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    alkaline_earth_metals.len()
AttributeError: 'list' object has no attribute 'len'
>>> len(alkaline_earth_metals)
6
>>> max(alkaline_earth_metals)
['Strontium', 38]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
>>> temps
[25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
>>> temp.sort()
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    temp.sort()
NameError: name 'temp' is not defined
>>> temps.sort()
>>> temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> cool_temps = temps[:2]
>>> cool_temps
[16.8, 19.6]
>>> warm_temps = temps[1:]
>>> warm_temps
[19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> warm_temps = temps[2:]
>>> warm_temps
[22.5, 23.9, 25.2, 28, 31.4]
>>> temps_in_celsius = cool_temps + warm_temps
>>> temps_in_celsius
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> temps_in_celsius
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> 
>>> 
>>> 
>>> 
>>> def same_first_last(L):
	""" (list) -> bool
	Precondition: len(L) >= 2

	Return True if and only if first iten of the list is
	the same as the last.

	>>> same_first_last([3, 4, 2, 8, 3])
	True
	>>> same_first_last(['apple', 'banana', 'pear'])
	False
	>>> same_first_last([4.0, 4.5])
	False
	"""
	return(same_first_last[0] == same_first_last[-1])

>>> same_first_last([123, 32234424, 244123432, 23,42,234, ,42,4 ,4,4,2432,4,2 123])
SyntaxError: invalid syntax
>>> same_first_last([123, 32234424, 244123432, 4534534, 345345, 23])
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    same_first_last([123, 32234424, 244123432, 4534534, 345345, 23])
  File "<pyshell#202>", line 15, in same_first_last
    return(same_first_last[0] == same_first_last[-1])
TypeError: 'function' object is not subscriptable
>>> same_first_last([123, 32234424, 244123432, 4534534, 345345, 123])
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    same_first_last([123, 32234424, 244123432, 4534534, 345345, 123])
  File "<pyshell#202>", line 15, in same_first_last
    return(same_first_last[0] == same_first_last[-1])
TypeError: 'function' object is not subscriptable
>>> def same_first_last(L):
	""" (list) -> bool
	Precondition: len(L) >= 2

	Return True if and only if first iten of the list is
	the same as the last.

	>>> same_first_last([3, 4, 2, 8, 3])
	True
	>>> same_first_last(['apple', 'banana', 'pear'])
	False
	>>> same_first_last([4.0, 4.5])
	False
	"""
	return L[0] == L[-1]

>>> same_first_last([123, 23423423, 23423423, 23423423, 23423432, 123])
True
>>> same_first_last	([3445345, 34543 53,345435 3,4534534])
SyntaxError: invalid syntax
>>> same_first_last	([34425465, eratert, errteete, erterte, 3443534534])
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    same_first_last	([34425465, eratert, errteete, erterte, 3443534534])
NameError: name 'eratert' is not defined
>>> same_first_last(['waeer', 'ewrwerwr', '45646546', '345345', 'ertret'])
False
>>> same_first_last([2342342, '32423432', 32432432432, 'werwerew'])
False
>>> same_first_last([weouioyweu, werwe, we, weewr, werew])
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    same_first_last([weouioyweu, werwe, we, weewr, werew])
NameError: name 'weouioyweu' is not defined
>>> same_first_last(['weouioyweu', 'werwe', 'we', 'weewr', 'werew'])
False
>>> def is_longer(L1, L2):
	""" (list, list) -> bool
	Return True if and only if the lenght of L1 is longer than the
	lenght os L2.

	>>> is_longer([1, 2, 3], [4, 5])
	True
	>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
	False
	>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
	False
	"""
	return L1 >> L2

>>> is_longer([2], [4])
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    is_longer([2], [4])
  File "<pyshell#228>", line 13, in is_longer
    return L1 >> L2
TypeError: unsupported operand type(s) for >>: 'list' and 'list'
>>> def is_longer(L1, L2):
	""" (list, list) -> bool
	Return True if and only if the lenght of L1 is longer than the
	lenght os L2.

	>>> is_longer([1, 2, 3], [4, 5])
	True
	>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
	False
	>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
	False
	"""
	return L1 > L2

>>> is_longer([2], [4])
False
>>> is_longer([2], [4, 4, 5, 6])
False
>>> is_longer([2, 4, 5, 6, 7], [4])
False
>>> def is_longer(L1, L2):
	""" (list, list) -> bool
	Return True if and only if the lenght of L1 is longer than the
	lenght os L2.

	>>> is_longer([1, 2, 3], [4, 5])
	True
	>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
	False
	>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
	False
	"""
	return len.L1 > len.L2

>>> is_longer([2, 4, 5, 6, 7], [4])
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    is_longer([2, 4, 5, 6, 7], [4])
  File "<pyshell#236>", line 13, in is_longer
    return len.L1 > len.L2
AttributeError: 'builtin_function_or_method' object has no attribute 'L1'
>>> def is_longer(L1, L2):
	""" (list, list) -> bool
	Return True if and only if the lenght of L1 is longer than the
	lenght os L2.

	>>> is_longer([1, 2, 3], [4, 5])
	True
	>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
	False
	>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
	False
	"""
	return(len.L1 > len.L2)

>>> is_longer([2, 4, 5, 6, 7], [4])
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    is_longer([2, 4, 5, 6, 7], [4])
  File "<pyshell#239>", line 13, in is_longer
    return(len.L1 > len.L2)
AttributeError: 'builtin_function_or_method' object has no attribute 'L1'
>>> def is_longer(L1, L2):
	""" (list, list) -> bool
	Return True if and only if the lenght of L1 is longer than the
	lenght os L2.

	>>> is_longer([1, 2, 3], [4, 5])
	True
	>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
	False
	>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
	False
	"""
	return(len.(L1) > len.(L2))
SyntaxError: invalid syntax
>>> def is_longer(L1, L2):
	""" (list, list) -> bool
	Return True if and only if the lenght of L1 is longer than the
	lenght os L2.

	>>> is_longer([1, 2, 3], [4, 5])
	True
	>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
	False
	>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
	False
	"""
	return len.(L1) > len.(L2)
SyntaxError: invalid syntax
>>> 
>>> 
>>> def is_longer(L1, L2):
	""" (list, list) -> bool
	Return True if and only if the lenght of L1 is longer than the
	lenght os L2.

	>>> is_longer([1, 2, 3], [4, 5])
	True
	>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
	False
	>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
	False
	"""
	return len(L1) > len(L2)

>>> is_longer([2, 4, 5, 6, 7], [4])
True
>>> is_longer([3, 4, 5, 6]), [4, 5, 6])
SyntaxError: invalid syntax
>>> is_longer([3, 4, 5, 6]), [4, 5, 6])
SyntaxError: invalid syntax
>>> is_longer([3, 4, 5, 6], [4, 5, 6])
True
>>> is_longer([1], [3, 4])
False
>>> values = [0, 1, 3]
>>> va
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    va
NameError: name 'va' is not defined
>>> values
[0, 1, 3]
>>> values[1] = values
>>> values[1]
[0, [...], 3]
>>> values
[0, [...], 3]
>>> print(values)
[0, [...], 3]
>>> values = [0, 1, 2]
>>> values
[0, 1, 2]
>>> values[1]
1
>>> values[1] = values
>>> values
[0, [...], 2]
>>> values[1]
[0, [...], 2]
>>> values[2]
2
>>> print(values[1])
[0, [...], 2]
>>> print(values[0:])
[0, [0, [...], 2], 2]
>>> print(values[0])
0
>>> print(values[:])
[0, [0, [...], 2], 2]
>>> print(values[1:])
[[0, [...], 2], 2]
>>> print(values[:1])
[0]
>>> 
>>> 
>>> units = [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
>>> units
[['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
>>> units[0]
['km', 'miles', 'league']
>>> units[-1]
['kg', 'pound', 'stone']
>>> l1 = units[0]
>>> l1
['km', 'miles', 'league']
>>> l1[0]
'km'
>>> l2 = units[-1]
>>> l2
['kg', 'pound', 'stone']
>>> l2[0]
'kg'
>>> l1[0:]
['km', 'miles', 'league']
>>> l1[1:]
['miles', 'league']
>>> l2[:2]
['kg', 'pound']
>>> units[-1]
['kg', 'pound', 'stone']
>>> units[-2]
['km', 'miles', 'league']
>>> l1[-3]
'km'
>>> l2[-3]
'kg'
>>> l1[-3:]
['km', 'miles', 'league']
>>> l1[-2:]
['miles', 'league']
>>> l2[:-1]
['kg', 'pound']
>>> 
>>> 
>>> 
