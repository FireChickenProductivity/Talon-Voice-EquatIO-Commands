from talon import actions, Module, clip

from .EquatIO import *

#todo: Clean the considerable repetition in this file
module = Module()
individual_selection_delay = module.setting(
    'equatio_individual_selection_delay',
    type = int,
    default = 10,
    desc = "How long to delay when selecting a single character in milliseconds."
    "Increase this if individual selection is not working."
)
def wait_for_individual_selection_delay():
    actions.sleep(f'{individual_selection_delay.get()}ms')


@module.action_class
class Actions:


    def equatio_text_navigation_words_left(num_words: int):
        '''Tries to navigate num_words words to the left using selection to compute the distance'''
        try:
            actions.edit.extend_line_start()
            text = get_selected_text()
            distance = distance_to_nth_word_left(text,num_words)
            actions.edit.right()
            for i in range(distance):
                actions.edit.left()
        except ValueError:
            actions.edit.line_start()

    def equatio_text_select_words_left(num_words: int):
        '''Tries to select num_words words to the left using selection to compute the distance'''
        try:
            actions.edit.extend_line_start()
            text = get_selected_text()
            distance = distance_to_nth_word_left(text,num_words)
            actions.edit.right()
            for i in range(distance):
                actions.edit.extend_left()
                wait_for_individual_selection_delay()
        except ValueError:
            actions.edit.extend_line_start()
 
    def equatio_text_navigation_words_right(num_words: int):
        '''Tries to navigate num_words words to the right using selection to compute the distance'''
        try:
            actions.edit.extend_line_end()
            text = get_selected_text()
            distance = distance_to_nth_word_right(text,num_words)
            actions.edit.left()
            for i in range(distance):
                actions.edit.right()
        except ValueError:
            actions.edit.line_end()

    def equatio_text_select_words_right(num_words: int):
        '''Tries to select num_words words to the right using selection to compute the distance'''
        try:
            actions.edit.extend_line_end()
            text = get_selected_text()
            distance = distance_to_nth_word_right(text,num_words)
            actions.edit.left()
            for i in range(distance):
                actions.edit.extend_right()
                wait_for_individual_selection_delay()
        except ValueError:
            actions.edit.extend_line_end()

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
            distance = distance_to_nth_word_right(text)
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
   
   
def distance_to_nth_word_left(text: str,num_words:int = 1):
    words = text.split(" ")
    if len(words) <= num_words: raise ValueError
    else:
        # initalize distance to number of words to include spaces
        distance = num_words
        # add the length of the words included
        for i in range(num_words):
            distance += len(words[-i-1])
        return distance

def distance_to_nth_word_right(text: str,num_words:int = 1):
    words = text.split(" ")
    if len(words) <= num_words: raise ValueError
    else:
        # initalize distance to number of words to include spaces
        distance = num_words
        # add the length of the words included
        for i in range(num_words):
            distance += len(words[i])
        return distance