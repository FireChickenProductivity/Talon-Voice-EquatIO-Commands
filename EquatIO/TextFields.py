from talon import actions, Module

module = Module()
@module.action_class
class Actions:
    def equatio_make_text_field():
        '''Makes an equatio text field'''
        actions.insert('\\text ')
    def equatio_exit_text_field():
        '''Exits the text field'''
        actions.key('escape')
    def equatio_switch_to_dictation_mode():
        '''Switches to dictation mode'''
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        actions.user.code_clear_language_mode()
        actions.mode.disable("user.gdb")
    def equatio_dictation_start_new_draft():
        '''Opens the draft window and selects all the text'''
        start_new_draft()
    def equatio_insert_with_text_field(text: str):
        '''Creates a text field, inserts the text into it, and exits the text field'''
        actions.user.equatio_make_text_field()
        actions.insert(text)
        actions.user.equatio_exit_text_field()
    def equatio_padded_insert_with_text_field(text: str):
        '''Creates a text field, inserts the text into it padded with spaces, and exits the text field'''
        actions.user.equatio_insert_with_text_field(' ' + text + ' ')
    def equatio_convert_text_to_capitalized_case(text: str) -> str:
        '''Converts the text to capitalized case'''
        return text.capitalize()
        
def start_new_draft():
    open_draft()
    actions.edit.select_all()

def open_draft():
    actions.user.draft_hide()
    actions.user.draft_show()
