import main

def test_min_func():
    assert main._min([3,2,1]) == min([3,2,1])
    assert main._min([3,-2,1]) == min([3,-2,1])
    assert main._min([-1000, 10])== min([-1000, 10])

def test_max_func():
    assert main._max([3,4,1]) == max([3,4,1])
    assert main._max([-3,-1232,1]) == max([-3,-1232,1])
    assert main._max([10, -12100])== max([10, -12100])

def test_sum_func():
    assert main._sum([3,4,1]) == sum([3,4,1])
    assert main._sum([-3,-1232,1]) == sum([-3,-1232,1])
    assert main._sum([10, -12100])== sum([10, -12100])

def test_mult_func():
    assert main._mult([3,4,1]) == 12
    assert main._mult([3,-4,1]) == -12
    assert main._mult([3,-4,-1]) == 12
    assert main._mult([3,0,-1]) == 0