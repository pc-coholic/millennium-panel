import binascii

def printframe(frame, direction = "IN"):
    colorend = '\033[0m'

    if direction == "IN":
        color = '\033[93m'
    elif direction == "OUT":
        color = '\033[92m'
    else:
        color = colorend

    print(color + direction + ": " + " ".join(hexlist(frame)) + colorend)

def hexlist(frame):
    newframe = []
    for i in frame:
        newframe.append(hex(i))

    return newframe

def mmByte(item):
    if isinstance(item, bool):
        return [int(item)]
    elif isinstance(item, int):
        return [item]
    elif isinstance(item, str):
        return bytearray.fromhex(item)
    elif item is None:
        return [0]
    else:
        pass

def mmWord(item):
    item = hex(item)[2:]

    item = item.zfill(4)

    item = bytearray.fromhex("".join([item[i:i+2] for i in range(0, len(item), 2)][::-1]))
    return item

def mmFlags(item):
    return [sum(map(int, item))]

def mmBCD(number, max = None):
    number = mmHextel(number, max)

    end = hex(number[-1])[2:]

    if end[-1] is '0':
        end = end[0] + 'E'

    del number[-1]
    return number + bytearray.fromhex(end)

def mmHextel(number, max = None):
    if number is None:
        number = '00'

    # Single digit strings need to zero in front
    if len(number) is 1:
        number = number.zfill(2)

    # Length of string must be an even number in order to be able to be hex'ed
    if len(number) % 2:
        number += '0'

    if max is not None:
        # Add or remove padding as necessary to get to maximum allowed length
        while (len(number) / 2 < max):
            number += '00'

        while (len(number) / 2 > max):
            number = number[:-2]

    return bytearray.fromhex(number)
