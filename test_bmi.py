import llab2.bmi as bmi

def test_bmi_normal_weight():
    inputbmi = 20
    result = bmi.classify_bmi(inputbmi)
    assert(result == 0)

def test_bmi_over_weight():
    inputbmi = 27
    result = bmi.classify_bmi(inputbmi)
    assert(result == 1)

def test_bmi_under_weight():
    inputbmi = 17
    result = bmi.classify_bmi(inputbmi)
    assert(result == -1)

