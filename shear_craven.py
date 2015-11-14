
print ('''
____________________________________________________________

    Welcome to the shear calculator!
____________________________________________________________
''')

import math
import time

#constants
kmh2ms = 0.277777778
kmh2kn = 0.539957
kn2ms = 0.514444444
ms2kn = 1.94384449

def calculate_shear(a, b, c, d):
    return (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(abs(d - c)))) ** 0.5

def convert_to_degrees(dir):
    dir = dir.upper()
    if dir == "N":
        return 0
    elif dir == "NNE":
        return 22.5
    elif dir == "NE":
        return 45
    elif dir == "ENE":
        return 67.5
    elif dir == "E":
        return 90
    elif dir == "ESE":
        return 112.5
    elif dir == "SE":
        return 135
    elif dir == "SSE":
        return 157.5
    elif dir == "S":
        return 180
    elif dir == "SSW":
        return 202.5
    elif dir == "SW":
        return 225
    elif dir == "WSW":
        return 247.5
    elif dir == "W":
        return 270
    elif dir == "WNW":
        return 292.5
    elif dir == "NW":
        return  315
    elif dir == "NNW":
        return 337.5
    else:
        print ("A wind direction was not provided")

def unit_converter(unit, speed):
    unit = unit.replace(" ", "")
    if unit == "km/h" or unit == "kmh" or unit == "kmh-1" or unit == "km" or unit == "kph":
        return speed * kmh2kn
    elif unit == "m/s" or unit == "ms" or unit == "ms-1" or unit == "m":
        return speed * ms2kn
    elif unit == "knots" or unit == "knot" or unit == "kn":
        return speed
    else:
        print ("Please enter knots, km/h or m/s")

def dir_degrees(a):
    b = a.replace(".", "")
    if b.isdigit():
        return float(a)
    else:
        return convert_to_degrees(a)

def craven_sigsvr(cape, shear):
    return cape * shear

units = ["km/h", "kmh", "kmh-1", "km", "kph", "m/s", "ms", "ms-1", "m", "knots", "knot", "kn"]

wind_directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]


while True:
    type = input("\n\nTo calculate 0-3 km shear, enter: 3 \nTo calculate 0-6 km shear, enter: 6\nTo quit, enter: q\n: ")
    print ("\n")

    if type == '3':
        while True:
            surfacewind = input("Enter surface wind speed: ")
            surfacewind_nodp = surfacewind.replace(".", "")
            if surfacewind_nodp.isdigit() and surfacewind.count(".") <= 1:
                surfacewind = float(surfacewind)
                break
            else:
                print ("Enter a numerical value.")

        while True:
            surfaceunits = input("Units: ")
            surfaceunits = surfaceunits.replace(" ", "")
            surfaceunits = surfaceunits.replace(".", "")
            if surfaceunits in units:
                break
            else:
                print ("Please enter knots, km/h or m/s.")

        while True:
            surfacedirection = input("Enter surface wind direction: ")
            surfacedirection_nodp = surfacedirection.replace(".", "")
            surfacedirection = surfacedirection.replace(" ", "")
            if surfacedirection_nodp.isdigit() and surfacedirection.count(".") <= 1:
                break
            if not surfacedirection_nodp.isdigit():
                surfacedirection = surfacedirection.replace(".", "")
            if surfacedirection.upper() in wind_directions:
                break
            else:
                print ("Enter a wind direction.")

        while True:
            threekmwind = input("Enter 3 km AGL wind speed: ")
            threekmwind_nodp = threekmwind.replace(".", "")
            if threekmwind_nodp.isdigit() and threekmwind.count(".") <= 1:
                threekmwind = float(threekmwind)
                break
            else:
                print ("Enter a numerical value")

        while True:
            threekmunits = input("Units: ")
            threekmunits = threekmunits.replace(" ", "")
            threekmunits = threekmunits.replace(".", "")
            if threekmunits in units:
                break
            else:
                print ("Please enter knots, km/h or m/s")

        while True:
            threekmdirection = input("Enter 3 km AGL wind direction: ")
            threekmdirection_nodp = threekmdirection.replace(".", "")
            threekmdirection = threekmdirection.replace(" ", "")
            if threekmdirection_nodp.isdigit() and threekmdirection.count(".") <= 1:
                break
            if not threekmdirection_nodp.isdigit():
                threekmdirection = threekmdirection.replace(".", "")
            if threekmdirection.upper() in wind_directions:
                break
            else:
                print ("Enter a wind direction.")

        surfacewind = unit_converter(surfaceunits, surfacewind)
        threekmwind = unit_converter(threekmunits, threekmwind)
        surfacedirection = dir_degrees(surfacedirection)
        threekmdirection = dir_degrees(threekmdirection)
        threekmshear = calculate_shear(surfacewind, threekmwind, surfacedirection, threekmdirection)

        print ("\n\n0-3 km shear is:", round((threekmshear), 1), "knots (", round((threekmshear * kn2ms), 1), "m/s).")
        if threekmshear < 20.0:
            print ("Weak shear.")
        elif 20 <= threekmshear < 30:
            print ("Moderate shear.")
        else:
            print ("Strong wind shear environment")

    elif type == '6':
        while True:
            surfacewind = input("Enter surface wind speed: ")
            surfacewind_nodp = surfacewind.replace(".", "")
            if surfacewind_nodp.isdigit() and surfacewind.count(".") <= 1:
                surfacewind = float(surfacewind)
                break
            else:
                print ("Enter a numerical value.")

        while True:
            surfaceunits = input("Units: ")
            surfaceunits = surfaceunits.replace(" ", "")
            surfaceunits = surfaceunits.replace(".", "")
            if surfaceunits in units:
                break
            else:
                print ("Please enter knots, km/h or m/s.")

        while True:
            surfacedirection = input("Enter surface wind direction: ")
            surfacedirection_nodp = surfacedirection.replace(".", "")
            surfacedirection = surfacedirection.replace(" ", "")
            if surfacedirection_nodp.isdigit() and surfacedirection.count(".") <= 1:
                break
            if not surfacedirection_nodp.isdigit():
                surfacedirection = surfacedirection.replace(".", "")
            if surfacedirection.upper() in wind_directions:
                break
            else:
                print ("Enter a wind direction.")

        while True:
            sixkmwind = input("Enter 6 km AGL wind speed: ")
            sixkmwind_nodp = sixkmwind.replace(".", "")
            if sixkmwind_nodp.isdigit() and sixkmwind.count(".") <= 1:
                sixkmwind = float(sixkmwind)
                break
            else:
                print ("Enter a numerical value.")

        while True:
            sixkmunits = input("Units: ")
            sixkmunits = sixkmunits.replace(" ", "")
            sixkmunits = sixkmunits.replace(".", "")
            if sixkmunits in units:
                break
            else:
                print ("Please enter knots, km/h or m/s")

        while True:
            sixkmdirection = input("Enter 6km AGL wind direction: ")
            sixkmdirection_nodp = sixkmdirection.replace(".", "")
            sixkmdirection = sixkmdirection.replace(" ", "")
            if sixkmdirection_nodp.isdigit() and sixkmdirection.count(".") <= 1:
                break
            if not sixkmdirection_nodp.isdigit():
                sixkmdirection = sixkmdirection.replace(".", "")
            if sixkmdirection.upper() in wind_directions:
                break
            else:
                print ("Enter a wind direction.")

        surfacewind = unit_converter(surfaceunits, surfacewind)
        sixkmwind = unit_converter(sixkmunits, sixkmwind)
        surfacedirection = dir_degrees(surfacedirection)
        sixkmdirection = dir_degrees(sixkmdirection)
        sixkmshear = calculate_shear(surfacewind, sixkmwind, surfacedirection, sixkmdirection)
        print ("\n\n0-6 km shear is:", round(sixkmshear, 1), "knots (", round((sixkmshear * kn2ms), 1), "m/s).")
        if sixkmshear < 20.0:
            print ("Very weak shear - disorganised multicells")
        elif 20 <= sixkmshear < 40:
            print ("Shear supportive of organised multicells")
        else:
            print ("Shear supportive of supercell thunderstorms")

        print ("\n")

# Asks user whether they want to calculate the Craven SigSvr. If yes, this code prompts
# the user to input CAPE.
        while True:
            cal_ind = input("Calculate Craven SigSvr? y/n: ")
            cal_ind = cal_ind.upper()
            cal_ind = cal_ind.replace(" ", "")
            cal_ind = cal_ind.replace(".", "")
            if cal_ind == "N" or cal_ind == "NO":
                break
            elif cal_ind == "Y" or cal_ind == "YES":
                while True:
                    cape = input("\n\nEnter 100 mb ML CAPE: ")
                    cape = cape.replace(" ", "")
                    cape_nodp = cape.replace(".", "")
                    if cape_nodp.isdigit() and cape.count(".") <= 1:
                        cape = float(cape)
                        break
                    else:
                        print ("Enter a numerical value")
                Craven_value = craven_sigsvr(cape, sixkmshear * kn2ms)
                print ("\n\nCraven SigSvr is " + str(round(Craven_value)) + "m3/s3.")
                if Craven_value > 20000:
                    print ('''
Craven SigSvr index exceeds 20,000 m3/s3. The majority of significant
severe events occur with a Craven SigSvr index greater than 20,000 m3/s3.
''')
                else:
                    print ('''
Craven SigSvr index does not exceeds 20,000 m3/s3. The majority of significant
severe events occur with a Craven SigSvr index greater than 20,000 m3/s3.
''')

    elif type == 'q':
        print ("Existing the shear calculator\n")
        break

    else:
        print ("Please enter either 3, 6 or q if you wish to quit")
