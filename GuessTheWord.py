import random

name = input("What is your name?:")
print("You have 11 chances in total to guess the right word! Hint: Camera")
print(f"Good luck with playing {name}!!")

words = ['Action', 'Film', 'Drone', 'Web', 'Security', 'Mirrorless', 'Lens', 'Sensor', 'Shutter', 'Viewfinder', 'ISO', 'Aperture', 'Image','Autofocus', 'Zoom', 'Flash', 'Image', 'Microphone', 'Expose', 'White Balance', 'Megapixels', 'Format', 'Histogram','Canon','Nikon','Sony','Fujifilm','Panasonic','GoPro','Lumix','Samsung']

guessword = random.choice(words)
displayed_word = ["*"] * len(guessword)
turns = 11

while turns > 0:
    for char in displayed_word:
        print(char, end = "")
    print()

    guess = input("Guess a letter:")
    
    if guess.lower() in guessword.lower():
        for i in range(len(guessword)):
            if guessword[i].lower() == guess.lower():
                displayed_word[i] = guessword[i]
    else:
        turns -= 1
        print(f"Wrong! You now have {turns} remaining guesses")

    if "*" not in displayed_word:
        print(f"You won! The correct word was: {guessword}")
        break
else:
    print(f"You lost the game! The word was: {guessword}")
