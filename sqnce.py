#!/usr/bin/python3
#
# Copyright (C) 2019 Mario Alcaraz, Avery King <avery98@pm.me>, and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Imports
from sys import argv
import libsqnce # libsqnce.py

#######################################################
def option(usr_option):
  if (usr_option == "1"):
    term_1 = input("What's the first term in the sequence? ")
    term_2 = input("What's the second term in the sequence? ")
    term_3 = input("What's the third term in the sequence? ")
    term_4 = input("What's the forth term in the sequence? ")

    # Calculate the common difference
    common_difference(term_1, term_2, term_3, term_4)

  else:
    print("Error: Unrecognized option: " + usr_option)
#######################################################

#######################################################
def main_screen(first_run):
  if (first_run == "true"):
    print("=================================\n")
    print("Welcome to sqnce!\n")
    print("=================================\n")

  print("Select an option below:\n\n")
  print("(1) Calculate the common difference")
  usr_option = input(">> ")
  option(usr_option)
#######################################################

main_screen("true")

