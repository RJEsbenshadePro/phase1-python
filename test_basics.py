def add_number(a, b):
    return a + b

def test_addition():
    assert add_number(2, 3) == 5
    
def test_addition_negative():
    assert add_number(-1, 1) == 0


