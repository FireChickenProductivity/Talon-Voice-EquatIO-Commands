app: EquatIO
-

#limits
goes to: '\\to '
limit: 'lim_'

#integration
integrate: '\\int '
dubintegrate:
    user.equatio_multi_integral(2)
triple integrate:
    user.equatio_multi_integral(3)
integral:
    insert('\\int ')
    key(right:2)
(integrate|integration|integral|from) line: 
    user.equatio_paste_text('\\stackrel{{\\mid }}{{\\stackrel{{\\mid }}{{\\stackrel{{\\mid }}{{\\ }}}}}}_{{ }}^{{ }}')
    edit.left()
    repeat(1)

dubintegrate (with|of) [respect to] <user.equatio_simple_variable_text>:
    user.equatio_multi_integral_with_variable(2, equatio_simple_variable_text)
triple integrate (with|of) [respect to] <user.equatio_simple_variable_text>:
    user.equatio_multi_integral_with_variable(3, equatio_simple_variable_text)

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
