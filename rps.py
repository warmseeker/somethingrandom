import random

plays = ("r p s")

letsplay = input("Lets play rock paper scissors ")

play = input("Type go when you have your play in your mind ")
print("My choice was " + random.choice(plays))
print("r means rock")
print("p means paper")
print("s means scissors")
print("Click run again if we tied or you want to play again.")
