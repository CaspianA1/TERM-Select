# option_screen.py

import os, sys, tty, termios

curr_pos = 0
func_list = []
label_list = []
COLOR_USED = ""
OPTION_MESSAGE = ""
SEPARATOR = ""

class OptionScreen:
    def __init__(self, *functions, **function_labels):
        for function in functions:
            func_list.append(function)
        for func_label in function_labels.values():
            label_list.append(func_label)

    def __call__(self):
        while True:
            char_input()
            os.system("printf '\033c'")
            exit_status = print_screen()
            if exit_status == "Exit":
                break
            elif exit_status == "Event":
                function = func_list[curr_pos]
                function()
                break
            else:
                continue

    def set_color(self, color):
        global COLOR_USED
        if color == "blue":
            COLOR_USED = "\033[48;5;37m{}\033[0m"
        elif color == "red":
            COLOR_USED = "\033[48;5;124m{}\033[0m"
        elif color == "green":
            COLOR_USED = "\033[48;5;34m{}\033[0m"

    def set_option_message(self, message):
        global OPTION_MESSAGE
        OPTION_MESSAGE = message

    def set_separator(self, separator):
        global SEPARATOR
        SEPARATOR = separator


def write_output(outp):
    with open("output_arrow_tracker.txt", "w") as out_file:
        out_file.write(outp)

class _Getchar:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def char_input():
        in_key = _Getchar()
        while True:
            k = in_key()
            if k != "":
                break
        if k == '\x1b[A':
            write_output("up")
        elif k == '\x1b[B':
            write_output("down")
        elif k == "\x1b[C":
            write_output("begin event")
        elif k == "\x1b[D":
            write_output("exit options")
        else:
            write_output("not an arrow key!")

def read_outp():
    global curr_pos, label_list
    with open("output_arrow_tracker.txt", "r") as output_file:
        outp = output_file.read()
        if outp == "up":
            if curr_pos == 0:
                curr_pos = len(label_list) - 1
                return curr_pos
            else:
                curr_pos -= 1
                return curr_pos

        elif outp == "down":
            if curr_pos == len(label_list) - 1:
                curr_pos = 0
                return curr_pos
            else:
                curr_pos += 1
                return curr_pos

        elif outp == "begin event":
            return "Event"

        elif outp == "exit options":
            return "Exit"

        elif outp == "not an arrow key!":
            return None

def print_screen():
    global label_list, COLOR_USED, OPTION_MESSAGE, SEPARATOR

    outp = read_outp()
    if outp is None or outp == "Exit":
        return "Exit"
    elif outp == "Event":
        return "Event"
    elif outp > len(label_list):
        outp = len(label_list) - 1
    elif outp < 0:
        outp = 0

    print("\n" + OPTION_MESSAGE)
    for text in label_list:
        if outp != label_list.index(text):
            print(text)
            print(SEPARATOR)
        else:
            print(COLOR_USED.format(text))
            print(SEPARATOR)
