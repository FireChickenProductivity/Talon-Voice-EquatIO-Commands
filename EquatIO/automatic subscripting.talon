app: EquatIO
and user.equatio_subscript: automatic
-
#after the initial variable, will subscript subsequent variable symbols, numbers and subscripts 
<user.equatio_variable_start> <user.equatio_variable_continuation>+:
    user.equatio_insert_variable_with_subscript(equatio_variable_start, equatio_variable_continuation_list)

# if subscripts immediately follow the variable start symbol, they will exponential the start symbol
# instead of going into the subscript
<user.equatio_variable_start> <user.equatio_exponentiation_specifier>+ <user.equatio_variable_continuation>+:
    user.equatio_insert_variable_with_subscript(equatio_variable_start, equatio_variable_continuation_list)
    user.insert_equatio_symbol_list(equatio_exponentiation_specifier_list)

#these versions of the above commands with the word times at the end is part of how I am overriding
#the community repository run multiple times command
<user.equatio_variable_start> <user.equatio_variable_continuation>+ times:
    user.equatio_insert_variable_with_subscript(equatio_variable_start, equatio_variable_continuation_list)
    insert('*')

<user.equatio_variable_start> <user.equatio_exponentiation_specifier>+ <user.equatio_variable_continuation>+ times:
    user.equatio_insert_variable_with_subscript(equatio_variable_start, equatio_variable_continuation_list)
    user.insert_equatio_symbol_list(equatio_exponentiation_specifier_list)
    insert('*')