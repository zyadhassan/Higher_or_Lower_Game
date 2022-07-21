from Data import data
import Art
import random



end_game=False
wrong_choice=False


while not end_game:
    print(Art.logo)
    score = 0

    choice_A = random.choice(data)
    choice_B = random.choice(data)

    while choice_A == choice_B:
        choice_B = random.choice(data)

    while not wrong_choice:
        print(f"Compare A: {choice_A['name']} , a {choice_A['description']} , from {choice_A['country']}  ")
        print(Art.vs)
        print(f" B: {choice_B['name']} , a {choice_B['description']} , from {choice_B['country']}  ")
        player_choice=str(input("Who has more Followers? Type 'A' or 'B' :")).upper()
        if choice_A['follower_count'] > choice_B['follower_count'] and player_choice=='A':
            choice_B=random.choice(data)
            while choice_A == choice_B:
                choice_B = random.choice(data)
            score+=1
            print(f"You are right  current score = {score}")



        elif choice_A['follower_count'] < choice_B['follower_count'] and player_choice=='B':
            choice_A=choice_B
            choice_B = random.choice(data)
            while choice_A == choice_B:
                choice_B = random.choice(data)
            score += 1
            print(f"You are right  current score = {score}")

        else:
            print(f"Sorry, that is wrong  your final score = {score}")
            wrong_choice=True
    play_more=input("want to play again ? type 'y' or 'n' : ")
    if play_more=='y':
        end_game=False
        wrong_choice=False
    else:
        end_game=True



