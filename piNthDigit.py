from decimal import *

print "The higher the decimal point, the more accurate the output will be\n\n"
getcontext().prec = int(raw_input("Enter the to which decimal point you'd like to print \npi including the integer before the decimal point: \n  >>  "))

#Due to the algorithm not being accurate at numbers lower than 5(including), a simple if-elif to output Pi more accurately.
if getcontext().prec == 1:
	print "3."
elif getcontext().prec == 2:
	print "3.1"
elif getcontext().prec == 3:
	print "Pi = 3.14"
elif getcontext().prec == 4:
	print "Pi = 3.141"
elif getcontext().prec == 5:
	print "Pi = 3.1415"
else:

	def factorial(n):
		if n<1:
			return 1
		else:
			return n * factorial(n-1)

	#read more about Chudnovsky's algorithm https://en.wikipedia.org/wiki/Chudnovsky_algorithm
	def chudnovskyAlgorithm(n): #calculate pi to a certain decimal point fast and accurately.
		pi = Decimal(0)
		k = 0
		while k < n:
			pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
			k+= 1
		pi = pi * Decimal(10005).sqrt()/4270934400
		pi = pi**(-1)
		return pi

	print "\t\t\tPi"
	#The program will iterate through the algorithm 20 times to get the most accurate results possible
	for i in xrange(1,21):
		print "Iteration number >",i, ">", chudnovskyAlgorithm(i), " "
