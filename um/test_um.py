from um import count
import pytest

def test_cap():
    assert count('Um') == 1

def test_count():
    assert count('Um, hello, um, world') == 2

def test_yum():
    assert count('yum') == 0
    assert count('Mum') == 0
    assert count('album') == 0

