Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> print('Metric:', velocities[0], 'm/sec;',
      'Imperial:', velocities[0] * 3.28, 'ft/sec')
Metric: 0.0 m/sec; Imperial: 0.0 ft/sec
>>> print('Metric:', velocities[1], 'm/sec;',
      'NOTMetric:', velocities[1], 'ft/sec')
Metric: 9.81 m/sec; NOTMetric: 9.81 ft/sec
>>> print('Metric:', velocities[1], 'm/sec;',
      'NOTMetric:', velocities[1] * 3.28, 'ft/sec')
Metric: 9.81 m/sec; NOTMetric: 32.1768 ft/sec
>>> print('Metric:', velocities[2], 'm/sec;',
      'NOTMetric:', velocities[2] * 3.28, 'ft/sec')
Metric: 19.62 m/sec; NOTMetric: 64.3536 ft/sec
>>> print('Metric:', velocities[3], 'm/sec:',
      'NOTMetric:, 'velocities[3] * 3.28, 'ft/sec')
SyntaxError: invalid syntax
>>> print('Metric:', velocities[3], 'm/sec:',
      'NOTMetric:, 'velocities[3] * 3.28, 'ft/sec')
SyntaxError: invalid syntax
>>> print('Metric:', velocities[3], 'm/sec:',
      'NOTMetric:, 'velocities[3] * 3.28, 'ft/sec')
SyntaxError: invalid syntax
>>> print('Metric:', velocities[3], 'm/sec:',
      'NOTMetric:', velocities[3] * 3.28, 'ft/sec')
Metric: 29.43 m/sec: NOTMetric: 96.5304 ft/sec
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> for velocities in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'Imperial:', velocities * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; Imperial: 0.0 ft/sec
Metric: 9.81 m/sec; Imperial: 32.1768 ft/sec
Metric: 19.62 m/sec; Imperial: 64.3536 ft/sec
Metric: 29.43 m/sec; Imperial: 96.5304 ft/sec
>>> for velocities in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    for velocities in velocities:
TypeError: 'float' object is not iterable
>>> velocities
29.43
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for velocities in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric: 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric: 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric: 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric: 96.5304 ft/sec
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for i in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Traceback (most recent call last):
  File "<pyshell#26>", line 3, in <module>
    'NOTMetric:', velocities * 3.28, 'ft/sec')
TypeError: can't multiply sequence by non-int of type 'float'
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> i = 0
>>> for i in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Traceback (most recent call last):
  File "<pyshell#30>", line 3, in <module>
    'NOTMetric:', velocities * 3.28, 'ft/sec')
TypeError: can't multiply sequence by non-int of type 'float'
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> for i in velocities:
	i = 0
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Traceback (most recent call last):
  File "<pyshell#33>", line 4, in <module>
    'NOTMetric:', velocities * 3.28, 'ft/sec')
TypeError: can't multiply sequence by non-int of type 'float'
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> for velocities in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric: 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric: 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric: 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric: 96.5304 ft/sec
>>> velocities
29.43
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for lo in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Traceback (most recent call last):
  File "<pyshell#40>", line 3, in <module>
    'NOTMetric:', velocities * 3.28, 'ft/sec')
TypeError: can't multiply sequence by non-int of type 'float'
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for velocities in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric: 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric: 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric: 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric: 96.5304 ft/sec

>>> 
>>> velocities
29.43
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for velocities in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric: 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric: 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric: 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric: 96.5304 ft/sec

>>> 
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for velocities in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric: 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric: 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric: 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric: 96.5304 ft/sec
>>> velocities
29.43
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for velocity in velocities:
	print('Metric:', velocities, 'm/sec;',
	      'NOTMetric:', velocities * 3.28, 'ft/sec')

	
Traceback (most recent call last):
  File "<pyshell#56>", line 3, in <module>
    'NOTMetric:', velocities * 3.28, 'ft/sec')
TypeError: can't multiply sequence by non-int of type 'float'
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for units in velocities:
	print('Metric:', units, 'm/sec;',
	      'NOTMetric', units * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric 96.5304 ft/sec
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> print('Metric:', velocities[1], 'm/sec;',
      'NOTMetric:', velocities[1] * 3.28, 'ft/sec')
Metric: 9.81 m/sec; NOTMetric: 32.1768 ft/sec
>>> velocit
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    velocit
NameError: name 'velocit' is not defined
>>> 
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for units in velocities:
	print('Metric:', units[-1], 'm/sec;',
	      'NOTMetric', units * 3.28, 'ft/sec')

	
Traceback (most recent call last):
  File "<pyshell#69>", line 2, in <module>
    print('Metric:', units[-1], 'm/sec;',
TypeError: 'float' object is not subscriptable
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> for units in velocities:
	print('Metric:', units[-1], 'm/sec;',
	      'NOTMetric', units[-1] * 3.28, 'ft/sec')

	
Traceback (most recent call last):
  File "<pyshell#72>", line 2, in <module>
    print('Metric:', units[-1], 'm/sec;',
TypeError: 'float' object is not subscriptable
>>> for units in velocities:
	print('Metric:', units, 'm/sec;',
	      'NOTMetric', units * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric 96.5304 ft/sec
>>> velocities = [0.0, 9.81, 19.62, 29.43, velocities]
>>> for units in velocities:
	print('Metric:', units, 'm/sec;',
	      'NOTMetric', units * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric 96.5304 ft/sec
Traceback (most recent call last):
  File "<pyshell#78>", line 3, in <module>
    'NOTMetric', units * 3.28, 'ft/sec')
TypeError: can't multiply sequence by non-int of type 'float'
>>> velocities
[0.0, 9.81, 19.62, 29.43, [0.0, 9.81, 19.62, 29.43]]
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> 
>>> for units in velocities:
	print('Metric:', units, 'm/sec;',
	      'NOTMetric', units * 3.28, 'ft/sec')

	
Metric: 0.0 m/sec; NOTMetric 0.0 ft/sec
Metric: 9.81 m/sec; NOTMetric 32.1768 ft/sec
Metric: 19.62 m/sec; NOTMetric 64.3536 ft/sec
Metric: 29.43 m/sec; NOTMetric 96.5304 ft/sec
>>> speed = 2
>>> velocities = [0.0, 9.81, 19.62, 29.43]
>>> for speed in velocities:
	print('Metric:', speed, 'm/sec')

	
Metric: 0.0 m/sec
Metric: 9.81 m/sec
Metric: 19.62 m/sec
Metric: 29.43 m/sec
>>> speed
29.43
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> for speed in velocities:
	print('Metric:', speed, 'm/sec')

	
Metric: 0.0 m/sec
Metric: 9.81 m/sec
Metric: 19.62 m/sec
Metric: 29.43 m/sec
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> for sp in velocities:
	print('Metric:', speed, 'm/sec')

	
Metric: 29.43 m/sec
Metric: 29.43 m/sec
Metric: 29.43 m/sec
Metric: 29.43 m/sec
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> for sp in velocities:
	print('Metric:', sp, 'm/sec')

	
Metric: 0.0 m/sec
Metric: 9.81 m/sec
Metric: 19.62 m/sec
Metric: 29.43 m/sec
>>> sp
29.43
>>> velocities
[0.0, 9.81, 19.62, 29.43]
>>> country = 'United States of America'
>>> for ch in country:
	if ch.isupper():
		print(ch)

		
U
S
A
>>> range(10)
range(0, 10)
>>> for num in range(10):
	print(num)

	
0
1
2
3
4
5
6
7
8
9
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(3))
[0, 1, 2]
>>> list(range(1))
[0]
>>> list(range(0))
[]
>>> 
>>> list(range(1, 5))
[1, 2, 3, 4]
>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(2000, 2050, 4))
[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
>>> list(range(2050, 2000, -4))
[2050, 2046, 2042, 2038, 2034, 2030, 2026, 2022, 2018, 2014, 2010, 2006, 2002]
>>> list(range(2052, 2000, -4))
[2052, 2048, 2044, 2040, 2036, 2032, 2028, 2024, 2020, 2016, 2012, 2008, 2004]
>>> list(range(2048, 1996, -4))
[2048, 2044, 2040, 2036, 2032, 2028, 2024, 2020, 2016, 2012, 2008, 2004, 2000]
>>> list(range(2000, 2050, -4))
[]
>>> list(range(2050, 2000, 4))
[]
>>> total = 0
>>> for i in range(1, 101):
	total = total + 1

	
>>> total
100
>>> total = 0
>>> for i in range(1, 101):
	total = total + i

	
>>> total
5050
>>> i
100
>>> values = [4, 10, 3, 8, -6]
>>> for num in values:
	num = num * 2

	
>>> values
[4, 10, 3, 8, -6]
>>> num
-12
>>> print(num)
-12
>>> values = [4, 10, 3, 8, -6]
>>> for num in values:
	num = num * 2
	print(num)

	
8
20
6
16
-12
>>> num
-12
>>> values
[4, 10, 3, 8, -6]
>>> values = [4, 10, 3, 8, -6]
>>> len(values)
5
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(len(values)))
[0, 1, 2, 3, 4]
>>> values = [4, 10, 3, 8, -6]
>>> for i in range(len(values)):
	print(i)

	
0
1
2
3
4
>>> values = [4, 10, 3, 8, -6]
>>> for i in range(len(values)):
	print(i, values[i])

	
0 4
1 10
2 3
3 8
4 -6
>>> values = [4, 10, 3, 8, -6]
>>> for i in range(len(values)):
	values[i] = values[i] * 2

	
>>> values
[8, 20, 6, 16, -12]
>>> stri = ['List', 'Mist', 'Fist', 'Wist']
>>> for item1 in range(len(stri)):
	stri = stri * 2

	
>>> stri
['List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist', 'List', 'Mist', 'Fist', 'Wist']
>>> metals = ['Li', 'Na', 'K']
>>> weights = [6.941, 22.98976928, 39.0983]
>>> for i in range(len(metals)):
	print(metals[i], weights[i])

	
Li 6.941
Na 22.98976928
K 39.0983
>>> metals
['Li', 'Na', 'K']
>>> print(metals[i])
K
>>> metals
['Li', 'Na', 'K']
>>> metals[i]
'K'
>>> weights
[6.941, 22.98976928, 39.0983]
>>> print(weights[i])
39.0983
>>> outer = ['Li', 'Na', 'K']
>>> inner = ['F', 'Cl', 'Br']
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
>>> 
