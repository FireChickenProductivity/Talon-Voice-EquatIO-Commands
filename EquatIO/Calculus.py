from talon import actions, Module

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
    def equatio_multi_integral_with_variable(num_integrals: int = 1, variable: str = 'x',position_right: bool = False):
        '''insert multiple intergral signs and positions cursor followed by ()d variable(defaults to x)'''
        actions.insert('(')
        insert_string = '()d' + variable
        actions.insert(insert_string)
        actions.key('home')
        actions.edit.delete()
        actions.user.equatio_multi_integral(num_integrals , position_right)
    #method currently untested with position_right = True
    def equatio_multi_integral(num_integrals: int = 1, position_right: bool = False):
        '''insert multiple intergral signs and positions cursor'''
        for i in range(num_integrals):
            actions.insert('\\int ')
            actions.key('left:1')

        if position_right:
            shift_right = 'right:' + str(3*num_integrals)
        else:
            shift_right = 'right:1'
        actions.key(shift_right)
    
