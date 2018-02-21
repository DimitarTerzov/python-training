Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print(2018_Feb_20)
SyntaxError: invalid syntax
>>> print('2018_Feb_20')
2018_Feb_20
>>> print	('7.6 Exercises / 11. Using string methods, write expressions that produce the following: ')
7.6 Exercises / 11. Using string methods, write expressions that produce the following: 
>>> 'boolean'.capitalize()
'Boolean'
>>> print('boolean'.capitalize())
Boolean
>>> 'C02 H20'.find('2')
2
>>> 'C02 H20'.find('H')
4
>>> 'C02 H20'.find('2', 3)
5
>>> 'Boolean'.startswith('B')
True
>>> '"Monday"'.lower().capitalize()
'"monday"'
>>> '"MoNDaY"'.capitalize()
'"monday"'
>>> '"MoNDaY"'.capitalize('M')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    '"MoNDaY"'.capitalize('M')
TypeError: capitalize() takes no arguments (1 given)
>>> "MoNDaY".capitalize()
'Monday'
>>> "MoNDaY".lower()
'monday'
>>> "MoNDaY".lower().capitalize()
'Monday'
>>> 'Boolean'[0].islower()
False
>>> 'Boolean'[0].islower()
False
>>> 'Boolean'.islower()
False
>>> 'Boolean'[1].islower()
True
>>> 'Boolean'[0].islower()
False
>>> '"monday"'[1].capitalize()
'M'
>>> '"MoNDaY"'[1][2].lower()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    '"MoNDaY"'[1][2].lower()
IndexError: string index out of range
>>> '"MoNDaY"'[1],[2].lower()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    '"MoNDaY"'[1],[2].lower()
AttributeError: 'list' object has no attribute 'lower'
>>> '"MoNDaY"'[3].lower()
'n'
>>> '"MoNDaY"'[3, 4].lower()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    '"MoNDaY"'[3, 4].lower()
TypeError: string indices must be integers
>>> "MoNDaY".lower().capitalize()
'Monday'
>>> "  Monday".lstrip()
'Monday'
>>> def total_occurrences(s1, s2, sh):
	""" (str, str, str) -> int

	Precondition: len(sh) == 1

	Return the number of times that sh occur in s1 and s2.

	>>> total_occurrences('color', 'yellow', 'l')
	3
	>>> total_occurrences('red', blue', 'l')
	1
	>>> total_occurrences('green', purple', 'b')
	0
	"""

	
>>> def total_occurrences(s1, s2, sh):
	""" (str, str, str) -> int

	Precondition: len(sh) == 1

	Return the number of times that sh occur in s1 and s2.

	>>> total_occurrences('color', 'yellow', 'l')
	3
	>>> total_occurrences('red', blue', 'l')
	1
	>>> total_occurrences('green', purple', 'b')
	0
	"""
	return((s1 + s2).count('sh'))

>>> total_occurrences('Wath the fuck', 'WTF', 'W')
0
>>> def total_occurrences(s1, s2, sh):
	""" (str, str, str) -> int

	Precondition: len(sh) == 1

	Return the number of times that sh occur in s1 and s2.

	>>> total_occurrences('color', 'yellow', 'l')
	3
	>>> total_occurrences('red', blue', 'l')
	1
	>>> total_occurrences('green', purple', 'b')
	0
	"""
	return((s1 + s2).count(sh))

>>> total_occurrences('Wath the fuck', 'WTF', 'W')
2
>>> def letter_occur(w1, w2, l)
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, l)
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return((w1 + w2).count(letter))

>>> letter_occur('word number one', 'word number two in book for wonderland', 'wo')
4
>>> letter_occur('wwwwwwwwwwwwwwwwwegukwaqldfjkqhwjkfgqwkjfgqwjkfgqw', 'kasdgafalewculaetuatecnnaewrytewarcn lwerbvtaweuatecrwil uatrwluai talw tfvweuitaf', 'w')
31
>>> letter_occur('2349862398264!#@#!@#%@$^!@%!&*@^*(!@*!_!_+!@_@*!@!&*^*!&%$!#$@$#!@#!@%&*!^@&*(!@&@)!&@)!(&@!(&@!@<>><><>?>?":":}{}{}"|"|}{{}{"|:"', '"|::"<>?><:"|"}{{}+_()()*()*&&*^&^&^&%$#$@@#@!!@#@!##@$$#%^&^&^&&*(*()(*)__)+_+_+_)_)+_+_)()*(*&&&^%%$#@$#!@!#@#$%^&**(()><?><?<>?:"|:"|{}
	     
SyntaxError: EOL while scanning string literal
>>> letter_occur('2349862398264!#@#!@#%@$^!@%!&*@^*(!@*!_!_+!@_@*!@!&*^*!&%$!#$@$#!@#!@%&*!^@&*(!@&@)!&@)!(&@!(&@!@<>><><>?>?":":}{}{}"|"|}{{}{"|:"', '"|::"<>?><:"|"}{{}+_()()*()*&&*^&^&^&%$#$@@#@!!@#@!##@$$#%^&^&^&&*(*()(*)__)+_+_+_)_)+_+_)()*(*&&&^%%$#@$#!@!#@#$%^&**(()><?><?<>?:"|:"|{}', '>')
10
>>> letter_occur('word number one', 'word number two in book for wonderland', 'w')
4
>>> letter_occur('word number one in first week', 'word number two in book for wonderland', 'w')
5
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return(w1.__add__(w2).count(letter))

>>> letter_occur('Python', 'Path', 'P')
2
>>> letter_occur('55555.7777755', '5FIVE5five5 f i  v e', '5')
10
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return w1.count(letter) + w2.count(letter))
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return w1.count(letter) + w2.count(letter)

>>> letter_occur	        (        '      weur    ewyriu   ', '5 6 7 8', ' ')
16
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return w1.count(letter) + w2.count(letter) 'characters'
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return (w1.count(letter) + w2.count(letter) 'characters')
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return (w1.count(letter) + w2.count(letter) characters)
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return (w1.count(letter) + w2.count(letter) + characters)

>>> letter_occur('airplane fly, fly', 'in the blue sky', 'y')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    letter_occur('airplane fly, fly', 'in the blue sky', 'y')
  File "<pyshell#88>", line 15, in letter_occur
    return (w1.count(letter) + w2.count(letter) + characters)
NameError: name 'characters' is not defined
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return (w1.count(letter) + w2.count(letter) + str.(characters))
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return (w1.count(letter) + w2.count(letter) + str.'characters')
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return (w1.count(letter) + w2.count(letter) + str(characters))

>>> letter_occur('airplane fly, fly', 'in the blue sky', 'y')
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    letter_occur('airplane fly, fly', 'in the blue sky', 'y')
  File "<pyshell#93>", line 15, in letter_occur
    return (w1.count(letter) + w2.count(letter) + str(characters))
NameError: name 'characters' is not defined
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	return (w1.count(letter) + w2.count(letter) str(characters))
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	
	return (w1.count(letter) + w2.count(letter) +str(characters))

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#97>", line 16, in letter_occur
    return (w1.count(letter) + w2.count(letter) +str(characters))
NameError: name 'characters' is not defined
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	
	print (w1.count(letter) + w2.count(letter) +str(characters))

	
>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#100>", line 16, in letter_occur
    print (w1.count(letter) + w2.count(letter) +str(characters))
NameError: name 'characters' is not defined
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	characters == characters
	return (w1.count(letter) + w2.count(letter) + characters)

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#103>", line 15, in letter_occur
    characters == characters
NameError: name 'characters' is not defined
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	CH == characters
	return (w1.count(letter) + w2.count(letter) + CH)

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#106>", line 15, in letter_occur
    CH == characters
NameError: name 'CH' is not defined
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	CH = characters
	return (w1.count(letter) + w2.count(letter)) + CH

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#109>", line 15, in letter_occur
    CH = characters
NameError: name 'characters' is not defined
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""
	CH = str(characters)
	return (w1.count(letter) + w2.count(letter)) + CH

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#112>", line 15, in letter_occur
    CH = str(characters)
NameError: name 'characters' is not defined
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return (w1.count(letter) + w2.count(letter)) + "characters"

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#115>", line 16, in letter_occur
    return (w1.count(letter) + w2.count(letter)) + "characters"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return ((w1.count(letter) + w2.count(letter)) + "characters")

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#118>", line 16, in letter_occur
    return ((w1.count(letter) + w2.count(letter)) + "characters")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> 
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return (w1.count(letter) + w2.count(letter)
		print(letter_occur + str(characters))
		
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return w1.count(letter) + w2.count(letter)

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
23
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return (w1.count(letter) + w2.count(letter) + {0}.format('characters'))

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#131>", line 16, in letter_occur
    return (w1.count(letter) + w2.count(letter) + {0}.format('characters'))
AttributeError: 'set' object has no attribute 'format'
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return w1.count(letter) + w2.count(letter) + {0}.format('characters')

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
  File "<pyshell#134>", line 16, in letter_occur
    return w1.count(letter) + w2.count(letter) + {0}.format('characters')
AttributeError: 'set' object has no attribute 'format'
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return 'w1.count(letter) + w2.count(letter) {0}'.format('characters')

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
'w1.count(letter) + w2.count(letter) characters'
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return (w1.count(letter) + w2.count(letter)) {0}.format('characters')
SyntaxError: invalid syntax
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return (w1.count(letter) + w2.count(letter))

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
23
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return w1.count(letter) + w2.count(letter)

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
23
>>> letter_occur()
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    letter_occur()
TypeError: letter_occur() missing 3 required positional arguments: 'w1', 'w2', and 'letter'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def letter_occur(w1, w2, letter):
	""" (srt, str, str) -> int

	Precondition: lenght(letter) == 1

	Return the total numbers of times that letter occurs in w1 and w2.

	>>> letter_occur('sample', 'apple', 'p')
	3
	>>> letter_occur('occur', occurrences', 'c')
	5
	>>> letter_occur('download all files', 'convert letter in .xlsx', 'l')
	6
	"""

	return '{} bananas'.format(w1.count(letter) + w2.count(letter))

>>> letter_occur('yyyyyyyyyyyyyyyy', 'hgfjhfyutyytytytyuty', 'y')
'23 bananas'
>>> 
