#!/usr/bin/env python3
NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


def sendKeyFromValue(usageID,shift=False):
    
    if shift == False:
        # Press a
        write_report(NULL_CHAR*2+chr(int(usageID))+NULL_CHAR*5)
    else:
        # Press SHIFT + a = A
        write_report(chr(32)+NULL_CHAR+chr(int(usageID))+NULL_CHAR*5)

    # Release keys
    write_report(NULL_CHAR*8)






while True:
    letter = raw_input("Please input letter hex value in denary:")

    if "s" in letter:
        letter = letter.replace("s","")
        sendKeyFromValue(letter,shift = True)
    else:
        sendKeyFromValue(letter)


# Press RETURN/ENTER key
#write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)

