import os
import sys

sys.stdout.write('Importing search paths ...\n')

# Add search paths to sys.path
appRootPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(appRootPath)
sys.path.append(appRootPath + '/..')
