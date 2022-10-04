#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 3rd, 2022
# This program calculates the surface area
# and volume of a right regular octagonal prism
# and displays the result back to the user,
# rounded to 2 decimal places, and formats
# the result in the user's choice of units.
import math


# this function calculates the surface area and
# volume of a right regular octagonal prism with
# user input, rounding and custom unit selection.
def main():
    # a little bit of introductory text to explain
    # to the user what this program does
    # and how to use it.
    print("This program will calculate the surface area")
    print("and the volume of a right regular octagonal prism!")
    print("Simply input your base edge value, height value")
    print("and preferred units, and the program will")
    print("do the rest!")
    print("")
    print("Rejoice.")
    print("")
    # getting the input from the user for the base edge,
    # units and height of the right regular octagonal prism
    base_edge = float(
        input("What is the base edge of your right regular octagonal prism?: ")
    )
    height = float(input("What is the height of your right regular octagonal prism?: "))
    units = input("What is the units you'd like to calculate in?: ")

    # process of calculating surface area and volume
    # of a right regular octagonal prism
    surface_area = 8 * base_edge * height + 4 * (1 + math.sqrt(2)) * base_edge**2
    volume = 2 * (1 + math.sqrt(2)) * (base_edge**2) * height

    # displaying the results of the surface area and
    # volume calculations for the right regular octagonal prism
    # with the user's dimensions and units, rounded to
    # two decimal places.
    print("")
    print("This program has calculated the surface area and volume")
    print("of the right regular octagonal prism with the dimensions")
    print("you supplied, in the units you supplied.")
    print("Volume = {:,.2f} {}^3".format(volume, units))
    print("Surface Area = {:,.2f} {}^2".format(surface_area, units))


if __name__ == "__main__":
    main()
