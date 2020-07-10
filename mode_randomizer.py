import numpy as np
from time import sleep
from sys import exit

modes = ["Lydian", "Ionian", "Mixolydian", "Dorian", "Aiolian", "Phrygian", "Locrian"]
keys = ["C", "F", "Bb", "Eb", "Ab", "Db/C#", "Gb", "Cb/B", "E", "A", "D", "G"]
strings = ["E", "A", "D", "G"]


def get_random_mode():
    rand_idx = np.random.randint(0, len(modes))
    return modes[rand_idx]


def get_random_key():
    rand_idx = np.random.randint(0, len(keys))
    return keys[rand_idx]


def get_random_string():
    rand_idx = np.random.randint(0, len(strings))
    return strings[rand_idx]


def get_random_mode_and_key():
    return f"Mode: {get_random_mode()}", f"Key: {get_random_key()}"  # 2-Tuple


def get_random_mode_key_and_string():
    return f"Mode: {get_random_mode()}", f"Key: {get_random_key()}", f"{get_random_string()}"  # 3-Tuple


def user_input_mode():
    print("User input mode initiated. Press 'S' or 's' to exit program or any other key\n"
          "to continue with next (mode, key, string) configuration.\n")
    sleep(3)
    while True:
        print(get_random_mode_key_and_string())
        inp_ui = input().strip().lower()
        if inp_ui == 's':
            break


def ready_go():
    sleep(3)
    print("Ready...")
    sleep(2)
    print("Go!")
    sleep(1)


def constant_looping_mode():
    delay = 3  # An integer delay to pad the sleeping seconds, which are calculated by the user-provided BPM.
    print("Constant looping mode initiated. 8 notes per 4 beat measure are assumed,\n"
          "so every note is an eighth rhythm. For two octaves, this means 15 beats total.\n")
    sleep(3)
    while True:
        inp_loop = input("Please provide a BPM between 30 and 300: ")
        if inp_loop.isnumeric() and (30 <= int(inp_loop, 10) <= 300):
            print(f"We are adding a delay of {delay} seconds to make it easier to switch to the next configuration.\n"
                  "You may stop the program at any time by using Ctrl / CMD + C.")
            ready_go()
            while True:  # Can end execution with Ctrl / CMD + c
                inp_loop = int(inp_loop)
                print(get_random_mode_key_and_string())
                seconds = 15 / (inp_loop / 60)
                sleep(delay + seconds)


if __name__ == '__main__':
    print("Welcome! This program randomizes modes, keys and string-crossings\n"
          "for the 4-string bass guitar when practicing 2-octave mode exercises,\n"
          "up and down in pitch. This gives us a total of 30 notes that are to be \n"
          "played with every provided configuration.\n")
    sleep(3)
    print("It is a very easy program to modify. Feel free to e-mail jason.filippou@gmail.com\n"
          "with any modifications you might want to suggest.\n")
    sleep(3)
    while True:
        inp = input("Press 'U' for User Input Mode or 'L' for Looping mode.").strip().lower()
        if inp == 'u':
            user_input_mode()
            break
        elif inp == 'l':
            try:
                constant_looping_mode()
                break
            except KeyboardInterrupt:
                print(" Loop halted by user. Exiting...")
                sleep(1)
                exit(0)
    print("Exiting...")
    sleep(1)
