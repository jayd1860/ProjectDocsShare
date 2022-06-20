
import os
import sys

def filesepStandard(pathname0=None, options=None):
    pathname = ''

    if pathname0 is None:
        return pathname
    if len(pathname0)==0:
        return pathname

    if options is None:
        options = ''

    # Change all path file separators to standard forward slash
    pathname = pathname0.replace('\\', '/')

    if os.path.isdir(pathname):
        if pathname[-1] != '/':
            pathname = pathname + '/'


    return pathname

# -----------------------------------------------------
if __name__ == "__main__":
    sys.stdout.write('WELCOME\n')
    if len(sys.argv)<2:
        print('Quitting before we started. BYE, BYE ...\n')
        quit(-5)
    pathname = sys.argv[1]
    sys.stdout.write('filesepStandard(%s) = %s\n'% (pathname, filesepStandard(pathname)))

