# Python Help Functions

colors = ('\033[m',       # 0 - no colors
         '\033[0;30;41m', # 1 - red
         '\033[0;30;42m', # 2 - green
         '\033[0;30;43m', # 3 - yellow
         '\033[0;30;44m', # 4 - blue
         '\033[0;30;45m', # 5 - purple
         '\033[7;30m'     # 6 - white
        );
        
def title(msg, color):
	size = len(msg) + 4
	print(colors[color], end = ' ')
	print('~' * size)
	print(f'  {msg}')
	print('~' * size)
	print(colors[0], end = ' ')
	
def helping(comand):
	title(f'Accessing the command manual \' {command}\' ', color = 4)
	print(colors[6], end = ' ')
	help(command)
	print(colors[0], end = ' ')
	
	
command = ' '
while True:
	title('HELP SYSTEM PyHELP', color = 2)
	command = str(input('Enter the name of the function!'))
	if command.upper() == 'END':
		print('Program finished!')
		break	
	else:
		helping(command)
		
title('Until next time!', 1)
		