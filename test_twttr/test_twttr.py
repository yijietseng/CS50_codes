from twttr import shorten

def test_str():
    assert shorten('Ilove You') == 'lv Y'
    assert shorten('MyNameisJosh') == 'MyNmsJsh'

def test_num():
    assert shorten('10000') == '10000'
    assert shorten('0') == '0'
    assert shorten('-1') == '-1'

def test_punc():
    assert shorten('Test. ,/test') == 'Tst. ,/tst'