class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self_conversation = None


    def describe(self):
        print(f"{self.name} is in this room")
        print(self.description)

    def set_converstaion(self, conversation):
        self.conversation = conversation


    def talk(self):
        if self.conversation is not None:
            print(f'[{self.name}] says: {self.conversation}')
        else:
            print(f'{self.name} does not want to talk to you')

    def fight(self, combat_item):
        print(f'{self.name} does not want to fight you')
        return True
    

class Friendly(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
    

    def hug(self):
        print(f'{self.name} embraces you :D')


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.likes = None

    def set_likes(self, enemy_likes):
        self.likes = enemy_likes

    def get_likes(self):
        return self.likes
    
    def bribe(self, bribe_item):
        self.bribary = bribe_item
        if bribe_item.lower() == self.likes:
            print(f'{self.name} seems to like what you have offered. They let you go for now...')#I might require a return true line to access the results of this code later.
            return True
        else:
            print(f'Your attempt to bribe {self.name} infuritates them. You fall victim to their fury')
            return False


    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.set_weakness
    
    def fight(self, combat_item):#This fight method within the enemy class overwrites the fight method within in the characterr superclass it is inheriting from.
        if combat_item.lower() == self.weakness:
            print(f'You fend {self.name} off with the {combat_item}!')
            return True
        else:
            print(f'{self.name} crushes you, puny adventurer!')
            return False
            
        
    












    def attack(self):
        print(f'{self.name} has attacked you!')

