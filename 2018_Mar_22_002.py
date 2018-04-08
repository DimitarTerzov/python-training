Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> list(range(1, 5))
[1, 2, 3, 4]
>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(5, -3))
[]
>>> list(range(44, 33))
[]
>>> list(range(-13, -5))
[-13, -12, -11, -10, -9, -8, -7, -6]
>>> list(range(2000, 2050, 4))
[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
>>> list(range(2000, 4050, 4))
[2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2100, 2104, 2108, 2112, 2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196, 2200, 2204, 2208, 2212, 2216, 2220, 2224, 2228, 2232, 2236, 2240, 2244, 2248, 2252, 2256, 2260, 2264, 2268, 2272, 2276, 2280, 2284, 2288, 2292, 2296, 2300, 2304, 2308, 2312, 2316, 2320, 2324, 2328, 2332, 2336, 2340, 2344, 2348, 2352, 2356, 2360, 2364, 2368, 2372, 2376, 2380, 2384, 2388, 2392, 2396, 2400, 2404, 2408, 2412, 2416, 2420, 2424, 2428, 2432, 2436, 2440, 2444, 2448, 2452, 2456, 2460, 2464, 2468, 2472, 2476, 2480, 2484, 2488, 2492, 2496, 2500, 2504, 2508, 2512, 2516, 2520, 2524, 2528, 2532, 2536, 2540, 2544, 2548, 2552, 2556, 2560, 2564, 2568, 2572, 2576, 2580, 2584, 2588, 2592, 2596, 2600, 2604, 2608, 2612, 2616, 2620, 2624, 2628, 2632, 2636, 2640, 2644, 2648, 2652, 2656, 2660, 2664, 2668, 2672, 2676, 2680, 2684, 2688, 2692, 2696, 2700, 2704, 2708, 2712, 2716, 2720, 2724, 2728, 2732, 2736, 2740, 2744, 2748, 2752, 2756, 2760, 2764, 2768, 2772, 2776, 2780, 2784, 2788, 2792, 2796, 2800, 2804, 2808, 2812, 2816, 2820, 2824, 2828, 2832, 2836, 2840, 2844, 2848, 2852, 2856, 2860, 2864, 2868, 2872, 2876, 2880, 2884, 2888, 2892, 2896, 2900, 2904, 2908, 2912, 2916, 2920, 2924, 2928, 2932, 2936, 2940, 2944, 2948, 2952, 2956, 2960, 2964, 2968, 2972, 2976, 2980, 2984, 2988, 2992, 2996, 3000, 3004, 3008, 3012, 3016, 3020, 3024, 3028, 3032, 3036, 3040, 3044, 3048, 3052, 3056, 3060, 3064, 3068, 3072, 3076, 3080, 3084, 3088, 3092, 3096, 3100, 3104, 3108, 3112, 3116, 3120, 3124, 3128, 3132, 3136, 3140, 3144, 3148, 3152, 3156, 3160, 3164, 3168, 3172, 3176, 3180, 3184, 3188, 3192, 3196, 3200, 3204, 3208, 3212, 3216, 3220, 3224, 3228, 3232, 3236, 3240, 3244, 3248, 3252, 3256, 3260, 3264, 3268, 3272, 3276, 3280, 3284, 3288, 3292, 3296, 3300, 3304, 3308, 3312, 3316, 3320, 3324, 3328, 3332, 3336, 3340, 3344, 3348, 3352, 3356, 3360, 3364, 3368, 3372, 3376, 3380, 3384, 3388, 3392, 3396, 3400, 3404, 3408, 3412, 3416, 3420, 3424, 3428, 3432, 3436, 3440, 3444, 3448, 3452, 3456, 3460, 3464, 3468, 3472, 3476, 3480, 3484, 3488, 3492, 3496, 3500, 3504, 3508, 3512, 3516, 3520, 3524, 3528, 3532, 3536, 3540, 3544, 3548, 3552, 3556, 3560, 3564, 3568, 3572, 3576, 3580, 3584, 3588, 3592, 3596, 3600, 3604, 3608, 3612, 3616, 3620, 3624, 3628, 3632, 3636, 3640, 3644, 3648, 3652, 3656, 3660, 3664, 3668, 3672, 3676, 3680, 3684, 3688, 3692, 3696, 3700, 3704, 3708, 3712, 3716, 3720, 3724, 3728, 3732, 3736, 3740, 3744, 3748, 3752, 3756, 3760, 3764, 3768, 3772, 3776, 3780, 3784, 3788, 3792, 3796, 3800, 3804, 3808, 3812, 3816, 3820, 3824, 3828, 3832, 3836, 3840, 3844, 3848, 3852, 3856, 3860, 3864, 3868, 3872, 3876, 3880, 3884, 3888, 3892, 3896, 3900, 3904, 3908, 3912, 3916, 3920, 3924, 3928, 3932, 3936, 3940, 3944, 3948, 3952, 3956, 3960, 3964, 3968, 3972, 3976, 3980, 3984, 3988, 3992, 3996, 4000, 4004, 4008, 4012, 4016, 4020, 4024, 4028, 4032, 4036, 4040, 4044, 4048]
>>> list(range(2050, 2000, -4))
[2050, 2046, 2042, 2038, 2034, 2030, 2026, 2022, 2018, 2014, 2010, 2006, 2002]
>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 1))
[]
>>> list(range(10, 1, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> list(range(10, 15, 3))
[10, 13]
>>> list(range(10, 15, 4))
[10, 14]
>>> list(range(10, 15, 5))
[10]
>>> list(range(10, 15, 15))
[10]
>>> total = 0
>>> for i in range(1, 101):
	total = total + i

	
>>> total
5050
>>> i
100
>>> range(1, 101)
range(1, 101)
>>> list(range(1, 101))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> 
>>> 
>>> values = [4, 10, 3, 8, -6]
>>> for num in values:
	num = num * 2

	
>>> values
[4, 10, 3, 8, -6]
>>> num
-12
>>> def sum(N):
	""" int, int -> numer

	Return the sum of n + 1 to the last number of m.

	>>> sum(1, 5)
	15
	"""
	return N * (N + 1) / 2

>>> sum(100)
5050.0
>>> def sum(N):
	""" int, int -> nubmer

	Return the sum of n + 1 to the last number of m.

	>>> sum(1, 5)
	15
	"""
	return N * (N + 1) // 2

>>> sum(100)
5050
>>> 5050.0 / 2
2525.0
>>> 10100.0 / 2
5050.0
>>> 10100.0 // 2
5050.0
>>> 10 //2
5
>>> 10 // 2.0
5.0
>>> 10.0 // 2
5.0
>>> 10.0 // 2.0
5.0
>>> sum(500)
125250
>>> sum(500) - 112725
12525
>>> sum(500)
125250
>>> def sum(N):
	""" jbjwbefwehfwe """
	return N / 2 * (N + 1)

>>> sum(100)
5050.0
>>> def sum(N):
	""" jbjwbefwehfwe """
	return N // 2 * (N + 1)

>>> sum(100)
5050
>>> motal = 0
>>> for i in range(1, 101):
	motal = motal + i

	
>>> motal
5050
>>> i
100
>>> total = 20
>>> for i in range(1, 101):
	total = total + i

	
>>> total
5070
>>> for i in range(1, 501):
	lklkl

	
Traceback (most recent call last):
  File "<pyshell#95>", line 2, in <module>
    lklkl
NameError: name 'lklkl' is not defined
>>> q = 0
>>> for i in range(1, 101):
	q = q + i

	
>>> q
5050
>>> i
100
>>> total = 20
>>> for i in range(1, 101):
	total = total + i

	
>>> total
5070
>>> i
100
>>> for i in range(1, 101)
SyntaxError: invalid syntax
>>> 
>>> for i in range(1, 101):
	print i
	
SyntaxError: Missing parentheses in call to 'print'
>>> for i in range(1, 101):
	print(i)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
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
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
>>> for i in range(1, 101):
	print(i + 1)

	
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
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
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in range(1, 101):
	print(i + 15)

	
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
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
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
>>> values = [4, 10, 3, 8, -6]
>>> for num in values:
	num = num * 2

	
>>> values
[4, 10, 3, 8, -6]
>>> num
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
>>> for num in values:
	num = num * 2
	return(num)
SyntaxError: 'return' outside function
>>> for num in values:
	num = num * 2
		return(num)
	
SyntaxError: unexpected indent
>>> 
>>> print(values)
[4, 10, 3, 8, -6]
>>> num
-12
>>> values
[4, 10, 3, 8, -6]
>>> len(values)
5
>>> list(range(6))
[0, 1, 2, 3, 4, 5]
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(len(values)))
[0, 1, 2, 3, 4]
>>> values
[4, 10, 3, 8, -6]
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
>>> metals = ['Li', 'Na', 'K']
>>> wieghts = [6.941, 22.98976928, 39.0983]
>>> for i in range(len(metals)):
	print(metals[i], weights[i])

	
Traceback (most recent call last):
  File "<pyshell#172>", line 2, in <module>
    print(metals[i], weights[i])
NameError: name 'weights' is not defined
>>> for i in range(len(metals)):
	print(metals[i], wieghts[i])

	
Li 6.941
Na 22.98976928
K 39.0983
>>> metals = ['Li', 'Na', 'K']
>>> wieghts = [6.941, 22.98976928]
>>> for i in range(len(metals)):
	print(metals[i], wieghts[i])

	
Li 6.941
Na 22.98976928
Traceback (most recent call last):
  File "<pyshell#178>", line 2, in <module>
    print(metals[i], wieghts[i])
IndexError: list index out of range
>>> 
>>> 
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
>>> halogen
'Br'
>>> outer
['Li', 'Na', 'K']
>>> metal
'K'
>>> inner
['F', 'Cl', 'Br']
>>> 
>>> 
>>> 
>>> def print_table(n):
	""" (int) -> NoneType

	Print thr multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
	    1	    2       3	    4       5
	1   1       2       3       4       5
	2   2       4       6       8       10
	3   3       6       9       12      15
	4   4       8       12      16      20
	5   5       10      15      20      25
	"""

	
>>> def print_table(n):
	""" (int) -> NoneType

	Print thr multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
	    1	    2       3	    4       5
	1   1       2       3       4       5
	2   2       4       6       8       10
	3   3       6       9       12      15
	4   4       8       12      16      20
	5   5       10      15      20      25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))

	
>>> def print_table(n):
	""" (int) -> NoneType

	Print thr multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
	    1	    2       3	    4       5
	1   1       2       3       4       5
	2   2       4       6       8       10
	3   3       6       9       12      15
	4   4       8       12      16      20
	5   5       10      15      20      25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))
	# Print the header row.
	for i in numbers:
		print('\t' + str(i), end='')

		
>>> def print_table(n):
	""" (int) -> NoneType

	Print thr multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
	    1	    2       3	    4       5
	1   1       2       3       4       5
	2   2       4       6       8       10
	3   3       6       9       12      15
	4   4       8       12      16      20
	5   5       10      15      20      25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))
	# Print the header row.
	for i in numbers:
		print('\t' + str(i), end='')
	# End the row.
	print()
	# Print each row number and the contents of each row.
	for i in numbers:

		print (i, end='')
		for j in numbers:
			print('\t', + str(i * j), end='')

			
>>> def print_table(n):
	""" (int) -> NoneType

	Print thr multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
	    1	    2       3	    4       5
	1   1       2       3       4       5
	2   2       4       6       8       10
	3   3       6       9       12      15
	4   4       8       12      16      20
	5   5       10      15      20      25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))
	# Print the header row.
	for i in numbers:
		print('\t' + str(i), end='')
	# End the row.
	print()
	# Print each row number and the contents of each row.
	for i in numbers:

		print (i, end='')
		for j in numbers:
			print('\t', + str(i * j), end='')
		# End the current row.
		print()

		
>>> print_table(5)
	1	2	3	4	5
1Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    print_table(5)
  File "<pyshell#231>", line 26, in print_table
    print('\t', + str(i * j), end='')
TypeError: bad operand type for unary +: 'str'
>>> def print_table(n):
	""" (int) -> NoneType

	Print thr multiplication table for numbers 1 through n inclusive.

	>>> print_table(5)
	    1	    2       3	    4       5
	1   1       2       3       4       5
	2   2       4       6       8       10
	3   3       6       9       12      15
	4   4       8       12      16      20
	5   5       10      15      20      25
	"""
	# The numbers to include in the table.
	numbers = list(range(1, n + 1))
	# Print the header row.
	for i in numbers:
		print('\t' + str(i), end='')
	# End the row.
	print()
	# Print each row number and the contents of each row.
	for i in numbers:

		print (i, end='')
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
>>> print_table(15)
	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15
1	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15
2	2	4	6	8	10	12	14	16	18	20	22	24	26	28	30
3	3	6	9	12	15	18	21	24	27	30	33	36	39	42	45
4	4	8	12	16	20	24	28	32	36	40	44	48	52	56	60
5	5	10	15	20	25	30	35	40	45	50	55	60	65	70	75
6	6	12	18	24	30	36	42	48	54	60	66	72	78	84	90
7	7	14	21	28	35	42	49	56	63	70	77	84	91	98	105
8	8	16	24	32	40	48	56	64	72	80	88	96	104	112	120
9	9	18	27	36	45	54	63	72	81	90	99	108	117	126	135
10	10	20	30	40	50	60	70	80	90	100	110	120	130	140	150
11	11	22	33	44	55	66	77	88	99	110	121	132	143	154	165
12	12	24	36	48	60	72	84	96	108	120	132	144	156	168	180
13	13	26	39	52	65	78	91	104	117	130	143	156	169	182	195
14	14	28	42	56	70	84	98	112	126	140	154	168	182	196	210
15	15	30	45	60	75	90	105	120	135	150	165	180	195	210	225
>>> print_table(34)
	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34
1	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34
2	2	4	6	8	10	12	14	16	18	20	22	24	26	28	30	32	34	36	38	40	42	44	46	48	50	52	54	56	58	60	62	64	66	68
3	3	6	9	12	15	18	21	24	27	30	33	36	39	42	45	48	51	54	57	60	63	66	69	72	75	78	81	84	87	90	93	96	99	102
4	4	8	12	16	20	24	28	32	36	40	44	48	52	56	60	64	68	72	76	80	84	88	92	96	100	104	108	112	116	120	124	128	132	136
5	5	10	15	20	25	30	35	40	45	50	55	60	65	70	75	80	85	90	95	100	105	110	115	120	125	130	135	140	145	150	155	160	165	170
6	6	12	18	24	30	36	42	48	54	60	66	72	78	84	90	96	102	108	114	120	126	132	138	144	150	156	162	168	174	180	186	192	198	204
7	7	14	21	28	35	42	49	56	63	70	77	84	91	98	105	112	119	126	133	140	147	154	161	168	175	182	189	196	203	210	217	224	231	238
8	8	16	24	32	40	48	56	64	72	80	88	96	104	112	120	128	136	144	152	160	168	176	184	192	200	208	216	224	232	240	248	256	264	272
9	9	18	27	36	45	54	63	72	81	90	99	108	117	126	135	144	153	162	171	180	189	198	207	216	225	234	243	252	261	270	279	288	297	306
10	10	20	30	40	50	60	70	80	90	100	110	120	130	140	150	160	170	180	190	200	210	220	230	240	250	260	270	280	290	300	310	320	330	340
11	11	22	33	44	55	66	77	88	99	110	121	132	143	154	165	176	187	198	209	220	231	242	253	264	275	286	297	308	319	330	341	352	363	374
12	12	24	36	48	60	72	84	96	108	120	132	144	156	168	180	192	204	216	228	240	252	264	276	288	300	312	324	336	348	360	372	384	396	408
13	13	26	39	52	65	78	91	104	117	130	143	156	169	182	195	208	221	234	247	260	273	286	299	312	325	338	351	364	377	390	403	416	429	442
14	14	28	42	56	70	84	98	112	126	140	154	168	182	196	210	224	238	252	266	280	294	308	322	336	350	364	378	392	406	420	434	448	462	476
15	15	30	45	60	75	90	105	120	135	150	165	180	195	210	225	240	255	270	285	300	315	330	345	360	375	390	405	420	435	450	465	480	495	510
16	16	32	48	64	80	96	112	128	144	160	176	192	208	224	240	256	272	288	304	320	336	352	368	384	400	416	432	448	464	480	496	512	528	544
17	17	34	51	68	85	102	119	136	153	170	187	204	221	238	255	272	289	306	323	340	357	374	391	408	425	442	459	476	493	510	527	544	561	578
18	18	36	54	72	90	108	126	144	162	180	198	216	234	252	270	288	306	324	342	360	378	396	414	432	450	468	486	504	522	540	558	576	594	612
19	19	38	57	76	95	114	133	152	171	190	209	228	247	266	285	304	323	342	361	380	399	418	437	456	475	494	513	532	551	570	589	608	627	646
20	20	40	60	80	100	120	140	160	180	200	220	240	260	280	300	320	340	360	380	400	420	440	460	480	500	520	540	560	580	600	620	640	660	680
21	21	42	63	84	105	126	147	168	189	210	231	252	273	294	315	336	357	378	399	420	441	462	483	504	525	546	567	588	609	630	651	672	693	714
22	22	44	66	88	110	132	154	176	198	220	242	264	286	308	330	352	374	396	418	440	462	484	506	528	550	572	594	616	638	660	682	704	726	748
23	23	46	69	92	115	138	161	184	207	230	253	276	299	322	345	368	391	414	437	460	483	506	529	552	575	598	621	644	667	690	713	736	759	782
24	24	48	72	96	120	144	168	192	216	240	264	288	312	336	360	384	408	432	456	480	504	528	552	576	600	624	648	672	696	720	744	768	792	816
25	25	50	75	100	125	150	175	200	225	250	275	300	325	350	375	400	425	450	475	500	525	550	575	600	625	650	675	700	725	750	775	800	825	850
26	26	52	78	104	130	156	182	208	234	260	286	312	338	364	390	416	442	468	494	520	546	572	598	624	650	676	702	728	754	780	806	832	858	884
27	27	54	81	108	135	162	189	216	243	270	297	324	351	378	405	432	459	486	513	540	567	594	621	648	675	702	729	756	783	810	837	864	891	918
28	28	56	84	112	140	168	196	224	252	280	308	336	364	392	420	448	476	504	532	560	588	616	644	672	700	728	756	784	812	840	868	896	924	952
29	29	58	87	116	145	174	203	232	261	290	319	348	377	406	435	464	493	522	551	580	609	638	667	696	725	754	783	812	841	870	899	928	957	986
30	30	60	90	120	150	180	210	240	270	300	330	360	390	420	450	480	510	540	570	600	630	660	690	720	750	780	810	840	870	900	930	960	990	1020
31	31	62	93	124	155	186	217	248	279	310	341	372	403	434	465	496	527	558	589	620	651	682	713	744	775	806	837	868	899	930	961	992	1023	1054
32	32	64	96	128	160	192	224	256	288	320	352	384	416	448	480	512	544	576	608	640	672	704	736	768	800	832	864	896	928	960	992	1024	1056	1088
33	33	66	99	132	165	198	231	264	297	330	363	396	429	462	495	528	561	594	627	660	693	726	759	792	825	858	891	924	957	990	1023	1056	1089	1122
34	34	68	102	136	170	204	238	272	306	340	374	408	442	476	510	544	578	612	646	680	714	748	782	816	850	884	918	952	986	1020	1054	1088	1122	1156
>>> print_table(34)
	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34
1	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34
2	2	4	6	8	10	12	14	16	18	20	22	24	26	28	30	32	34	36	38	40	42	44	46	48	50	52	54	56	58	60	62	64	66	68
3	3	6	9	12	15	18	21	24	27	30	33	36	39	42	45	48	51	54	57	60	63	66	69	72	75	78	81	84	87	90	93	96	99	102
4	4	8	12	16	20	24	28	32	36	40	44	48	52	56	60	64	68	72	76	80	84	88	92	96	100	104	108	112	116	120	124	128	132	136
5	5	10	15	20	25	30	35	40	45	50	55	60	65	70	75	80	85	90	95	100	105	110	115	120	125	130	135	140	145	150	155	160	165	170
6	6	12	18	24	30	36	42	48	54	60	66	72	78	84	90	96	102	108	114	120	126	132	138	144	150	156	162	168	174	180	186	192	198	204
7	7	14	21	28	35	42	49	56	63	70	77	84	91	98	105	112	119	126	133	140	147	154	161	168	175	182	189	196	203	210	217	224	231	238
8	8	16	24	32	40	48	56	64	72	80	88	96	104	112	120	128	136	144	152	160	168	176	184	192	200	208	216	224	232	240	248	256	264	272
9	9	18	27	36	45	54	63	72	81	90	99	108	117	126	135	144	153	162	171	180	189	198	207	216	225	234	243	252	261	270	279	288	297	306
10	10	20	30	40	50	60	70	80	90	100	110	120	130	140	150	160	170	180	190	200	210	220	230	240	250	260	270	280	290	300	310	320	330	340
11	11	22	33	44	55	66	77	88	99	110	121	132	143	154	165	176	187	198	209	220	231	242	253	264	275	286	297	308	319	330	341	352	363	374
12	12	24	36	48	60	72	84	96	108	120	132	144	156	168	180	192	204	216	228	240	252	264	276	288	300	312	324	336	348	360	372	384	396	408
13	13	26	39	52	65	78	91	104	117	130	143	156	169	182	195	208	221	234	247	260	273	286	299	312	325	338	351	364	377	390	403	416	429	442
14	14	28	42	56	70	84	98	112	126	140	154	168	182	196	210	224	238	252	266	280	294	308	322	336	350	364	378	392	406	420	434	448	462	476
15	15	30	45	60	75	90	105	120	135	150	165	180	195	210	225	240	255	270	285	300	315	330	345	360	375	390	405	420	435	450	465	480	495	510
16	16	32	48	64	80	96	112	128	144	160	176	192	208	224	240	256	272	288	304	320	336	352	368	384	400	416	432	448	464	480	496	512	528	544
17	17	34	51	68	85	102	119	136	153	170	187	204	221	238	255	272	289	306	323	340	357	374	391	408	425	442	459	476	493	510	527	544	561	578
18	18	36	54	72	90	108	126	144	162	180	198	216	234	252	270	288	306	324	342	360	378	396	414	432	450	468	486	504	522	540	558	576	594	612
19	19	38	57	76	95	114	133	152	171	190	209	228	247	266	285	304	323	342	361	380	399	418	437	456	475	494	513	532	551	570	589	608	627	646
20	20	40	60	80	100	120	140	160	180	200	220	240	260	280	300	320	340	360	380	400	420	440	460	480	500	520	540	560	580	600	620	640	660	680
21	21	42	63	84	105	126	147	168	189	210	231	252	273	294	315	336	357	378	399	420	441	462	483	504	525	546	567	588	609	630	651	672	693	714
22	22	44	66	88	110	132	154	176	198	220	242	264	286	308	330	352	374	396	418	440	462	484	506	528	550	572	594	616	638	660	682	704	726	748
23	23	46	69	92	115	138	161	184	207	230	253	276	299	322	345	368	391	414	437	460	483	506	529	552	575	598	621	644	667	690	713	736	759	782
24	24	48	72	96	120	144	168	192	216	240	264	288	312	336	360	384	408	432	456	480	504	528	552	576	600	624	648	672	696	720	744	768	792	816
25	25	50	75	100	125	150	175	200	225	250	275	300	325	350	375	400	425	450	475	500	525	550	575	600	625	650	675	700	725	750	775	800	825	850
26	26	52	78	104	130	156	182	208	234	260	286	312	338	364	390	416	442	468	494	520	546	572	598	624	650	676	702	728	754	780	806	832	858	884
27	27	54	81	108	135	162	189	216	243	270	297	324	351	378	405	432	459	486	513	540	567	594	621	648	675	702	729	756	783	810	837	864	891	918
28	28	56	84	112	140	168	196	224	252	280	308	336	364	392	420	448	476	504	532	560	588	616	644	672	700	728	756	784	812	840	868	896	924	952
29	29	58	87	116	145	174	203	232	261	290	319	348	377	406	435	464	493	522	551	580	609	638	667	696	725	754	783	812	841	870	899	928	957	986
30	30	60	90	120	150	180	210	240	270	300	330	360	390	420	450	480	510	540	570	600	630	660	690	720	750	780	810	840	870	900	930	960	990	1020
31	31	62	93	124	155	186	217	248	279	310	341	372	403	434	465	496	527	558	589	620	651	682	713	744	775	806	837	868	899	930	961	992	1023	1054
32	32	64	96	128	160	192	224	256	288	320	352	384	416	448	480	512	544	576	608	640	672	704	736	768	800	832	864	896	928	960	992	1024	1056	1088
33	33	66	99	132	165	198	231	264	297	330	363	396	429	462	495	528	561	594	627	660	693	726	759	792	825	858	891	924	957	990	1023	1056	1089	1122
34	34	68	102	136	170	204	238	272	306	340	374	408	442	476	510	544	578	612	646	680	714	748	782	816	850	884	918	952	986	1020	1054	1088	1122	1156
>>> 