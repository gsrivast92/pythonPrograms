def wrap(string, max_width):
    n =''
    for i in range(0, len(string), max_width):
        j  = string[i:i+max_width]
        n += j + '\n'
    return n




# def wrap(string, max_width):
#    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

s = "bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjd"
max_width = 15

out  = wrap(s,max_width)
print(out)

