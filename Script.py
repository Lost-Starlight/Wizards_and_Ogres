class Player:
  def __init__(self, name, hp, items=[], attack= 12):
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

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    item_list = self.items
    item_list.remove(item)
  
  def use_item(self, item):
    for i in self.items:
      if i.name == item:
        self.remove_item(i)
        i.heal_user(self)
        print("You consumed the " + item + " and gained " + str(i.heal_amount) + ".")
     

  


class Enemy:
  def __init__(self, name, hp, attack_power):
    self.name = name
    self.hp = hp
    self.attack_power = attack_power
    self.is_defeated = False

  def __repr__(self):
    return "{name} has {hp} health left.".format(name=self.name, hp=self.hp)
  
  def lose_hp(self, hp):
    self.hp -= hp
    if self.hp <= 0:
      self.hp = 0
      self.is_defeated = True

class Location:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.next_location = next_location

  def __repr__(self):
    return self.description


class HealthItem:
  def __init__(self, name, heal_amount):
    self.name = name
    self.heal_amount = heal_amount

  def __repr__(self):
    return self.name

  def heal_user(self, user):
    user.add_hp(self.heal_amount)


potion = HealthItem("Potion", 25)
mega_potion = HealthItem("Mega Potion", 75)
cookie = HealthItem("Cookie", 10)
apple = HealthItem("Apple", 15)
player1 = Player("", 100, [potion, cookie, apple, mega_potion])
goblin = Enemy("Goblin", 55, 6)
goblin2 = Enemy("Goblin", 55, 6)
goblin3 = Enemy("Goblin", 55, 6)
goblin4 = Enemy("Goblin", 55, 6)
ogre = Enemy("Ogre", 62, 12)
forest = Location("Forest", "You can see towering pine trees all around you. There seems to be two distinct paths going off into oppisite directions deep into the woods.")
plains = Location("Plains", "You stand in the middle of a vast grassland. You can see the entrance to a forest nearby.")
Ogres_house = Location("Ogre's House", "You come to another wider clearing in the woods. Directly in front of you lies the Ogre's house. You can see smoke billowing out of the chimney.")
forest_clearing = Location("Forest Clearing", "The trees give way to a small grassy patch. Sunlight streams in from the uncovered patch of sky.")
deep_woods = Location("Deep Woods", "Rotund branches and thick folage blot out most of the sunlight as you venture deeper into the woods. It is unaturally quiet and the only sound you hear is from your own footsteps.")

def combat(player, enemy):
  while player.game_over == False and enemy.is_defeated == False:
    print(enemy)
    choiceb = input("What would you like to do?: attack, check status, use item. ")
    while choiceb != 'attack' and choiceb != 'check status' and choiceb != 'use item': 
      choiceb = input("Oops! That was not a valid input! Please try again! ")
    if choiceb == 'attack':
      print("You attack " + enemy.name +"!")
      enemy.lose_hp(player.attack)
      print(enemy.name + " lost " + str(player.attack) + " HP!")
      print(enemy.name + " attacks you!")
      player.lose_hp(enemy.attack_power)
      print("You lose " + str(enemy.attack_power) + " HP!")
      continue
    elif choiceb == 'check status':
      print(player)
      continue
    else:
      choicei = input("Which item would you like to use: {items}. ".format(items=player1.items))
      player1.use_item(choicei)
      continue
    
  if player.game_over == True:
    print("You succomb to your injuries and are unable to continue. GAME OVER :( ")
    raise SystemExit()
  elif enemy.is_defeated == True:
    print("You have defeated {enemy}!".format(enemy=enemy.name))


#combat(player1, goblin)

#Game Start:
player1.name = input("Hello & welcome to Wizards and Ogres! You are an aspiring Wizard who's spellbook has been taken by a nefarious Ogre bent on world domination! Tell me, young apprentice, what is your name? ")

print(player1.name + "! what a wonderful name! Your journey awaits!")

print(plains)
choicep = input("What would you like to do?: move forward, check status, use item. ")
while choicep != "move forward":
  while choicep != "move forward" and choicep != "check status" and  choicep != "use item":
    choicep = input("Not a valid action! Please try again. What would you like to do?: move forward, check status, use item. ")
  if choicep == "check status":
    print(player1)
    choicep = input("What would you like to do?: move forward, check status, use item. ")
    continue
    

  elif choicep == "use item":
    choiceit = input("Which item would you like to use: {items}. ".format(items=player1.items))
    player1.use_item(choiceit)
    choicep = input("What would you like to do?: move forward, check status, use item. ")
    continue

if choicep == "move forward":
  print("A goblin jumps out and attacks you!")
  combat(player1, goblin)
  print("You continue on your way")

print(forest)
choicep2 = input("What would you like to do?: move forward, check status, use item. ")
while choicep2 != "move forward":
  while choicep2 != "move forward" and choicep2 != "check status" and choicep2 != "use item":
    choicep2 = input("Not a valid action! Please try again. What would you like to do?: move forward, check status, use item. ")
  if choicep2 == "check status":
      print(player1)
      choicep2 = input("What would you like to do?: move forward, check status, use item. ")
      continue

  elif choicep2 == "use item":
      choiceit2 = input("Which item would you like to use: {items}. ".format(items=player1.items))
      player1.use_item(choiceit2)
      choicep2 = input("What would you like to do?: move forward, check status, use item. ")
      continue

if choicep2 == "move forward":
  print("A goblin jumps out and attacks you!")
  combat(player1, goblin2)
  print("You continue on your way")

print(forest_clearing)
choicep3 = input("What would you like to do?: move forward, check status, use item. ")
while choicep3 != "move forward":
  while choicep3 != "move forward" and choicep3 != "check status" and choicep3 != "use item":
    choicep3 = input("Not a valid action! Please try again. What would you like to do?: move forward, check status, use item. ")
  if choicep3 == "check status":
      print(player1)
      choicep3 = input("What would you like to do?: move forward, check status, use item. ")
      continue

  elif choicep3 == "use item":
      choiceit3 = input("Which item would you like to use: {items}. ".format(items=player1.items))
      player1.use_item(choiceit3)
      choicep3 = input("What would you like to do?: move forward, check status, use item. ")
      continue

if choicep3 == "move forward":
  print("A goblin jumps out and attacks you!")
  combat(player1, goblin3)
  print("You continue on your way")

print(deep_woods)
choicep4 = input("What would you like to do?: move forward, check status, use item. ")
while choicep4 != "move forward":
  while choicep4 != "move forward" and choicep4 != "check status" and choicep4 != "use item":
    choicep4 = input("Not a valid action! Please try again. What would you like to do?: move forward, check status, use item. ")
  if choicep4 == "check status":
      print(player1)
      choicep4 = input("What would you like to do?: move forward, check status, use item. ")
      continue

  elif choicep4 == "use item":
      choiceit4 = input("Which item would you like to use: {items}. ".format(items=player1.items))
      player1.use_item(choiceit4)
      choicep4 = input("What would you like to do?: move forward, check status, use item. ")
      continue

if choicep4 == "move forward":
  print("A goblin jumps out and attacks you!")
  combat(player1, goblin4)
  print("You continue on your way")


print(Ogres_house)
choicep5 = input("What would you like to do?: move forward, check status, use item. ")
while choicep5 != "move forward":
  while choicep5 != "move forward" and choicep5 != "check status" and choicep5 != "use item":
    choicep5 = input("Not a valid action! Please try again. What would you like to do?: move forward, check status, use item. ")
  if choicep5 == "check status":
      print(player1)
      choicep5 = input("What would you like to do?: move forward, check status, use item. ")
      continue

  elif choicep5 == "use item":
      choiceit5 = input("Which item would you like to use: {items}. ".format(items=player1.items))
      player1.use_item(choiceit5)
      choicep5 = input("What would you like to do?: move forward, check status, use item. ")
      continue

if choicep5 == "move forward":
  print("You boldly venture forth and yank open the door to the fiend's abode. You see the ogre's hulking figure lounging upon a large tanned leather couch. Your not so subtle entrance has caused your nemesis to spad his face in your direction. He snarls loudly, bolting up and grabing the couch. He hurls it in your direction with a loud roar! You just barely manage to doge out of the way before it takes out part of the doorway. It's a fight!")
  combat(player1, ogre)
  print("As the Ogre crumples to the floor, you make a mad dash to reunite with your spellbook. You tear through the house, searching every room until you come to a chest in the Ogre's bedroom. Upon opening it, you find your spell book, alittle worse for wear but safe in your arms at last!")
print("Authors Notes:")
print("Thank you for playing my game! this is my first ever personal Python project! I will return to it in the future and tidy it up and maybe add some new features. Feel free to send me any messages or comments about my game! All input on it is appreciated!")

