from main import arithmetic
from main import is_year_leap
from main import is_year_leap_second_v


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

def test_calendar_isleap():
    isleap=is_year_leap(2024)
    isntleap= is_year_leap(2023)
    assert isleap == True and isntleap == False

def test_calendar_isleap_v2():
    isleap = is_year_leap_second_v(2020)
    isnt = is_year_leap_second_v(2021)
    assert isleap == True and isnt == False