def _min(array):
    min_ = array[0]
    for i in array:
        if i < min_:
            min_ = i
    return min_