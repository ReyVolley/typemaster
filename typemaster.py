import random

words = ["bug","test","virus"]
right = 0
wrong = 0

while words:
    random_choice = random.choice(words)
    print(random_choice)
    guess = input("Enter a word: ")
    if(guess == random_choice):
        print("correct!")
        right += 1
    else:
        print("wrong")
        wrong += 1
    
    words.remove(random_choice)