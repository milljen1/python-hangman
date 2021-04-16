def print_game(misses = 0, guesses = [], answer = ''):
    print("missed: " + str(misses))
    print("guesses: " + str(guesses))
    print("answer: " + answer)

answer = "hangman"
guesses = []
misses = 0
solved = False

while(solved == False):
    input("Pick a letter:")
    print_game(misses, guesses, answer)