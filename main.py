import random

#welcome lines:
print("Welcome to Mad Libs")
print("Begin by choosing wether or not you would like to choos your own words or let the computer generate them for you and then wait for your story to unfold!")

#the arrays
name_array = ["Billy", "Charlie", "Dick", "Andres", "Andy", "Isaak", "Mr. Berandino", "Oliver", "Isa", "Jackson", "Lily", "Sarah", "Roger", "Emily"]
basicverb_array = ["die", "cry", "fly", "exist", "sleep", "smile", "run", "talk", "sing", "sit", "swim", "stare", "drive", "watch", "type", "code", "golf"]
singularnoun_array = ["cat", "pencil", "dog", "bird", "bank", "computer", "ring", "hoodie", "hat", "guitar", "man", "woman", "child", "kid", "baby", "teenager", "mom", "dad", "friend", "lobster"]
occupation_array = ["firefighter", "banker", "student", "chef", "chipotle employee", "teacher", "surgeon", "train conductor", "police officer"]
shape_array = ["circle", "square", "star", "triangle", "hexagon", "pentagon", "archimedean solid", "rhombus", "trapezoid, dadecagon"]
adjective_array = ["sexy", "sleepy", "hot", "cold", "lukewarm", "charming", "cruel", "stunning", "fantastic", "gentle", "aggressive", "huge", "small", "perfect", "annoying", "silly", "goofy", "shiny", "pretty"]
place_array = ["your moms", "the post oak school", "MFAH", "the zoo", "narnia", "chipotle", "the bathroom"]
importantmonument_array = ["the lincoln memorial", "luigi's mansion", "the washington monument", "the met", "mount rushmore", "the leaning tower of pisa", "the eiffel tower", "big ben"]
vehicle_array = ["electric razor scooter", "F-150", "F-250", "ambulance", "fire truck", "skate board", "heelies", "roller blades", "segway", "cadillac", "lamborghini", "alligator"]
verbing_array = ["running, crying", "swimming", "throwing", "exploding", "consuming", "creating", "cracking", "eating", "driving", "charging", "coding", "sitting", "laying", "working", "flying"]
restaurant_array = ["torchys tacos", "mcdonalds", "chick-fil-a", "raising cane's", "escalantes", "chipotle", "fogo chao", "the hard rock cafe"]
emotion_array = ["love", "hatred", "sadness", "happiness", "emptiness", "depression", "anxiety"]

#the words
computer_or_human = input("Would you like the computer to make the mad libs for you or do want to choose your own words? Y/N")

if computer_or_human == "N":
    Name1 = input("enter a name")
    occupation = input("enter an occupation")
    noun1 = input("enter a singular noun")
    noun2 = input("enter another singular noun")
    noun3 = input("enter another singular noun")
    shape = input("enter a shape")
    noun4 = input("enter another singular noun")
    verb1 = input("enter a basic verb (one without an ending i.e. -ing, -s, -ed, etc.)")
    adjective1 = input("enter an adjective")
    Name2 = input("enter another name ")
    place1 = input("enter another place")
    verb2 = input("enter another basic verb")
    verb3 = input("enter a verb ending in -ing")
    verb4 = input("enter another basic verb")
    noun5 = input("enter another singular noun")
    place2 = input("enter another place")
    restaurant = input("enter a restaurant name")
    importantmonument = input("enter an important monument")
    vehicle = input("enter a vehicle")
    verb5 = input("enter another basic verb")
    adjective2 = input("enter another adjective")
    adjective3 = input("enter another adjective")
    emotion = input("enter an emotion")
    verb6 = input("enter another basic verb")
    place3 = input("enter another place")

else:
    random.shuffle(name_array)
    random.shuffle(singularnoun_array)
    random.shuffle(shape_array)
    random.shuffle(emotion_array)
    random.shuffle(importantmonument_array)
    random.shuffle(vehicle_array)
    random.shuffle(restaurant_array)
    random.shuffle(occupation_array)
    random.shuffle(basicverb_array)
    random.shuffle(verbing_array)
    random.shuffle(adjective_array)
    random.shuffle(place_array)

    Name1 = name_array[0]
    Name2 = name_array[1]
    noun1 = singularnoun_array[0]
    noun2 = singularnoun_array[1]
    noun3 = singularnoun_array[2]
    noun4 = singularnoun_array[3]
    noun5 = singularnoun_array[4]
    shape = shape_array[0]
    emotion = emotion_array[0]
    importantmonument = importantmonument_array[0]
    vehicle = vehicle_array[0]
    restaurant = restaurant_array[0]
    occupation = occupation_array[0]
    verb1 = basicverb_array[0]
    verb2 = basicverb_array[1]
    verb4 = basicverb_array[2]
    verb5 = basicverb_array[3]
    verb6 = basicverb_array[4]
    verb3 = verbing_array[0]
    adjective1 = adjective_array[0]
    adjective2 = adjective_array[1]
    adjective3 = adjective_array[2]
    place1 = place_array[0]
    place2 = place_array[1]
    place3 = place_array[2]


#the story itself:
print(Name1, "is a normal", occupation, ". Then one day, a", noun1, "explodes, causing a", noun2, "to blow up, and a nearby", noun3, "erupt into a", shape, "of flames")
print(Name1, "realizes that they're being chased by the", noun4, ", who's trying to", verb1, "them. While on the run, they team up with an incredibly", adjective1)
print("human named", Name2, ". They may be from the", place1, "but they can", verb2, "like nobody's business. The duo decide to turn the tables on their pursuers by")
print(verb3, "causing the enemy to", verb4, ". The bad guys then decide to react by blowing up a", noun5, ", which triggers a chain reaction causing the local", place2, ", ")
print(restaurant, ", and the", importantmonument, "to explode. Much to the enemy's dismay, doing this caused a part of the explosion to hit their", vehicle, "causing them to")
print(verb5, "eventually leading to their demise. Everything is", adjective2, "and the two decide that such a", adjective3, "ordeal has caused them to fall in", emotion, "with each other.")
print(" They decide to celebrate by", verb6, "ing on the", place3)
