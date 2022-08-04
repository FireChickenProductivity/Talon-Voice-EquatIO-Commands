app: EquatIO
and mode: dictation
-
^finish$:
    mode.disable("dictation")
    mode.enable("command")
    user.equatio_exit_text_field()