from talon import actions, Module

from .EquatIO import *

module = Module()
@module.action_class
class Actions:
    def equatio_text_navigation_word_left():
        '''Tries to navigate one word to the left using selection to compute the distance'''
        try:
            actions.edit.extend_line_start()
            text = get_selected_text()
            distance = distance_to_word_left(text)
            actions.edit.right()
            for i in range(distance):
                actions.edit.left()
        except ValueError:
            actions.edit.line_start()
    def equatio_text_navigation_word_right():
        '''Tries to navigate one word to the right using selection to compute the distance'''
        try:
            actions.edit.extend_line_end()
            text = get_selected_text()
            distance = distance_to_word_right(text)
            actions.edit.left()
            for i in range(distance):
                actions.edit.right()
        except ValueError:
            actions.edit.line_end()
#Throws ValueError if no remaining words
def find_next_word_to_the_right(text: str):
    return text.index(' ')

def distance_to_word_right(text: str):
    index = find_next_word_to_the_right(text)
    return index + 1

#Throws ValueError if no remaining words
def find_next_word_to_the_left(text: str):
    return text.rindex(' ')

def distance_to_word_left(text: str):
    index = find_next_word_to_the_left(text)
    return len(text) - index

def get_selected_text():
    with clip.revert():
        actions.edit.copy()
        wait_long_enough_to_let_clipboard_revert_properly()
        result = clip.text()
    return result
