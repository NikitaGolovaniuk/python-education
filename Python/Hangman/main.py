"""Hangman without any tips and tricks"""
from os import system
from random import choice
from urllib.request import Request, urlopen
from colorama import Fore, Back, Style
from frames import get_frame

DICT_LINK = "http://svnweb.freebsd.org/csrg/share/dict/" \
            "words?view=co&content-type=text/plain"
HEADERS = {'User-Agent': 'Mozilla/5.0'}
print(Fore.LIGHTRED_EX + Back.BLACK + Style.BRIGHT)
state = {
    "curr_frame": 0,
    "empty_letters": 0,
    "letter_state": []
}


def clear():
    """clear terminal window for animation"""
    system('clear')


def word_gen(url_dict, headers):
    """Download/make a dictionary if it doesn't exist"""
    req = Request(url_dict, headers=headers)
    with urlopen(req) as webdict:
        webdict = webdict.read().decode('utf-8')
    with open("dictionary.txt", 'w', encoding="utf-8") as file:
        file.write(webdict)
    with open("dictionary.txt", 'r', encoding="utf-8") as file:
        dictionary = file.read().splitlines()
        return choice(dictionary).lower()


def animation(current_frame):
    """Clear console and do frame by frame animation"""
    clear()
    print(get_frame(current_frame))
    print(state["letter_state"])


def game_init():
    """Get word from dictionary"""
    secret_word = word_gen(DICT_LINK, HEADERS)
    state["empty_letters"] = len(secret_word)
    for i in secret_word:
        state["letter_state"].append("|X| ")
        print(i)
    return secret_word


def check_answer(answer, secret_word):
    """check answer and change list of characters"""
    if answer in secret_word:
        for i in range(len(secret_word)):
            if secret_word.startswith(answer, i):
                state["letter_state"][i] = answer
                state["empty_letters"] -= 1
                secret_word = secret_word[:i] + secret_word[i + 1:]
    else:
        state["curr_frame"] += 1


def validate_answer(answer):
    """character must be alphabetic and single"""
    return answer.isalpha() and len(answer) == 1


def game_status(secret_word):
    """game logic"""
    while state["curr_frame"] <= 6 and state["empty_letters"] != 0:
        animation(state["curr_frame"])
        answer = input("Welcome to Nightmire Hangman. There are not any tips"
                       " or tricks. Nobody helps you.\n"
                       "Lets the pain begin.\n").lower()
        if not validate_answer(answer):
            animation("lose")
            break
        check_answer(answer, secret_word)
    if state["empty_letters"] == 0:
        animation("win")
    else:
        animation("lose")


def game():
    """main function"""
    secret_word = game_init()
    game_status(secret_word)


game()
