#!/usr/bin/env python3
import serial

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def sendKeyFromValue(usageID,shift=False):
    print(usageID,shift)
    if shift == False:
        # Press a
        write_report(NULL_CHAR*2+chr(int(usageID))+NULL_CHAR*5)
    else:
        # Press SHIFT + a = A
        write_report(chr(32)+NULL_CHAR+chr(int(usageID))+NULL_CHAR*5)

    # Release keys
    write_report(NULL_CHAR*8)

###########################################################

string = """



Keyboard a and A
Keyboard b and B
Keyboard c and C
Keyboard d and D
Keyboard e and E
Keyboard f and F
Keyboard g and G
Keyboard h and H
Keyboard i and I
Keyboard j and J
Keyboard k and K
Keyboard l and L
Keyboard m and M
Keyboard n and N
Keyboard o and O
Keyboard p and P
Keyboard q and Q
Keyboard r and R
Keyboard s and S
Keyboard t and T
Keyboard u and U
Keyboard v and V
Keyboard w and W
Keyboard x and X
Keyboard y and Y
Keyboard z and Z
Keyboard 1 and !
Keyboard 2 and @
Keyboard 3 and #
Keyboard 4 and $
Keyboard 5 and %
Keyboard 6 and ^
Keyboard 7 and &
Keyboard 8 and *
Keyboard 9 and (
Keyboard 0 and )
Keyboard Return (ENTER)
Keyboard ESCAPE
Keyboard DELETE (Backspace)
Keyboard Tab
Keyboard Spacebar
Keyboard - and (underscore)
Keyboard = and +
Keyboard [ and {
Keyboard ] and }
Keyboard \ and |
Keyboard Non-US # and ~
Keyboard ; and :
Keyboard ' and "
Keyboard Grave Accent and Tilde
Keyboard, and <
Keyboard . and >
Keyboard / and ?
Keyboard Caps Lock
Keyboard F1
Keyboard F2
Keyboard F3
Keyboard F4
Keyboard F5
Keyboard F6
Keyboard F7
Keyboard F8
Keyboard F9
Keyboard F10
Keyboard F11
Keyboard F12
Keyboard PrintScreen
Keyboard Scroll Lock
Keyboard Pause
Keyboard Insert
Keyboard Home
Keyboard PageUp
Keyboard Delete Forward
Keyboard End
Keyboard PageDown
Keyboard RightArrow
Keyboard LeftArrow
Keyboard DownArrow
Keyboard UpArrow
Keypad Num Lock and Clear
Keypad /
Keypad *
Keypad -
Keypad +
Keypad ENTER
Keypad 1 and End
Keypad 2 and Down Arrow
Keypad 3 and PageDn
Keypad 4 and Left Arrow
Keypad 5
Keypad 6 and Right Arrow
Keypad 7 and Home
Keypad 8 and Up Arrow
Keypad 9 and PageUp
Keypad 0 and Insert
Keypad . and Delete
Keyboard Non-US \ and |
Keyboard Application
Keyboard Power
Keypad =
Keyboard F13
Keyboard F14
Keyboard F15
Keyboard F16
Keyboard F17
Keyboard F18
Keyboard F19
Keyboard F20
Keyboard F21
Keyboard F22
Keyboard F23
Keyboard F24
Keyboard Execute
Keyboard Help
Keyboard Menu
Keyboard Select
Keyboard Stop
Keyboard Again
Keyboard Undo
Keyboard Cut
Keyboard Copy
Keyboard Paste
Keyboard Find
Keyboard Mute
Keyboard Volume Up
Keyboard Volume Down
Keyboard Locking Caps Lock
Keyboard Locking Num Lock
Keyboard Locking Scroll Lock
Keypad Comma
Keypad Equal Sign
Keyboard International1
Keyboard International2
Keyboard International3
Keyboard International4
Keyboard International5
Keyboard International6
Keyboard International7
Keyboard International8
Keyboard International9
Keyboard LANG1
Keyboard LANG2
Keyboard LANG3
Keyboard LANG4
Keyboard LANG5
Keyboard LANG6
Keyboard LANG7
Keyboard LANG8
Keyboard LANG9
Keyboard Alternate Erase
Keyboard SysReq/Attention
Keyboard Cancel
Keyboard Clear
Keyboard Prior
Keyboard Return
Keyboard Separator
Keyboard Out
Keyboard Oper
Keyboard Clear/Again
Keyboard CrSel/Props
Keyboard ExSel
Keyboard LeftControl
Keyboard LeftShift
Keyboard LeftAlt
Keyboard Left GUI
Keyboard RightControl
Keyboard RightShift
Keyboard RightAlt
Keyboard Right GUIv
"""

class KeyboardKey():

    def __init__(self,number,dataRepresented):

        self.number = number
        self.dataRepresented = dataRepresented

keys = []
counter = 0
for each_line in string.split("\n"):
    allData = []
    each_line = each_line.replace("Keyboard","").rstrip().lstrip()

    if "and" in each_line:
        withoutShift = each_line.split("and")[0].lstrip().rstrip()
        withShift    = each_line.split("and")[1].lstrip().rstrip()
    elif each_line == "":
        allData = [each_line]
    else:
        allData = [each_line]

    if allData == []:
        allData = [withoutShift,withShift]

    keys.append( KeyboardKey(counter,allData[:]))

    counter = counter + 1

#for each_key in keys:
#    print(each_key.number,each_key.dataRepresented)

def convert(letter):
    shift = False
    for each_key in keys:
        shiftCounter = 0
        for each_data_represented in each_key.dataRepresented:
            shiftCounter = shiftCounter + 1
            if letter == each_data_represented:
                finalKey = each_key
                if shiftCounter == 2:
                    shift = True

    return(finalKey,shift)


def convertNumber(receive):
    if "s" in receive:
        shift = True
    elif "r" in receive:
        shift = False

    receive = receive.replace("r","").replace("s","")
    number = int(receive)

    for each_key in keys:
        if each_key.number == number:
            final_key = each_key

    return(final_key, shift)

# h,shift = convert(".")

# print(h.number,h.dataRepresented,shift)

############################################################

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

while True:
    rcv = ""
    rcv = port.read(4)
    if rcv != "":
        print("Received '" + str(rcv) + "' via serial")
        keyClass,shift = convertNumber(str(rcv))
        sendKeyFromValue(keyClass.number,shift)


