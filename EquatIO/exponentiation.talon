app: EquatIO
-


<user.equatio_exponentiation_specifier>:
    user.equatio_exponentiation(equatio_exponentiation_specifier)

power: '^'
poof: '^('
puff <number_small>: user.equatio_exponentiate_parenthesized_number(number_small)
poof (transpose|pose):
    insert('^()^T')
    edit.left()
    repeat(2)
