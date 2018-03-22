def print_table(n):
    """ (int) -> NoneType
    
    Print the multiplication table for numbers 1 through n inclusive.
    
    >>> print_table(5)
        1       2       3       4       5
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
        
    # End the header row.    
    print()
    
    # Print each row number and the contents of each row.
    for i in numbers:
        print (i, end='')
        for j in numbers:
            print('\t' + str(i * j), end='')
        # End the current row.    
        print()  