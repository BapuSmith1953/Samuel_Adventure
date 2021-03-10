
####  NEXT TO DO:
    #### add "found" flags for artifacts, "done" flags for deeds, wahing hands, wearing mask etc.
    ##### error-test "input" statements. Error-trap?
    #### When "take" or "drop" or "put" an "artifact" update the data for that artifact:  art.where =
    #### Make sure "look" statement "sees" artifacts with that art.where ==  plnm
    #### make sure loc.thingshere and art.where don't duplicate
    #### make sure you update "newplace" and "return newplace" everywhere.
    #### work on "use camera" action (scratch file)
    #### work on displaying images (scratch file)?
    #### load rover routine
    #### Launchpad
    #### repair rocket
    #### rocketlaunch
    #### inspace
    #### spacewalk
    #### planet landing
    #### rover on surface
    #### swamp
    #### prairie
    #### robotmom house
    #### planetlaunch
    #### reentry alarm
    #### parachute
    #### chewandswallow
    #### city hall
    #### build raft  (bread, peanut butter, rudder, sail
    #### boating goods store
    #### ocean
    #### super Spot
    #### back home

#####Initialize Classes, functions, lists, action dictionary, and files#####
    ####### Consider writing files via separate routine?#######
##### For each new location:  add to places list; add "placeoptions"; add reference in options{}dictionary; add place text; add class data for that loc including number, names, look, thinkgshere etc.; add that loc to loop reading in the list to "Trylist"
global plnm,listofthings
items = []
listofthings = ["grabber","camera","excavator","flashlight","flowers","net","rover","shovel","mask", "walking stick", "socket wrench", "spacesuit", "magnet", "parachute", "raft", "bread", "peanut butter", "floating vest", "rudder", "flowers", "gold nugget", "bigger gold nugget", "even bigger gold nugget","plant samples", "soil sample", "airfish" ]
places = ["kitchen","backdeck","garden","driveway","sidewalk","construction_site","outside_tunnel","dark_tunnel","mine","spaceport","bottom_of_mine","loading_rover","launchpad","rocket_launch","outer_space","spacewalk","landing_planet","roverout","planet surface","swamp","robotmom","roverback","launchhome","reentry","parachute","chewandswallow","ocean_storm","backhome"]
plnm = 1

plnm = 0
place = places[plnm]
kitchenstring = "You are standing in the kitchen.\nThere is a round wooden table with chairs around it.\nThere is something on the table.\nNot far from the table is the kitchen sink."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(kitchenstring)
myfile.close()

plnm = 1
place = places[plnm]
deckstring = "You are standing on the back deck at Yaya’s house.\nIt is a warm sunny day, so there is no wood or fire in the fire pit.\nYou see on the table several objects.\nThe flowers are blooming in the garden.\nThere are stairs going down into the garden.\nYou see an open gate leading to the front side of the house."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(deckstring)
myfile.close()

plnm = 2
place = places[plnm]
gardenstring = "You are walking through Yaya’s Garden.\nYou notice a pretty butterfly with blue wings is flying near the phlox in the garden.\nYou see a gate standing open at the back of the yard, and another gate leading to the front yard.\nA grabber is lying on the ground near the gate.\nAn owl is watching you from the trees nearby.\nThere is a swing back by the fence and nearby there is a pile of sticks."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(gardenstring)
myfile.close()

plnm = 3
place = places[plnm]
drivewaystring = "There is one car in the driveway but the area around the basketball hoop is clear.\nYou hear the rumble of heavy motors in the distance and remember there is a construction site down the street."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(drivewaystring)
myfile.close()

plnm = 4
place = places[plnm]
sidewalkstring = "You walk down the sidewalk.\nYou have walked back and forth to the construction site before, and you pass familiar houses and streets marked with No Outlet signs.\nThere are always interesting things to see as you walk along.\nYou notice Japanese Maples in some yards."
fileToGet = place + ".txt"
myfile = open(fileToGet, "w")
myfile.write(sidewalkstring)
myfile.close()

plnm = 5
place = places[plnm]
construction_sitestring = "You hear the rumbling of heavy trucks and the shouts of construction workers.\nSoon you recognize the construction site where a new house has been built.\nThe workers are all leaving for the day.\nYou are curious and want to see the heavy equipment up close, especially the big yellow excavator.\nSuddenly, you see the little yellow robot. He runs into a hole down by the house.\nYou walk down onto the construction site to get a better look at that hole, but the hole is dark inside and too small for you to climb into."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(construction_sitestring)
myfile.close()

plnm = 6
place = places[plnm]
outside_tunnelstring = "You are standing on the construction site, outside the tunnel. It looks dark inside."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(outside_tunnelstring)
myfile.close()

plnm = 7
place = places[plnm]
dark_tunnelstring = "As you walk farther into the tunnel, you see dim lights up ahead, along the side of the path.\nThese lights guide you deeper into the tunnel.\nFor a long time  you walk, not hearing any sound except the drip-drip-drip of water.\nThen you see a mine shaft going down deep underground.\nThere is an old sign by the mine shaft."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(dark_tunnelstring)
myfile.close()

plnm = 8
place = places[plnm]
minestring = "You climb down deeper and deeper into the mine, until you reach a floor with a tunnel leading away.\nAll of a sudden you hear a loud crack and the sound of rocks breaking and falling up above you!\nYou quickly jump out of the way, just in time, as a huge pile of rocks falls down behind you.\nYou cannot go back up the mine shaft\nYou have no choice but to follow the tunnel and see where it goes."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(minestring)
myfile.close()

plnm = 9
place = places[plnm]
spaceportstring = "\nYou see the little yellow robot talking to Buzz Lightyear, and behind them you see what looks like a spaceport."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(spaceportstring)
myfile.close()

plnm = 10
place = places[plnm]
bottom_of_minestring = "You have arrived at the bottom of the mineshaft.\nA large pile of rocks blocks your way back to the top.\nAn underground tunnel leads on into the mine."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(bottom_of_minestring)
myfile.close()

plnm = 11
place = places[plnm]
loading_roverstring = "Buzz Lightyear and the Robot begin loading up the Rover with supplies for the space trip.\nYou see them putting in food, water, extra batteries, and other items."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(loading_roverstring)
myfile.close()

plnm = 12
place = places[plnm]
launchpadstring = "Standing by the launchpad, the rocket looks enormous as it towers above you.\nSome engineers are busy with last minute repairs.\nYou hear one of the engineers say, 'I sure wish somebody had a socket wrench.\n I need to tighten up this bolt or the stabilizer could come off!'"
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(launchpadstring)
myfile.close()

plnm = 13
place = places[plnm]
rocket_launchstring = "xxxxxxxx."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(rocket_launchstring)
myfile.close()

plnm = 14
place = places[plnm]
outer_spacestring = "xxxxxxxx."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(outer_spacestring)
myfile.close()

plnm = 15
place = places[plnm]
space_walkstring = "xxxxxxxx."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(space_walkstring)
myfile.close()

plnm = 16
place = places[plnm]
landing_planetstring = "xxxxxxx."
fileToGet = place+".txt"
myfile = open(fileToGet, "w")
myfile.write(landing_planetstring)
myfile.close()

#plnm = 15
#place = places[plnm]
#gardenstring = "."
#fileToGet = place+".txt"
#myfile = open(fileToGet, "w")
#myfile.write(gardenstring)
#myfile.close()
#plnm = 15
#place = places[plnm]
#gardenstring = "."
#fileToGet = place+".txt"
#myfile = open(fileToGet, "w")
#myfile.write(gardenstring)
#myfile.close()
#plnm = 15
#place = places[plnm]
#gardenstring = "."
#fileToGet = place+".txt"
#myfile = open(fileToGet, "w")
#myfile.write(gardenstring)
#myfile.close()
#plnm = 15
#place = places[plnm]
#gardenstring = "."
#fileToGet = place+".txt"
#myfile = open(fileToGet, "w")
#myfile.write(gardenstring)
#myfile.close()
#plnm = 15
#place = places[plnm]
#gardenstring = "."
#fileToGet = place+".txt"
#myfile = open(fileToGet, "w")
#myfile.write(gardenstring)
#myfile.close()
#plnm = 15
#place = places[plnm]
#gardenstring = "."
#fileToGet = place+".txt"
#myfile = open(fileToGet, "w")
#myfile.write(gardenstring)
#myfile.close()
#plnm = 15
#place = places[plnm]
#gardenstring = "."
#fileToGet = place+".txt"
#myfile = open(fileToGet, "w")
#myfile.write(gardenstring)
#myfile.close()
#plnm = 15
#place = places[plnm]
#gardenstring = "."
#fileToGet = place+".txt"
#myfile = open(fileToGet, "w")
#myfile.write(gardenstring)
#myfile.close()

###
# ####Initialize functions inventory; options for each location's set of possible actions
#def getchoice():
 #   while True:
  #      number = input("Enter a number:\n")
   #     if number.isdigit():
    #        return number


###Initialize picture {dictionary of pics}
pictures = {0: "Deer",
           1: "Elmo",
           2: "Fawn",
           3: "Frog",
           4: "Launch Pad",
           5: "Lost Galaxy",
           6: "Monarch Butterfly",
           7: "Owl",
           8: "Robot Mom",
           9: "Rover",
           10: "Spacewalk",
           11: "Surprise Lily",
           12: "Weasel"}

import time
import Image

import json

##   Save Game Routine
##save items list, veh list elements needed, loc list elements needed, artifact list elements needed, deeds list elements needed.
def savegame():
    print("We reached savegame")
    savelist = []
    saveloclist = []
    savevehlist = []
    saveartlist = []
    savedeedlist = []
    savepiclist = []
    for loc in trylist:
        saveloclist.append(loc.thingshere)
    for veh in vehlist:
        savevehlist.append(veh.where)
        savevehlist.append(veh.whowith)
        savevehlist.append(veh.thingshere)
    for art in artlist:
        saveartlist.append(art.where)
        saveartlist.append(art.found)
        saveartlist.append(art.points)
    for deed in deedlist:
        savedeedlist.append(deed.done)
        savedeedlist.append(deed.points)
    for pic in piclist:
        savepiclist.append(pic.taken)
        savepiclist.append(pic.points)
    savelist.append(saveloclist)
    savelist.append(savevehlist)
    savelist.append(saveartlist)
    savelist.append(savedeedlist)
    savelist.append(savepiclist)
    savelist.append(items)
    savelist.append(plnm)
    #  input from user for name of saved file
    print("Enter a number for this saved game 1 to 5")
    answer = input()
    gamename = "saved_game_"+answer+".txt"
    # open output file for writing
    with open(gamename, 'w') as filehandle:
        json.dump(savelist, filehandle)
    print("Game saved as ", gamename)
    return gamename

def restoregame(plnm,items):
    #  Get name of saved game file
    answer = input(
        "What game to you want to restore? Enter a number: \n 1. saved_game_1\n 2. saved_game_2\n 3. saved_game_3\n 4. saved_game_4\n 5. saved_game_5")
    gamename = "saved_game_"+answer+".txt"

    savelist = []
    saveloclist = []
    savevehlist = []
    saveartlist = []
    savedeedlist = []
    savepiclist = []
    with open(gamename, 'r') as filehandle:
        savelist = json.load(filehandle)
    saveloclist = savelist[0]
    savevehlist = savelist[1]
    saveartlist = savelist[2]
    savedeedlist = savelist[3]
    savepiclist = savelist[4]
    itemslist = savelist[5]
    plnm = savelist[6]
    itemslist.append(plnm)

    for i in range(len(vehlist)):
        for veh in vehlist:
            if veh.num == i:
                j = i * 3
                k=j+1
                l=k+1
                veh.where = savevehlist[j]
                veh.whowith = savevehlist[k]
                veh.thingshere = savevehlist[l]

    for i in range(len(deedlist)):
        for deed in deedlist:
            if deed.num == i:
                j = i * 2
                k=j+1
                deed.done = savedeedlist[j]
                deed.points = savedeedlist[k]

    for i in range(len(trylist)):
        for loc in trylist:
            if loc.num == i:
                loc.thingshere = saveloclist[i]

    for i in range(len(artlist)):
        for art in artlist:
            if art.num == i:
                j = i * 3
                k=j+1
                l=k+1
                art.where = saveartlist[j]
                art.found = saveartlist[k]
                art.points = saveartlist[l]

    for i in range(len(piclist)):
        for pic in piclist:
            if pic.num == i:
                j = i * 2
                k=j+1
                pic.taken = savepiclist[j]
                pic.points = savepiclist[k]

    return itemslist

def specialactions(action,items,plnm):
    if action == "look":
        if plnm == 10:
            if not ("flashlight" in items):
                print("You can't see much without your flashlight.")
            else:
                for loc in trylist:
                    if loc.num == plnm:
                        loc.descriptionprint()
                        loc.printlooktxt()
                        if plnm == 4:
                            deed4.done = 1
                        print("You also see:")
                        for i in loc.thingshere:
                            print(i)
                for veh in vehlist:
                    if veh.where == plnm:
                        for i in veh.thingshere:
                            print (i, ", in the", veh.name)
            newplace = plnm
            return newplace
        else:
            for loc in trylist:
                if loc.num == plnm:
                    loc.descriptionprint()
                    loc.printlooktxt()
                    if plnm == 4:
                        deed4.done = 1
                    print ("You also see:")
                    for i in loc.thingshere:
                        print (i)
                    for art in artlist:
                        if art.where == plnm:
                            print (art.name)
                    for veh in vehlist:
                        if veh.where == plnm:
                            for i in veh.thingshere:
                                print (i, ", in the", veh.name)

        newplace = plnm
        return newplace
    elif action == "take":
####In “TAKE” routine: check # of items in list – can only carry 5? Spacesuit, mask and parachute don’t count while wearing/using.
        max = 5
        for i in range(len(items)):
            if items[i] == "spacesuit":
                max += 1
            if items[i] == "mask":
                max += 1
            if items[i] == "parachute":
                max += 1
        if len(items) >= max:
            print("You can't carry anything else. You need to drop something.")
        else:
            print("What do you want to take?")
###  NEED TO DO TWO THINGS HERE: 1.  IF THE OBJECT IS IN LOC.THINGS HERE, ADD TAKEN OBJECT TO ITEMS LIST; 2. REMOVE ITEM FROM LOC.THINGSHERE LIST
    ## ADD TAKEN OBJECT TO ITEMS LIST:
            flag = 0
            for loc in trylist:
                if loc.num == plnm:
                    length = len(loc.thingshere)
                    for i in range(length):
                        print(">>>", loc.thingshere[i])
                    grabbed = input("Type name of item.\n").lower()
                    if grabbed == "excavator" or grabbed == "rover" or grabbed == "mine_cart" or grabbed == "rock" or grabbed == "a big hole":
                        print("You can't pick up the " + grabbed + "! It is too heavy!")
                        newplace = plnm
                        return newplace
            for loc in trylist:
                if loc.num == plnm:
                    for veh in vehlist:
                        if (veh.where == plnm):
                            if grabbed in veh.thingshere:
                                items.append(grabbed)
                                veh.thingshere.remove(grabbed)
                                print("\n>>>"+items[-1], "Taken")
                                flag = 1
                    if grabbed in loc.thingshere:
                        items.append(grabbed)
                        loc.thingshere.remove(grabbed)
                        print("\n>>>"+items[-1], "Taken")
                        flag = 1
                        if grabbed == "mask":
                            plnm = usemask(items, plnm)
                        if grabbed == "sticks":
                            plnm = usesticks(items, plnm)
                        if loc.num == 5:
                            loc6.thingshere = loc5.thingshere
                        if loc.num == 6:
                            loc5.thingshere = loc6.thingshere
            if flag == 0:
                print("\nThere is no " + grabbed + " here to take.\n")
        newplace=plnm
        return newplace

    elif action == "drop":
        if len(items) < 1:
            print ("You are not holding anything!")
        else:
            print("You are holding these things:")
            inventory(items)
            flag = 0
            print("What do you want to drop?\n")
            putdown = input("Type name of item.\n")
            putdown = putdown.lower()
            droplist = []
            if putdown == "all":
                flag = 1
                for i in items:
                    droplist.append(i)
                print ("You have dropped these:", droplist)
                for j in droplist:
                    items.remove(j)
            else:
                for i in range(len(items)):
                    if putdown == items[i].lower():
                        flag = 1
                        print("You have dropped the ", items[i])
                        droplist.append(items[i])
                        if putdown == "glass of milk":
                            print("SPLAT!! Good thing it had a lid on it!")
                        if putdown == "sticks" and plnm == 1:
                            deed3.done = 1
            if flag == 1:
                for plc in trylist:
                    if plc.num == plnm:
                        for j in range(len(droplist)):
                            thing = droplist[j]
                            plc.thingshere.append(thing)
                            if plc.num == 5:
                                loc6.thingshere = []
                                loc6.thingshere = plc.thingshere
                            if plc.num == 6:
                                loc5.thingshere = []
                                loc5.thingshere = plc.thingshere
                            if thing in items:
                                items.remove(thing)
            else:
                print("You are not holding that item.")
        newplace = plnm
        return newplace
######
###### FOR PUT ROUTINE:
####Get vehicles at location
####identify which vehicle he wants to put something int
####identify what he wants to put in that vehicle
####make sure he has that itme
###if so, take it out of items list; put it into veh.thingshere list
###when leaves that location, take out of loc.thingshere list and add to new loc.thingshere list.

    elif action == "put":
        print("You are holding these things:")
        inventory(items)
        flag = 0
        thing = input("What item do you want to put in the vehicle?\n")
        cart = input("Type name of vehicle you want to put it in.\n")
        for veh in vehlist:
            if (veh.name == cart) and (veh.where == plnm):
                putdown = thing
                for i in range(len(items)):
                    if putdown == items[i]:
                        flag = 1
                        print("You have put the " + items[i] + " in the " + cart)
        if flag == 1:
            print("You see the following items here:")
            for veh in vehlist:
                if veh.name == cart:
                    veh.thingshere.append(putdown)
                    for i in veh.thingshere:
                        print (i, "in the", veh.name)
            for loc in trylist:
                if loc.num == plnm:
                    for i in loc.thingshere:
                        print (i)
            items.remove(putdown)
        else:
            print("You can't put the " + thing  +" in the " + cart + ".")
        newplace = plnm
        return newplace

    elif action == "use":
        ### ?What does he want to use?
        ### does he have it / is it here?
        ###get index for item from listofthings
        ###use index idx to access dictionary usestuff[idx](items)
        ###def a handler for each item in listofthings covering only places where it can be used, else print "can't use that here". call useexcavator routine via holeisbig=useexcavator.
        ### handler  is there something to use? if so, use what? get input, use item to?
        print("You are holding these things:")
        inventory(items)
        flag = 0
        print("What do you want to use?")
        thing = input("Type name of item.\n")
        thing = thing.lower()
        if (thing in items):
            for i in range(len(listofthings)):
                if thing == listofthings[i].lower():
                    idx = int(i)
                    newplace = usestuff[idx](items, plnm)
                    return newplace

        elif thing == "excavator":
            newplace = useexcavator(items, plnm)
            return newplace

        elif thing == "sink":
            newplace = usesink(items, plnm)
            return newplace

        elif thing == "sticks":
            newplace = usesticks(items, plnm)
            return newplace


        elif thing == "raft":
            newplace = useraft(items, plnm)
            return newplace

        elif thing == "rover":
            newplace = userover(items, plnm)
            return newplace

        else:
            print("You aren't holding the "+thing)
            newplace = plnm
            return newplace

    elif action == "hint":
        print("You can look around to see if there is anything special to see by typing 'look.'\nIf you want to see a list of items to take or drop by writing 'take' or 'drop.'\nYou can type 'put' to put things in vehicles.\nYou can get a list of things you can use by typing 'use.'\nSome things that are too big to pick up you can still use.\nSome things that you wear (space suit, mask, parachute) you be wearing as soon as you 'take' them.\nYou can only carry 5 things at a time, not counting things you are wearing.\nBe careful not to leave behind something important that you might need later on!\n")
        newplace=plnm
        return newplace
        ### handler for hints at this location?

    elif action == "inv":
        print ("You are holding these things:")
        inventory(items)
        newplace=plnm
        return newplace

    else:
        print ("I don't understand that.")
        newplace = plnm
        return newplace

###def a handler for each item in listofthings covering only places where it can be used, else print "can't use that here". call useexcavator routine via holeisbig=useexcavator.
### handler  is there something to use? if so, use what? get input, use item to?


def useexcavator(items, plnm):
    if not (plnm == 5):
        print ("You can't use that here.")
        newplace = plnm
        return newplace
    else:
        if not (len(items) <= 1):
            print ("You can only take one thing with you if you want to climb into the excavator.")
            newplace = 5
            return newplace
        else:
            print("You climb into the seat of the excavator and drive over toward the tunnel.\nJust then, a big yellow truck drives in front of you!\nYou slam on the brakes and slide to a stop.\nA furry red head pops out of the truck window.\n'Hey! Watch out where you are going!' says Elmo.\n‘Elmo wants to sing a song! La la la LA la la laaaa!’\nThe truck continues on, with Elmo singing, ‘I’m driving in my truck! I’m driving in my truck!’\nWhat do you want to do?\n1. Drive the excavator over to the tunnel\n2. Take a picture of Elmo")
            answer = input()
            if answer.isnumeric():
                choice = int(answer)
                while choice > 2:
                    choice = int(input("Choose one of the numbers."))
                if choice == 2:
                    if "camera" in items:
                        print("You quickly aim your camera at the yellow truck and snap a picture.")
                        newplace = usecamera(items, plnm)
                    else:
                        print("You are not holding the camera.")
            print("You carefully drive the excavator over to the tunnel and start to dig.\n Pretty soon, you have made the entrance much larger. Should you:\n1. Drive into the tunnel.\n2. Climb down so you can walk into the tunnel.\n3. Keep digging.")
            loc6.thingshere.append("a big hole")
            nxtanswer = input()
            if nxtanswer.isnumeric():
                choice = int(nxtanswer)
                while choice > 3:
                    choice = int(input("Choose one of the numbers."))
                if choice == 1:
                    print ("You can't do that. The excavator is much too large to fit into the tunnel.")
                    newplace = 6
                    return newplace
                elif choice == 2:
                    print ("You climb down out of the excavator and look at the hole. It is now big enough for you to walk in.")
                    newplace = 6
                    return newplace
                elif choice == 3:
                    print ("You dig a little more and then the hole looks big enough to walk into.")
                    newplace = 6
                    return newplace
            if not (nxtanswer.isnumeric()):
                if nxtanswer == "quit":
                    endgame = 1000
                    return endgame
                else:
                    specialactions(nxtanswer, items, plnm )
                    newplace=6
                    return newplace

def useflashlight(items,plnm):
    print("You have turned on the flashlight. You can see better now.")
    newplace = plnm
    return newplace

def usemask(items,plnm):
    print("You put on your mask to stay safe. Good job!")
    deed2.done = 1
    newplace = plnm
    return newplace

def usesink(items,plnm):
    print("You carefully wash your hands with soap and water.\nGood job washing your hands in the sink!")
    if "empty glass" in loc0.thingshere:
        print("It is better to wash your hands BEFORE you eat.")
    else: deed0.points = 4
    deed0.done = 1
    newplace = plnm
    return newplace

def usesticks(items, plnm):
    print("You can carry the sticks back up to the deck for Bapu to use in the firepit. Thanks!")
    plnm = 1
    newplace = plnm
    return newplace

def usesocket_wrench(items,plnm):
    if not (plnm == 13) or (plnm == 15):
        print ("There is nothing to use that for here.")
    if plnm == 13:
        print("You remember there is a socket wrench in the Rover.\n'I have the right tool!' you say. 'I can help fix it!'\nYou grab the socket wrench and go to work, fastening down the loose stabilizer.")
        deed7.done = 1
    if plnm == 15:
        print ("With your socket wrench ready, you go to work on the repair.\n The work is difficult as you drift around in space. Then you see a new problem.\n 'Hey, Buzz!' you say. 'The reentry rocket was damaged by that space rock!\n 'I don't think I can fix it.'\n 'OK, Samuel,' says Buzz. 'You better come back inside before you run out of air.'")
        deed8.done = 1
    newplace = plnm
    return newplace

def usespacesuit(items,plnm):
    print("You put on your spacesuit and carefully check that all the connections are sealed tight.\nYou remember to turn your oxygen supply on for air to breathe.\n'Now I am ready for space!' you say. 'What tools should I take?'")
    newplace = plnm
    return newplace


def usemagnet(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace


def usenet(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace

def userover(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace

def useshovel(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace

def usegrabber(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace

def usewalking_stick(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace


def useparachute(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace

def useraft(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace

def usebread(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace


def usepeanut_butter(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace


def usefloating_vest(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace

def userudder(items,plnm):
    print("Need handler for using item")
    newplace = plnm
    return newplace

def usecamera(items,plnm):
    flag = 0
    for pic in piclist:
        if pic.where == plnm:
            print (pic.name)
            flag = 1
    if flag == 1:
        answer = input ("What do you want to take a picture of?")
        for pic in piclist:
            if ((pic.name == answer) or (pic.name.lower == answer.lower)):
                photo = takepicture(pic.name, plnm)
                pic.taken = 1
    else:
        print("There is nothing to take a picture of here.")
    newplace = plnm
    return newplace

def takepicture(chosenpic, plnm):
    fl = "0"
    while fl == "0":
        im = Image.open(r"/Users/lauriesmith/Desktop/AdventureImages/"+chosenpic+".png")
        im.show()
        fl = "1"
    input("Press Return to continue")
    time.sleep(2)
    im.close()
    newplace = plnm
    return newplace

def kitchenoptions(items):
    print("1. Eat PBJ"," 2. Drink milk ","3. Take your plate and glass to the sink","4. Go out on deck", "5. Put flowers in vase on table.")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 5:
            choice = int(input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            print ("You ate the PBJ. Yum! That was tasty!\n\n")
            if "pbj" in loc0.thingshere:
                loc0.thingshere.remove("pbj")
            if "PBJ" in loc0.thingshere:
                loc0.thingshere.remove("PBJ")
            if "pbj" in items:
                items.remove("pbj")
            if "PBJ" in items:
                items.remove("PBJ")
            loc0.thingshere.append("empty plate")
            newplace = 0
            return newplace
        elif choice == 2:
            print ("You drank the milk. You feel better now.\n\n")
            if "glass of milk" in loc0.thingshere:
                loc0.thingshere.remove("glass of milk")
            if "glass of milk" in items:
                items.remove("glass of milk")
            if "Glass of milk" in items:
                items.remove("Glass of milk")
            loc0.thingshere.append("empty glass")
            newplace = 0
            return newplace
        elif choice == 3:
            print ("Great job taking your plate and glass to the sink!")
            deed1.done = 1
            loc0.thingshere.remove("empty glass")
            loc0.thingshere.remove("empty plate")
            newplace = 0
            return newplace
        ###Do points for this
        elif choice == 5:
            if "flowers" in items:
                print ("Great job picking flowers for your Mother!")
                deed11.done = 1
                items.remove("flowers")
                loc0.thingshere.append("flowers")
            else:
                print ("You don't have any flowers.")
            newplace = 0
            return newplace
        else:
            newplace = 1
            return newplace
    if not (answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer, items, plnm)
            newplace = 0
            return newplace

def backdeckoptions(items):
    print("\nWhat do you want to do? Type a command or enter a number:")
    print("1. Go down into garden","2. Go inside for a snack", "3. Stay on the deck.")
    answer = input()
    if answer.isnumeric():
        choice=int(answer)
        while choice > 3:
            choice = int(input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            print("You walk down the stairs into the garden\n\n")
            newplace = 2
            return newplace
        elif choice == 2:
            print("You go into the house to find something to eat.\n\n")
            newplace = 0
            return newplace
        elif choice == 3:
            newplace = 1
            return newplace
    if not (answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer,items,plnm)
            newplace = 1
            return newplace

def gardenoptions(items):
    print("\nWhat do you want to do? Type a command or enter a number:")
    print("1. Go back up on the deck","2. Go out the gate", "3. Sit in the swing", "4. Chase the butterfly", "5. Talk to the owl", "6. Take pictures with the camera")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 6:
            choice = (input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            print("You walk back up on the deck.")
            newplace = 1
            return newplace
        elif choice == 2:
            print("You head out the gate toward the front side of the house.\nAs you go through the gate, you hear a small voice say, 'WAIT! This soup will not taste good. It has no stories in it.'\nYou also see a basketball hoop and a ball.")
            newplace = 3
            return newplace
        elif choice == 3:
            print("You sit in swing and go back and forth. Isn't it nice!\nYou are enjoying the cool shade and the sound of the chimes.\nSuddenly, you hear something go 'Beebop! Beebop!'\nYou see a little yellow robot run out of the house and through the gate.\n")
            newplace = 2
            return newplace
        elif choice == 4:
            if "net" not in items:
                print("You chase the butterfly around the garden.  You need something to catch it with.\n")
            else:
                print("You chase the butterfly around the garden.\nWith a quick swipe of your net you catch the butterfly!\nAs look look closely at the butterfly, a tiny voice says, 'Hey! Why don't you pick on someone your own size!'\nThe butterfly flaps twice and quickly flies away.")
            newplace = 2
            return newplace
        elif choice == 5:
            print("You talk to the owl. He turns his head around and peers at you.  He says, 'Who? Who? Who?'\n1")
            newplace = 2
            return newplace
        elif choice == 6:
            if "camera" not in items:
                print ("You didn't bring a camera with you.")
            else:
                newplace = usecamera(items, plnm)
            newplace = 2
            return newplace
    if not (answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer,items,plnm)
            newplace = 2
            return newplace

def drivewayoptions(items):
    print("\nWhat do you want to do? Type a command or enter a number:")
    print ("1. Play basketball", "2. Go back to the garden", "3. Walk to the construction site")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 3:
            choice = (input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            if len(items) > 1:
                print("You can't play basketball holding so many things.")
            elif "basketball" not in items:
                print("You need to get the basketball.")
            else:
                print("Samuel dribbles the ball! He goes left! He goes right!\nSamuel dribbles the ball between his legs!\nHe drives for the basket and leaps high in the air.\nIt's a slam-dunk! Samuel scores!\n")
            newplace = 3
            return newplace
        elif choice == 2:
            print("You head back through the gate to the garden.\n")
            newplace = 2
            return newplace
        elif choice == 3:
            print("You decide to head down the street, away from the house.\n")
            newplace = 4
            return newplace
    if not(answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer,items,plnm)
            newplace = 3
            return newplace

def sidewalkoptions(items):
    print("\nWhat do you want to do? Type a command or enter a number:")
    print ("1. Take a picture of some of the sights you see", "2. Go back to Yaya's house", "3. Walk to the construction site")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 3:
            choice = int(input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            if "camera" not in items:
                print("You don't have the camera with you!")
            else:
                print("You stop and take a picture with the camera.")
                photo = takepicture(pic12.name, plnm)
            newplace=4
            return newplace
        elif choice ==2:
            print("You decide to head back toward Yaya's house.")
            newplace =3
            return newplace
        else:
            print("You hear the construction equipment rumbling as you walk up the long hill toward the construction site.")
            newplace = 5
            return newplace
    if not(answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer,items,plnm)
            newplace = 4
            return newplace

def construction_siteoptions(items):
    if "a big hole" not in loc6.thingshere:
        print("\nWhat do you want to do? Type a command or enter a number:")
        print("1. Leave and walk back to the house","2. Try to go into the tunnel","3. Find something to dig with")
        answer = input()
        if answer.isnumeric():
            choice = int(answer)
            while choice > 3:
                choice = (input("Choose one of the numbers."))
            print("\n\n\n\n\n\n\n")
            if choice == 1:
                print("You turn back toward the house.\n")
                newplace = 4
                return newplace
            elif choice == 2:
                print("The entrance is too small for you to go into the tunnel.\nYou peer into the tunnel but it is very dark in there.\n")
                if "flashlight" in items:
                    print("You try shining the flashlight into the tunnel to get a better look.\nFor a moment you see the little yellow robot disappearing around a corner.\n")
                newplace = 5
                return newplace
            elif choice == 3:
                if "shovel" in items:
                    print("You try digging with the shovel but it is hard work and takes a long time.\nThe tunnel entrance is still too small.\n")
                else:
                    print("You do not have a shovel to dig with!")
                newplace = 5
                return newplace
        if not (answer.isnumeric()):
            if answer == "quit":
                endgame = 1000
                return endgame
            else:
                if answer=="use":
                    newplace=specialactions(answer, items, plnm)
                    return newplace
                else:
                    specialactions(answer, items, plnm)
                    newplace = 5
                    return newplace
    else:
        newplace=6
        return newplace

### outside tunnel location 6
def outside_tunneloptions(items):
    print("The tunnel entrance is now a hole big enough to walk into.\n'I wonder if I have everything I need,' you think.\nYou notice a sign posted by the entrance to the tunnel.\n\nWhat do you want to do?\n\n1. Walk into the tunnel.\n2. Look into the tunnel.\n3. Read the sign.\n4. Walk back home.\n5. Check to see what you are carrying.\n")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 5:
            choice = (input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            print("You start to walk into the dark tunnel.")
            newplace = 7
            return newplace
###look in tunnel
        elif choice == 2:
            print("It looks a little dark and scary in there.")
            if "flashlight" in items:
                print("You shine your flashlight around and peer into the tunnel.\nIn the light it does not look scary any more.\nExcept for the dirt where you have been digging, the tunnel looks clean inside.\nA smooth tile floor runs down the center of the tunnel, which curves away out of your sight in the distance.\n")
            newplace = 6
            return newplace
###read sign
        elif choice == 3:
            print("The sign says:\n       IMPORTANT SAFETY RULES:\n  Everyone who enters should have:\n  >>> A flashlight\n  >>> A camera\n  >>> A grabber, and\n  >>> A net.")
            newplace = 6
            return newplace
### go back toward home
        elif choice == 4:
            print("You turn and begin to walk back toward the house.\n")
            newplace = 4
            return newplace
        elif choice == 5:
            print("You are holding these things:")
            inventory(items)
            newplace = 6
            return newplace
    if not(answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer, items, plnm)
            newplace = 6
            return newplace

### dark tunnel location 7
def dark_tunneloptions(items):
    print("\nWhat do you want to do? Type a command or enter a number:")
    print ("  1. Go down into the mine.", "2. Go back out of the tunnel.", "3. Keep going in the tunnel.", "4. Read the sign.")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 4:
            choice = (input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            print("You start carefully climbing down into the mine shaft.")
            newplace=8
            return newplace
        elif choice ==2:
            print("You decide to head back out of the tunnel.\n After walking for quite a while, you come back out of the tunnel.")
            newplace =6
            return newplace
        elif choice ==3:
            print("You decide to leave the mine alone, and head on down the tunnel.\nAfter walking for a while longer, you hear voices up ahead.\nYou turn a corner and suddenly the tunnel ends.\nYou see the little yellow robot talking to Buzz Lightyear, and behind them you see what looks like a spaceport.")
            newplace = 9
            return newplace
        elif choice == 4:
            print("The old sign says, \n        WARNING        \n    Gold Mine Closed\n       due to        \n    Risk of Cave-Ins.\n")
            newplace=7
            return newplace
        else:
            print("You hear the construction equipment rumbling as you walk up the long hill toward the construction site.")
            newplace = 5
            return newplace
    if not(answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer,items, plnm)
            newplace = 7
            return newplace

### descending into mine, location 8
def mineoptions(items):
    print("\n\n\n\n\n\n\n")
    time.sleep(3)
    print("'Boy oh boy, that was a close one!' you say to yourself. 'Now here I am, stuck at the bottom of a mine!'")
    newplace=10
    return newplace

### spaceport, location 9
def spaceportoptions(items):
    print("\nWhat do you want to do? Type a command or enter a number:")
    print ("  1. Go back into the mine.", "  2. Ask Buzz if they have a grabber.", "  3. Ask if you can go with them in the rocket.")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 3:
            choice = (input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            print("You hop back into the mine cart and ride back down into the mine.\n Soon you reach the end of the tracks, climb out of the cart and walk deeper into the mine.")
            veh1.where = 10
            newplace = 10
            return newplace
        elif choice ==2:
            print("'Hi Buzz!' you say. 'I don't have my grabber with me. Do you have a spare one I can borrow?'\n 'Sure,' says Buzz. 'There is a spare one leaning against the Rover over there.'")
            newplace = 9
            return newplace
        elif choice == 3:
            print("'Hi Buzz!' you say. 'Are you getting ready for a space launch? Can I go with you?'\nBuzz says, 'I don't know, you look pretty young for space travel. \nWe need a scientist who knows a lot about insects and plants and strange animals.'")
            print("'But I do know a lot of things about plants and insects and animals!' you say.\n 'Did you know there is a lizard that squirts blood out of its eyes?\nDid you know the secretary bird stomps on snakes?\nDid you know Monarch butterflies like milkweed and phlox plants?'")
            print("The robot says, 'HE REALLY DOES KNOW A LOT ABOUT THOSE THINGS.'\n'Wow!' adds Buzz!'He sure does! OK, Samuel, you can come along as our science officer! Let's load up the Rover.'")
            veh1.where = 11
            newplace = 11
            return newplace
    if not(answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer,items, plnm)
            newplace = 9
            return newplace

###bottom of mine, location 10
def bottom_of_mineoptions(items):
    print("\nWhat do you want to do? Type a command or enter a number:")
    print ("1. Keep walking through the mine shaft", "2. Take a look around.")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 2:
            choice = (input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            print("As you continue on, you see a mining cart sitting on a track nearby. \n'I can ride in that!' you think to yourself.")
            print("What do you want to do?\n  1. Take a ride in the mining cart.\n  2. Put something in the mining cart.\n  3. Walk back to where the rocks caved in.")
            secanswer = input()
            if secanswer.isnumeric():
                choice = int(secanswer)
                while choice > 3:
                    choice = int(input("Choose one of the numbers."))
                if choice == 1:
                    print("You climb in, pull a lever and soon you are rolling faster and faster through the tunnel.\nAs the track begins to slope up, the cart slows down, and comes to a stop just as the tunnel ends.\nYou climb out of the cart in bright sunlight. You are out of the mine!")
                    veh1.where = 9
                    newplace = 9
                    return newplace
                elif choice == 2:
                    didit = specialactions("put", items, plnm)
                    newplace=10
                    return newplace
                elif choice == 3:
                    print("You walk back to where the rocks caved in.")
                    newplace = 10
                    return newplace
            if not (secanswer.isnumeric()):
                if secanswer == "quit":
                    endgame = 1000
                    return endgame
                else:
                    specialactions(secanswer, items, plnm)
                    newplace = 10
                    return newplace
        elif choice == 2:
            if "flashlight" in items:
                print("Even with your flashlight you cannot see very much,\nbut you notice something shiny where the rocks have fallen away. You can't quite reach it.")
                if art3.found < 0:
                    if ("grabber" in items):
                        print("Then you remember you have the grabber with you!\nUsing the grabber, you can just reach it. At first it slips out.\nBut on the second try, you get it! A large gold nugget is on the ground in front of you.")
                        if art3.where == 10 and art2.where > 10:
                            loc10.thingshere.append(art3.name)
                            art3.where += 40
                            art3.found += 1
                        elif art2.where == 10 and art1.where > 10:
                            loc10.thingshere.append(art2.name)
                            art2.where += 40
                            art2.found += 1
                        elif art1.where == 10:
                            loc10.thingshere.append(art1.name)
                            art1.where += 40
                            art1.found += 1
                    else:
                        print("Too bad, you don't have the grabber with you.")
                else:
                    print ("There is no more gold to find here.")
                    newplace = 10
                    return newplace
            else:
                print("It is too dark to see very much without a flashlight.")
            newplace = 10
            return newplace
    if not(answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer, items, plnm)
            newplace = 10
            return newplace


####place 11, loading rover
def loading_roveroptions(items):
    print ("\n'I wonder what I should take along for the trip,' you say to yourself.\n'I better put some things in the Rover too!'")
    print("\nWhat do you want to do? Type a command or enter a number:")
    print ("1. PUT things in the Rover.", "2. Hop in the Rover and drive over to the Rocket., 3. Go back to the mine.")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 3:
            choice = (input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 1:
            print("Use the PUT command to place items you are holding in the Rover.\nUse the TAKE command to pick up items, then PUT them in the Rover.\nAnything you DROP will be left behind.")
            newplace = 11
            return newplace
        elif choice == 2:
            print("'Come on, guys, let's go!' you say. \nBuzz and the Robot hop into the Rover with you, and you drive away toward the Rocket Launchpad.\nBuzz says, 'I sure hope we brought everything we are going to need!'\n It takes only a few minutes to drive over to the launchpad.")
            veh2.where = 12
            newplace = 12
            return newplace
        elif choice == 3:
            print("You head back down into the mine.")
            veh1.where = 10
            newplace = 10
            return newplace
    if not (answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer, items, plnm)
            newplace = 11
            return newplace

####place 12, launchpad options
def launchpadoptions(items):
    print("\nWhat do you want to do? Type a command or enter a number:")
    print ("1. Climb into the Rocket", "2. Help unload the Rover and put things in the Rocket", "3. Try to help fix the Rocket")
    answer = input()
    if answer.isnumeric():
        choice = int(answer)
        while choice > 3:
            choice = (input("Choose one of the numbers."))
        print("\n\n\n\n\n\n\n")
        if choice == 2:
            print("Use the TAKE and PUT commands to load up the Rocket.\nMake sure you PUT them in the Rocket.\nAnything you DROP outside the Rocket will be left behind.")
            newplace = 12
            return newplace
        elif choice == 1:
            print("'I'm ready to go!' you say, as you climb into the Rocket.\nYou see a spacesuit hanging near to a seat labeled FOR SCIENCE OFFICER.\nBuzz and the Robot load a few more things into the Rocket before they climb in.\n")
            newplace = 13
            return newplace
        elif choice == 3:
            act = usesocket_wrench(items, 12)
            newplace = 12
            return newplace

    if not (answer.isnumeric()):
        if answer == "quit":
            endgame = 1000
            return endgame
        else:
            specialactions(answer, items, plnm)
            newplace = 12
            return newplace



def mining_cart(items):
    print("NEED MINING CART STUFF HERE")


def inventory(things):
    for i in things:
        print(">>>"+i)

####Initialize actions {dictionary of choices}
options = {0: kitchenoptions,
           1: backdeckoptions,
           2: gardenoptions,
           3: drivewayoptions,
           4: sidewalkoptions,
           5: construction_siteoptions,
           6: outside_tunneloptions,
           7: dark_tunneloptions,
           8: mineoptions,
           9: spaceportoptions,
           10: bottom_of_mineoptions,
           11: loading_roveroptions,
           12: launchpadoptions}
###initialize USE actions

usestuff = {0: usegrabber,
           1: usecamera,
           2: useexcavator,
           3: useflashlight,
           4: usenet,
           5: userover,
           6: useshovel,
           7: usemask,
           8: usewalking_stick,
           9: usesocket_wrench,
           10: usespacesuit,
           11: usemagnet,
           12: useparachute,
           13: useraft,
           14: usebread,
           15: usepeanut_butter,
           15: usefloating_vest,
           16: userudder}

### def vehicle class and attributes
class Vehicle:
    def __init__(self):
        self.num=1
        self.name="minecart"
        self.where = plnm
        self.whowith=[]
        self.thingshere=[]

    def whatsinsideprint(self):
        veh=self.name
        who=self.whowith
        what=self.thingshere
        print(who + "are in the " + veh + " with you.")
        print("These things are in the " + veh + " with you:\n")
        print (what)
veh0 = Vehicle()
veh0.num = 0
veh0.name = "excavator"
veh0.where = 5
veh0.whowith = []
veh0.thingshere = []

veh1 = Vehicle()
veh1.num = 1
veh1.name = "mining cart"
veh1.where = 10
veh1.whowith = []
veh1.thingshere=[]

veh2 = Vehicle()
veh2.num = 2
veh2.name = "rover"
veh2.where = 11
veh2.whowith = []
veh2.thingshere=[]

veh3 = Vehicle()
veh3.num = 3
veh3.name ="rocket"
veh3.where = 12
veh3.whowith = []
veh3.thingshere = []

#veh4 = Vehicle()
#veh4.num = 4
#veh4.name = "raft"
#veh4.where =
#veh4.whowith = []
#veh4.thingshere = []

vehlist=[]
vehlist.append(veh0)
vehlist.append(veh1)
vehlist.append(veh2)
vehlist.append(veh3)
#vehlist.append(veh4)
##vehlist.append(veh###)

##Define Artifact Class and artifacts, put in artlist

class Artifact:
    def __init__(self):
        self.num = 1
        self.name ="thing"
        self.where = 5
        self.found = 1
        self.points = 2

art0 = Artifact()
art0.num = 0
art0.name = "flowers"
art0.where = 2
art0.found = 0
art0.points = 1

art1 = Artifact()
art1.num = 1
art1.name = "gold nugget"
art1.where = 10
art1.found = 0
art1.points = 2

art2 = Artifact()
art2.num = 2
art2.name = "bigger gold nugget"
art2.where = 10
art2.found = 0
art2.points = 2

art3 = Artifact()
art3.num = 3
art3.name = "even bigger gold nugget"
art3.where = 10
art3.found = 0
art3.points = 3

art4 = Artifact()
art4.num =4
art4.name = "plant samples"
art4.where = 16
art4.found = 0
art4.points = 2

art5 = Artifact()
art5.num = 5
art5.name = "airfish"
art5.where = 17
art5.found = 0
art5.points = 2

art6 = Artifact()
art6.num = 6
art6.name = "large ruby"
art6.where = 17
art6.found = 0
art6.points = 3

art7 = Artifact()
art7.num = 7
art7.name = "soil sample"
art7.where = 17
art7.found = 0
art7.points = 1

#art8 = Artifact()
#art8.num = 8
#art8.name = ""
#art8.where =
#art8.found = 0
#art8.points = 2

artlist=[]
artlist.append(art0)
artlist.append(art1)
artlist.append(art2)
artlist.append(art3)
artlist.append(art4)
artlist.append(art5)
artlist.append(art6)
artlist.append(art7)
##artlist.append(art8)

##Define DEEDS clas and attributes of members

class Deed:
    def __init__(self):
        self.num =1
        self.name = "name"
        self.where = 5
        self.done = 0
        self.points = 3

deed0 = Deed()
deed0.num = 0
deed0.name = "washing_hands"
deed0.where = 0
deed0.done = 0
deed0.points = 3

deed1 = Deed()
deed1.num = 1
deed1.name = "putting dishes in sink"
deed1.where = 0
deed1.done = 0
deed1.points = 3

deed2 = Deed()
deed2.num = 2
deed2.name = "wearing mask"
deed2.where = 0
deed2.done = 0
deed2.points = 3

deed3 = Deed()
deed3.num = 3
deed3.name = "collecting sticks for fire"
deed3.where = 2
deed3.done = 0
deed3.points = 3

deed4 = Deed()
deed4.num = 4
deed4.name = "seeing mouse and weasel"
deed4.where = 4
deed4.done = 0
deed4.points = 3

deed5 = Deed()
deed5.num = 5
deed5.name = "using excavator"
deed5.where = 5
deed5.done = 0
deed5.points = 3

deed6 = Deed()
deed6.num = 6
deed6.name = "reading sign"
deed6.where = 6
deed6.done = 0
deed6.points = 3

deed7 = Deed()
deed7.num = 7
deed7.name = "repairing rocket"
deed7.where = 13
deed7.done = 0
deed7.points = 3

deed8 = Deed()
deed8.num = 8
deed8.name = "spacewalk"
deed8.where = 15
deed8.done = 0
deed8.points = 3

deed9 = Deed()
deed9.num = 9
deed9.name = "building raft"
deed9.where = 26
deed9.done = 0
deed9.points = 3

deed10 = Deed()
deed10.num = 10
deed10.name = "wearing life jacket"
deed10.where = 28
deed10.done = 0
deed10.points = 3

deed11 = Deed()
deed11.num = 11
deed11.name = "picking flowers for your Mother"
deed11.where = 0
deed11.done = 0
deed11.points = 3

deedlist = []
deedlist.append(deed0)
deedlist.append(deed1)
deedlist.append(deed2)
deedlist.append(deed3)
deedlist.append(deed4)
deedlist.append(deed5)
deedlist.append(deed6)
deedlist.append(deed7)
deedlist.append(deed8)
deedlist.append(deed9)
deedlist.append(deed10)
deedlist.append(deed11)

#####Def Locations Class and attributes of all class members
class Location:
    def __init__(self):
        self.num = 1
        self.name = "backdeck"
        self.description = ""
        self.looktext = ""
        self.thingshere=[]
    def descriptionprint(self):
        name=self.name
        thefile = self.description
        mytext = open(thefile, "r")
        words = mytext.read()
        mytext.close()
        print("\n"+words)
    def printlooktxt(self):
        print(self.looktext+"\n")
######Populate location class

class Photograph:
    def __init__(self):
        self.num = 1
        self.name = "Deer"
        self.where = 1
        self.taken = 0
        self.points = 1

pic0 = Photograph()
pic0.num = 0
pic0.name = "Deer"
pic0.where = 1
pic0.taken = 0
pic0.points = 1

pic1 = Photograph()
pic1.num = 1
pic1.name = "Elmo"
pic1.where = 5
pic1.taken = 0
pic1.points = 1

pic2 = Photograph()
pic2.num = 2
pic2.name = "Fawn"
pic2.where = 2
pic2.taken = 0
pic2.points = 1

pic3 = Photograph()
pic3.num = 3
pic3.name = "Frog"
pic3.where = 18
pic3.taken = 0
pic3.points = 1

pic4 = Photograph()
pic4.num = 4
pic4.name = "Launch pad"
pic4.where = 13
pic4.taken = 0
pic4.points = 1

pic5 = Photograph()
pic5.num = 5
pic5.name = "Lost Galaxy"
pic5.where = 14
pic5.taken = 0
pic5.points = 1

pic6 = Photograph()
pic6.num = 6
pic6.name = "Monarch Butterfly"
pic6.where = 2
pic6.taken = 0
pic6.points = 1

pic7 = Photograph()
pic7.num = 7
pic7.name = "Owl"
pic7.where = 2
pic7.taken = 0
pic7.points = 1


pic8 = Photograph()
pic8.num = 8
pic8.name = "Robot Mom"
pic8.where = 20
pic8.taken = 0
pic8.points = 1

pic9 = Photograph()
pic9.num = 9
pic9.name = "Rover"
pic9.where = 17
pic9.taken = 0
pic9.points = 1

pic10 = Photograph()
pic10.num = 10
pic10.name = "Spacewalk"
pic10.where = 15
pic10.taken = 0
pic10.points = 1

pic11 = Photograph()
pic11.num = 11
pic11.name = "Surprise Lily"
pic11.where = 2
pic11.taken = 0
pic11.points = 1

pic12 = Photograph()
pic12.num = 12
pic12.name = "Weasel"
pic12.where = 4
pic12.taken = 0
pic12.points = 1

pic13 = Photograph()
pic13.num = 13
pic13.name = "xx"
pic13.where = 22
pic13.taken = 0
pic13.points = 1

piclist = []
piclist.append(pic0)
piclist.append(pic1)
piclist.append(pic2)
piclist.append(pic3)
piclist.append(pic4)
piclist.append(pic5)
piclist.append(pic6)
piclist.append(pic7)
piclist.append(pic8)
piclist.append(pic9)
piclist.append(pic10)
piclist.append(pic11)
piclist.append(pic12)

loc0 = Location()
loc0.num = 0
loc0.name = "kitchen"
loc0.description = "kitchen.txt"
loc0.looktext = "You see a flower vase and some other things on the table."
loc0.thingshere = ["PBJ", "glass of milk", "camera", "mask"]

loc1 = Location()
loc1.num = 1
loc1.name = "backdeck"
loc1.description = "backdeck.txt"
loc1.looktext = "You see some items on the table, a garden, and a grabber by the gate. \nAs you look you see something moving behind the fence."
loc1.thingshere = ["flashlight", "net", "walking stick"]

loc2 = Location()
loc2.num = 2
loc2.name = "garden"
loc2.description = "garden.txt"
loc2.looktext = "You see a butterfly, an owl, and pretty flowers."
loc2.thingshere = ["grabber", "sticks", "flowers"]

loc3 = Location()
loc3.num = 3
loc3.name = "driveway"
loc3.description = "driveway.txt"
loc3.looktext = "You see a basketball and a basketball hoop."
loc3.thingshere = ["basketball"]

loc4 = Location()
loc4.num = 4
loc4.name = "sidewalk"
loc4.description = "sidewalk.txt"
loc4.looktext = "As you look around, you see a small mouse peering around a rock near a Japanese Maple tree.\nThe mouse is watching a weasel.\nThe weasel is covered in mud, has a beehive on his head, and is surrounded by noisy crickets.\nHe is also carrying a large stone and a prickly thorn bush.\nThe mouse is covering his mouth and trying not to laugh."
loc4.thingshere = []

loc5 = Location()
loc5.num = 5
loc5.name = "construction_site"
loc5.description = "construction_site.txt"
loc5.looktext = "There is a pile of shovels nearby. You notice the excavator's engine is running."
loc5.thingshere = ["shovel", "excavator"]

loc6 = Location()
loc6.num = 6
loc6.name = "outside_tunnel"
loc6.description = "outside_tunnel.txt"
loc6.looktext = "You can't see very far into the tunnel."
loc6.thingshere = ["shovel", "excavator"]

loc7 = Location()
loc7.num = 7
loc7.name = "dark_tunnel"
loc7.description = "dark_tunnel.txt"
loc7.looktext = "You see a sign up ahead near a shaft leading down under ground."
loc7.thingshere = ["sign"]

loc8 = Location()
loc8.num = 8
loc8.name = "mine"
loc8.description = "mine.txt"
loc8.looktext = "Even with your flashlight you cannot see very much,\nbut you notice something shiny where the rocks have fallen away."
loc8.thingshere = []

loc9 = Location()
loc9.num = 9
loc9.name = "spaceport"
loc9.description = "spaceport.txt"
loc9.looktext = "A rover is parked near where Buzz and the robot are talking.\nIn the distance, a large rocket stands on a launchpad.\nYou see white streams of vapor coming from the rocket.\nIt looks like the plan to launch the rocket soon."
loc9.thingshere = ["rover", "grabber", "net", "socket wrench"]

loc10 = Location()
loc10.num = 10
loc10.name = "bottom_of_mine"
loc10.description = "bottom_of_mine.txt"
loc10.looktext = "                   "
loc10.thingshere = ["pile of rocks, blocking the way up."]

loc11 = Location()
loc11.num = 11
loc11.name = "loading_rover"
loc11.description = "loading_rover.txt"
loc11.looktext = "As you look around, you see some tools and other useful items to take."
loc11.thingshere = ["socket wrench", "grabber", "net", "spacesuit", "magnets", "mining cart"]

loc12 = Location()
loc12.num = 12
loc12.name = "launchpad"
loc12.description = "launchpad.txt"
loc12.looktext = "As you look around, you remember you have put things in the Rover you might want to take.\n'Better make sure I have everything!' you say."
loc12.thingshere = ["magnet, socket wrench"]

loc13 = Location()
loc13.num = 13
loc13.name = "rocket_launch"
loc13.description = ".txt"
loc13.looktext = "                   "
loc13.thingshere = ["spacesuit, magnet"]


loc14 = Location()
loc14.num = 14
loc14.name = "outer_space"
loc14.description = "outer_space.txt"
loc14.looktext = "                   "
loc14.thingshere = ["p"]


loc15 = Location()
loc15.num = 15
loc15.name = "space_walk"
loc15.description = "space_walk.txt"
loc15.looktext = "                   "
loc15.thingshere = [""]


loc16 = Location()
loc16.num = 16
loc16.name = "landing_planet"
loc16.description = "landing_planet.txt"
loc16.looktext = "                   "
loc16.thingshere = ["p"]


loc17 = Location()
loc17.num = 17
loc17.name = "rover on planet"
loc17.description = "rover on planet.txt"
loc17.looktext = "From your seat in the Rover, you can see in the distance a hillside.\nSomething seems to be moving among the brightly colored plants there.\nOff to the left, you see a fog-like mist rising from a lower area surrounded by large trees."
loc17.thingshere = ["pi."]


loc18 = Location()
loc18.num = 18
loc18.name = "swamp"
loc18.description = "b.txt"
loc18.looktext = "You have arrived next to a swamp that has a large green rock in the center of it.\nStrange creatures shaped like fish are floating around in the air above the swamp.\n'What do you know!' says Buzz excitedly. 'Look at all those Airfish!'\n Just then you hear a noise that sounds like a giant B-U-R-P-P!\nRings of water spread out from the rock, and you suddenly realize it isn't a rock at all.\nA giant frog-like alien opens its eyes and blinks at you./n Something shiny and red sparkles in the water near the shore."
loc18.thingshere = ["airfish", "frog", "large ruby"]

loc19 = Location()
loc19.num = 19
loc19.name = "prairie"
loc19.description = "prairie.txt"
loc19.looktext = "All around you strange-looking plants are growing in the dark orange soil of the planet surface.\nThe plants have orange and purple and ruby-red flowers.\nSome of the plants give off a sweet fragrance that smells like chocolate.\nOther plants smell like a skunk to you.\n A strange creature with a large round body like a potato is stuffing the stinky plants into its wide mouth."
loc19.thingshere = ["strange plants", "soil samples", "Potato Head"]

loc20 = Location()
loc20.num = 20
loc20.name = "robot mom house"
loc20.description = "robot_mom_house.txt"
loc20.looktext = "                   "
loc20.thingshere = ["Robot Mom"]

# planetlaunch
# reentry alarm
# parachute
# chewandswallow
# city hall
# build raft  (bread, peanut butter, rudder, sail
# boating goods store
# ocean
# super Spot
# back home

trylist = []
trylist.append(loc0)
trylist.append(loc1)
trylist.append(loc2)
trylist.append(loc3)
trylist.append(loc4)
trylist.append(loc5)
trylist.append(loc6)
trylist.append(loc7)
trylist.append(loc8)
trylist.append(loc9)
trylist.append(loc10)
trylist.append(loc11)
trylist.append(loc12)
trylist.append(loc13)
trylist.append(loc14)
trylist.append(loc15)
trylist.append(loc16)
trylist.append(loc17)
trylist.append(loc18)
trylist.append(loc19)
trylist.append(loc20)


######Main Loop###### Initialize plnm and continuegame, print initial screen
continuegame = 1
plnm = 1
print ("Do you want to restore a saved game?  y / n \n")
answer = input()
while (answer != "y" and answer != "Y" and answer != "n" and answer != "N"):
    answer = input ("Enter y or n and hit return")
if answer == "y" or answer == "Y":
    itemslist = restoregame(plnm,items)
    items = itemslist[:-1]
    plnm = int(itemslist[-1])
place = places[plnm].upper()
print("\n",place)
for loc in trylist:
    if loc.num == plnm:
        loc.descriptionprint()
###Use plnm variable to get description of location
while continuegame == 1:
    pl = int(plnm)
    place = places[pl].upper()
    print(place)

#### go to options dictionary to get options available for this place
    plnm = options[pl](items)
    endgame = plnm
    if endgame == 1000:
        plnm = pl
        continuegame = 0
    if int(plnm) != pl:
        for loc in trylist:
            if loc.num == plnm:
                place = places[pl].upper()
#                print("\n\n\n\n\n\n\n")
                loc.descriptionprint()
print ("Save Game?  Y / N\n")
answer = input()
while (answer != "y" and answer != "Y" and answer != "n" and answer != "N"):
    answer = input("Enter y or n and hit return\n")
if answer == "y" or answer == "Y":
    savename = savegame()
    print ("We saved ", savename)
print ("Your Adventure is Over!  You found these Artifacts:\n")
score = 0
for art in artlist:
    score += art.found
    for i in items:
        if i ==  art.name:
            score += art.points
    if art.found == 1:
        print (art.name, art.found)
print("You also earned extra points for the following achievements:\n")
for d in deedlist:
    if d.done == 1:
        print (d.name, d.points)
        score += d.points
print("Every picture you took is also worth points.\n")
for pic in piclist:
    if pic.taken == 1:
        print (pic.name, pic.points)
        score += pic.points
print("You earned a total of", score, " points!")















