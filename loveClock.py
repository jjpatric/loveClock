#!python3.6

import datetime
import time
import math

def getNow():
    return datetime.datetime.now()


def inputToDate(input):
    optionsDict = {
        "1"             : "   first  met   ",
        "first met"     : "   first  met   ",
        "2"             : "   got engaged  ",
        "got engaged"   : "   got engaged  ",
        "3"             : "   got married  ",
        "got married"   : "   got married  ",
        "4"             : "  got our puppy ",
        "got our puppy" : "  got our puppy "
    }
    option = optionsDict.getKey(input, "not found")
    return option


def convertToDate(chosenOption):

    optionSwitcher = {
        "first  met    "    : datetime.datetime(2018, 3, 3, 22, 30),
        "got engaged   "  : datetime.datetime(2018, 11, 14, 21, 20),
        "got married   "  : datetime.datetime(2019, 2, 15, 18, 30),
        "got our puppy " : datetime.datetime(2019, 1, 10, 10, 10)
    }

    chosenDate = optionSwitcher.get(chosenOption, "not found")

    return chosenDate


def displayLove(option, date):

    def calculateTimeSince(date):
        return date - getNow()


    def fixThing(thing):
        thing[0] = thing[0] - 1
        thing[1] = 12 + thing[1]

    now = getNow()

    years = now.year - date.year
    months = now.month - date.month
    if (months < 0):
        fixThing([years, months, 12])
    days = now.day - date.day
    if (days < 0):
        fixThing([months, days, 31]) # not perfect
    hours = now.hour - date.hour
    if (hours < 0):
        fixThing([days, hours, 24])
    minutes = now.minute - date.minute
    if (minutes < 0):
        fixThing([hours, minutes, 60])
    seconds = now.second - date.second
    if (seconds < 0):
        fixThing([minutes, seconds, 60])

    dateStrYM = "{:^4} years {:^2} months".format(years, months)
    dateStrDH = "{:^2} days {:^4} hours".format(days, hours)
    dateStrMS = "{:^6} minutes and {:^8} seconds".format(minutes, seconds)

    print("               ------                     -------               ")
    print("             ./      \.                 ./       \.             ")
    print("           ./          \.             ./           \.           ")
    print("         ./              \.         ./               \.         ")
    print("       ./                  \.     ./                   \.       ")
    print("       |                     \___/                       |      ")
    print("       |                                                 |      ")
    print("        \                We %s              /       "% (option))
    print("         \                                             /        ")
    print("          \           %s            /         "% (dateStrYM))
    print("           \            %s           /          "% (dateStrDH))
    print("            \. %s ./           "% (dateStrMS))
    print("              \.                                 ./             ")
    print("                \..           ago             ../               ")
    print("                   \..                     ../                  ")
    print("                      \_    I LOVE YOU   _/                     ")
    print("                        \_             _/                       ")
    print("                          \__       __/                         ")
    print("                             \_   _/                            ")
    print("                               ---                              ")


def loveClock():
    print("Hello my love! \n\n\nI made this program to show you how much I love every ")
    print("single moment I get to spend with you <3\n\n\n")
    print("I have made this program for you to show you that every moment counts\n")
    chosenDate = input("Please enter one of the following important dates...\n"
        "1 First met\n"
        "2 Got engaged\n"
        "3 Got Married\n"
        "4 Got our puppy\n")
    return chosenDate


def main():
    inputD = loveClock()
    option = inputToDate(inputD)
    chosenDate = convertToDate(option)
    displayLove(option, chosenDate)
    input("Do you love me?")


main()
