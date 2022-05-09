#1

import cProfile
command = """reactor.run()"""
cProfile.runctx( command, globals(), locals(), filename="OpenGLContext.profile" )

# python runsnake.py result_file.profile
