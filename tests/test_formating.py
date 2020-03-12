from projecteuler.mathlibrary import utilities

def test_ms_less_than_10():
    expected = '00:00:00.006'
    actual = utilities.format_milliseconds(0.006)
    assert expected == actual

def test_ms_less_than_100():
    expected = '00:00:00.076'
    actual = utilities.format_milliseconds(0.076)
    assert expected == actual

def test_sec_less_than_10():
    expected = '00:00:05.000'
    actual = utilities.format_milliseconds(5.000)
    assert expected == actual

def test_min_less_than_10():
    expected = '00:03:00.000'
    actual = utilities.format_milliseconds(180.000)
    assert expected == actual

def test_hours_less_than_10():
    expected = '02:00:00.000'
    actual = utilities.format_milliseconds(7200.000)
    assert expected == actual

def test_ms_not_more_than_999():
    expected = '00:00:01.000'
    actual = utilities.format_milliseconds(1.0001)
    assert expected == actual

def test_sec_less_than_60():
    expected = '00:00:59.000'
    actual = utilities.format_milliseconds(59.000)
    assert expected == actual

def test_min_less_than_60():
    expected = '01:00:00.000'
    actual = utilities.format_milliseconds(3600.000)
    assert expected == actual

def test_hours_more_than_99():    
    expected = '100:00:00.000'
    actual = utilities.format_milliseconds(360000.000)
    assert expected == actual
