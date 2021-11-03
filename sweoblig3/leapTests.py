# Should pass as 2000 is in fact a leap year
import pytest

from leapYear import leapYear

def test_DivisibleBy4Not100():
    assert leapYear(1800) % 4 == 0 and leapYear(1800) % 100 == False

def test_DivisibleBy400():
    assert leapYear(1600) % 400 == True


def test_NotDivisibleBy4():
    assert leapYear(1598) % 4 == False


def test_DivisibleBy100Not400():
    assert leapYear(1000) % 100 == 0 and leapYear(1013) % 400 == False









