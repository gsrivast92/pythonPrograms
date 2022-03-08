def split_and_join(line):
    s = line.split(" ")
    t = '-'.join(line)
    return t


print(split_and_join("This is the string"))