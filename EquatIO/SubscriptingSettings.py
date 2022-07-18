from talon import Module

module = Module()

@module.action_class
class Actions:
    def equatio_update_subscript_setting(new_value: str):
        '''Updates the subscript setting'''
        current_subscript_scope.update_scope(new_value)

default_subscript_setting = module.setting(
    'equatio_default_subscript_setting',
    type = str,
    default = 'automatic',
    desc = 'This is the subscript setting initially active upon starting up talon',
)

@module.capture(rule = 'automatic|auto|manual|(auto|automatic) numbers')
def equatio_subscript_setting_option(input) -> str:
    initial_word = str(input[0])
    if initial_word == 'auto':
        initial_word = 'automatic'
    if len(input) == 1:
        return initial_word
    return initial_word + ' ' + str(input[1])

@module.scope
def subscript_scope_updater():
    return {'equatio_subscript': current_subscript_scope.get_scope()}

class SettingScopeManager:
    def __init__(self, default, updater):
        self.value = ''
        self.updater = updater
        self.update_scope(default)
        

    def update_scope(self, value):
        self.value = value
        self.updater.update()
    
    def get_scope(self):
        return self.value



current_subscript_scope = SettingScopeManager(default_subscript_setting.get(), subscript_scope_updater)
