import sys
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
from PyQt5 import QtWidgets
import webbrowser

from Utils import strlib
from pathlib import Path
from MainGUI import MainGUI
from ConsoleUI import ConsoleUI


#######################################################################################
class ProjectDocuShare:

    # ------------------------------------------------------------------
    def __init__(self, platformId=None):
        if platformId is None:
            return
        self.platformId = platformId
        self.rootDir = '/Customers'
        self.rootDirTest = '/Customers/Archive/Test'
        self.platform = []
        self.entries = []
        self.customerList = []
        self.projectList = []
        self.authorize_url = ''
        self.auth_flow = []
        self.projectStructure = [
            'Action Items  (RFI, RFC, RFP, RFA)',
            'Change Orders',
            'Communications',
            'Field Drawings',
            'Plans',
            'SOV',
            'Submittals'
            ]

        self.GetAuthCode()

    # -------------------------------------------------------------------
    def GetAuthCode(self):
        self.auth_flow = DropboxOAuth2FlowNoRedirect(self.platformId, use_pkce=True, token_access_type='offline')
        self.authorize_url = self.auth_flow.start()
        webbrowser.open_new(self.authorize_url)


    # -------------------------------------------------------------------
    def Connect(self, auth_code):
        try:
            oauth_result = self.auth_flow.finish(auth_code)
        except Exception as e:
            print('Error: %s'% e)
            return -1
        self.platform = dropbox.Dropbox(oauth2_refresh_token=oauth_result.refresh_token, app_key=self.platformId)
        self.Update()
        return 0


    # -------------------------------------------------------------------
    def Update(self):
        response = self.platform.files_list_folder(self.rootDir, recursive=True)
        self.entries = self.platform.files_list_folder_continue(response.cursor).entries


    # -------------------------------------------------------------------
    def GetCustomers(self, test = False):
        self.customerList = []
        if type(test) is str:
            if test == 'Test':
                test = True
            else:
                test = False
        if test:
            nParts = 5
        else:
            nParts = 3
        for ii in range(0,len(self.entries)-1):
            p = Path(self.entries[ii].path_display)
            if len(p.parts) == nParts:
                if not test:
                    if len(strlib.findstr(self.entries[ii].path_display, 'Archive')) > 0:
                        continue
                else:
                    if len(strlib.findstr(self.entries[ii].path_display, 'Archive')) == 0:
                        continue
                self.customerList.append(p.parts[nParts-1])
        return self.customerList


    # -------------------------------------------------------------------
    def GetProjects(self, customerName, test = False):
        self.projectList = []
        if type(test) is str:
            if test == 'Test':
                test = True
            else:
                test = False
        if test:
            nParts = 6
        else:
            nParts = 4
        for ii in range(0,len(self.entries)-1):
            p = Path(self.entries[ii].path_display)
            if len(p.parts) == nParts:
                if not test:
                    if len(strlib.findstr(self.entries[ii].path_display, 'Archive')) > 0:
                        continue
                else:
                    if len(strlib.findstr(self.entries[ii].path_display, 'Archive')) == 0:
                        continue
                self.projectList.append(p.parts[nParts-1])
        return self.projectList




    # -------------------------------------------------------------------
    def CreateCustomer(self, customerName):
        if len(strlib.findstr(customerName, 'Test')):
            customerRootDir = self.rootDirTest + '/' + customerName
        else:
            customerRootDir = self.rootDir + '/' + customerName

        sys.stdout.write('Creating new customer folder %s\n'%  customerRootDir)
        self.platform.files_create_folder_v2(customerRootDir)


    # -------------------------------------------------------------------
    def CreateProject(self, customerName, projectName):
        if len(strlib.findstr(customerName, 'Test')):
            customerRootDir = self.rootDirTest + '/' + customerName
        else:
            customerRootDir = self.rootDir + '/' + customerName

        sys.stdout.write('Adding project %s to customer %s\n'%  (customerRootDir, projectName))
        sys.stdout.write('--------------------------------------\n')
        projectRootDir = customerRootDir + '/' + projectName
        for ii in range(0,len(self.projectStructure)):
            sys.stdout.write('    Adding  %s\n'%  (projectRootDir + '/' + self.projectStructure[ii]))
            # self.platform.files_create_folder_v2(customerRootDir)



# -----------------------------------------------------
def MainGUI_Launch(dbx):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainGUI(MainWindow, dbx)
    app.exec_()



# --------------------------------------------------------------------------
if __name__ == '__main__':
    appkey = 'xxxxxxxxx'
    uitype = 'GUI'
    if len(sys.argv) == 2:
        appkey = sys.argv[1]
    elif len(sys.argv) == 3:
        appkey = sys.argv[1]
        uitype = sys.argv[2]
    else:
        exit(-1)

    dbx = ProjectDocuShare(appkey)
    if uitype.lower() == 'console':
        ConsoleUI(dbx)
    elif uitype.lower() == 'gui':
        MainGUI_Launch(dbx)

