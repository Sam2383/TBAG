class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}#This dictionary stores pairs of the rooms' names as well as the direction they are linked in.
        self.character = None
        self.item = None


    def get_description(self):
        return self.description
    
    
    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)#Does same thing as get method but quicker

    def set_name(self, room_name):
        self.name = room_name


    def get_name(self):
        return self.name
    

    def item_description(self):
        print(self.description)
    

    def set_item(self, room_item):
         self.item = room_item

    def get_item(self):
         return self.item
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link #The dictionary's items are updated with the value of the argument assigned to room_to_link and direction

    def get_details(self):
        print(self.name)
        print('-------------------------')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'The {room.get_name()} is {direction}')  

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print('You cannot go that way!')
            return self
        
    