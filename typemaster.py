import random

words = ["mountain","nature", "guitar","music","ocean","water", "canvas","art","telescope","astronomy", "piano","instrument""bicycle","transportation","chef"]
count = len(words)
right = 0

while words:
    random_choice = random.choice(words)
    print(random_choice)
    guess = input("Enter a word: ")
    if(guess == random_choice):
        print("correct!")
        right += 1
    else:
        print("wrong")
    
    words.remove(random_choice)

print(f"Accuracy: {right} out of {count}.")