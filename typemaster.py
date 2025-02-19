print("test")
import random

words = ["bug","test","virus"]
while words:
    guess = input("Enter a word: ")
    if(guess == random.choice(words)):
        print("correct!")
    else:
        print("wrong")