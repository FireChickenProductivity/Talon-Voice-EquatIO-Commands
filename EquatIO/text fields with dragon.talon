speech.engine: dragon
mode: command
app: EquatIO
-
^Dragon text$:
	insert('\\text ')
	user.dragon_mode()

