from plates import is_valid

def test_punc():
    punclist = [',',' ','.',';',':','/','?','(',')','-']
    for i in punclist:
        assert is_valid('CS'+i+'50') == False

def test_first2():
    assert is_valid('50050') == False

def test_len():
    assert is_valid('CS50') == True
    assert is_valid('CS5050') == True
    assert is_valid('CS505000') == False

def test_0():
    assert is_valid('CS0000') == False
    assert is_valid('CS50') == True

def test_NumPlacement():
    assert is_valid('CS50CS') == False
    assert is_valid('CS50') == True
