import pytest
from TestNumber import IntegerSet


def test_sum():
    int_set = IntegerSet([1, 2, 3, 4, 5])
    assert int_set.sum() == 15


def test_average():
    int_set = IntegerSet([1, 2, 3, 4, 5])
    assert int_set.average() == 3


def test_maximum():
    int_set = IntegerSet([1, 2, 3, 4, 5])
    assert int_set.maximum() == 5


def test_minimum():
    int_set = IntegerSet([1, 2, 3, 4, 5])
    assert int_set.minimum() == 1



"""
Для запуска, в терминале pytest test_TestNumber.py"""