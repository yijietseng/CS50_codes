from seasons import get_Bday
import pytest

def test_get_Bday():
    with pytest.raises(SystemExit):
        get_Bday('January 1, 1999')
        get_Bday('January-1-1999')
        get_Bday('1991, March 1st')
