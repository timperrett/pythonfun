#try/except example


rawstr = raw_input('enter a number: ')

try: 
	ival = int(rawstr) #string conversion to integer

#if user input isn't a number, then run the except clause, skip to else statement
except: 
	ival = -1

if ival > 0: 
	print 'awesome!'
else: 
	print 'not a number dude! reenter!'