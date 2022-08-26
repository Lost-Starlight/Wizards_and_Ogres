class Player:
  def __init__(self, name, hp, items=[], attack= 9):
    self.name = name
    self.hp = hp
    self.items = items
    self.attack = attack
    self.game_over = False
  
  def __repr__(self):
    return "{self} has {hp} health and is carrying the following item[s]: {items}".format(self=self.name, hp=str(self.hp), items=self.items)
  
  def add_hp(self, hp):
    self.hp += hp

  def lose_hp(self, hp):
    self.hp -= hp
    if self.hp <= 0:
      self.hp = 0
      self.game_over = True

  def check_gameover(self):
    if self.gameover == True:
      print("You succomb to your injuries and are unable to continue. GAME OVER :( ")

  def add_item(self, item):
    self.items.append(item)
    print(item + " has been added to your inventory.")

  def remove_item(self, item):
    if item in self.items:
      self.items.pop(item)
      print(item + " has been removed from your inventory.")

class Enemy:
  def __init__(self, name, hp, attack_power):
    self.name = name
    self.hp = hp
    self.attack_power = attack_power
    self.is_defeated = False

  def __repr__(self):
    return "{name} has {hp} health left."
  
  def lose_hp(self, hp):
    self.hp -= hp
    if self.hp <= 0:
      self.hp = 0
      self.is_defeated = True

class Location:
  def __init__(self, name, description, next_location=None):
    self.name = name
    self.decription = description
    self.next_location = next_location

  def __repr__(self):
    return self.description

  def set_next_location(self, next_location):
    self.next_location = next_location

class HealthItem:
  def __init__(self, name, heal_amount):
    self.name = name
    self.heal_amount = heal_amount

  def __repr__(self):
    return self.name

  def heal_user(self, user):
    user.add_hp += self.heal_amount

def combat(player, enemy):
  while player.game_over == False and enemy.is_defeated == False:
    print(enemy)
    choiceb = input("What would you like to do?: attack, check status. ")
    while choiceb != 'attack' and choiceb != 'check status': 
      choiceb = input("Oops! That was not a valid input! Please try again! ")
    if choiceb == 'attack':
      print("You attack " + enemy.name +"!")
      enemy.lose_hp(player.attack)
      print(enemy.name + " lost " + str(player.attack) + " HP!")
      print(enemy.name + " attacks you!")
      player.lose_hp(enemy.attack_power)
      print("You lose " + str(enemy.attack_power) + " HP!")
      continue
    else:
      print(player)
      continue

potion = HealthItem("Potion", 25)
mega_potion = HealthItem("Mega Potion", 75)
cookie = HealthItem("Cookie", 10)
player1 = Player("", 100, [potion, cookie])
goblin = Enemy("Goblin", 55, 6)
ogre = Enemy("Ogre", 62, 12)
forest = Location("Forest", "You can see towering pine trees all around you. There seems to be two distinct paths going off into oppisite directions deep into the woods.")
plains = Location("Plains", "You stand in the middle of a vast grassland. You can see the entrance to a forest nearby.", forest)
Ogres_house = Location("Ogre's House", "Directly in front of you lies the Ogre's house. You can see smoke billowing out of the chimney.")

#Game Start:
player1.name = input("Hello & welcome to Wizards and Ogres! You are an aspiring Wizard who's spellbook has been taken by a nefarious Ogre bent on world domination! Tell me, young apprentice, what is your name?")

print(player1.name + "! what a wonderful name! Your journey awaits!")
