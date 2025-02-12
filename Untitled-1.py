import tkinter
age = int(input("What is your age? "))

if age <= 7:
    print("Are you a bit too young to be on the laptop?")
    print("And on coding?")
    print("I hope your parents are watching you!")
elif age == 8:
    print("What do you call a fish with no eyes? A fsh.")
elif age == 9:    
    print("What do you say when you lose a Wii game? I want a Wii-match.")
elif age == 10:
    print("Why was the snowman at the grocery store? He was picking his nose.")
elif age == 11:
    print("How do you get a cat to code? You scratch it.")
elif age == 12:
    print("What did mama cow say to baby cow? It's pasture bedtime.")
elif age == 13: 
    print("What did the fisherman say to the magician? Pick a cod, any cod.")
elif age == 14:
    print("What did the janitor say when he jumped out of the closet? Supplies.")
elif age == 15:
    print("Why are robots never afraid? They have nerves of steel.")
elif age == 16:
    print("How do you make a tissue dance? Put a little boogie in it.")
elif age == 17:
    print("How do pickles enjoy a day out? They relish it.")
elif age == 18:
    print("If athletes get athlete's foot, what do astronauts get? Missile toe.")
elif age >= 19 and age <= 24:
    print("You're too old for normal jokes!")
    print("So you get knock knock jokes! Age 19 to 24")
    print("Knock knock")
    print("Who's there?")
    if age == 19:
        print("Pilipe")
        print("Pilipe who?")
        print("Pilipe the car, we're out of gas!")
    elif age == 20:
        print("Cookie")
        print("Cookie who?")
        print("Cookie quit now and I have to make all the food!")
    elif age == 21:
        print("Dee")
        print("Dee who?")
        print("Dee-licious!")
    elif age == 22:
        print("Anna")
        print("Anna who?")
        print("Anna one, Anna two, Anna three!")
    elif age == 23:
        print("Harry")
        print("Harry who?")
        print("Harry up and answer the door!")
    elif age == 24:
        print("Cow")
        print("Cow who?")
        print("Cow much longer are you going to put up with all his knocking?")
    elif age >= 25 and age <= 30:
        print("You're too old for jokes!")
        print("So you get riddles! Age 25 to 30")
    if age == 25:
        print("What has keys but can't open locks?")
        print("A piano.")
    elif age == 26:
        print("I have no blood pumping through me but I have 4 fingers and 1 thumb. What am I?")
        print("A glove.")
    elif age == 27:
        print("What is as big as an elephant but weighs nothing?")
        print("An elephant's shadow.")
    elif age == 28:
        print("I have wings and a tail. Across the sky is where I sail. Yet I have no eyes, ears, or mouth. What am I?")
        print("A kite.")   
    elif age == 29:
        print("What has a neck but no head, two arms but no hands?")
        print("A shirt.")
    elif age == 30:
        print("Make the number 1 disappear.")
        print("Add the letter G and it's gone.")
elif age >= 31 and age <= 39:
    print("You're too old for jokes and riddles!")
    print("So you get tongue twisters! Age 31 to 39")
    if age == 31:
        print("She sells seashells by the seashore.")
    elif age == 32:
        print("How much wood would a woodchuck chuck if a woodchuck could chuck wood?")
    elif age == 33:
        print("Two to two Toulouse.")
    elif age == 34:
        print("Peter Piper picked a peck of pickled peppers.")
    elif age == 35:
        print("How can a clam cram in a clean cream can?")
    elif age == 36:
        print("If practice makes perfect and perfect needs practice, I'm perfectly practiced and practically perfect.")
    elif age == 37:
        print("Tim, the thin twin tinsmith.")
    elif age == 38:
        print("Tim the thin twin tinsmith's twin brother.")
    elif age == 39:
        print("Did Doug dig David's garden or did David dig Doug's garden?")
elif age >= 40 and age <= 60:      
    print("You're too old for jokes, riddles, and tongue twisters.")
    print("So you get math problems! Age 40 to 60")
    num1 = int(input("Pick any number: "))
    num2 = int(input("Pick another number: "))
    answer = int(input(f"What is {num1} + {num2}? "))
    correct_answer = num1 + num2
    if answer == correct_answer:
        print("Correct!")
    else:
        print("Wrong!")
    print(f"The correct answer is {correct_answer}")
elif age >= 61 and age <= 100:
    print("You're too old for jokes, riddles, tongue twisters, and math problems.")
    print("So you get a story! Age 61 to 100")
    print("Once upon a time in a small village, there lived an old man.")
    print("He was known for his wisdom and kindness. Every day, he would sit under a large oak tree and share stories with the children of the village.")
    print("One day, a young boy asked him, 'What is the secret to a happy life?'")
    print("The old man smiled and said, 'The secret to a happy life is to always be kind, to always be curious, and to always find joy in the little things.'")
    print("The boy thought about this for a moment and then asked, 'But how do I do that?'")
    print("The old man replied, 'By treating others with respect, by always asking questions and seeking knowledge, and by appreciating the beauty of the world around you.'")
    print("The boy nodded and thanked the old man for his wisdom. From that day on, he tried to live by the old man's advice, and he found that his life was indeed much happier.")
    print("The end.")
    print("I hope you enjoyed the story!")
else:
    print("are you to old to be alive?")
    print(f"you are {age} years old.")
    print("I hope you are not dead!")
    print("If you are, I am sorry for your loss.")
    print("plus then you are a ghost!")
    print("ah! a ghost!")
tkinter.Tk().mainloop()
 