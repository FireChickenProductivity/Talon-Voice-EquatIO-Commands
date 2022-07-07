speech.engine: dragon
mode: all
app: EquatIO
-
^text field$:
	insert('\\text ')
	user.dragon_mode()

^finish$:
	key(escape)
	user.talon_mode()


