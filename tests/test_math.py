import pytest
def test_one_plus_one():
    assert 1 + 1 == 2

#Testcase with failure
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

#Test with exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)

#Adding parameterized multiplication tests
#Creating tuples for future tests
products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

#Creating a parameterized testcase
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product