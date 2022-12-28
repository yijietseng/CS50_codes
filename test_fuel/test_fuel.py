import fuel
import pytest


def test_ZeroDivision():
    with pytest.raises(ZeroDivisionError):
        fuel.convert('0/0')
def test_value():
    with pytest.raises(ValueError):
        fuel.convert('cat/cat')

def test_gauge():
    assert fuel.convert('99/100') == 99 and fuel.gauge(99) == 'F'
    assert fuel.convert('1/2') == 50 and fuel.gauge(50) == '50%'
    assert fuel.convert('1/100') == 1 and fuel.gauge(1) == 'E'

