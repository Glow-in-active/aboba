import time

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

def test_timerun():
    time_start = time.time()
    f = open("10000.txt")
    array_str = f.readline().split()
    array_int = []

    for i in array_str:
        array_int.append(int(i))

    main._min(array_int)
    main._max(array_int)
    main._sum(array_int)
    main._mult(array_int)
    f.close()
    time_stop = time.time()
    assert time_stop-time_start < 1
    print("10000:", time_stop-time_start)

    time_start = time.time()
    f = open("15000.txt")
    array_str = f.readline().split()
    array_int = []

    for i in array_str:
        array_int.append(int(i))

    main._min(array_int)
    main._max(array_int)
    main._sum(array_int)
    main._mult(array_int)
    f.close()
    time_stop = time.time()
    assert time_stop - time_start < 1
    print("15000:", time_stop - time_start)

    time_start = time.time()
    f = open("20000.txt")
    array_str = f.readline().split()
    array_int = []

    for i in array_str:
        array_int.append(int(i))

    main._min(array_int)
    main._max(array_int)
    main._sum(array_int)
    main._mult(array_int)
    f.close()
    time_stop = time.time()
    assert time_stop - time_start < 1
    print("20000:", time_stop - time_start)

    time_start = time.time()
    f = open("25000.txt")
    array_str = f.readline().split()
    array_int = []

    for i in array_str:
        array_int.append(int(i))

    main._min(array_int)
    main._max(array_int)
    main._sum(array_int)
    main._mult(array_int)
    f.close()
    time_stop = time.time()
    assert time_stop - time_start < 1
    print("25000:", time_stop - time_start)