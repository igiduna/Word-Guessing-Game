import random

wordList =["frog","lamp","coin","bake","nest",
           "drip","clap","quiz","joke","wind"]
chosenWord = random.choice(wordList)

lives = 5

print("Selection of words: "+ str(wordList))

print(chosenWord)

while lives > 0:

    word = input("\nguess the word: ")

    if word != chosenWord:
        lives -= 1
        print("Lives: " + str(lives))
        if lives == 0:
            print("\ngame over :<")
            break
    else:
        print("\nWINNER ^^")
        break