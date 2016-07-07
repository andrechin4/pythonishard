#from sys import exit

#Look around to find items in room
#Start off in a room where you can pick up, or ignore the items in the room(lighter, sword, crowbar)
#Look around to find ledge
#Next room has a pit with a ledge to walk across(choose to jump in ledge, walk the ledge)
#If you fall into the ledge, you will encounter a lion(lighter will scare lion, sword will kill lion, crowbar will kill you)
#After lion is defeated you can climb a path to the door
#If you climb the ledge you'll get to the other side, or fall in
#The next room has a rope.
#Climbing the rope will waste your time and have a possibility of you falling
#Looking around will make you see a hole in the wall with something to cut the rope
#If you have the lighter, you can burn the rope, sword will cut rope, crowbar will do nothing
#Person with crowbar will have to walk toward hole and use their crowbar, than walk toward the rope cut it.
#When the rope is cut, the player can go up the stairs that fall.



#Make a function for each room
#/Make a boolean for each tool
#Make a function for being near walls, and climbing the rope
lighter = False
crowbar = False
knife = False
axe = False
looked_around = False
choice = ""


def room1():
	print "You are in a poorly lit room with a door on the other side. "
	print "Do you proceed through the door, or look around?"
	choice = raw_input(">>> ")

	if "look" in choice:
		print "You find an axe, lighter and crowbar lying on the ground. You should take one."
		weapon()
	elif "open" in choice or "proceed" in choice or "continue" in choice or "walk" in choice:
		print "You decide to go through the door."
		room2()
	else:
		print "Try a different action"
		room1()

def room2():
	print "This room has big hole in the floor. What do you do?"

	choice = raw_input(">>> ")

	if "jump" in choice:
		print "You jump, and fall into the pit."
		lionroom()
	elif "look" in choice:
		print "You find a ledge leading toward the door."
		room2()
	elif "ledge" in choice:
		print "You cross the ledge enter the room behind the door."
		room3()
	else:
		print "I don't know what you were trying to do, but it caused you to fall into the pit."
		lionroom()

def lionroom():
	print """You hit the ground. The fall wasn't pleasent but you survive. The room is dark and cold. As your standing up, you hear growling and two eyes emerge from the darkness. What do you do?"""

	choice = raw_input(">>> ")

	if "run" in choice:
		print "You run for your life, but run into a wall, unconscience. RIP"
	elif "roar" in choice:
		print "The lion growls in approval. Torches leading to rocks light. "
		climb_rocks()
	elif "axe" in choice:
		if axe == True:
			print "You take out your axe and swing at the enemy."
			print "The axe hits and you hear whimpering. The axe"
			print " falls to the floor. You bend down and pick it"
			print " up. You search the walls of the dark room and"
			print " discover rocks that you use to get to the door"
			climb_rocks()
		else:
			print "You don't have an axe!"
			lionroom()

	elif "lighter" is choice:
		if lighter == True:
			print "You light your ligher. The creature is revealed to be a lion."
			print "He is now in a corner cowering in fear. You look in the distance"
			print "And see rocks you can climb up to get to the door."
			climb_rocks()
		else: 
			print "You don't have a lighter!"
			lionroom()
	elif "crowbar" in choice:
		if crowbar == True:
			print "You take out your crowbar and start swinging. The growling gets "
			print "louder. The animal swipes at you. RIP"
		else:
			print "You don't have a crowbar!"
			lionroom()




def climb_rocks():

	choice = raw_input(">>> ")

	if "climb" in choice:
		print "You climb the rocks, open the door, and enter the next room."
		room3()
	else:
		print "Whatcha doing? Shouldn't you get to climbing those rocks!?"
		print "It doesn't seem safe, but it's your only option!"

		climb_rocks()





def room3():
	print "This room has nothing but a rope leading from the ceiling to the "
	print "ground. The rope seems to be supporting something."

	choice = raw_input(">>> ")

	if looked_around == False:
		if "look" in choice:
			global looked_around
			print "You look around the room and find a hole in the wall "
			print "that may contain something useful."
			looked_around = True

			if crowbar == True:
				reach_for_item()
			else:
				room3()

		elif "crowbar" in choice:
			print "You hit the rope with the crowbar. The rope wiggles "
			print "a little, doesn't do much against the rope. You "
			print "should look for something sharper."
			room3()
		elif "axe" in choice:
			print "You hit the rope with the axe. The rope snaps and "
			print "stairs drop leading to outside. "
		elif "lighter" in choice or "burn" in choice:
			print "You use your lighter on the rope. The rope burns "
			print "and snaps. Stairs drop leading to outside. "
		else:
			print "Try a different action."
			room3()

	else:
		if "crowbar" in choice:
			print "You should use the knife instead of the crowbar now."
			room3()
		elif "axe" in choice:
			print "You hit the rope with the axe. The rope snaps and "
			print "stairs drop leading to outside. "
		elif "knife" in choice:
			print "You use the knife on the rope, the rope snaps and "
			print " stairs drop leading to outside."
		elif "lighter" in choice or "burn" in choice: 
			print "You use your lighter on the rope. The rope burns "
			print "and snaps. Stairs drop leading to outside. "
		else:
			print "Try a different action."
			room3()


def reach_for_item():
	print "You walk toward the wall and try to reach for the "
	print "item that's in the wall but find that your arms are "
	print "too short."
	choice = raw_input(">>> ")

	if "crowbar" in choice or "reach" in choice or "grab" in choice:
		print "You use your crowbar to reach for the item in the "
		print "wall. The item turns out to be a knife."
		room3()
	else: 
		print "You should use your crowbar to reach the item!"
		reach_for_item()




def weapon():

	choice = raw_input(">>> ")

	if "crowbar" in choice:
		global crowbar
		print "You pick up the crowbar,"
		print "and continue to the next room."
		crowbar = True
		room2()
	elif "axe" in choice:
		global axe
		print "You pick up the axe,"
		print "and continue to the next room."
		axe = True
		room2()
	elif "lighter" in choice:
		global lighter
		print "You pick up the lighter,"
		print "and continue to the next room."
		lighter = True
		room2()
	else:
		print "Try a different action."
		weapon()

room1()


