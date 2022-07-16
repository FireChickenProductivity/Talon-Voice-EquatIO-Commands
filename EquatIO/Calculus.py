from talon import actions, Module
from enum import Enum

class IntegralType(Enum):
    DEFINITE = 1
    INDEFINITE = 2

module = Module()

@module.action_class
class Actions:
    def equatio_leibniz_notation_derivative(order: int, differentiation_symbol: str = 'd'):
        '''Inserts the leibniz differentiation notation with the specified order'''
        actions.insert(differentiation_symbol)
        if order != 1:
            actions.user.equatio_exponentiate_text(str(order))
        actions.insert('/')
        actions.insert(differentiation_symbol)
        if order != 1:
            actions.user.equatio_exponentiate_text(str(order))
        actions.edit.line_start()
        actions.edit.right()
    #method currently untested with position_right = True
    def equatio_multi_integral_with_variable(num_integrals: int = 1, variable: str = 'x', integral_type: IntegralType = IntegralType.DEFINITE):
        '''insert multiple intergral signs and positions cursor followed by ()d variable(defaults to x)'''
        actions.insert('(')
        insert_string = '()d' + variable
        actions.insert(insert_string)
        actions.key('home')
        actions.edit.delete()
        actions.user.equatio_multi_integral(num_integrals, integral_type)
        if should_move_cursor_to_the_right_of_the_integral(integral_type):
            actions.edit.right()

    def equatio_multi_integral(num_integrals: int = 1, integral_type: IntegralType = IntegralType.DEFINITE):
        '''insert multiple intergral signs and positions cursor'''
        for i in range(num_integrals):
            actions.insert('\\int ')
            actions.key('left:1')

        if should_move_cursor_to_the_right_of_the_integral(integral_type):
            shift_right = 'right:' + str(3*num_integrals)
        else:
            shift_right = 'right:1'
        actions.key(shift_right)

def should_move_cursor_to_the_right_of_the_integral(type):
    return type == IntegralType.INDEFINITE

@module.capture(rule = 'dub|double|triple')
def equatio_prefix_number(input) -> int:
    if input[0] == 'dub' or input[0] == 'double':
        return 2
    elif  input[0] == 'triple':
        return 3

@module.capture(rule = 'integrate|integral')
def equatio_definite_or_indefinite_integral(input) -> IntegralType:
    word = input[0]
    if word == 'integrate':
        return IntegralType.DEFINITE
    else:
        return IntegralType.INDEFINITE
