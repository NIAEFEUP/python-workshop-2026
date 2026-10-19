# Exercise 8: 24-Hour to 12-Hour Clock Conversion
# Read hours and minutes in 24-hour format and print the 12-hour equivalent.
# Minutes are shown with two digits; if minutes are 0 they are omitted.
# If input is invalid print "INVALID DATE FORMAT".
#
# Example input/output:
#
#   +-------------+-------------------------+
#   | Input       | Output                  |
#   +-------------+-------------------------+
#   | 0           | 12 am                   |
#   | 0           |                         |
#   +-------------+-------------------------+
#   | 12          | 12 pm                   |
#   | 0           |                         |
#   +-------------+-------------------------+
#   | 17          | 5:08 pm                 |
#   | 8           |                         |
#   +-------------+-------------------------+
#   | 24          | INVALID DATE FORMAT     |
#   | 0           |                         |
#   +-------------+-------------------------+

hours = int(input())
minutes = int(input())

if not (0 <= hours < 24 and 0 <= minutes < 60):
    print("INVALID DATE FORMAT")
else:
    if hours == 0:
        display_hour = 12
        period = "am"
    elif hours == 12:
        display_hour = 12
        period = "pm"
    elif hours < 12:
        display_hour = hours
        period = "am"
    else:
        display_hour = hours - 12
        period = "pm"

    if minutes == 0:
        print(f"{display_hour} {period}")
    else:
        print(f"{display_hour}:{minutes:02d} {period}")
