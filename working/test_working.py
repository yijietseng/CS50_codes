from working import convert
import pytest

def test_12to24():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'

def test_wrong_hr():
    with pytest.raises(ValueError):
        assert convert('13:00 PM to 15:00 PM')
def test_wrong_min():
    with pytest.raises(ValueError):
        assert convert('9:60 AM to 8:70 PM')
def test_omit_to():
    with pytest.raises(ValueError):
        assert convert('9:00 AM 5:00 PM')
def test_value_error():
    with pytest.raises(ValueError):
        assert convert('9AM to 5PM')


