# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
# Declare all the rooms

class Room:
    def __init__(self, name: str , description: str, item: Item):
        self.name = name
        self.description = description
        self.item = item
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def get_to_next_room(self, description):
        if hasattr(self, f"{description}_to"):
            return getattr(self, f'{description}_to')
        return None

    def grab_items(name, description):
        if hasattr(self, f"{item}" ):
            return getattr
            
