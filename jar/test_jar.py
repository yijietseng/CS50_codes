from jar import Jar
import pytest

def test_init():
    jar = Jar(12)
    assert jar.capacity == 12
    jar2 = Jar(5)
    assert jar2.capacity == 5
    jar3 = Jar(100)
    assert jar3.capacity == 100

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(6)
    assert jar.size == 11


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.withdraw(13)
    jar.withdraw(2)
    assert jar.size == 10
    jar.withdraw(5)
    assert jar.size == 5
