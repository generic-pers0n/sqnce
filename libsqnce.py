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

from sys import argv

# term_1 = -9, term_2 = -5
def common_difference(term_1, term_2, term_3, term_4):
  common_diff = 0

  term_1_inc = term_1

  # We know that term 1 and term 2 will not have the same value,
  # so we need to increment the diff
  while (term_1_inc != term_2 + 1):
    common_diff += 1 # Increment common_diff
    term_1_inc += 1

    # If term 1 is equal to term 2, then break
    if (term_1 == term_2):
      break;

  print("The common difference is ", common_diff)

