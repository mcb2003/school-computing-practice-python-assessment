#!/usr/bin/env python
#random-boardgame   -   the most random boardgame made for a school project
#    Copyright (C) 2017  Michael C Buchan
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#    email:  mikeybuchan@hotmail.co.uk

#create the main board class
class game(object):
    def __init__(self):
        self.board = "43   44   45   46   47   48   49\n\n42   41   40   39   38   37   36\n\n29   30   31   32   33   34   35\n\n28   27   26   25   24   23   22\n\n15   16   17   18   19   20   21\n\n14   13   12   11   10   09   08\n\n01   02   03   04   05   06   07"

boardgame = game()
print(boardgame.board)