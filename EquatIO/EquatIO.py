from talon import Module, actions, clip

mod = Module()




clipboard_operation_delay = mod.setting(
    'equatio_clipboard_operation_delay',
    type = int,
    default = 200,
    desc = 'How long equatio commands should pause when doing copying and pasting'
)

symbol_input_delay = mod.setting(
    'equatio_symbol_input_delay',
    type = int,
    default = 200,
    desc = 'How long equatio commands should pause when inputting symbols'
)

selection_delay = mod.setting(
    'equatio_selection_delay',
    type = int,
    default = 500,
    desc = 'How long equatio command should pause when selecting'
)

movement_delay = mod.setting(   
    'equatio_movement_delay',
    type = int,
    default = 50,
    desc = 'How long certain commands will pause during movement'
)




POINT_RULE = 'dot|period|point|full stop'
@mod.capture(rule = POINT_RULE)
def equatio_point(input) -> str:
    return '.'

MINUS_RULE = 'minus|dash|hyphen|negative'
@mod.capture(rule = MINUS_RULE)
def equatio_minus(input) -> str:
    return '-'

@mod.capture(rule = '<number_small>|<user.equatio_minus>|<user.equatio_point>')
def equatio_small_number_symbol(input) -> str:
    return input

@mod.action_class
class Actions:
    def equatio_paste_text (text: str):
        '''Used to paste text into EquatIO'''
        paste_text(text)
    def paste_symbol_with_containing_braces (beginning: str, stuff_that_goes_within_braces: str):
        '''Pastes the beginning string and then the stuff in braces enclosed in braces'''
        pass
    def equatio_insert_small_number(number: int):
        '''Inserts a small number'''
        actions.insert(str(number))

    def equatio_type_symbol_name_and_press_enter (symbol_name: str):
        '''Types the symbol name and presses enter'''
        actions.insert(' ' + symbol_name)
        actions.sleep(f'{symbol_input_delay.get()}ms')
        actions.key('enter')

    def equatio_input_symbols_into_matrix(symbols: list):
        '''Inputs the specified symbols into the matrix'''
        for symbol in symbols:
            actions.insert(symbol)
            if str(symbol).isdigit():
                actions.key('escape')
    def equatio_summation():
        '''Creates the summation symbol and moves the cursor to the start of it'''
        paste_text(r'\sum _{ }^{ }')
        actions.edit.left()
        actions.edit.left()
    def equatio_build_product():
        '''Creates the product symbol and moves the cursor to the start of it'''
        paste_text(r'\prod _{ }^{ }')
        actions.edit.left()
        actions.edit.left()

    def equatio_wait_movement_delay():
        '''Waits for the movement delay amount'''
        actions.sleep(f'{movement_delay.get()}ms')
    def equatio_wait_selection_delay():
        '''Waits for the selection delay amount'''
        actions.sleep(f'{selection_delay.get()}ms')
    def equatio_get_selected_text() -> str:
        '''Obtains the selected text through the clipboard'''
        with clip.revert():
            actions.edit.copy()
            wait_long_enough_to_let_clipboard_revert_properly()
            result = clip.text()
        return result


def paste_text (text: str):
	with clip.revert():
		clip.set_text(text)
		actions.edit.paste()
		wait_long_enough_to_let_clipboard_revert_properly()

def wait_long_enough_to_let_clipboard_revert_properly():
	actions.sleep(f'{clipboard_operation_delay.get()}ms')


