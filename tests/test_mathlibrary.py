from projecteuler.mathlibrary import MathLibrary

def test_reverse_even_number_digits():
    # even number of digits
    expected = 4321
    actual = MathLibrary.reverse_digits(1234)
    assert expected == actual

def test_reverse_odd_number_digits():
    # odd number of digits
    expected = 987654321
    actual = MathLibrary.reverse_digits(123456789)
    assert expected == actual

def test_pass_multiples():
    #
    assert True == MathLibrary.is_multiple(4, 2)
    assert True == MathLibrary.is_multiple(9, 3)
    assert True == MathLibrary.is_multiple(12, 6)
    assert True == MathLibrary.is_multiple(25, 5)
    assert True == MathLibrary.is_multiple(4648, 332)
    assert True == MathLibrary.is_multiple(2, 1)

def test_fail_multiples():
    #
    assert False == MathLibrary.is_multiple(4, 3)
    assert False == MathLibrary.is_multiple(1, 0)
    assert False == MathLibrary.is_multiple(13, 3)
    assert False == MathLibrary.is_multiple(19, 18)
    assert False == MathLibrary.is_multiple(23, 2)
    assert False == MathLibrary.is_multiple(37, 6)
