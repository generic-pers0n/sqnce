#!/usr/bin/python3
#
# Copyright (C) 2019 Mario Alcaraz <captainamario2006@gmail.com>, Avery King <avery98@pm.me>, and contributors
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

from sys import argv
import os

def clear():
  if (os.name == "posix"):
    os.system("clear")
  elif (os.name == "nt"):
    os.system("cls")

def common_difference(term_1, term_2, term_3, term_4):
  common_diff_1 = 0 # Common difference
  common_diff_2 = 0
  common_diff_overall = 0

  term_1_inc = term_1
  term_2_inc = term_2

  # We know that term 1 and term 2 will not have the same value,
  # so we need to increment the common difference. When we
  # increment the common difference, we basically count it.
  while (term_1 != term_2):
    common_diff_1 += 1 # Increment common_diff
    term_1_inc += 1

    # If term 1 is equal to term 2, then break
    if (term_1_inc == term_2):
      common_diff_overall = common_diff_1
      break;

    # If the common difference is NOT constant, subtract the 2nd
    # common difference variable from the first common differece
    # variable. We'll assume that this will be constant. In other
    # words, the common difference increases per term (e.g. 1, 2, 5, 10...,
    # the common difference is increasing by 2 (1 to 3 to 5 and etc).
    if (term_1_inc != term_2):
      while (ter_1_inc != term_2):
        common_diff_2 +=1 # Increment this until it equals term 3
        term_2_inc += 1

        if (term_2_inc == term_3):
          common_diff_overall = common_diff_2

  # That should work for arithmetic sequences that either have a
  # constant or a non-constant common difference. Either me
  # (@generic_pers0n) or Mario (@Megitsune-MA) will figure out how
  # to solve geometric sequences one time. For now, that remains a
  # mystery.

  print("The common difference is ", common_diff_overall)

