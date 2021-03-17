import keyboard
import os

selected = 1
size = os
size = int(str(size.get_terminal_size()).split("column")[1].split("=")[1].split(",")[0])

# make sure that you add in an array of string options that you want to be able to cycle through: x = Selection_Menu(['hi', 'how', 'sup'])
class Selection_Menu:
    def __init__(self, options):
        self.selected = 1
        self.options = options

    # Manages the way that the console looks:
    def option_maker(self):
        __options__ = self.options

        print("\n" * size)
        for i in range(0, len(__options__)):
            # if self.selected > len(self.options):
            #     self.selected = 0
            #     print(self.selected)
            
            if (i + 1) == self.selected:
                __new__ = (str(i + 1) + ". ") + "> " + __options__[i] + " <"
                print(__new__)
            else:
                __new__ = (str(i + 1) + ". ") + __options__[i]
                print(__new__)

    # Manages the up selection of the console:
    def __selection_up__(self):
        if self.selected == 1:
            self.selected = 4
        else:
            self.selected -= 1
        self.option_maker()

    # Manages the down selection of the console:
    def __selection_down__(self):
        if self.selected == len(self.options):
            self.selected = 1
        else:
            self.selected += 1
        self.option_maker()

    # Keyboard library stuff that will be needed for this to function properly:
    def up(self):
        keyboard.add_hotkey('up', self.__selection_up__)
    def down(self):
        keyboard.add_hotkey('down', self.__selection_down__)
    def wait(self):
        keyboard.wait()


# x = Selection_Menu(selections)
# x.up()
# x.down()
# x.wait()
# keyboard.add_hotkey('up', x.selection_up)
# keyboard.add_hotkey('down', x.selection_down)
# keyboard.wait()

# def show_menu():
#     global selected
#     print("\n" * size)
#    ("Choose an option:")
#     for i in range(1, 5):
#          print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))

# def up():
#     global selected
#     if selected ==      return
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
