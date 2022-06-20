from Utils import strlib

def optionExists(options, option=''):
    # Check if option (arg2) exists in a set of options (arg1)

    if len(options) == 0:
        return False
    if len(option) == 0:
        return False

    options2 = strlib.str2list(options, [':',';',','])
    for ii in range(0, len(options2)):
        if option == options2[ii]:
            return True
    return False
