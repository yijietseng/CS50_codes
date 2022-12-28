from bank import value


def test_0():
    assert value('hello') == 0

def test_20():
    assert value('heasdli') == 20

def test_100():
    assert value('My Name is Josh') == 100

def test_case():
    assert value('HELLO') == 0
    assert value('HEASDLI') == 20
    assert value('MY NAME IS JOSH') == 100