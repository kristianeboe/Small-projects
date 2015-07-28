__author__ = 'Kristian'

def fibb_sum_with_list(n):
    fibb_list = [0, 1]
    while fibb_list[-1] < n:
        print fibb_list[-1]
        fibb_list.append(fibb_list[-1]+fibb_list[len(fibb_list)-2])
    return sum(fibb_list)

print fibb_sum_with_list(4000000)

def fibb_iterative(n):
    sum_ = 0
    n0 = 0
    n1 = 1
    while n0 < n:
        print n0
        sum_ += n0
        n2 = n0 + n1
        n0 = n1
        n1 = n2
    return sum_

print fibb_iterative(4000000)