Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Mutable Parameters')
Mutable Parameters
>>> def remove_last_item(L):
	""" (list) -> list

	Return list L with the last item removed.

	Precondition: len(L) >= 0

	>>> remove_last_item([1, 2, 3, 4])
	[1, 2, 3]
	"""
	del L[-1]
	return L

>>> celegans_markets = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl')
SyntaxError: invalid syntax
>>> celegans_markets = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> remove_last_item(celegans_markets)
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
>>> celegans_markets
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
>>> def remove_last_item(L):
	""" (list) -> NoneType

	Remove the last item from L.

	Precondition: len(L) >= 0

	>>> remove_last_item([1, 3, 2, 4])
	"""
	del L[-1]

	
>>> celegans_markets = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> remove_last_item(celegans_markets)
>>> celegans_markets
['Emb', 'Him', 'Unc', 'Lon', 'Dpy']
>>> colors = ['Red', 'orange', 'Green']
>>> colors.extend['Black', 'Blue']
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    colors.extend['Black', 'Blue']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> colors.extend(['Black', 'Blue'])
>>> colors
['Red', 'orange', 'Green', 'Black', 'Blue']
>>> colors.append('Purple')
>>> colors
['Red', 'orange', 'Green', 'Black', 'Blue', 'Purple']
>>> colors.insert(2, 'yellow')
>>> colors
['Red', 'orange', 'yellow', 'Green', 'Black', 'Blue', 'Purple']
>>> colors.remove('Black')
>>> colors
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Purple']
>>> colors = backup
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    colors = backup
NameError: name 'backup' is not defined
>>> backup = colors[:]
>>> backup
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Purple']
>>> colors.clear(4)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    colors.clear(4)
TypeError: clear() takes no arguments (1 given)
>>> colors.clear()
>>> colors
[]
>>> backup
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Purple']
>>> colors = backup[:]
>>> colors
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Purple']
>>> colors = one
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    colors = one
NameError: name 'one' is not defined
>>> one = colors
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Purple']
>>> one[5] = 'Deep'
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep']
>>> colors
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep']
>>> backup
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Purple']
>>> one.append('LAST_item)
	   
SyntaxError: EOL while scanning string literal
>>> one.append('LAST_item')
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item']
>>> colors
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item']
>>> backup
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Purple']
>>> backup.count('Blue')
1
>>> one.extend('Object numer 76354265342', 'and number 2')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    one.extend('Object numer 76354265342', 'and number 2')
TypeError: extend() takes exactly one argument (2 given)
>>> one.extend(['Object numer 76354265342', 'and number 2'])
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item', 'Object numer 76354265342', 'and number 2']
>>> one.index('Blue')
4
>>> 
>>> 
>>> one.index('Blue', 3)
4
>>> one.index('Blue', 0)
4
>>> one.index('Blue', 4)
4
>>> one.index('Blue', 5)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    one.index('Blue', 5)
ValueError: 'Blue' is not in list
>>> one.append('Blue')
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item', 'Object numer 76354265342', 'and number 2', 'Blue']
>>> one.index('Blue', 5)
9
>>> one.index('Blue', 5, 8)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    one.index('Blue', 5, 8)
ValueError: 'Blue' is not in list
>>> one.index('Blue', 5, 21763271)
9
>>> one.insert(9, 'Ten')
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item', 'Object numer 76354265342', 'and number 2', 'Ten', 'Blue']
>>> one[9]
'Ten'
>>> one.insert(9, 'Nine')
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item', 'Object numer 76354265342', 'and number 2', 'Nine', 'Ten', 'Blue']
>>> one[9]
'Nine'
>>> one[7] = 'Number 1'
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item', 'Number 1', 'and number 2', 'Nine', 'Ten', 'Blue']
>>> one.pop()
'Blue'
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item', 'Number 1', 'and number 2', 'Nine', 'Ten']
>>> one.remove()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    one.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> one
['Red', 'orange', 'yellow', 'Green', 'Blue', 'Deep', 'LAST_item', 'Number 1', 'and number 2', 'Nine', 'Ten']
>>> one.remove('Blue')
>>> one
['Red', 'orange', 'yellow', 'Green', 'Deep', 'LAST_item', 'Number 1', 'and number 2', 'Nine', 'Ten']
>>> one.pop()
'Ten'
>>> one
['Red', 'orange', 'yellow', 'Green', 'Deep', 'LAST_item', 'Number 1', 'and number 2', 'Nine']
>>> one.reverse()
>>> one
['Nine', 'and number 2', 'Number 1', 'LAST_item', 'Deep', 'Green', 'yellow', 'orange', 'Red']
>>> one.reverse()
>>> one
['Red', 'orange', 'yellow', 'Green', 'Deep', 'LAST_item', 'Number 1', 'and number 2', 'Nine']
>>> one.sort()
>>> one
['Deep', 'Green', 'LAST_item', 'Nine', 'Number 1', 'Red', 'and number 2', 'orange', 'yellow']
>>> one.sort(reverse=True)
>>> one
['yellow', 'orange', 'and number 2', 'Red', 'Number 1', 'Nine', 'LAST_item', 'Green', 'Deep']
>>> 
