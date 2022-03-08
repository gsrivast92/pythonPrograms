def count_words(str):
    result = {}
    temp = str.split()
    for i in temp:
        if i not in result:
            result[i] = 1
        else:
            result[i] +=1
    return result

a = "Sugandha is having a child name Avyaan and Avyaan with Sugandha is very good and Sugandha Avyaan and Avyaan"
print(count_words(a))
