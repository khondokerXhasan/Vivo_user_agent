from core.ua import *
from core.logo import *

def user_agent():

	print(banner())
	print('\x1b[38;5;161m[\x1b[38;5;118m+\x1b[38;5;161m] User-Agent : \x1b[38;5;118m{}\n'.format(ua_vivo()))
user_agent()