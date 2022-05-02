import random

name = input("What is your name? ")

print()
print(f"Welcome to the game Hilo {name}!")
print()
print("The Game is simple. You will start with 300 points.")
print("Individual Cards will be displayed represented as numbers 1 - 13")
print("The first card will be displayed. Your task is to simply guess if the next card will be higher or lower than the previous card.")
print("If you are correct you gain 100 points!")
print("If you are incorrect you will lose 75 points.")
print()
print("If you reach 0 points you lose. As long as you have higher than 0 points you can keep playing.")
print("At the end of each turn you will decide if you would like to keep playing or not.")
print("Deciding to discontiune means the game is over and you win as long as you have higher than 0 points.")

value = 0
#classes of players and cards
class Card:
    def __init__(self, number):
        self.number = number
    def value(self):
        value = random.randint(1, 13)
        print(value)


#c1=Card(1)
score = 300
play = "yes"

#c1.value()
#print(value)
while score > 0 and play.lower() == "yes":
    if play.lower() == "yes":
        print()
        print(f"Your score is {score}")
        card1 = random.randint(1, 13)
        print(f"The card is {card1}.")
        print()
        answer = input("Will the next card be Higher or Lower? ")

        card2 = random.randint(1, 13)
        print(f"The card is {card2}")
        if card1 > card2 and answer.lower() == "lower":
            score += 100
            print(f"That is correct! Your score is {score}")
        elif card1 < card2 and answer.lower() == "higher":
            score += 100
            print(f"That is correct! Your score is {score}")
        elif card1 > card2 and answer.lower() == "higher":
            score -= 75
            print(f"Sorry, that is incorrect. Your score is {score}")
        elif card1 < card2 and answer.lower() == "lower":
            score -= 75
            print(f"Sorry, that is incorrect. Your score is {score}")


        if score <= 0:
            play = "no" 
        elif score > 0:
            play = input("Would you like to keep playing? (yes/no) ")
        
        if play.lower() == "no":
            if score > 0:
                print(f"Congradulations, you finished with a score of {score}")
            elif score < 1:
                print(f"Your score is less than 0 ({score}) you lose, GAME OVER.")
