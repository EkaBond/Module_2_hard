num = int(input('Введите число от 3 до 20: '))
def your_password(num):
    result_ = []
    for i in range(1, num):
        for j in range(i + 1, num):
            if i == j:
                continue
            if num % (i + j)  == 0:
                result_.extend([i, j])
    return result_
result = your_password(num)
result = ''.join(map(str, result))
print('Ваш код ', result)

#print(' '.join(map(str, lst))) -  нашла в инете переделать тип список в строку.

