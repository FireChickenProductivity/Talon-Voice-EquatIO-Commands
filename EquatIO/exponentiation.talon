app: EquatIO
-


<user.equatio_exponentiation_specifier>:
    user.equatio_exponentiation(equatio_exponentiation_specifier)

power: '^'
poof: '^('
poof (transpose|pose):
    insert('^()^T')
    edit.left()
    repeat(2)
