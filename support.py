def read_file_int_array(filename):
    r=[]
    with open(filename, 'r') as f:
        for line in f:
            r.append(int(line))
    return r
      