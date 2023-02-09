app: EquatIO
-
text: user.equatio_make_text_field()
text dictate:
  user.equatio_make_text_field()
  user.equatio_switch_to_dictation_mode()
text window:
  user.equatio_make_text_field()
  user.equatio_switch_to_dictation_mode()
  user.equatio_dictation_start_new_draft()

weild <user.word>:
  user.equatio_insert_with_text_field(word)
peeled <user.word>:
  capital_word = user.formatted_text(word, "hammer")
  user.equatio_insert_with_text_field(capital_word + ' ')
warp <user.word>:
  user.equatio_padded_insert_with_text_field(word)
sealed <user.prose>:
  user.equatio_padded_insert_with_text_field(prose)
