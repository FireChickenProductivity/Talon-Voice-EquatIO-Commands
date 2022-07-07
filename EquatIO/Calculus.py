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
        