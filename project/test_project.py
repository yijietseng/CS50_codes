import pytest
from project import *

def test_draw_x_y_test():
    assert draw_x_y_test(0, 0) == True
    assert draw_x_y_test(500, 300) == True
    assert draw_x_y_test(1500,1500) == False

def test_init_param_test():
    assert init_param_test(10, 10, 75) == True
    assert init_param_test(-1, 10, 75) == False
    assert init_param_test(10, -1, 75) == False
    assert init_param_test(10, 10, -1) == False

def test_score_test():
    assert score_test(10) == True
    assert score_test(10000000) == True
    assert score_test(-1) == False

