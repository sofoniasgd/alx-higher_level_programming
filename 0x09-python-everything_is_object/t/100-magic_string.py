


#!/usr/bin/python3
def magic_string():
    global retstring
    if not retstring:
        retstring += "BestSchool"
    else:
        retstring += ", BestSchool"
    return retstring
