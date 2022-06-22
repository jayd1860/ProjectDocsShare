import sys
import time
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
import webbrowser

from MainGUI_0 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


##############################################################
class MainGUI(Ui_MainWindow):

    # --------------------------------------------------------
    def __init__(self, parentGui=None, dbx=None):
        Ui_MainWindow.__init__(self)
        self.setupUi(parentGui)
        self.dbx = dbx

        self.pushButtonNewCustomer.clicked.connect(self.pushButtonNewCustomer_Callback)
        self.pushButtonAddNewCustomer.clicked.connect(self.pushButtonAddNewCustomer_Callback)
        self.listWidgetCustomerList.itemSelectionChanged.connect(self.listWidgetCustomerList_Callback)
        # self.plainTextEditAuthenticationKey.textChanged.connect(self.plainTextEditAuthenticationKey_Callback)
        self.pushButtonLogin.clicked.connect(self.pushButtonLogin_Callback)
        self.plainTextEditNewCustomer.hide()
        self.pushButtonAddNewCustomer.hide()
        parentGui.setWindowTitle('ProjectDocuShare')
        parentGui.show()


    # --------------------------------------------------------
    def pushButtonNewCustomer_Callback(self):
        if self.pushButtonNewCustomer.isChecked():
            self.plainTextEditNewCustomer.show()
            self.pushButtonAddNewCustomer.show()
        else:
            self.plainTextEditNewCustomer.hide()
            self.pushButtonAddNewCustomer.hide()


    # --------------------------------------------------------
    def listWidgetCustomerList_Callback(self):
        item = self.listWidgetCustomerList.item(self.listWidgetCustomerList.currentRow()).text()
        sys.stdout.write('Selected item %s\n'% item)


    # --------------------------------------------------------
    def plainTextEditAuthenticationKey_Callback(self):
        time.sleep(2)
        auth_code = self.plainTextEditAuthenticationKey.toPlainText()
        if self.dbx.Connect(auth_code) < 0:
            exit(-1)

        self.pushButtonLogin.hide()
        self.plainTextEditAuthenticationKey.hide()

        self.UpdateCustomerList()


    # --------------------------------------------------------
    def pushButtonLogin_Callback(self):
        auth_code = self.plainTextEditAuthenticationKey.toPlainText()
        self.pushButtonLogin.hide()
        self.plainTextEditAuthenticationKey.hide()
        self.pushButtonLogin.update()
        self.plainTextEditAuthenticationKey.update()

        if self.dbx.Connect(auth_code) < 0:
            exit(-1)
        self.UpdateCustomerList()


    # --------------------------------------------------------
    def pushButtonAddNewCustomer_Callback(self):
        customerNameNew = self.plainTextEditNewCustomer.toPlainText()
        customerList = self.dbx.GetCustomers()
        for ii in range(0, len(customerList)):
            if customerNameNew == customerList[ii]:
                return
        self.pushButtonNewCustomer.setChecked(False)
        self.plainTextEditNewCustomer.clear()
        self.plainTextEditNewCustomer.hide()
        self.pushButtonAddNewCustomer.hide()
        self.dbx.CreateCustomer(customerNameNew)
        self.UpdateCustomerList()


    # --------------------------------------------------------
    def UpdateCustomerList(self):
        self.listWidgetCustomerList.clear()
        customersExisting = self.dbx.GetCustomers()
        for ii in range(0, len(customersExisting)):
            sys.stdout.write('Adding customer %s  ...\n'% customersExisting[ii])
            self.listWidgetCustomerList.insertItem(ii, customersExisting[ii])
            self.listWidgetCustomerList.update()



