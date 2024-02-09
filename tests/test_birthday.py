from lib.birthday import Birthdays

def test_add_friends_name_and_birthdays():
    birthdays = Birthdays()
    birthdays.add("Patrick", "02-05-1992")
    birthdays.add("Hayri", "29-10-1987")
    assert birthdays.list_added() == {"Patrick": ["02-05-1992", False], "Hayri": ["29-10-1987", False]}

def test_update_friends_name_and_birthdays():
    birthdays = Birthdays()
    birthdays.add("Patrick", "02-05-1992")
    birthdays.update("Patrick", "Hayri", "29-10-1987")
    assert birthdays.list_added() == {"Hayri": ["29-10-1987", False]}

def test_list_upcoming_birthday():
    birthdays = Birthdays()
    birthdays.add("Patrick", "02-10-1992")
    birthdays.add("Hayri", "12-02-1987")
    birthdays.add("George", "14-02-1995")
    assert birthdays.upcoming() == ["Hayri", "George"]
