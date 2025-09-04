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

class GuessGame:
    def __init__(self):
        self.score = 100
        self.display = []

    def guess_number1(self):
        ask = int(input ('Enter your guessed number between 1 to 10 : '))
        if ask == computer_choice2:
            self.score += 25
            print(f'Correct guessed ! This is your score {self.score}')
        elif ask > computer_choice2:
            print('Too high ! try again later')
        elif ask < computer_choice2:
            print('Too low ! try again later')
        else :
            print('Wrong answer ! try again later')
            
    def guess_number2(self):
        ask = int(input ('Enter your guessed number between 1 to 50 : '))
        if ask == computer_choice1:
            self.score += 30
            print(f'Correct guessed ! This is your score {self.score}')
        elif ask > computer_choice1:
            print('Too high ! try again later')
        elif ask < computer_choice1:
            print('Too low ! try again later')
        else :
            print('Wrong answer ! try again later')    
    
    def guess_anime(self):
        print("""
1. Naruto
2. One Piece
3. Attack on Titan
4. Death Note
5. Demon Slayer
6. Dragon Ball Z
7. Tokyo Ghoul
8. Jujutsu Kaisen
""")
        print ('This is your word length ')
        self.display = ['_'] * len(Random_Anime)
        print(' '.join(self.display))
        print()
        ask = int(input ('choose a anime character name as showed (type number) :'))
        print()
        if anime_names[ask-1].lower() == Random_Anime:
            self.score += 25
            print(f'correct guess here is your score :{self.score}')
            print() 
        else :
            ask = input ('wrong guess if you want hint then type (yes/no) :').lower().strip()
            print()
            if ask == 'yes':
                self.hint_anime()
            else:
                print('No hints taken. Better luck next time!')
                
    def hint_anime(self):
        print('One hints = 5 points will be deducted from your score')
        hints = int(input ('how many hints you want :'))
        print()
        hint_sol = random.sample(range(len(Random_Anime)), hints)
        for pos in hint_sol:
            self.display[pos] = Random_Anime[pos]
        self.score -= hints * 5
        # print(' '.join(self.display))
        print()
        
        print ("After taking hints this is your length of the word :")
        print()
        print(' '.join(self.display))
        print()
        # game.guess_anime()
        print("""
1. Naruto
2. One Piece
3. Attack on Titan
4. Death Note
5. Demon Slayer
6. Dragon Ball Z
7. Tokyo Ghoul
8. Jujutsu Kaisen
""")
        print()
        ask = int(input ('choose a anime character name as showed (type number) :'))
        print()
        if anime_names[ask-1].lower() == Random_Anime:
            self.score += 25
            print(f'correct guess here is your score :{self.score}')
            print() 
        else :
            print('Sorry, wrong guess. Better luck next time!')
            print()
                
    def guess_song(self):
        print("""
1. Shape of You
2. Believer
3. Blinding Lights
4. Levitating
5. Perfect
6. Calm Down
""")
        print ('this is your word length ')
        display = ['_'] * len(Random_Song)
        print(' '.join(display))
        print()
        ask = int(input ('choose a song name as showed (type number) : '))
        print()
        if song_names[ask-1].lower() == Random_Song:
            self.score += 25
            print(f'correct guess here is your score :{self.score}')
            print()
        else :
            ask = input ('wrong guess if you want hint then type (yes/no) :').lower().strip()
            print()
            if ask == 'yes':
                self.hint_song()
            else:
                print('No hints taken. Better luck next time!')
    def hint_song(self):
        print('One hints = 5 points will be deducted from your score')
        hints = int(input ('how many hints you want :'))
        print()
        hint_sol = random.sample(range(len(Random_Song)), hints)
        for pos in hint_sol:
            self.display[pos] = Random_Song[pos]
        self.score -= hints * 5
        # print(' '.join(self.display))
        print()
        
        print ("After taking hints this is your length of the word :")
        print()
        print(' '.join(self.display))
        print()
        # game.guess_anime()
        print("""
1. Shape of You
2. Believer
3. Blinding Lights
4. Levitating
5. Perfect
6. Calm Down
""")
        print()
        ask = int(input ('choose a song name as showed (type number) :'))
        print()
        if song_names[ask-1].lower() == Random_Song:
            self.score += 25
            print(f'correct guess here is your score :{self.score}')
            print() 
        else :
            print('Sorry, wrong guess. Better luck next time!')
            print()
        
game = GuessGame()
while True:
    Random_Anime = random.choice(anime_names).lower()
    Random_Song = random.choice(song_names).lower()
    print()
    ask_user = input('what you want to guess (guess number / guess anime name / guess song name ) or exit(404) : ').lower().strip()
    print()
    if ask_user == 'guess number':
        level = input('Choose level (easy/hard) : ').lower().strip()
        if level == 'easy':
            game.guess_number1()
        elif level == 'hard':
            game.guess_number2()
        else:
            print('Invalid level choice. Please choose "easy" or "hard".')
    elif ask_user == '404':
        print('Exiting the game. Goodbye!')
        break
    elif ask_user == 'anime name':
        game.guess_anime()
    elif ask_user == 'song name':
        game.guess_song()
    else:
        print('Invalid choice. Please choose "guess number", "guess anime name", or "guess song name".')


        
        
# def guess_game ():
#     score = 100 # if user take hints the then score reduces to how many letters you ask for bot 
# # one letter = - 5
# # correct guess = +25
#     if ask_user == 'guess number':
#         print('If you choose right answer in hard mode then you will get 5 points extra')
#         ask = input ('hard (guess number between 1 to 100) / easy (guess number between 1 to 10) :')
#         if ask == 'hard': 
#             ask1 = int(input ('Enter your guessed number : '))
#             if ask1 == 'computer_choice1':
#                 score += 30
#                 print(f'Correct guessed ! This is your score {score}')
#             else :
#                 print('Wrong answer ! try again later')
#         elif ask == 'easy':
#             print(computer_choice2)
#             ask1 = int(input ('Enter your guessed number : '))
#             if ask1 == 'computer_choice1':
#                 score += 30
#                 print(f'Correct guessed ! This is your score {score}')
#             else :
#                 print('Wrong answer ! try again later')
#     elif ask_user == 'anime name':
#         print ('''"Naruto",
#     "One Piece",
#     "Attack on Titan",
#     "Death Note",
#     "Demon Slayer",
#     "Dragon Ball Z",
#     "Tokyo Ghoul",
#     "Jujutsu Kaisen"''')
#         print ('this is your word length ')
#         display = ['_'] * len(Random_Anime)
#         print(' '.join(display))
#         print()
#         ask = input ('choose a anime character name as showed :').lower().strip()
#         print()
#         if ask == Random_Anime:
#             score += 25
#             print(f'correct guess here is your score :{score}')
#             print()
#         else :
#             ask = input ('wrong guess if you want hint then type (yes/no) :').lower().strip()
#             print()
#             if ask == 'yes':
#                 hints = int(input ('how many hints you want :'))
#                 print()
#                 hint_sol = random.sample(range(len(Random_Anime)), hints)
#                 for pos in hint_sol:
#                     display[pos] = Random_Anime[pos]
#                 print(' '.join(display))
#                 print()
#     elif ask_user == 'song name':
#         print('''"Shape of You",
#     "Believer",
#     "Blinding Lights",
#     "Levitating",
#     "Perfect",
#     "Calm Down"''')
#         print()
#         print ('this is your word length ')
#         display = ['_'] * len(Random_Song)
#         print(' '.join(display))
#         print()
#         ask = input ('choose a song name as showed : ').lower().strip()
#         print()
#         if ask == Random_Song:
#             score += 25
#             print(f'correct guess here is your score :{score}')
#             print()
#         else :
#             ask = input ('wrong guess if you want hint then type (yes/no) :').lower().strip()
#             print()
#             if ask == 'yes':
#                 hints = int(input ('how many hints you want :'))
#                 print()
#                 hint_sol = random.sample(range(len(Random_Song)), hints)
#                 for pos in hint_sol:
#                     display[pos] = Random_Song[pos]
#                 print(' '.join(display))
#                 print()
                
            
# # while True:
# print()
# ask_user = input('what you want to guess (guess number / guess anime name / guess song name ) : ').lower().strip()
# print()
# guess_game()
    
#     # user_input = input('what is you final answer :')