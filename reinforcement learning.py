import math
import random

def rockpaperscissors(human,AI):

    if human == 'rock':
        if AI == 'rock':
            return (0,0,0)
        if AI == 'paper':
            return (0,10,0)
        if AI == 'scissors':
            return (0,0,-10)

    if human == 'paper':
        if AI == 'rock':
            return (-10,0,0)
        if AI == 'paper':
            return (0,0,0)
        if AI == 'scissors':
            return (0,0,10)

    if human == 'scissors':
        if AI == 'rock':
            return (10,0,0)
        if AI == 'paper':
            return (0,-10,0)
        if AI == 'scissors':
            return (0,0,0)

def probability(rf,x,y,z):

    numerator = math.exp(rf * x)

    denominator = math.exp(rf * x) + math.exp(rf * y) + math.exp(rf * z)

    return numerator/denominator

#how many rounds the game will run
times = int(input("How many rounds?"))

rf_level = float(input("What's my reinforcement level?"))

phi= float(input("What's my forgetting parameter?"))

R_rock_list = [0]
R_paper_list = [0]
R_scissors_list = [0]

for i in range(times):

    human  = input("rock! paper! scissors!...") 

    strats = {
        'rock': probability(rf_level, R_rock_list[i], R_paper_list[i], R_scissors_list[i]),
        'paper': probability(rf_level, R_paper_list[i], R_rock_list[i], R_scissors_list[i]),
        'scissors': probability(rf_level, R_scissors_list[i], R_paper_list[i], R_rock_list[i])
    }

    hand = [i for i in strats]
    weight = [j for i,j in strats.items()]

    print(strats)

    play = random.choices(hand, weight)[0]

    print("I pick "+ play)

    value = rockpaperscissors(human, play)
    
    if 10 in value:
        print("Game " + str(i+1) +": You lose!")
    elif -10 in value:
        print("Game " + str(i+1) +": You win!")
    else:
        print("Game " + str(i+1) +": Tie!")

    
    R_rock_list.append(R_rock_list[i] * phi + value[0])
    R_paper_list.append(R_paper_list[i] * phi + value[1])
    R_scissors_list.append(R_rock_list[i] * phi + value[2])


#    print(R_rock_list)
#    print(R_paper_list)
#    print(R_scissors_list)
