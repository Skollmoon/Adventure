import random
class Zombie:
    def __init__(self) -> None:
        self.health = random.randrange(6, 10)
        
    def hurt(self, damage_taken):
        self.health -= damage_taken
        
        
class Player:
    def __init__(self) -> None:
        self.maxhealth = 20
        self.health = 20
    
    def hurt(self, damage_taken):
        self.health -= damage_taken
        print(f'The zombie attacks, you take {damage_taken} damage ({self.health} hp left)')
    
    def heal(self, amount):
        self.health = self.health+amount if self.health+amount<self.maxhealth else self.maxhealth


player = Player()
print("Welcome player, you'll be fighting enemies to save this python program!!")
print(f"You currently have {player.health}/{player.maxhealth} hp!")
heals_remaining = 3
heal_amount = 8
while(player.health>0):
    zombo = Zombie()
    print(f'You have {heals_remaining} healing potions left({heal_amount} hp each) ')
    choice = input(f'You encountred a zombie with {zombo.health} hp! what are you going to do? Type (Attack/Heal) : ').lower()
    while(zombo.health>0):
        while(choice not in ['attack', 'heal']):
            choice = input('please type attack or heal : ')
        if choice=='attack':
            damage = random.randint(1,3)
            zombo.hurt(damage)
            print(f'You just dealt {damage} damage to the zombie! it has {zombo.health} hp left.')
            if(zombo.health==0):
                print('The zombie died!')
                continue
        else:
            player.heal(heal_amount)
            heals_remaining-=1
            print(f'You healed {heal_amount} hp, you now have {player.health}/{player.maxhealth} hp.\nYou have {heals_remaining} healing potions')
        zombi_damage = random.randint(1, 2)
        player.hurt(zombi_damage)
        if player.health < 0:
            print(f'Game Over.')
            exit()
        choice = ''
