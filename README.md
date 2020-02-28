# TERM-Select

#### This is a little GUI application written in Python for the terminal.
#### Its purpose is to make selection screens easy to make if you're writing an application that needs one.

Things to know:
1. Option tags are assigned in order to your desired functions.
2. The up and down arrows go up and down, the left arrow exits the application, and the right one selects that tag.
3. At the moment, red, green and blue are the only available color options.

Here's a simple example of how you could use this:

    def func_1():
        print("func_1.")

    def func_1():
        print("func_2.")

    def func_3():
        print("func_3.")

    selection_screen = OptionScreen(func_1, func_2, func_3,
                                    label_one = "First Function"
                                    label_2 = "Second Function"
                                    label_3 = "Third Function")

    selection_screen.set_color("red")
    selection_screen.set_option_message("Welcome to my terminal application!: ")
    selection_screen.set_separator("___")

    selection_screen()

Here's what it looks like in practice:




![Example](https://i.imgur.com/P2XyrE9.jpg)
