Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_pi = 3.14159
>>> 'Pi rounded to {0} decimal places is {1:.2f}.'.format(2, my_pi)
'Pi rounded to 2 decimal places is 3.14.'
>>> 'Pi rounded to {0} decimal places is {1:.3f}.'.format(3, my_pi)
'Pi rounded to 3 decimal places is 3.142.'
>>> '	 &^*&% 		Pi rounded to 3 decimal places is 3.142.'.lstrip('c')
'\t &^*&% \t\tPi rounded to 3 decimal places is 3.142.'
>>> '	 &^*&% 		Pi rounded to 3 decimal places is 3.142.'.lstrip('c'Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
									 
SyntaxError: invalid syntax
>>> '	 &^*&% 		Pi rounded to 3 decimal places is 3.142.'.lstrip()
'&^*&% \t\tPi rounded to 3 decimal places is 3.142.'
>>> '	 		Pi rounded to 3 decimal places is 3.142.'.lstrip()
'Pi rounded to 3 decimal places is 3.142.'
>>> '	 		Pi rounded to 3 decimal places is 3.142.'.lstrip()
'Pi rounded to 3 decimal places is 3.142.'
>>> '	 		Pi rounded to 3 decimal places is 3.142.'.lstrip('c', 1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    '	 		Pi rounded to 3 decimal places is 3.142.'.lstrip('c', 1)
TypeError: lstrip() takes at most 1 argument (2 given)
>>> '	 		Pi rounded to 3 decimal places is 3.142.'.lstrip('P')
'\t \t\tPi rounded to 3 decimal places is 3.142.'
>>> '	 		Pi rounded to 3 decimal places is 3.142.'.lstrip('3')
'\t \t\tPi rounded to 3 decimal places is 3.142.'
>>> '	 		Pi rounded to 3 decimal places is 3.142.'.lstrip('1')
'\t \t\tPi rounded to 3 decimal places is 3.142.'
>>> '	 		Pi rounded to 3 decimal places is 3.142.'.lstrip()
'Pi rounded to 3 decimal places is 3.142.'
>>> '     Pi rounded to 3 decimal places is 3.142.'.lstrip()
'Pi rounded to 3 decimal places is 3.142.'
>>> '     Pi rounded to 3 decimal places is 3.142.'.lstrip(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    '     Pi rounded to 3 decimal places is 3.142.'.lstrip(2)
TypeError: lstrip arg must be None or str
>>> '     Pi rounded to 3 decimal places is 3.142.'.lstrip('i')
'     Pi rounded to 3 decimal places is 3.142.'
>>> '     Pi rounded to 3 decimal places is 3.142.'.lstrip('1')
'     Pi rounded to 3 decimal places is 3.142.'
>>> '     Pi rounded to 3 decimal places is 3.142.'.lstrip('to')
'     Pi rounded to 3 decimal places is 3.142.'
>>> '	 &^*&% 		Pi rounded to 3 decimal places is 3.142.'.lstrip()
'&^*&% \t\tPi rounded to 3 decimal places is 3.142.'
>>> '	 &^*&% 		Pi rounded to 3 decimal places is 3.142.'.lstrip(\t)
SyntaxError: unexpected character after line continuation character
>>> '	 &^*&% 		Pi rounded to 3 decimal places is 3.142.'.lstrip(\t)
SyntaxError: unexpected character after line continuation character
>>> '	 &^*&% 		Pi rounded to 3 decimal places is 3.142.'.lstrip('\t')
' &^*&% \t\tPi rounded to 3 decimal places is 3.142.'
>>> '	 &^*&% 		Pi rounded to 3 decimal places is 3.142.'.lstrip('\t')
' &^*&% \t\tPi rounded to 3 decimal places is 3.142.'
>>> '     Pi rounded to 3 decimal places is 3.142.'.lstrip('P')
'     Pi rounded to 3 decimal places is 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.'.lstrip('P')
'i rounded to 3 decimal places is 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.'.lstrip('p')
'Pi rounded to 3 decimal places is 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.'.lstrip('.')
'Pi rounded to 3 decimal places is 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.'.replace('Pi', 'Number Pi')
'Number Pi rounded to 3 decimal places is 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.     '.rstrip()
'Pi rounded to 3 decimal places is 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142     .'.rstrip()
'Pi rounded to 3 decimal places is 3.142     .'
>>> 'Pi rounded to 3 decimal places is 3.142. TTTTTTTTTTT'.rstrip()
'Pi rounded to 3 decimal places is 3.142. TTTTTTTTTTT'
>>> 'Pi rounded to 3 decimal places is 3.142. TTTTTTTTTTT'.rstrip('T')
'Pi rounded to 3 decimal places is 3.142. '
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.rstrip('T')
'Pi rounded to 3 decimal places is 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.split()
['Pi', 'rounded', 'to', '3', 'decimal', 'places', 'is', '3.142.TTTTTTTTTTT']
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.startseith('K')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.startseith('K')
AttributeError: 'str' object has no attribute 'startseith'
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.startwith('K')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.startwith('K')
AttributeError: 'str' object has no attribute 'startwith'
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.startswith('K')
False
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.startswith('P')
True
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.startswith('p')
False
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.lower().startswith('p')
True
>>> '       Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT         '.strip()
'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'
>>> '       Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT         '.rstrip('T')
'       Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT         '
>>> 'Pi rounded to 3 decimal places is 3.142.TTTTTTTTTTT'.rstrip('T')
'Pi rounded to 3 decimal places is 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.'.strip('.')
'Pi rounded to 3 decimal places is 3.142'
>>> 'Pi rounded to 3 decimal places is 3.142.'.swapcse()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    'Pi rounded to 3 decimal places is 3.142.'.swapcse()
AttributeError: 'str' object has no attribute 'swapcse'
>>> 'Pi rounded to 3 decimal places is 3.142.'.swapcase()
'pI ROUNDED TO 3 DECIMAL PLACES IS 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.'.swapcase(1)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    'Pi rounded to 3 decimal places is 3.142.'.swapcase(1)
TypeError: swapcase() takes no arguments (1 given)
>>> 'Pi rounded to 3 decimal places is 3.142.'.swapcase
<built-in method swapcase of str object at 0x000002407B6CA750>
>>> 'Pi rounded to 3 decimal places is 3.142.'.swapcase()
'pI ROUNDED TO 3 DECIMAL PLACES IS 3.142.'
>>> 'Pi rounded to 3 decimal places is 3.142.'.upper()
'PI ROUNDED TO 3 DECIMAL PLACES IS 3.142.'
>>> 'species'.startswith('a')
False
>>> 'species'.startswith('spe')
True
>>> 'species'.endswith('es')
True
>>> 'species'.endswith('s')
True
>>> 'species'.endswith('e')
False
>>> compound = '     \n  Methyl \n butanol   \n'
>>> compound.lstrip()
'Methyl \n butanol   \n'
>>> compound.rstrip()
'     \n  Methyl \n butanol'
>>> compound.strip()
'Methyl \n butanol'
>>> compound.strip('\n')
'     \n  Methyl \n butanol   '
>>> compound.strip()
'Methyl \n butanol'
>>> compound.strip((), .strip('\n')
	       
SyntaxError: invalid syntax
>>> compound.strip()
'Methyl \n butanol'
>>> compound.strip('\n')
'     \n  Methyl \n butanol   '
>>> compound.strip()
'Methyl \n butanol'
>>> 'Computer Science'.swapcase()
'cOMPUTER sCIENCE'
>>> '"{0}" is derived from "1"'.format('none', 'no one')
'"none" is derived from "1"'
>>> '"{0}" is derived from "{1}"'.format('none', 'no one')
'"none" is derived from "no one"'
>>> '"{0}" is derived from {1} "{2}"'.format('Etymology', 'Greek',
			'ethos')
'"Etymology" is derived from Greek "ethos"'
>>> '"{0}" is derived from the {2} "{1}"'.format('Decemver', 'decem', 'Latin')
'"Decemver" is derived from the Latin "decem"'
>>> my_pi = 3.14159
>>> 'Pi rounded to {0} decimal places is {1:.2f}.'.format(2, my_pi)
'Pi rounded to 2 decimal places is 3.14.'
>>> 'Pi rounded to {0} decimal places is {1:.3f}.'.format(3, my_pi)
'Pi rounded to 3 decimal places is 3.142.'
>>> compound
'     \n  Methyl \n butanol   \n'
>>> compound.strip().compound.strip('\n')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    compound.strip().compound.strip('\n')
AttributeError: 'str' object has no attribute 'compound'
>>> '     \n  Methyl \n butanol   \n'.strip().strip('\n')
'Methyl \n butanol'
>>> '     \n  Methyl \n butanol   \n'.strip().replace('\n', '')
'Methyl  butanol'
>>> '     \n  Methyl\n butanol   \n'.strip().replace('\n', '')
'Methyl butanol'
>>> 'Computer Science'.swapcase().endswith('ENCE')
True
>>> help(o)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    help(o)
NameError: name 'o' is not defined
>>> help(0)
Help on int object:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(...)
 |      default object formatter
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      Returns size in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  bit_length(...)
 |      int.bit_length() -> int
 |      
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  from_bytes(...) from builtins.type
 |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
 |      
 |      Return the integer represented by the given array of bytes.
 |      
 |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument indicates whether two's complement is
 |      used to represent the integer.
 |  
 |  to_bytes(...)
 |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
 |      
 |      Return an array of bytes representing an integer.
 |      
 |      The integer is represented using length bytes.  An OverflowError is
 |      raised if the integer is not representable with the given number of
 |      bytes.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument determines whether two's complement is
 |      used to represent the integer.  If signed is False and a negative integer
 |      is given, an OverflowError is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> int('0b100', base=10)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    int('0b100', base=10)
ValueError: invalid literal for int() with base 10: '0b100'
>>> int('0b100', base=0)
4
>>> 'TTA' + 'GGG'
'TTAGGG'
>>> 'TTA'.__add__('GGG')
'TTAGGG'
>>> 'TTT' + '444'
'TTT444'
>>> '444' + '555'
'444555'
>>> '444'.__add__('five')
'444five'
>>> abs(-3)
3
>>> -3.__abs__()
SyntaxError: invalid syntax
>>> -3 .__abs__()
-3
>>> -3 .__abs__()
-3
>>> -3    .__abs()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    -3    .__abs()
AttributeError: 'int' object has no attribute '__abs'
>>> -3    .__abs__()
-3
>>> -3    .__abs__(-)
SyntaxError: invalid syntax
>>> -3    .__abs__(+)
SyntaxError: invalid syntax
>>>  -3 .__abs__()
 
SyntaxError: unexpected indent
>>> '-3' .__abs__()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    '-3' .__abs__()
AttributeError: 'str' object has no attribute '__abs__'
>>> int(-3) .__abs()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    int(-3) .__abs()
AttributeError: 'int' object has no attribute '__abs'
>>> -34764553.__abs__()
SyntaxError: invalid syntax
>>> abs(-4368573645783645)
4368573645783645
>>> -3 ._abs_()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    -3 ._abs_()
AttributeError: 'int' object has no attribute '_abs_'
>>> -3 .__abs__()
-3
>>> .abs()
SyntaxError: invalid syntax
>>> 876 .__abs__()
876
>>> 6586.8587578 .__abs__()
6586.8587578
>>> -6586.8587578 .__abs__()
-6586.8587578
>>> -3 .__abs__(-3)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    -3 .__abs__(-3)
TypeError: expected 0 arguments, got 1
>>> 3 + 5
8
>>> 3 .__add__(5)
8
>>> 3 > 5
False
>>> 3 .__gt__(5)
False
>>> 5 > 3
True
>>> 5 .__gt_(3)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    5 .__gt_(3)
AttributeError: 'int' object has no attribute '__gt_'
>>> 5 .__gt__(3)
True
>>> abs.__doc__
'Return the absolute value of the argument.'
>>> print(abs.__doc__)
Return the absolute value of the argument.
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> abs(-3)
3
>>> abs('-3', /)
SyntaxError: invalid syntax
>>> abs('-3', )
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    abs('-3', )
TypeError: bad operand type for abs(): 'str'
>>> -5 .__abs__()
-5
>>> -9.__abs__()
SyntaxError: invalid syntax
>>> -9 .__abs__()
-9
>>> (-7) .__abs__()
7
>>> (-34796563453.384758374563745834) .__abs__()
34796563453.38476
>>> (-3) .__ABS__()
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    (-3) .__ABS__()
AttributeError: 'int' object has no attribute '__ABS__'
>>> (-3) .__abs__()
3
>>> 'hello'.upper()
'HELLO'
>>> 'hello'.upper()
'HELLO'
>>> 65875.upper()
SyntaxError: invalid syntax
>>> 'Happy Birthday!'.lowwer()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    'Happy Birthday!'.lowwer()
AttributeError: 'str' object has no attribute 'lowwer'
>>> 'Happy Birthday!'.lower()
'happy birthday!'
>>> 'WeeeEEEEeeeEEEEeee'.swapcase()
'wEEEeeeeEEEeeeeEEE'
>>> 'KGLGFLIUFIYFgfjkfjfyyfytf6446654564654GHJGHGHf f fFJfj56776'.swapcase()
'kglgfliufiyfGFJKFJFYYFYTF6446654564654ghjghghF F FfjFJ56776'
>>> 'ABC123'.isupper()
True
>>> 'ajhgjafsasAAAAAAAAAAAAAAAAAAAAAAAAA'.count('a')
3
>>> 'hello'.endswith('o')
True
>>> 'hello'.startswith('H')
False
>>> 'Hello {0}'.format('Python')
'Hello Python'
>>> 'Hello {0}! Hello {1}'.format('Python', 'World')
'Hello Python! Hello World'
>>> 'Hello {0}! Hello {1}'.format('Python', 'World!')
'Hello Python! Hello World!'
>>> 'tomato'.count('o')
2
>>> 'tomato'.find('o', 1)
1
>>> 'tomato'.find('o')
1
>>> 'ttttttttttomato'.find('o')
10
>>> 'tomato'.find('0', 2, end)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    'tomato'.find('0', 2, end)
NameError: name 'end' is not defined
>>> 'tomato'.find('0', 2, )
-1
>>> 'tomato'.find('0', 2, 5)
-1
>>> 'tomato'.find('0', [2], [5])
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    'tomato'.find('0', [2], [5])
TypeError: slice indices must be integers or None or have an __index__ method
>>> 'tomato'.find('0', 4)
-1
>>> 'tomato'.find('0', 10)
-1
>>> 'tomato'.find('0')
-1
>>> 'tomato'.find('o')
1
>>> 'tomato'.find('o', 2)
5
>>> 'tomato'.find('o').find('o', 5)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    'tomato'.find('o').find('o', 5)
AttributeError: 'int' object has no attribute 'find'
>>> 'tomato'.find('o').find('o')
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    'tomato'.find('o').find('o')
AttributeError: 'int' object has no attribute 'find'
>>> 'tomato'.find()
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    'tomato'.find()
TypeError: find() takes at least 1 argument (0 given)
>>> 'tomato'.find('')
0
>>> 'tomato'.find('o', + 1)
1
>>> 'tomato'.find('o') + 1
2
>>> 'TOMATO'.find('o', 1+1)
-1
\
>>> 'tomato'.find('o', 1 + 1)
5
>>> 'tomato'.find('o', abs(-1) + 1)
5
>>> 'tomato'.find('o', 'tomato'.find('o') + 1.000000000000000)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    'tomato'.find('o', 'tomato'.find('o') + 1.000000000000000)
TypeError: slice indices must be integers or None or have an __index__ method
>>> 'tomato'.find('o', 'tomato'.find('o') + int(1.000000000000000))
5
>>> 'tomato'.find('o', 5)
5
>>> 'tomato'.replace('tomato', 'tOmato').find('o')
5
>>> 'tomato'.replace('tomato', 'tOmato').find('o')print
SyntaxError: invalid syntax
>>> print'tomato'.replace('tomato', 'tOmato').find('o')
SyntaxError: invalid syntax
>>> print('tomato'.replace('tomato', 'tOmato').find('o'))
5
>>> 'avocado'.find('o', 6)
6
>>> 'avocado'.find('o', 2)
2
>>> 'avocado'.find('o', 3)
6
>>> 'avocado'.find('o', 6)
6
>>> 'runner'.replace('nn', 'bb')
'rubber'
>>> print('runner'.replace('nn', 'bb'))
rubber
>>> '  yes  '.strip()
'yes'
>>> print('  yes  '.strip())
yes
>>> 'pineapple'.find('p', pinaapple.count('p'))
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    'pineapple'.find('p', pinaapple.count('p'))
NameError: name 'pinaapple' is not defined
>>> 'pineapple'.find('p', pineaapple.count('p'))
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    'pineapple'.find('p', pineaapple.count('p'))
NameError: name 'pineaapple' is not defined
>>> 2
2
>>> 'pineapple'.find('p', pineapple.count('p'))
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    'pineapple'.find('p', pineapple.count('p'))
NameError: name 'pineapple' is not defined
>>> 'pineapple'.find('p', 'pineapple'.count('p'))
5
>>> 'pineapple'.find('p')
0
>>> 'pineapple'.find('p', 1)
5
>>> 3
3
>>> 'pineapple'.count('p')
3
>>> 'Pineapple'.find('p)
		 
SyntaxError: EOL while scanning string literal
>>> 'Pineapple'.find('p')
5
>>> 'pineapple'.count()
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    'pineapple'.count()
TypeError: count() takes at least 1 argument (0 given)
>>> 1
1
>>> 'pineapple'.count('pineapple')
1
>>> 'pineapple'.count('pineapple'.upper().swapcase())
1
>>> 'pineapple'.upper().swapcase()
'pineapple'
>>> 'pineapple'.upper()
'PINEAPPLE'
>>> print 'pineapple'
SyntaxError: Missing parentheses in call to 'print'
>>> print(''pineapple' count is pineapple')
SyntaxError: invalid syntax
>>> print('pineapple count is pineapple')
pineapple count is pineapple
>>> print('/pineapple/ count is pineapple')
/pineapple/ count is pineapple
>>> print('"pineapple" count is pineapple')
"pineapple" count is pineapple
>>> 'pineapple'.upper()
'PINEAPPLE'
>>> 'pineapple'.lower()
'pineapple'
>>> 'The pineapple is tropical fruit'.replace('PINEAPPLE'.swapcase(), 'BANAN'.lower())
'The banan is tropical fruit'
>>> 'I love winter season in Australia.'.replace('I love winter season in Australia.', 'I love season "X"').replace('season "X"', '{0}').format('summer')
'I love summer'
>>> 'I love winter season in Australia.'.replace('I love winter season in Australia.', 'I love season "X"').replace('season "X"', '{0}').format('summer!')
'I love summer!'
>>> 'In Pythagoras theorem the sides have lenghts {2}, {1} and {0}'.format('5', '4', '3')
'In Pythagoras theorem the sides have lenghts 3, 4 and 5'
>>> 'In Pythagoras theorem the sides have lenghts {2}, {1} and {0} kilometers'.format('5', '4', '3')
'In Pythagoras theorem the sides have lenghts 3, 4 and 5 kilometers'
>>> 'In Pythagoras theorem the sides have lenghts {2}, {1} and {0} gogleplex'.format('5', '4', '3')
'In Pythagoras theorem the sides have lenghts 3, 4 and 5 gogleplex'
>>> 'In Pythagoras theorem the sides have lenghts {2}, {1} and {0} googolplex'.format('5', '4', '3')
'In Pythagoras theorem the sides have lenghts 3, 4 and 5 googolplex'
>>> 'In Pythagoras theorem the sides have lenghts {2}, {1} and {0} googolplex. Find the radian of inscribed circle.'.format('5', '4', '3')
'In Pythagoras theorem the sides have lenghts 3, 4 and 5 googolplex. Find the radian of inscribed circle.'
>>> 'In triangle with sides have lenghts {2}, {1} and {0} googolplex. Find the radian of inscribed circle.'.format('5', '4', '3')
'In triangle with sides have lenghts 3, 4 and 5 googolplex. Find the radian of inscribed circle.'
>>> t
