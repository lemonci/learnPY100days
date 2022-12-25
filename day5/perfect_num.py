def get_factor_sum(input_num):
    sum_amount = 0
    for i in range(1, int(input_num/2)+1):
        if input_num % i == 0:
            sum_amount += i
    return sum_amount


def find_perfectnumber(input_num: int):
    for i in range(1, input_num):
        if get_factor_sum(i) != i:
            #print("%d is not a perfect number" % i)
            continue
        else:
            print("%d is a perfect number" % i)

if __name__ == '__main__':
    find_perfectnumber(10000)