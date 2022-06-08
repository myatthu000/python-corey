

def one_line_dir(x):
    directory = dir(x)
    j = 0
    for i in directory:
        j += 1
        print(j, '--->', i,"---->",type(i))


