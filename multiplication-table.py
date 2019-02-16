"""
multiplication-table.py
Author: MiViriaz15
Credit: 
Assignment:

Write and submit a Python program that prints a multiplication table. The user 
must be prompted to give the width and height of the table before it is printed.

The final multiplication table should look like this:

Width of multiplication table: 10
Height of multiplication table: 8

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
"""
width=int(input("Width of multiplication table: ")) 
height=int(input("Height of multiplication table: "))

width=range(1,width+1)
height=range(1,height+1)



for i in height:
    for j in width:
        print(i, "{0:>3}".format(width[1]*i), "{0:>3}".format(width[2]*i),"{0:>3}".format(width[3]*i), "{0:>3}".format(width[4]*i), "{0:>3}".format(width[5]*i), "{0:>3}".format(width[6]*i),"{0:>3}".format(width[7]*i),"{0:>3}".format(width[8]*i),"{0:>3}".format(width[9]*i), "{0:>3}".format(width[10]*i),"{0:>3}".format(width[11]*i))
