import os
import sys
print("\033[1;31;40m	face recognition v1.5(beta) \n\033[1;37;40m") # green
print("\033[5;31;40m	developed by Shameel Abdulla  \033[0;31;40m\n")# blink red
print("\033[1;32;40m 1 For Add Face \n 2 For Traine faces \n 3 For Start Reco. \n 4 For Exit") # white
#raw_input("	Press Enter to continue...")
var = eval(input("enter a number between 1 and 4 \n"))
if var==1:
	exec(compile(open('A.py').read(), 'A.py', 'exec'))
elif var==2:
	exec(compile(open('B.py').read(), 'B.py', 'exec'))
elif var==3:
	exec(compile(open('C.py').read(), 'C.py', 'exec'))
elif var==4:
	sys.exit()
elif var!= 1|2|3|4:
	print("\033[5;31;40m Invalid Key\033[0;31;40m\n")# blink red


