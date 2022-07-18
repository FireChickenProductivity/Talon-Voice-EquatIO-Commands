app: EquatIO
and user.equatio_subscript: automatic numbers
-
#this will subscript numbers but not letters
<user.equatio_simple_variable_text> <number>+:
    insert(equatio_simple_variable_text)
    user.equatio_subscript_list(number_list)

<user.equatio_simple_variable_text> <user.equatio_exponentiation_specifier>+ <number>+:
    insert(equatio_simple_variable_text)
    user.equatio_subscript_list(number_list)
    user.insert_equatio_symbol_list(equatio_exponentiation_specifier_list)
    
