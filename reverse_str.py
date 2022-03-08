def reverse_str(str):
    result = []
    for i in range(len(str)-1, -1, -1):
        result.append(str[i])
    result = ''.join(result)
    return result



a = "Sugandha and Avyaan"

print(reverse_str(a))