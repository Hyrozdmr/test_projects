"""
As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"

"""
import datetime

class Birthdays():
    def __init__(self):
        self.contents = {}

    def add(self, name, dob):
        self.contents[name] = [dob, False] 

    def list_added(self):
        return self.contents
    
    def update(self, name, new_name, new_dob):
        self.contents.pop(name)
        self.contents[new_name] = [new_dob, False]

    def upcoming(self):
        new_list = []
        upcoming_date = datetime.datetime.now() + datetime.timedelta(days=60)
        for name in self.contents:
            date_object = datetime.datetime.strptime(self.contents[name][0], '%d-%m-%Y')
            date_object = date_object.replace(year=upcoming_date.year)
            if self.contents[name][1] == False and date_object <= upcoming_date:
                new_list.append(name)
        return new_list                
    
    