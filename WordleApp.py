import random

name = input("What is your name?:")
print("You have 5 chances in total to guess the right word")
print(f"Good luck with playing {name}!!")

words = ['Action', 'Film', 'Drone', 'Web', 'Security', 'Mirrorless', 'Lens', 'Sensor', 'Shutter', 'Viewfinder', 'ISO', 'Aperture', 'Image','Autofocus', 'Zoom', 'Flash', 'Image', 'Microphone', 'Expose', 'White Balance', 'Megapixels', 'Format', 'Histogram','Canon','Nikon','Sony','Fujifilm','Panasonic','GoPro','Lumix','Samsung']

word = random.choice(words)
guess = ""
turns = 5
