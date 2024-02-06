from lib.high_value import *


def test_high_value():
        subject = HighValue(8,6)
        assert subject.get_highest() == "First value is higher"
        subject = HighValue(6,8)
        assert subject.get_highest() == "Second value is higher"
        subject = HighValue(6,6)
        assert subject.get_highest() == "Values are equal"

def test_add():
        subject = HighValue(4,6)
        subject.add(2, "first")
        subject.add(3, "second")
        assert subject.value_first == 6

