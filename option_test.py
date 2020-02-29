# option_test.py

from option_screen import OptionScreen

def func_1():
    print("func_1.")

def func_2():
    print("func_2.")

def func_3():
    print("func_3.")

selection_screen = OptionScreen(func_1, func_2, func_3,
                                label_one = "First Label",
                                label_two = "Second Label",
                                label_three = "Third Label")

selection_screen.set_color("red")
selection_screen.set_option_message("Welcome to my terminal application: ")
selection_screen.set_separator("___")

selection_screen()
