# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:16:01 2017

@author: eloy
"""

class UserSimple:
    pass

user1 = UserSimple()
user1.first_name = "David"
user1.last_name = "Bowman"

user2 = UserSimple()
user2.first_name = "Frank"
user2.last_name = "Poole"

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"

# Now create a more detailed User() class
import datetime

class User:
    """A member of FriendFace. For now we are
    only storing their name and birthday.
    But soon we will store an uncomfortable
    amount of user information."""
    
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday # Format YYYYMMDD
        
        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
        
    def age(self):
        """Return the age of the user in years."""
        bd = datetime.datetime.strptime(str(self.birthday),"%Y%m%d")
        today = datetime.datetime.today()
        birthday_passed = ((today.month,today.day) > (bd.month, bd.day))
        print(birthday_passed)
        age = today.year - bd.year - (not birthday_passed)
        return age        
        
        
user = User("Dave Bowman", "19710315")

print(user.name)
print(user.birthday)
print(user.first_name)
print(user.last_name)
print(user.age())


