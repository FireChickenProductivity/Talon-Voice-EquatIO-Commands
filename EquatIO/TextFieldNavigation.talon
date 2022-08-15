app: EquatIO
mode: dictation
mode: command
-



swim left: user.equatio_text_navigation_word_left()
swim right: user.equatio_text_navigation_word_right()
swim left <number_small>: user.equatio_text_navigation_words_left(number_small)
swim right <number_small>: user.equatio_text_navigation_words_right(number_small)
swim (select|cell) left <number_small>: user.equatio_text_select_words_left(number_small)
swim (select|cell) right <number_small>: user.equatio_text_select_words_right(number_small)
