#your wish is my command!
import os
import time
def theos():
	global whatos
	try:
		os.system('clear')
		whatos = 'linux'
		return whatos
	except:
		pass
	try:
		os.system('cls')
		whatos = 'windows'
		return whatos
	except:
		pass
	try:
		import console
		console.clear()
		whatos = 'pythonista'
		return whatos
	except:
		pass
def whatoss():
	global clear
	global whatos
	global useless
	useless = 0
	if whatos == 'linux':
		try:
			def clear():
				os.system('clear')
		except:
			def clear():
				useless = 'failed'
	elif whatos == 'windows':
		try:
			def clear():
				os.system('cls')
		except:
			def clear():
				global useless
				useless = 'failed'
	elif whatos == 'pythonista':
		try:
			import console
			def clear():
				console.clear()
		except:
			def clear():
				global useless
				useless = 'failed'
	else:
		whatos = input('insert OS>>> ')
		whatoss()

def setup():
	theos()
	whatoss()

#variables
string = ''
llist = []
checkvar = ''
fix = ''
def somethingwrong():
    whatos = input('what os are you on')
    return whatos
class slowtext():
    def actualslow():
        setup()
        add = ''
        new = ''
        goup = 0
        while goup != len(string):
            add = (string[goup])
            goup = goup + 1
            new = new + add
            print(new)
            time.sleep(0.03)
            clear()
        add = ''
        new = ''
        goup = 0
        print(string)

def maxnum():
	global winner
	nextup = 0
	amountinlist = len(llist)
	winner = llist[nextup]
	while nextup != amountinlist:
		if winner > llist[nextup]:
			nextup = nextup + 1
		else:
			winner = llist[nextup]
			nextup = nextup + 1
	return winner


class check():
	class checkv():
		isv = ''
		try:
			checkvar = checkvar + 1
			checkvar = checkvar - 1
			isv = 'int'
		except:
			pass
		try:
			backup = checkvar
			checkvar = checkvar + 'a'
			checkvar = backup
			isv = 'str'
		except:
			pass
