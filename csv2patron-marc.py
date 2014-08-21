#!/usr/bin/env python
##########################################
#                                        #
#           csv2patron-marc.py           #
#           by Eric Phetteplace          #
# California College of the Arts, 2014   #
#                                        #
##########################################
#
# This script takes a CSV export from Informer and maps it
# into a format appropriate for import into Millennium.
#
# We should run it once per semester just prior to the semester's
# beginning. Note that a few things should be manually checked:
# - ensure PCODE mappings haven't changed (see mapping.py)
# - look up last day of the semester (this will be the expiration
# date, which is captured in the "-e" flag when the script is run)
# - ensure Informer export column names are consistent with keys in
# the "row" dict (the script will throw exceptions if not)

import csv  # docs.python.org/2/library/csv.html
from mapping import ptype, pcode3  # PCODE mappings, etc.
import datetime
import argparse  # docs.python.org/2.7/library/argparse.html

parser = argparse.ArgumentParser(description='Convert Informer export CSV into'
                                 + ' text file ready for import into '
                                 + 'Millennium')
parser.add_argument('file', type=str, help='CSV from Informer')
parser.add_argument('semester', type=str, choices=['F', 'sp', 'Su'],
                    help='Season of present semester')
parser.add_argument('-o', '--out', type=str, default='import.txt',
                    help='Name for output file')
# hard-coding in Fall 2014 expiration as default
parser.add_argument('-e', '--expiry', type=str, default='12-12-14',
                    help='Patron record expiration date')
args = parser.parse_args()

# used later to construct notes
yr = str(datetime.date.today().year)[2:]


def blanks(i):
    # Return i number of blank spaces
    # Used in places where reading number of blanks is tough
    return ''.join(' ' * i)

# files
csv = csv.DictReader(open(args.file, 'r'))
output = open(args.out, 'w')

for row in csv:
    # "zero field"
    output.write('0')

    # PTYPE & PCODE3 are defined in mapping.py
    # P TYPE
    if row['Academic Level'] in ptype:
        output.write(ptype[row['Academic Level']])
    else:
        output.write(blanks(3))

    # PCODE 1 & 2 are not relevant for students
    # (1 is unused & 2 is faculty  department)
    output.write(blanks(2))

    # PCODE 3 with default to empty string
    # PCODE 3 is a little more complicated because the Informer export
    # contains multiple comma-separated values in a single field. Below,
    # we parse the values into a list and find out which ones are in our
    # PCODE 3 mapping, then add the first available one to the record.
    programs = row['Programs'].split(', ')
    matches = [pcode3[program] for program in programs if program in pcode3]
    try:
        output.write(matches[0])
    # no matches
    except IndexError:
        output.write(blanks(3))

    # Home Library (5 chars), Message Code (1), & Block Code (1)
    # are all left blank
    output.write(blanks(7))

    # Expiration Date, end of fixed-length fields
    output.write(args.expiry + '\n')

    output.write('n' + row['Family Name'] + ', ' + row['Given Name'] + '\n')
    # not worth recording telephone, per Nancy on 7/10/14
    # output.write('t' + row['Home Phone'] + '\n')
    output.write('u' + row['ID'] + '\n')  # student ID
    output.write('z' + row['CCA Email'] + '\n')  # email
    # note - we put in what semester the record was created
    output.write('x' + args.semester + yr + '\n')

# wrapping up
output.close()
