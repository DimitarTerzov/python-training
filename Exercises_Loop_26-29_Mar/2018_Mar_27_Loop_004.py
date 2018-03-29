Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> rabbits = 3
>>> while rabbits > 0:
	print(rabbits)
	rabbits = rabbits - 1

	
3
2
1
>>> time = 0
>>> population = 1000	# 1000 bacteria to start with
>>> growth_rate = 0.21 	# 21% growth per minute
>>> while population < 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1

	
1210
1464
1772
2144
>>> while population < 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1

	
>>> while population < 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1
    print("It took", time, "minutes for bacteria to double.")
    
SyntaxError: unindent does not match any outer indentation level
>>> time = 0
>>>  population = 1000	# 1000 bacteria to start with
 
SyntaxError: unexpected indent
>>> time = 0
>>> population = 1000	# 1000 bacteria to start with
>>> growth_rate = 0.21  # 21% growth per minute
>>> while population < 2000:
	population = population + growth_rate * population
	time = time + 1
    print("It took", time, "minutes for the bacteria to double.")
    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> 
>>> 
>>> # Use multivalued assigment to set up controls
time, population, growth_rate = 0, 1000, 0.21

# Don't stop until we're exactly double the original size
while population != 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1
    
print("It took", time, "minutes for bacteria to double.")
SyntaxError: multiple statements found while compiling a single statement
>>> time, population, growth_rate = 0, 1000, 0.21
>>> while population != 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1
    print("It took", time, "minutes for the bacteria to double.")
    
SyntaxError: unindent does not match any outer indentation level
>>> while population != 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1
    print("It took", time, "minutes for the bacteria to double.")
    
SyntaxError: unindent does not match any outer indentation level
>>> while population != 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1
     print("It took", time, "minutes for the bacteria to double.")
     
SyntaxError: unindent does not match any outer indentation level
>>> while population != 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1
        print("It took", time, "minutes for the bacteria to double.")
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while population != 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1
    print("It took", time, "minutes for the bacteria to double.")
    
SyntaxError: unindent does not match any outer indentation level
>>> while population != 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1
	
    print("It took", time, "minutes for the bacteria to double.")
    
SyntaxError: unindent does not match any outer indentation level
>>> time, population, growth_rate = 0, 1000, 0.21
>>> while population != 2000:
	population = population + growth_rate * population
	print(round(population))
	time = time + 1
	
    print("It took", time, "minutes for the bacteria to double.")
    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> 
>>> 
>>> s = 'CeH7'
>>> digit_index = -1    # This will be -1 until we find a digit
>>> for i in range(len(s)):
	# If we haven't found a digit, and s[i] is a digit
	if digit_index == -1 and s[i].isdigit():
		digit_index = i

		
>>> digit_index
3
>>> 
>>> 
>>> s = 'C3H7'
>>> digit_index = -1 # This will be -1 until we found a digit
>>> for i in range(len(s)):
	# If we haven't found a digit, and s[i] is a digit
	if digit_index = i
	
SyntaxError: invalid syntax
>>> for i in range(len(s)):
	# If we haven't found a digit, and s[i] is a digit
	if digit_index == -1 and s[i].isdigit():
		digit_index = i

		
>>> digit_index
1
>>> s = 'kjghewuoghweugbwkehgw45252leshgflhglwhgwegewleg'
>>> s = 'kjghewuoghweugbwkehgw45252leshgflhglwhgwegewleg'
>>> for i in range(len(s)):
	# If we haven't found a digit, and s[i] is a digit
	if digit_index == -1 and s[i].isdigit():
		digit_index = i

		
>>> digit_index
1
>>> s
'kjghewuoghweugbwkehgw45252leshgflhglwhgwegewleg'
>>> digit_index
1
>>> s = 'kjghewuoghweugbwkehgw45252leshgflhglwhgwegewleg'
>>> digit_index = -1 # This will be -1 until we found a digit
>>> for i in range(len(s)):
	# If we haven't found a digit, and s[i] is a digit
	if digit_index == -1 and s[i].isdigit():
		digit_index = i

		
>>> digit_index
21
>>> s = 'C3H7'
>>> digit_index = -1 # This will be -1 until we found a digit
>>> for i in range(len(s)):
	# If we find a digit
	if s[i],isdigit():
		
SyntaxError: invalid syntax
>>> for i in range(len(s)):
	# If we find a digit
	if s[i].isdigit():
		digit_index = i
		break # This exits the loop.

	
>>> dogit_index
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dogit_index
NameError: name 'dogit_index' is not defined
>>> digit_index
1
>>> 
>>> 
>>> s = 'C3H7'
>>> total = 0 # The sum of the digit seen so far.
>>> count = 0 # The number of digit seen so far.
>>> for i in range(len(s)):
	if s[i].isalpha():
		continue
	total = total + int(s[i])
	count = count + 1

	
>>> total
10
>>> count
2
>>> s
'C3H7'
>>> s = 'C3H7'
>>> for i in range(len(s)):
	if not s[i].isalpha():
		total = total + int(s[i])
		count = count + 1

		
>>> total
20
>>> count
4
>>> total
20
>>> count
4
>>> s = 'C3H7'
>>> total = 0
>>> count = 0
>>> for i in range(len(s)):
	if not s[i].isalpha():
		total = total + int(s[i])
		count = count + 1

		
>>> total
10
>>> count
2
>>> 
>>> 
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> for i in celegans_phenotypes:
	print(item)

	
Traceback (most recent call last):
  File "<pyshell#128>", line 2, in <module>
    print(item)
NameError: name 'item' is not defined
>>> for i in celegans_phenotypes:
	print(i)

	
Emb
Him
Unc
Lon
Dpy
Sma
>>> for worms in celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']:
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> for worms in celegans_phenotypes:
	print(worms)

	
Emb
Him
Unc
Lon
Dpy
Sma
>>> 
>>> half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
>>> for values in half_lives:
	print(values)

	
87.74
24110.0
6537.0
14.4
376000.0
>>> for values in half_lives:
	print(values, end=' ')

	
87.74 24110.0 6537.0 14.4 376000.0 
>>> for values in half_lives:
	print(values, end=' 	')

	
87.74 	24110.0 	6537.0 	14.4 	376000.0 	
>>> for values in half_lives:
	print(values, end='	')

	
87.74	24110.0	6537.0	14.4	376000.0	
>>> for values in half_lives:
	print(values, end='    ')

	
87.74    24110.0    6537.0    14.4    376000.0    
>>> celegans_phenotypes
['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']
>>> for worms in celegans_phenotypes:
	print(worms, end='    ')

	
Emb    Him    Unc    Lon    Dpy    Sma    
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> for more_whales in whales:
	whales = whales + 1
	print(more_whales)

	
Traceback (most recent call last):
  File "<pyshell#160>", line 2, in <module>
    whales = whales + 1
TypeError: can only concatenate list (not "int") to list
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> more_whales = []
>>> for number_of_whales in whales:
	print(more_whales.append(number_of_whales + 1))

	
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
None
None
>>> more_whales
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)
	print(more_whales[-1])

	
6
5
8
4
3
4
3
7
5
3
2
8
2
4
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)
    print(more_whales)
    
SyntaxError: unindent does not match any outer indentation level
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)

>>> more_whales
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4, 6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4, 6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> more_whales = []
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)

	
>>> more_whales
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> more_whales = []
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)
    print(more_whales)
    
SyntaxError: unindent does not match any outer indentation level
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)

	
>>> more_whales
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)
        print(more_whales)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)
        print(more_whales)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)
	print(more_whales[-1])

	
6
5
8
4
3
4
3
7
5
3
2
8
2
4
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> more_whales
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4, 6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> more_whales = []
>>> for number_of_whales in whales:
	more_whales.append(number_of_whales + 1)
	print(more_whales)

	
[6]
[6, 5]
[6, 5, 8]
[6, 5, 8, 4]
[6, 5, 8, 4, 3]
[6, 5, 8, 4, 3, 4]
[6, 5, 8, 4, 3, 4, 3]
[6, 5, 8, 4, 3, 4, 3, 7]
[6, 5, 8, 4, 3, 4, 3, 7, 5]
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3]
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2]
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8]
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2]
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> def func(alist):
	more_whales = []
	for number_of_whales in alist:
		more_whales.append(number_of_whales + 1)
	print(more_whales)

	
>>> func(whales)
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> func(more_whales)
[7, 6, 9, 5, 4, 5, 4, 8, 6, 4, 3, 9, 3, 5]
>>> func(whales)
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> func(more_whales)
[7, 6, 9, 5, 4, 5, 4, 8, 6, 4, 3, 9, 3, 5]
>>> def func(alist):
	more_whales = []
	for number_of_whales in alist:
		more_whales.append(number_of_whales + 1)
	return(more_whales)

>>> func(whales)
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> func(more_whales)
[7, 6, 9, 5, 4, 5, 4, 8, 6, 4, 3, 9, 3, 5]
>>> 
>>> 
>>> 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> def func(www):
	more_whales = []
	for count in www:
		whales.append(count + 1)
	print(more_whales)

	
>>> more_whales
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> def func(www):
	more_whales = []
	for count in www:
		whales.append(count + 1)
    print(more_whales)
    
SyntaxError: unindent does not match any outer indentation level
>>> whales
[5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> more_whales = []
>>> 
