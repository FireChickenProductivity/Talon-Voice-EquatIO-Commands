from talon import Module

module = Module()
@module.action_class
class Actions:
    def equatio_get_infinity_symbol_text() -> str:
        '''Returns the equatio text for inserting the infinity symbol'''
        return r'\infinity '