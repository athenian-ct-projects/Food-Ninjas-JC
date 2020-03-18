import random

x = random.randint(0,5)

#Story Line/ Instructions 
fooditems = ("Terkey", "Piza", "Chps", "Weffles", "Sandwhich", "Samon", "Checken Breaasts","Fired Chikens","Chiken Wings", "Cups of Nodles", "Burgrs", "Firied Rice", "Eggs and Bacoon", "Chick Mcnuget", "Gummmie Bear", "Friies", "Doonut", "Porck", "Brockolii", "Froosted Flakes", "Aples", "Bananana", "Chickens Nodle Sup" )
notfooditems = ("Tidepods", "Airpods", "Durgs", "Steak", "Pillows", "Brick", "Candy", "Trash", "Chairs", "Sharpie", "Paper", "Cement", "Hair", "Yogurt", "Table", "Tape", "Yellow Snow", "Toilet Water", "Toilet Bowl", "Pen", "Cyanide", "Plastic", "Sweat")
print("Welcome to FoodNinjas");
print("FooodNinjas is a food HUNTING game.");
print("Long long ago, there was a tribe of humans who acheived the ?>:@ Potion.");
print("This potion allowed people to mutate into super sayan food items.");
print("Humans have been at war with the food tribe for a long time.");
print("Your job is to kill these food items and bring them home.")
print("Whenever you see a mutated food item being listed, please type it excatly in the input box inorder to annihilate the target.");
print("Remember, do not engage with the target if it is not a mutated food item. Your score will be set back to zero")
print("After you annihilated the mutated FOOD item, type in yes inorder to collect the item. ")
print("Next, after you have collected your item, you will see a number in a box. This is your score.")
print("For example: ");
print("Terkey: Terkey");
print("You have slain Terkey!")
print("Collect?: Yes")
print("You got Terkey [1]")
print("Remeber, whenever you fail to anniahate the target, you will die. It is KILL or BE KILLED mission!")
name = input("What is your name? ")
weapon = input("Aright " + name + ", chose your weapon (Fork, Knife, Spoon, Spatula, Chopsticks, Spork):")
if weapon =="Fork":
  print("Here is your Fork ")
if weapon == "Knife":
  print("Here is your Knife  ")
if weapon == "Spatula":
  print("Here is your Spatula ")
if weapon == "Chopsticks":
  print("Here is your Chopsticks ")
if weapon == "Spoon":
  print("Here is your Spoon ")
if weapon == "Spork":
  print("Here is your Spork ")
while weapon not in ("Fork", "Knife", "Spoon", "Spatula", "Chopsticks", "Spork"):
  weapon = input("Please input a valid weapon: ")
gamestart = input("Are you Ready? Do you want to start game; yes/no: ")
breaker = 1


# Mutated food items that can be killed for points 
def begin(x,score): 
    global breaker
    breaker = 1
    coin = random.choice([1, 2])
    #random picking system
    if coin == 1:
      game = input(fooditems[x] + ": " )
      while game == fooditems[x]:
        print("you have slain: " + fooditems[x]) 
        collect = input("Collect?:")
        if collect != "yes":
          print("You lost " + fooditems[x] + "["+ str(score) + "]")
          begin(x,score)
          break
        if collect == 'yes': 
          score += 1
          print("You got " + fooditems[x] + " [" + str(score) + "]")
          x = random.randint(0,22)
          begin(x,score)
          break
      if game != fooditems[x]:
        if breaker != 0:
          print("Your broke your " + weapon + " You died") 
          print("Your final score is " + "[" + str(score) + "]")
          breaker = 0


#non-mutated food and other items that can not be killed
    #random picking system
    if coin == 2: 
      x = random.randint(0,22)
      game = input(notfooditems[x] + ": " )
      while game != notfooditems[x]:
        print("Good Job! You did not kill " + notfooditems[x] + " ["+ str(score) + "]") 
        continuee = input("Continue?: ")
        while continuee != 'yes' and continuee != 'no':
          continuee = input('Please input yes or no: ')
        if continuee == "yes":
          x = random.randint(0,22)
          begin(x,score)
          break
        elif continuee == "no":
          print("Ok.... Bye")
          break
      if game == notfooditems[x]: 
        score = 0
        print("This is not a mutated food item, you killed a innocent creature" + " [" + str(score) + "]")
        continuee = input("Continue?: ")
        while continuee != 'yes' and continuee != 'no':
          continuee = input('Please input yes or no: ')
        if continuee == "yes":
          x = random.randint(0,22)
          begin(x,score)
        elif continuee == "no":
          print("Ok.... Bye")

#first game start     
while gamestart != 'yes' and gamestart != 'no':
  gamestart = input('please input yes or no: ')

if gamestart == "yes":
    print("Lets start soilder!!!")
    begin(random.randint(0,22),0)
elif gamestart == "no":
    print("Ok.... Bye")












  
