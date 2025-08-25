import random

score = 100 # if user take hints the then score reduces to how many letters you ask for bot 
# one letter = - 5
# correct guess = +25

computer_choice1 = random.randint(1,50) # ask for user if he/she wants harder level 
computer_choice2 = random.randint(1,10) # easy level

anime_names = [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "Death Note",
    "Demon Slayer",
    "Dragon Ball Z",
    "Tokyo Ghoul",
    "Jujutsu Kaisen"
]
song_names = [
    "Shape of You",
    "Believer",
    "Blinding Lights",
    "Levitating",
    "Perfect",
    "Calm Down"
]
Random_Anime = random.choice(anime_names).lower()
Random_Song = random.choice(song_names).lower()
def guess_game ():
    if ask_user == 'guess number':
        print('If you choose right answer in hard mode then you will get 5 points extra')
        ask = input ('hard (guess number between 1 to 100) / easy (guess number between 1 to 10) :')
        if ask == 'hard': 
            ask1 = int(input ('Enter your guessed number : '))
            if ask1 == 'computer_choice1':
                score += 30
                print(f'Correct guessed ! This is your score {score}')
            else :
                print('Wrong answer ! try again later')
        elif ask == 'easy':
            ask1 = int(input ('Enter your guessed number : '))
            if ask1 == 'computer_choice1':
                score += 30
                print(f'Correct guessed ! This is your score {score}')
            else :
                print('Wrong answer ! try again later')
# while True:
ask_user = input('what you want to guess (guess number / guess anime name / guess song name ) : ')
guess_game()
    
    # user_input = input('what is you final answer :')
    
    
