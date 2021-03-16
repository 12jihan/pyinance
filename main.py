import keyboard
import os

selected = 1
size = os
size = int(str(size.get_terminal_size()).split("column")[1].split("=")[1].split(",")[0])


selections = [
    'option 1',
    'option 2',
    'option 3',
    'option 4',
]


class Selection_Menu:
    def __init__(self, options):
        self.selected = 1
        self.options = options

    def option_maker(self):
        __options__ = self.options

        print("\n" * size)
        for i in range(0, len(__options__)):
            if self.selected > len(self.options):
                self.selected = 0
                print(self.selected)
            
            if (i + 1) == self.selected:
                __new__ = (str(i + 1) + ". ") + "> " + __options__[i] + " <"
                print(__new__)
            else:
                __new__ = (str(i + 1) + ". ") + __options__[i]
                print(__new__)

    # def __selection_position___(self, position):
    #     __position__ = position


x = Selection_Menu(selections)
x.selected += 1
x.option_maker()

# def show_menu():
#     global selected
#     print("\n" * size)
#     print("Choose an option:")
#     for i in range(1, 5):
#          print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))

# def up():
#     global selected
#     if selected == 1:
#         return
#     selected -= 1
#     show_menu()


# def down():
#     global selected
#     if selected == 4:
#         return
#     selected += 1
#     show_menu()

# show_menu()
# keyboard.add_hotkey('up', up)
# keyboard.add_hotkey('down', down)
# keyboard.wait()

# print("\n" * 73)
