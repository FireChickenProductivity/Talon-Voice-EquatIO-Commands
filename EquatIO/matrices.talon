app: EquatIO
-

(matrix|mat) <user.equatio_matrix_boundary> <number_small> [by] <number_small>:
    user.equatio_build_matrix_with_boundary(equatio_matrix_boundary, number_small_1, number_small_2)

(matrix|mat) <number_small> [by] <number_small>:
    user.equatio_build_matrix_with_square_boundary(number_small_1, number_small_2)

[matrix|mat] augment <number_small> [by] <number_small>:
    user.equatio_build_matrix_augment(number_small_1, number_small_2)

[matrix|mat] augment <number_small>:
    user.equatio_build_matrix_augment(number_small_1, 1)

column <number_small>:
    user.equatio_build_matrix_with_square_boundary(number_small, 1)

column <user.equatio_matrix_boundary> <number_small>:
    user.equatio_build_matrix_with_boundary(equatio_matrix_boundary, number_small, 1)

(matrix|mat) column <user.equatio_matrix_boundary> <number_small> [by] <number_small>:
    user.equatio_build_column_matrix_with_boundary(equatio_matrix_boundary, number_small_1, number_small_2)
(matrix|mat) column <number_small> [by] <number_small>:
    user.equatio_build_column_matrix_with_square_boundary(number_small_1, number_small_2)

send <user.equatio_small_number_symbol>+:
    user.equatio_input_symbols_into_matrix(equatio_small_number_symbol_list)

toss <user.equatio_small_number_symbol>+:
    user.equatio_input_symbols_into_matrix(equatio_small_number_symbol_list)
    edit.right()

new column:
    key(shift-space)

[(go|move|matrix)] entry <number_small> <number_small>:
    user.equatio_go_to_matrix_entry(number_small_1, number_small_2)
[(go|move|matrix)] first entry:
    user.equatio_go_to_matrix_first_entry()
[(go|move|matrix)] last entry:
    user.equatio_go_to_matrix_last_entry()

[(go|move|matrix)] next entry:
    user.equatio_go_to_matrix_next_entry()
[(go|move|matrix)] (previous|back) entry:
    user.equatio_go_to_matrix_previous_entry()
leave matrix left:
    user.equatio_leave_matrix_left()
leave matrix [right]:
    user.equatio_leave_matrix_right()
