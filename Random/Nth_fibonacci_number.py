#python3

def Nth_fibonacci_number(number):

    f_0 = 0
    f_1 = 1
    for i in range(number):
        if (number <= 1):
            return number
        else:
            f_n = f_1 + f_0
            f_0 = f_1
            f_1 = f_n
    return f_n


print(Nth_fibonacci_number(100))
