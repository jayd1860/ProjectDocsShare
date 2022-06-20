
import sys
import os
from pathlib import Path

from Utils import searchpaths

from Utils import strlib
from Utils.optionExists import optionExists


# -----------------------------------------------------
def filesepStandard(pathname0=None, options=None):
    if pathname0 is None:
        return
    if len(pathname0) == 0:
        return

    if options is None:
        options = ''

    pathname = pathname0
    if not optionExists(options, 'nameonly'):
        if ispathvalid(pathname0) and optionExists(options, 'full'):
            pathname = os.path.abspath(pathname0)
        elif not ispathvalid(pathname0):
            return ''

    pathname = pathname.replace('\\','/')

    # Change all path file separators to standard forward slash
    if os.path.isdir(pathname):
        if pathname[-1] != '/':
            pathname = pathname + '/'
    return pathname



# -----------------------------------------------------
def pathsubtract(p2_0, p1_0):
    p1 = filesepStandard(p1_0, 'full')
    p2 = filesepStandard(p2_0, 'full')
    k = strlib.findstr(p2, p1)
    if k == 1:
        diff = p2[k+len(p1):]
    else:
        diff = p2[:k-1]
    return diff



# -----------------------------------------------------
def ispathfull(pathname=None):
    if pathname is None:
        return False

    if not ispathvalid(pathname):
        return False

    c = strlib.str2list(pathname, ['/', '\\'])
    if pathname[0] == '/' or pathname[0] == '\\':
        return True
    if strlib.findstr(c[0], ':'):
        return True

    return False



# -----------------------------------------------------
def ispathvalid(pathname=None):
    if pathname is None:
        return []
    p = Path(pathname)
    return p.exists()



# -----------------------------------------------------
if __name__ == "__main__":
    arg1 = []
    sys.stdout.write('\n')
    sys.stdout.write('Number of arguments:   %d\n' % len(sys.argv))
    if len(sys.argv)>1:
        arg1 = sys.argv[1]
    else:
        arg1 = 'tryme1\subdir1'
    newpath = filesepStandard(arg1, 'full')
    sys.stdout.write('%s\n'% newpath)

