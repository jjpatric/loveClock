
import datetime
import time
import math

def getNow():
    return datetime.datetime.now()

def inputToDate(input):
    optionsDict = {
        "1"             : "first  met    ",
        "first met"     : "first  met    ",
        "2"             : "got engaged   ",
        "got engaged"   : "got engaged   ",
        "3"             : "got married   ",
        "got married"   : "got married   ",
        "4"             : "got our puppy ",
        "got our puppy" : "got our puppy "
    }
    option = optionsDict.get(input, "not found")
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


    def fixThing(thing, t, c):
        thing[t-1] = thing[t-1] - 1
        thing[t] = c + thing[t]

    now = getNow()

    diffs = [0, 1, 2, 3, 4, 5]
    diffs[0] = now.year - date.year

    diffs[1] = now.month - date.month
    if (diffs[1] < 0):
        fixThing(diffs, 1, 12)

    diffs[2] = now.day - date.day
    if (diffs[2] < 0):
        fixThing(diffs, 2, 31) # not perfect

    diffs[3] = now.hour - date.hour
    if (diffs[3] < 0):
        fixThing(diffs, 3, 24)

    diffs[4] = now.minute - date.minute
    if (diffs[4] < 0):
        fixThing(diffs, 4, 60)

    diffs[5] = now.second - date.second
    if (diffs[5] < 0):
        fixThing(diffs, 5, 60)
    
    dateStrYM = "{:^4} years {:^2} months".format(diffs[0], diffs[1])
    dateStrDH = "{:^2} days {:^4} hours".format(diffs[2], diffs[3])
    dateStrMS = "{:^6} minutes and {:^8} seconds".format(diffs[4], diffs[5])

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
    print("inputD = ", inputD)
    option = inputToDate(inputD)
    print("option = ", option)
    chosenDate = convertToDate(option)
    print("chosenDate = ", chosenDate)
    displayLove(option, chosenDate)
    input("Do you love me? ")


main()
