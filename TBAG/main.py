from room import Room
from character import Enemy #used to be character
from character import Friendly
from item import Item

kitchen = Room('Kitchen')
ballroom = Room('Ballroom')
dining_hall = Room('Dining Hall')
outside = Room('Outside')

dave = Enemy("Dave", "A smelly zombie") #used to be character
dave.set_converstaion('I want brains')
dave.set_weakness('cheese')
dining_hall.set_character(dave)


dracula = Enemy('Dracula', 'An ancient vampire')
dracula.set_converstaion('I want to suck your blood')
dracula.set_weakness('silver')
dracula.set_likes('blood')
ballroom.set_character(dracula)

# bob = Friendly('Bob', 'Friendly middle aged man')
# bob.set_converstaion('Hello there lad!')
# kitchen.set_character(bob) #All of this is for task 4, however I commentted it out to prevent clutter within the kitchen room as the key item will be in the kitchen.

item = Item('Key', 'A rusty key that seems to fit into a particular lock in the building..')
ballroom.set_item(item)
# current_inventory = self.invetory



kitchen.set_description('A dank and dirty room with flies')
# print(kitchen.get_description())#this line of code will now be done with the .describe method

ballroom.set_description('A now decrepit room, once housing only the most elegant guests')
dining_hall.set_description('A large room intended for great feasts')


kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')
outside.link_room(kitchen, 'north')

current_room = kitchen 
# second_room = ballroom

while True:
     print("\n")
     current_room.get_details()
     inhabitant = current_room.get_character()
     item = current_room.get_item()
     if inhabitant is not None:
       inhabitant.describe()
       inhabitant.talk()
       user_item = input('What will you fight with?') #Line 36-38 is Task 1
       inhabitant.fight(user_item)
       if user_item == 'cheese':
          True
       else:
         False #Line 39 - 42 is Task 2
     
     if item is not None: #Im trying to make an inventory as well as set the code to pick up the key here. If something goes wrong, remove the feature to add an invetory and it might work.(it did not work lol)
         print('You have found an item!')
         item.item_description()
         collect = input('Would you like to pick up this item?')
         if collect.lower() == 'yes':
            use = input('This key can be used to open a door north of the kitchen. Would you like to use it to do so?')
            if use.lower() == 'yes':
               print('You have escaped!')
     
     command = input('> ')
     current_room = current_room.move(command)
     if current_room == kitchen:
        if command.lower() == 'north':
           print('This door is locked. It seems it requires a key to open')
    #  if command == 'north east':
    #     key.get_description()
    #     print('This door is locked!')


    #  if current_room == ballroom:
    #     print('This door is locked! However you seem to have an item to help with that')
    #     key.get_description()
    #     leave_house = input('Would you like to use this key to escape?')
    #     if leave_house.lower() == 'yes':
    #        print('You have left the house.')     

     
     


   #   print("\n")
   #   current_room.get_details()
   #   if inhabitant is not None:
   #      inhabitant.describe()
   #      inhabitant.talk()
   #      user_bribe = input('You have no items - the only option is bribery. What do you bribe them with?')
   #      inhabitant.bribe(user_bribe)
   #      if user_bribe == 'blood':
   #          True
   #      else:
   #          False

     






        


# draculas_room = draculas_room.move
       







