def _min(array):
    min_ = array[0]
    for i in array:
        if i < min_:
            min_ = i
    return min_

def _max(array):
    max_ = array[0]
    for i in array:
        if i > max_:
            max_ = i
    return max_

def _mult(array):
    mult_ = 1
    for i in array:
        mult_ *= i
    return mult_

def _sum(array):
    sum_ = 0
    for i in array:
        sum_ += i
    return sum_

print(_min([1, 2, 33, 4]))
print(_max([1, 2, 33, 4]))
print(_sum([1, 2, 33, 4]))
print(_mult([1, 2, 1, 4]))