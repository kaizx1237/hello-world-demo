from random_words import RandomWords

i = 10
r = RandomWords()
p = r.random_word()

words = p

wordList = []
wordCens = []
guessedWords = []

for x in words:
    wordList.append(x)
    wordCens.append("*")

print("".join(wordCens))
while "*" in wordCens:
    pos = -1
    userIn = input("Guess a letter: ")


    if userIn in guessedWords:
        print("You have guessed this letter already, here are your total guesses: ")
        print(" ".join(guessedWords))
    else:
        for x in range(len(wordList)):
            if wordList[x] == userIn:
                pos = x
                wordCens[pos] = userIn
                guessedWords.append(userIn)
        if pos > -1:
            print("".join(wordCens))
        else:
            print("".join(wordCens))
            i -= 1
            print("Incorrect, guess again. You have " + str(i) + " tries remaining.")
            guessedWords.append(userIn)

    if i == 0:
        break

if "*" not in wordCens:
    print("Good Job you got the word right! It was " + words)
else:
    print("You didn't get the word, it was " + words)