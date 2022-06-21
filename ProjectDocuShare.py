import sys
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
from Utils import strlib
from pathlib import Path
#from Utils import mypathlib


class ProjectDocuShare:

    # ------------------------------------------------------------------
    def __init__(self, platformId=None):
        if platformId is None:
            return
        self.platformId = platformId
        self.rootDir = '/Customers'
        self.rootDirTest = '/Customers/Archive/Test'
        self.platform = []
        self.customerList = []
        self.customerList = []
        self.Connect()
        self.GetCustomers()


    # -------------------------------------------------------------------
    def Connect(self):
        auth_flow = DropboxOAuth2FlowNoRedirect(self.platformId, use_pkce=True, token_access_type='offline')
        authorize_url = auth_flow.start()
        print("1. Go to: " + authorize_url)
        print("2. Click \"Allow\" (you might have to log in first).")
        print("3. Copy the authorization code.")
        auth_code = input("Enter the authorization code here: ").strip()

        oauth_result = []
        try:
            oauth_result = auth_flow.finish(auth_code)
        except Exception as e:
            print('Error: %s'% e)
            exit(1)

        self.platform = dropbox.Dropbox(oauth2_refresh_token=oauth_result.refresh_token, app_key=self.platformId)


    # -------------------------------------------------------------------
    def GetCustomers(self, test=False):
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
        response = self.platform.files_list_folder(self.rootDir, recursive=True)
        entries = self.platform.files_list_folder_continue(response.cursor).entries
        for ii in range(0,len(entries)-1):
            p = Path(entries[ii].path_display)
            if len(p.parts) == nParts:
                if test == False:
                    if len(strlib.findstr(entries[ii].path_display, 'Archive')) > 0:
                        continue
                else:
                    if len(strlib.findstr(entries[ii].path_display, 'Archive')) == 0:
                        continue
                self.customerList.append(p.parts[nParts-1])
        return self.customerList


    # -------------------------------------------------------------------
    def CreateCustomer(self, customerName):
        if len(strlib.findstr(customerName, 'Test')):
            customerRootDir = self.rootDirTest + '/' + customerName
        else:
            customerRootDir = self.rootDir + '/' + customerName

        sys.stdout.write('Creating new customer folder %s\n'%  customerRootDir)
        self.platform.files_create_folder_v2(customerRootDir)


