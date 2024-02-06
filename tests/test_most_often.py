from lib.most_often import *
def test_add_new():
    most_often = MostOften([])
    most_often.add_new("Icardi")
    most_often.add_new("Muslera")
    most_often.add_new("Mertens")
    most_often.add_new("Icardi")
    assert most_often.starting_list  == ["Icardi","Muslera", "Mertens", "Icardi"]

def test_get_most_often():
    most_often = MostOften(["Icardi","Muslera", "Mertens", "Icardi"])
    result = most_often.get_most_often()
    assert result == "Icardi"
    most_often = MostOften(["Icardi","Muslera", "Mertens"])
    result = most_often.get_most_often()
    assert result == "no clear winner"