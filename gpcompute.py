#examle of raw_input calculating pay rate via a floating function

#gp = raw_input ('enter hours')
#gp = int(gp)+1
#rt = raw_input ('enter rate')
#rt = float (rt) 
#pay = gp*rt

#print 'pay'

inp = raw_input ('enter hours: ')
hrs = float(inp)
inp = raw_input ('enter rate: ')
rt = float (inp) 

if hrs <= 40: 
	pay = rt * hrs  
#if hrs > 40:
else: 
	pay = (rt * 40) + (rt * 1.5 * (hrs - 40))
print pay


hrs = raw_input ('enter hours: ')
h = float(hrs)
rt = raw_input ('enter rate: ')
r = float (rt) 


if hrs <= 40: 
	pay = r * hrs  
else: 
	pay = (r * 40) + (r * 1.5 * (hrs - 40))
print pay