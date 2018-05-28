import time_series

def smallest_value_skip(reader):
    """ (file open for reading) -> NoneType
    
    Read and process reader, which must start with a time_series header.
    Return the smallest value after the header. Skip missing values, which
    are indicaded with a hyphen.
    """
    
    line = time_series.skip_header(reader).strip()
    
    # If no data in first line after the header -> None, or edit the .txt file.
    if line != '':
        smallest = int(line)
    
        for line in reader:
            line = line.strip()
            if line != '-':
                value = int(line)
                smallest = min(smallest, value)
            
        return smallest

if __name__ == '__main__':
    with open('hebron_002.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))
        