app: EquatIO
-

#limits
goes to: '\\to '
limit: 'lim_'

integrate: '\\int '
dubintegrate:
    insert('\\int ')
    key(right:2)
    insert('\\int ')
    key(left:3)
triple integrate:
    insert('\\int ')
    key(right:2)
    insert('\\int ')
    key(right:2)
    insert('\\int ')
    key(left:6)
integral:
    insert('\\int ')
    key(right:2)
(integrate|integration|integral|from) line: 
    user.equatio_paste_text('\\stackrel{{\\mid }}{{\\stackrel{{\\mid }}{{\\stackrel{{\\mid }}{{\\ }}}}}}_{{ }}^{{ }}')
    edit.left()
    repeat(1)
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
