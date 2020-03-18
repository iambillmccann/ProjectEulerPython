from projecteuler.mathlibrary import MathLibrary

def test_reverse_digits():
    # even number of digits
    expected = 4321
    actual = MathLibrary.reverse_digits(1234)
    assert expected == actual

    # odd number of digits
    expected = 987654321
    actual = MathLibrary.reverse_digits(123456789)
    assert expected == actual
