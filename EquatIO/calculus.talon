app: EquatIO
-

#limits
goes to: '\\to '
limit: 'lim_'

#integration

[<user.equatio_prefix_number>] <user.equatio_definite_or_indefinite_integral>:
    user.equatio_multi_integral(equatio_prefix_number or 1, equatio_definite_or_indefinite_integral)

(integrate|integration|integral|from) line: 
    user.equatio_paste_text('\\stackrel{{\\mid }}{{\\stackrel{{\\mid }}{{\\stackrel{{\\mid }}{{\\ }}}}}}_{{ }}^{{ }}')
    edit.left()
    repeat(1)

[<user.equatio_prefix_number>] <user.equatio_definite_or_indefinite_integral> (with|of) [respect to] <user.equatio_simple_variable_text>+:
    user.equatio_multi_integral_with_variable(equatio_prefix_number or 1, equatio_simple_variable_text_list, equatio_definite_or_indefinite_integral)

#differentiation
prime: "'"
partial|part: '\\partial '
derive: 'd/d'
derive [order|by] <number_small>: user.equatio_leibniz_notation_derivative(number_small)
derive [order|by] <number_small> of <user.equatio_simple_variable_text>:
    user.equatio_leibniz_notation_derivative(number_small)
    insert(equatio_simple_variable_text)
    key(escape)
(partial|part) (derive|drive|rive): '\\partial /\\partial '
(partial|part) (derive|drive|rive) [order|by] <number_small>: user.equatio_leibniz_notation_derivative(number_small, '\\partial ')
(partial|part) (derive|drive|rive) [order|by] <number_small> of <user.equatio_simple_variable_text>:
    user.equatio_leibniz_notation_derivative(number_small, '\\partial ')
    insert(equatio_simple_variable_text)
    key(escape)
