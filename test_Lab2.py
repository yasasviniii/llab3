import llab2.Lab2 as lab2

import statistics

def test_find_min_max():
    inputtemp = [22.6, 33, 27.5, 30.5, 25.4]
    result = lab2.find_min_max(inputtemp)

    assert(result == [22.6, 33])

def test_calc_average():
    inputtemp = [22.6, 33, 27.5, 30.5, 25.4]
    ave = sum(inputtemp)/len(inputtemp)
    result = lab2.calc_average(inputtemp)

    assert(result == ave)

def test_calc_median_temperature():
    inputtemp = [22.6, 33, 27.5, 30.5, 25.4]
    median = statistics.median(inputtemp)
    result = lab2.calc_median_temperature(inputtemp)

    assert(result == median)

def test_sort_temperature():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result= lab2.sort_temperature(inp_list)

    assert (result == [10, 12.5, 15.8, 18.2, 20.3])

def test_calc_median_temperature_odd():
    inp_list = [10, 12.5, 20.3, 15.8, 18.2]

    result= lab2.calc_median_temperature(inp_list)

    assert (result == 15.8) 

def test_calc_median_temperature_even():
    inp_list = [10, 12.5, 20.3, 15.8]

    result= lab2.calc_median_temperature(inp_list)

    assert (result == 14.15)    