app: EquatIO
-
#includes letters and many greek symbols
<user.equatio_variable_start>:
    user.insert_equatio_symbol(equatio_variable_start)

#handles variable start symbol alongside exponentiation
#needed to avoid some of the other commands running and putting the exponent in the subscript
<user.equatio_variable_start> <user.equatio_exponentiation_specifier>+:
    user.insert_equatio_symbol(equatio_variable_start)
    user.insert_equatio_symbol_list(equatio_exponentiation_specifier_list)

#this will subscript numbers but not letters
(straight|flat) <user.equatio_variable_continuation>+:
    user.insert_equatio_symbol_list_with_numbers_sub_scripted(equatio_variable_continuation_list)

#these versions of the above commands with the word times at the end is part of how I am overriding
#the community repository run multiple times command

(straight|flat) <user.equatio_variable_continuation>+ times:
    user.insert_equatio_symbol_list_with_numbers_sub_scripted(equatio_variable_continuation_list)
    insert('*')

<user.equatio_variable_start> <user.equatio_exponentiation_specifier>+ times:
    user.insert_equatio_symbol(equatio_variable_start)
    user.insert_equatio_symbol_list(equatio_exponentiation_specifier_list)
    insert('*')

#updates the subscripting setting to the specified value
subscript (setting|mode|style) <user.equatio_subscript_setting_option>:
    user.equatio_update_subscript_setting(equatio_subscript_setting_option)
