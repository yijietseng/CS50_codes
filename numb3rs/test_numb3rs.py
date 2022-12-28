from numb3rs import validate

def test_str():
    assert validate('a.b.c.d') == False
    assert validate('aa.bb.cc.dd') == False
    assert validate('aaa.bbb.ccc.ddd') == False

def test_puc():
    punclist = [',',' ','.',';',':','/','?','(',')','-',' ']
    for i in punclist:
        assert validate(i+'.'+i+'.'+i+'.'+i) == False

def test_ip():
    assert validate('1.2.3.4') == True
    assert validate('11.22.33.44') == True
    assert validate('111.222.233.144') == True
    assert validate('111.222.333.444') == False
    assert validate('255.255.255.255') == True
    assert validate('1111.1111.1111.0') == False
