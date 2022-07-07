from talon import Module, actions
    
mod = Module()

class VariablePart:
    def __init__(self, type, text):
        self.type = type
        self.text = text
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.__str__()
    
@mod.action_class
class Actions:
    def insert_equatio_symbol(symbol: VariablePart):
        '''Produces the specified equatio symbol'''
        actions.insert(symbol.text)
    def insert_equatio_symbol_list(symbol_list: list):
        '''Inserts the list of equatio symbols'''
        if symbol_list == None:
            return 
        insertion_text = ''
        for element in symbol_list:
            if element.type == 'exponentiation':
                actions.user.equatio_exponentiation(element)
            elif element.type == 'prime':
                actions.insert(PRIME_SYMBOL)
            else:
                actions.insert(element.text)
        actions.insert(insertion_text)
    def insert_equatio_symbol_list_with_numbers_sub_scripted(symbol_list: list):
        '''Inserts the list of equatio symbols with the numbers sub scripted'''
        if symbol_list == None:
            return 
        for element in symbol_list:
            if element.type == 'number or letter' and element.text.isnumeric():
                insert_subscript(element.text)
            else:
                actions.user.insert_equatio_symbol_list([element])
    def equatio_exponentiation(exponent: VariablePart):
        '''Inputs the specified exponent into equatio'''
        actions.user.equatio_exponentiate_text(exponent.text)
        
    def equatio_insert_variable_with_subscript(variable_start: VariablePart, variable_subscript: list):
        '''Inserts the specified subscripted variable'''
        actions.user.insert_equatio_symbol(variable_start)
        actions.insert('_')
        actions.user.insert_equatio_symbol_list(variable_subscript)
        actions.key('right')

    
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
        return VariablePart('prime', '')
    input_length = len(input)
    if input_length == 1:
        word = EXPONENTIATION_SPECIFIER[input[0]]
    else:
        word = str(input.ordinals)
    return VariablePart('exponentiation', word)
    


variable_start_symbols = {
    'alpha': '\\alpha ',
    'beta': '\\beta ',
    'gamma': '\\gamma ',
    'epsilon': '\\epsilon ',
    'zeta': '\\zeta ',
    'eta': '\\eta ',
    'angle': '\\theta ',
    'theta': '\\theta ',
    'iota': '\\iota ',
    'kappa': '\\kappa ',
    'lambda': '\\lambda ',
    'mu': '\\mu ',
    'nu': '\\nu ',
    'xi': '\\xi ',
    'pi': '\\pi ',
    'rho': '\\rho ',
    'sigma': '\\sigma ',
    'tau': '\\tau ',
    'upsilon': '\\upsilon ',
    'phi': '\\phi ',
    'fee': '\\phi  ',
    'chi': '\\chi ',
    'psi': '\\psi ',
    'omega': '\\omega ',
    'small delta': '\\delta ',
}

capital_variable_start_symbols = {
    'gamma': '\\Gamma ',
    'theta': '\\Theta ',
    'lambda': '\\Lambda ',
    'xi': '\\Xi ',
    'pi': '\\Pi ',
    'sigma': '\\Sigma ',
    'phi': '\\Phi ',
    'fee': '\\Phi ',
    'psi': '\\Psi ',
    'omega': '\\Omega ',
}

variable_continuation_symbols = {
    'delta': '\\Delta ',
}

@mod.capture(rule = '[big|tall|ship] (alpha|beta|gamma|epsilon|zeta|small delta|eta|theta|angle|iota|kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|upsilon|phi|fee|chi|psi|omega|<user.letter>)' )
def equatio_variable_start(input) -> VariablePart:
    '''Produces a symbol denoting the start of a variable'''
    if input[0] == 'small' and input[1] == 'delta':
        return VariablePart('variable start', variable_start_symbols['small delta'])
    capitalized = get_variable_capitalization(input)
    word = get_variable_word(input, capitalized)
    if word in variable_start_symbols:
        return VariablePart('variable start', get_greek_variable_text(word, capitalized))
    else:
        return VariablePart('variable start', get_letter_variable_text(word, capitalized))


@mod.capture(rule = '<user.equatio_variable_start>|<number>|delta|<user.equatio_exponentiation_specifier>')
def equatio_variable_continuation(input) -> VariablePart :
    symbol = input[0]
    if type(symbol) == VariablePart:
        return symbol
    elif symbol in variable_continuation_symbols:
        return VariablePart('continuation symbol', variable_continuation_symbols[symbol])
    else:
        return VariablePart('number or letter', str(symbol))

def get_greek_variable_text(word, capitalized):
    if capitalized and word in capital_variable_start_symbols:
        return capital_variable_start_symbols[word]
    else:
        return variable_start_symbols[word]
def get_letter_variable_text(word, capitalized):
    if capitalized:
        return word.upper()
    else:
        return word
def get_variable_capitalization(input):
    return input[0] in ['big', 'tall', 'ship']
def get_variable_word(input, capitalized):
    if capitalized:
        return input[1]
    else:
        return input[0]

def insert_subscript(text):
    actions.insert('_' + text)
    actions.edit.right()
