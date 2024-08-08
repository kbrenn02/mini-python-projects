
# Types of imports
# 1. import turtle (this means every time you call on it, you have to type turtle.Turtle or turtle.Screen
# 2. from turtle import Turtle (this way you are calling in just one class written as x = Turtle()
# 3. from turtle import * (this imports every class and can make code confusing. Don't do this)
# 4. import turtle as t (this is alias, and allows you to shorten the name of potentially long imports)
        # this will look like the first thing, but shorted: t.Turtle() or t.Screen


import random
import turtle
from turtle import Turtle, Screen
tim = Turtle()
turtle.colormode((255))
tim.shape("turtle")