from talon import Module, actions
    
mod = Module()

from .VariablePart import VariablePart
    
EXPONENTIATION_SPECIFIER = {
    'squared': '2',
    'cubed': '3',
    'inverse': '-1',
    'transpose': 'T',
}

PRIME_SYMBOL = "'"



@mod.capture(rule = 'squared|cubed|inverse|transpose|prime|(to the <user.ordinals>)')
def equatio_exponentiation_specifier(input) -> VariablePart:
    if input[0] == 'prime':
        return VariablePart('prime', PRIME_SYMBOL)
    input_length = len(input)
    if input_length == 1:
        word = EXPONENTIATION_SPECIFIER[input[0]]
    else:
        word = str(input.ordinals)
    return VariablePart('exponentiation', word)
    

@mod.action_class
class Actions:
    def equatio_exponentiation(exponent: VariablePart):
        '''Inputs the specified exponent into equatio'''
        actions.user.equatio_exponentiate_text(exponent.text)
    def equatio_exponentiate_text(exponent: str):
        '''Performs the desired exponentiation'''
        actions.insert('^' + exponent)
        actions.edit.right()
    def equatio_exponentiate_parenthesized_number(number: int):
        '''Performs the exponentiation of the specified number in parentheses'''
        number_string = str(number)
        actions.user.equatio_exponentiate_text('(' + number_string + ')')
    def equatio_exponentiate_parenthesized_transposed_number(number: int):
        '''Performs the exponentiation of the specified number in parentheses and transposed'''
        number_string = str(number)
        actions.insert(f'^({number_string})^T')
        actions.edit.right()
        actions.edit.right()
