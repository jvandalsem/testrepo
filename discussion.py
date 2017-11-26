def discussiontest():

	import random
	print (random.randint(0,10))

#discussiontest()

def numcode():

	number = int(raw_input("Please enter a whole number: "))
	sum = 0
	for i in range(number + 1):
		sum += i
	print sum

#numcode()

def turtletest():

	import turtle
	wn = turtle.Screen()
	me = turtle.Turtle()
	for a in range(5):
		me.penup()
		me.pendown()
		me.circle(45)

#turtletest()

def accumtest():

	farenheit_temps = [70, 45, 90, 30]
	celsius_temps = []
	for a in farenheit_temps:
		celsius_temps.append((a - 32.0) * 5.0 / 9.0)
	print celsius_temps

#accumtest()

def reversetest():
	S = raw_input("Enter a string: ")
	reverse = ""
	for x in range(len(S)):
		reverse += S[-1 - x]
	print reverse

#reversetest()

def filetest():
	j = open("states.csv", 'r')
	p = j.readlines()
	print p

#filetest()

def SquareRootFormula():
	a = raw_input("Enter an 'a' value: ")
	b = raw_input("Enter a 'b' value: ")
	c = math.sqrt((a ** a)+(b ** b))
	print c

#SquareRootFormula()
