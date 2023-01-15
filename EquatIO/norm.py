from talon import Module, actions
from typing import Union
subscript_type = [int, str]

module = Module()
@module.action_class
class Actions:
    def equatio_insert_norm_operator():
        '''Inserts the norm operator into equatio'''
        actions.user.equatio_insert_norm_operator_around_cursor()
        exit_norm_right()
    
    def equatio_insert_norm_operator_with_subscript(subscript: subscript_type):
        '''Inserts the norm operator into equatio with the specified subscript'''
        actions.user.equatio_insert_norm_operator()
        insert_subscript(str(subscript))
    
    def equatio_insert_norm_operator_around_cursor():
        '''Inserts the norm operator into equatio around the cursor'''
        actions.insert('||')
        actions.edit.left()
        actions.insert('|')
    
    def equatio_insert_norm_operator_with_subscript_around_cursor(subscript: subscript_type):
        '''Inserts the norm operator into equatio with the specified subscript around the cursor'''
        actions.user.equatio_insert_norm_operator_with_subscript(subscript)
        exit_subscript_left()
        enter_norm_operator_from_left()
    
def insert_subscript(subscript: str):
    actions.insert('_' + subscript)

def enter_norm_operator_from_left():
    actions.edit.left()
    actions.edit.left()

def exit_norm_right():
    actions.edit.right()
    actions.edit.right()

def exit_subscript_left():
    actions.key('shift-escape')