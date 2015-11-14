# Shear-Calculator
Very simple command line tool for calculating 0-3 / 0-6 km shear and Craven SigSvr index

## Instructions

This program is written in Python 3 and therefore Python 3 is required. Python may be downloaded from the following source (note that users of popular Linux distros likely have Python 3 pre-installed):

https://www.python.org/downloads/

The script can be run by entering:

`python3 shear_craven.py`

The user is prompted whether he/she wants to calculate 0-3 or 0-6 km shear. If 0-6 km is selected, Craven SigSvr index can also be calculated if CAPE is also provided.

Once selecting either 0-3 or 0-6 km shear, the user is prompted to enter information on wind speeds/directions. Wind speeds can be provided in units of knots, km/h or m/s. Wind directions may be provided in either arimuth degrees or cardinal directions.

Shear is reported in units of knots and m/s. Carven SigSvr is reported in units of m3/s3.
