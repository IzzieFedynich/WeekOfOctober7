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
# A string being multiplied by a number and lot of periods
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

# CheeseBurger spelt out right now letter by letter
print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter %(True, False, False, True))
print(formatter %(formatter, formatter, formatter, formatter))
# Formatter printed in different ways

# Why did I use %r instead of %s

# Time for some strange stuff in the world of printing...

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days)
print("Here are the months:", months)

if print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like
Even 4 lines if we want, or 5, or 6.
""")

#What if I didn't like Jan being listed on the line with the rest of the
# text and away from the other months? How could I fix that?

# More escaping

tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ cat."
taskCat= """
I'll make a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabbyCat)
print(persianCat)
print(backslashCat)
print(taskCat)

# Escape Seq            What does it do
# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \N{name}
# \r
# \t
# \uxxx
# \Uxxxxxx
# \v
# \ooo
# \xhh


# What's the following code do:
# While True:
#       for i in ["/","-","|","\\","|"]
            print("%s\r" % i, ends='')
# Can you replace """ with '''
