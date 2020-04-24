# Part 1 calling the game
import random


def hangman():
    word_list = ['cat', 'random', 'dog', 'legumes', 'laptop', 'kindle']
    random_number = random.randint(0, 5)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
              "_____      ",
              "|   |     ",
              "|   O    ",
              "|   |    ",
              "|  /|\   ",
              "|   |    ",
              "|  / \   ",
              "|      "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Benvenuto al Gioco dell'Impiccato")

    # Part 2 Loops the game
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Guess a letter: '
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((''.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You win! It was:')
            print(''.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! It was:\n{}.'.format(word))

hangman()
