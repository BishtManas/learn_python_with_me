import random

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
    score = 100 # if user take hints the then score reduces to how many letters you ask for bot 
# one letter = - 5
# correct guess = +25
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
            print(computer_choice2)
            ask1 = int(input ('Enter your guessed number : '))
            if ask1 == 'computer_choice1':
                score += 30
                print(f'Correct guessed ! This is your score {score}')
            else :
                print('Wrong answer ! try again later')
    elif ask_user == 'anime name':
        print ('''"Naruto",
    "One Piece",
    "Attack on Titan",
    "Death Note",
    "Demon Slayer",
    "Dragon Ball Z",
    "Tokyo Ghoul",
    "Jujutsu Kaisen"''')
        print ('this is your word length ')
        display = ['_'] * len(Random_Anime)
        print(' '.join(display))
        print()
        ask = input ('choose a anime character name as showed :').lower().strip()
        print()
        if ask == Random_Anime:
            score += 25
            print(f'correct guess here is your score :{score}')
            print()
        else :
            ask = input ('wrong guess if you want hint then type (yes/no) :').lower().strip()
            print()
            if ask == 'yes':
                hints = int(input ('how many hints you want :'))
                print()
                hint_sol = random.sample(range(len(Random_Anime)), hints)
                for pos in hint_sol:
                    display[pos] = Random_Anime[pos]
                print(' '.join(display))
                print()
    elif ask_user == 'song name':
        print('''"Shape of You",
    "Believer",
    "Blinding Lights",
    "Levitating",
    "Perfect",
    "Calm Down"''')
        print()
        print ('this is your word length ')
        display = ['_'] * len(Random_Song)
        print(' '.join(display))
        print()
        ask = input ('choose a song name as showed : ').lower().strip()
        print()
        if ask == Random_Song:
            score += 25
            print(f'correct guess here is your score :{score}')
            print()
        else :
            ask = input ('wrong guess if you want hint then type (yes/no) :').lower().strip()
            print()
            if ask == 'yes':
                hints = int(input ('how many hints you want :'))
                print()
                hint_sol = random.sample(range(len(Random_Song)), hints)
                for pos in hint_sol:
                    display[pos] = Random_Song[pos]
                print(' '.join(display))
                print()
                
            
# while True:
print()
ask_user = input('what you want to guess (guess number / guess anime name / guess song name ) : ').lower().strip()
print()
guess_game()
    
    # user_input = input('what is you final answer :')a