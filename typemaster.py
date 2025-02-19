print("test")
import random

words = ["bug","test","virus"]
while words:
    random_choice = random.choice(words)
    guess = input("Enter a word: ")
    if(guess == random_choice):
        print("correct!")
    else:
        print("wrong")
    
    words.remove(random_choice)