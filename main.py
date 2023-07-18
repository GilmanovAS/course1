# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import utils
from classes.player import Player


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    player = Player(name)
    print(f"Hi, {player.name}")
    random_word = utils.load_random_word()
    stop = True
    while stop and player.count_used_words() < random_word.count_subword():
        print(f"Make {random_word.count_subword()-player.count_used_words()} words from {random_word.word}")
        print(f"Words must be at least 3 letters long.")
        print(f"To end the game, guesses all the words or type 'stop'")
        print(f"Let's go , your {player.count_used_words() + 1} word?")
        candidet = input("Input word: ").lower()
        if candidet in ["stop", "стоп"]: break
        if len(candidet) < 3:
            print("malo")
            continue
        if player.is_used(candidet):
            print("Already has")
            continue
        if random_word.has_subword(candidet):
            print("Yes")
            player.add_word(candidet)
            # print(player.use_word)
        else:
            print("No")
    print(f"Game over!")
    print(f"Your guessed {player.count_used_words()} words")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'What is you name?')
    print_hi(input())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
