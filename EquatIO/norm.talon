app: EquatIO
-
norm: user.equatio_insert_norm_operator_around_cursor()
norm <number_small>: user.equatio_insert_norm_operator_with_subscript_around_cursor(number_small)
norm (infinite|infinity): user.equatio_insert_norm_operator_with_subscript_around_cursor(user.equatio_get_infinity_symbol_text())