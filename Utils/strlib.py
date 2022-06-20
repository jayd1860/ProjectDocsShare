import sys
import numpy


# ----------------------------------------------------------------------------
def findstr(s, c):
    k = []
    if len(c)==0:
        return k
    ii = 0;
    while ii+len(c) <= len(s):
        if s[ii:ii+len(c)] == c:
            k.append(ii)
            ii = ii+len(c)
        ii = ii+1
    return k


# -----------------------------------------------------------------------------
# def str2int(s):
#     c = str.split(s)
#     a = numpy.array([0] * len(c))
#     for ii in range(0, len(c)):
#         a[ii] = int(c[ii])
#     return a
#


# ----------------------------------------------------------------------------
def str2bytes(sl):
    if type(sl) != list:
        if type(sl) == str:
            idxE = len(sl)

            # NOTE: if string has any newine the number str next to it will be
            # dropped by the code below. To avoid this we drop newline in slist
            s2 = sl.replace('\n', ' ')
            slist = s2[0:idxE].split(' ')
        else:
            return bytes([])
    else:
        slist = sl
    byteslist = []
    for ii in range(0, len(slist)):
        if slist[ii].isdigit():
            # numstr = slist[ii]
            # num = int(numstr)
            # byte = bytes([num])  # Remeber to put array brackets around num or else you'll get nonsense
            # byteslist.append(byte)
            byteslist.append(int(slist[ii]))

    return bytes(byteslist)


# ----------------------------------------------------------------------------
def num2str(a=None):
    # Init return value

    # Check that argument is provided else return empty string
    if a is None:
        return ''
    if numpy.isscalar(a):
        a = numpy.array([a])
    else:
        a = numpy.array(a)
    astr0 = str(a)[1:-1]
    kk = 0
    flag = 0
    for ii in range(0, len(astr0)):
        # Remove leading spaces
        if flag == 0 and astr0[ii] == ' ':
            kk = kk + 1
        break

    astr = astr0[kk:]
    return astr


# ----------------------------------------------------------------------------
def str2list(s, delimiters='\n'):
    if type(delimiters) is not list:
        delimiters = [delimiters]

    # Change all delimters in s to be the first delimiter
    for ii in range(1, len(delimiters)):
        s.replace(delimiters[ii], delimiters[0])
    lst = s.split(delimiters[0])
    return lst


# -----------------------------------------------------
if __name__ == "__main__":
    arg1 = []
    if len(sys.argv)>0:
        arg1 = []
    r = findstr('/customers/newcustomer/subdir1', 'customers')
    r = findstr('/customers/newcustomer/subdir1', 'customer')
    r = findstr('/customers/newcustomer/subdir1/customer', 'customer')
    r = findstr('/customers/newcustomer/subdir1', 'dir1')
    r = findstr('/customers/newcustomer/subdir1', 'u')
    r = findstr('/customers/newcustomer/subdir1', '/')
    r = findstr('/customers/newcustomer/subdir1', '1')
    r = findstr('', 'xxx1')
    r = findstr('', '')
    r = findstr('t', 'ttttt')
    r = findstr('t///', 'ttttt')
    r = findstr('t', 't')
    r = findstr('u', 't')
    r = findstr('', 't')

    s = num2str(890)
    print(s)
