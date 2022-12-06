
from random import choice

names = ("Muxammad", "Dilshod", "Shaxzod")
bot_choice = choice(names)

for game in range(1,3):
    user_choice = input(f"Bot ism o'yladi {names}\nToping: ")
    if user_choice.lower() == bot_choice.lower():
        print("Bravo!")
        break
    else:
        print("Topolmadingiz")
