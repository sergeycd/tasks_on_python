from dev import arithmetic


def test_adding():
    adding=arithmetic(2,3,'+')
    assert adding ==5

def test_subtraction():
    subtraction = arithmetic(5, 1,'-')
    assert subtraction==4

def test_multiplication():
    multiplication = arithmetic(2, 3,'*')
    assert multiplication==6

def test_division():
    multiplication = arithmetic(10, 2,'/')
    assert multiplication==5

def test_incorrect_sing():
    multiplication = arithmetic(2, 3,'test')
    assert multiplication=="Неизвестная операция "
