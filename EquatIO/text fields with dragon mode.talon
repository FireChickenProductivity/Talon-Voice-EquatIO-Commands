speech.engine: dragon
app: EquatIO
not mode: command
and not mode: dictation
-
^finish$:
	key(escape)
	user.talon_mode()


