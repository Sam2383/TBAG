from character import Character
from character import Enemy

dave = Enemy('Dave', 'A smelly zombie')
dave.describe()

dave.set_converstaion('I want brains')
dave.talk()

dave.set_weakness('cheese')

print('Dave is attacking you! What will you fight with?')
fight_with = input()
dave.fight(fight_with)

# dion = Enemy('Dion', 'A small boy')#This is me testing out the enemy class & the method I have created.
# dion.attack()


