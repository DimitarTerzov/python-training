Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Storing Collections of Data Using Lists

SyntaxError: invalid syntax
>>> print(Storing Collections of Data Using Lists)
SyntaxError: invalid syntax
>>> print('Storing Collections of Data Using Lists')
Storing Collections of Data Using Lists
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> whales[0]
5
>>> whales[1]
4
>>> whales[12]
1
>>> whales[13]
3
>>> whales[3745639563945]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    whales[3745639563945]
IndexError: list index out of range
>>> whales[-5]
2
>>> whales[-15]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    whales[-15]
IndexError: list index out of range
>>> whales[-11]
3
>>> third = whales[2]
>>> print('Third day:', third)
Third day: 7
>>> whales = []
>>> whales[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    whales[0]
IndexError: list index out of range
>>> whales[-1]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    whales[-1]
IndexError: list index out of range
>>> krypton = ['Krypton', 'Kr', -157.2, 153.4]
>>> krypton[1]
'Kr'
>>> krypton[2]
-157.2
>>> nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
>>> nobles[1]
'none'
>>> nobles[1] = neon
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    nobles[1] = neon
NameError: name 'neon' is not defined
>>> nobles[1] = 'neon'
>>> nobles[1]
'neon'
>>> nobles
['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
>>> L[i]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    L[i]
NameError: name 'L' is not defined
>>> name = Darwin
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name = Darwin
NameError: name 'Darwin' is not defined
>>> name = 'Darwin'
>>> capitalized = name.upper()
>>> print(capitalized)
DARWIN
>>> print(name)
Darwin
>>> half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
>>> len(half_lives)
5
>>> max(half_lives)
373300.0
>>> min(half_lives)
14
>>> sum(half_lives)
404864.7
>>> sorted(half_lives)
[14, 887.7, 6563.0, 24100.0, 373300.0]
>>> half_lives
[887.7, 24100.0, 6563.0, 14, 373300.0]
>>> original = ['H', 'He', 'Li']
>>> final = original + ['Be']
>>> final
['H', 'He', 'Li', 'Be']
>>> len(final)
4
>>> max(final)
'Li'
>>> min(final)
'Be'
>>> sum(final)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sum(final)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum(final)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    sum(final)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sorted(fibal)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    sorted(fibal)
NameError: name 'fibal' is not defined
>>> sorted(final)
['Be', 'H', 'He', 'Li']
>>> ['H', 'He', 'Li'] + 'Be'
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    ['H', 'He', 'Li'] + 'Be'
TypeError: can only concatenate list (not "str") to list
>>> metals = ['Fe', 'Ni']
>>> metals * 3
['Fe', 'Ni', 'Fe', 'Ni', 'Fe', 'Ni']
>>> metals
['Fe', 'Ni']
>>> del metals[0]
>>> metals
['Ni']
>>> del metals[0]
>>> metals
[]
>>> metals2 = metals + ['Silver', 'Gold']
>>> metals
[]
>>> metals2 = metals + ['Silver'] + ['Gold']
>>> metals2
['Silver', 'Gold']
>>> metals3 = metals2 + ['Aluminium', 'Titan']
>>> metals3
['Silver', 'Gold', 'Aluminium', 'Titan']
>>> del metals3[1]
>>> metals3
['Silver', 'Aluminium', 'Titan']
>>> sum(metals3)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    sum(metals3)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
>>> gas = input('Enter a gas: ')
Enter a gas: argon
>>> if gas in nobles:
	print('{} is noble.'.format(gas))

	
argon is noble.
>>> gas = input('Enter a gas: ')
Enter a gas: nitrogen
>>> if gas in nobles:
	print('{} is noble.'.format(gas))

	
>>> [1, 2] in [0, 1, 2, 3]
False
>>> [1, 2] in [1, 2, 3]
False
>>> [1, 2] in [1, 2]
False
>>> [1, 2] in [1]
False
>>> [0, 1] in [0, 1, 2, 3]
False
>>> [0] in [0, 1, 2, 3]
False
>>> [1, 2] in [1, 2]
False
>>> [2] in [2]
False
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> useful_markets = celegans_phenotypes[0:4]
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes[:4]
['Emb', 'Him', 'Unc', 'Lon']
>>> celegans_phenotypes[4:]
['Dpy', 'Sma']
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_copy = celegans_phenotypes[:]
>>> celegans_copy
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes[5] = 'Lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> celegans_copy
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> celegans_alias = celegans_phenotypes
>>> celegans_phenotypes[5] = 'Lvl'
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> celegans_alias
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Lvl']
>>> 
