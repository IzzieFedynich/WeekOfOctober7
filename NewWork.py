x = "There are %d tupes of people." % 10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s." % (binary, doNot)
#plugging in 2 strings into 2 types of people

print(x)
print(y)
#printing out "there are 10 types of people"

print("I said: %r" % x)
#plugging in a string into this joke
print("I also said: '%s'." % y)
#plugging in a string into this joke

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)
#Evaluation and 2 strings for the joke above

w = "This is the left side of..."
e = "a string with a right side."
#w and e strings for this joke down here

print(w + e)
#left and right side of a string

# More stuff 10/8

# Mary had a little lamb printed in a string
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
# A string being multiplied by a number and lot of periods?
print("." * 10)

# CheeseBurger spelt out with a string
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# CheeseBurger
print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter %(True, False, False, True))
print(formatter %(formatter, formatter, formatter, formatter))
# Formatter printed in different ways

# Why did I use %r instead of %s

