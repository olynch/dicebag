#!/usr/bin/env python3
import random, pickle, sys, cmd

class Dice:
	""" Contains x dice with n sides, or a plain modifier """
	def __init__(self, dice):
		""" Either takes in a string with a modifier, such as +4, or a dice description, such as 2d8 """
		if dice[0] in ("+", "-"):
			self.mod = int(dice)
			self.num, self.sides = None, None
		else:
			self.num, self.sides = map(int, dice.split("d"))
			self.mod = None

	def roll(self):
		""" rolls the dice, or just returns the modifier """
		if self.mod != None:
			return self.mod
		else:
			return sum([random.randrange(1, self.sides + 1) for x in range(self.num)])
	
	def __str__(self):
		if self.mod != None:
			if self.mod < 0:
				return "-" + str(self.mod)
			else:
				return "+" + str(self.mod)
		return "+" + str(self.num) + "d" + str(self.sides)

class Roll:
	""" Contains a set of dice and modifiers, provides a roll method to roll all its dice """
	def __init__(self, desc_str):
		desc = desc_str.split(" ")
		self.dice_list = list(map(Dice, desc))

	def roll(self):
		return sum([x.roll() for x in self.dice_list])

	def __str__(self):
		return "".join(list(map(str, self.dice_list)))

def parse(args):
	return args.split(" ")

class DiceInterpreter(cmd.Cmd):
	""" The command line interface to the Roll class
	Provides a dictionary that users can set and delete keys in, each key is a Roll
	that users can roll. Users can also just specify a roll description on the command line, like 2d6 +10
	Also provides a facility for saving the dictionary and opening it up again."""
	prompt = "dice> "
	DICE_PREFIX = ("+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
	def preloop(self):
		""" Initializes the rolls dictionary, possibly with a file passed as an argument """
		self.rolls = {}
		if len(sys.argv) > 1:
			self.pickled_rolls = sys.argv[1]
			self.rolls = pickle.load(open(self.pickled_rolls, 'rb'))
			self.prompt = self.pickled_rolls + "> "
		else:
			self.pickled_rolls = None

	def do_open(self, args):
		""" Read a file into the rolls dictionary """
		args = parse(args)
		self.rolls = pickle.load(open(args[0], 'rb'))
	
	def do_list(self, args):
		""" List the contents of the rolls dictionary """
		args = parse(args)
		print(self.rolls)
	
	def do_new(self, args):
		""" Add a new Roll to the dictionary 
		The first argument is the name of the roll, the rest are the specifications. """
		args = parse(args)
		self.rolls[args[0]] = Roll(" ".join(args[1:]))
	
	def do_del(self, args):
		""" Deletes a roll from the dictionary
		The first argument is the name of the roll """
		args = parse(args)
		del self.rolls[args[0]]
	
	def default(self, line):
		self.do_roll(line)
	
	def do_roll(self, args):
		""" Roll the specified rolls """
		args = parse(args)
		acc = 0
		acc_str = ""
		for dice in args:
			if dice in self.rolls.keys():
				acc_str += " " + str(self.rolls[dice])
				acc += self.rolls[dice].roll()
			elif dice[0] in self.DICE_PREFIX:
				temp_dice = Dice(dice)
				acc_str += " " + str(temp_dice)
				acc += temp_dice.roll()
			else:
				print("A Roll of that name could not be found")
				return
		print(acc_str)
		print(acc)
	
	def do_exit(self, args):
		""" Save the rolls dictionary, if desired, and then exit. """
		return True
	
	def postloop(self):
		if self.pickled_rolls == None:
			will_save = input("Do you wish to save (y/n): ")
			if will_save != "n":
				self.pickled_rolls = input("Where do you wish to save to: ")
				pickle.dump(self.rolls, open(str(self.pickled_rolls), 'wb'))
		else:
			pickle.dump(self.rolls, open(str(self.pickled_rolls), 'wb'))

if __name__ == "__main__":
	DiceInterpreter().cmdloop()
