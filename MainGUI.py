import sys
import time
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
import webbrowser

from MainGUI_0 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


##############################################################
class MainGUI(Ui_MainWindow):

    # --------------------------------------------------------
    def __init__(self, parentGui=None, dbx=None):
        Ui_MainWindow.__init__(self)
        self.setupUi(parentGui)
        self.dbx = dbx

        # Set up callbaks
        self.pushButtonLogin.clicked.connect(self.pushButtonLogin_Callback)
        self.pushButtonNewCustomer.clicked.connect(self.pushButtonNewCustomer_Callback)
        self.pushButtonAddCustomer.clicked.connect(self.pushButtonAddCustomer_Callback)
        self.pushButtonAddProject.clicked.connect(self.pushButtonAddProject_Callback)
        self.listWidgetCustomerList.itemSelectionChanged.connect(self.listWidgetCustomerList_Callback)
        self.listWidgetProjectList.itemSelectionChanged.connect(self.listWidgetProjectList_Callback)

        # Hide objects
        self.plainTextEditNewCustomerName.hide()
        self.pushButtonAddCustomer.hide()

        # Set window params
        parentGui.setWindowTitle('ProjectDocuShare')
        parentGui.show()


    # --------------------------------------------------------
    def pushButtonLogin_Callback(self):
        auth_code = self.plainTextEditAuthenticationKey.toPlainText()
        if self.dbx.Connect(auth_code) < 0:
            self.DisplayErrorMsg('Invalid authorization code. Please try again.')
            return
        self.pushButtonLogin.hide()
        self.plainTextEditAuthenticationKey.hide()
        self.pushButtonLogin.update()
        self.plainTextEditAuthenticationKey.update()
        self.UpdateCustomerList()


    # --------------------------------------------------------
    def pushButtonNewCustomer_Callback(self):
        if self.pushButtonNewCustomer.isChecked():
            self.plainTextEditNewCustomerName.show()
            self.pushButtonAddCustomer.show()
        else:
            self.plainTextEditNewCustomerName.hide()
            self.pushButtonAddCustomer.hide()


    # --------------------------------------------------------
    def listWidgetProjectList_Callback(self):
        self.listWidgetProjectList.clear()
        customerName = self.listWidgetCustomerList.item(self.listWidgetCustomerList.currentRow()).text()
        sys.stdout.write('Selected item %s\n'% customerName)
        projectList = self.dbx.GetProjectList(customerName)
        #for ii in range(0,len(self.entries)):


    # --------------------------------------------------------
    def listWidgetCustomerList_Callback(self):
        self.listWidgetProjectList.clear()
        customerName = self.listWidgetCustomerList.item(self.listWidgetCustomerList.currentRow()).text()
        sys.stdout.write('Selected item %s\n'% customerName)
        self.UpdateProjectList()


    # --------------------------------------------------------
    def pushButtonAddCustomer_Callback(self):
        customerNameNew = self.plainTextEditNewCustomerName.toPlainText()
        customerList = self.dbx.GetCustomers()
        for ii in range(0, len(customerList)):
            if customerNameNew == customerList[ii]:
                return
        self.pushButtonNewCustomer.setChecked(False)
        self.plainTextEditNewCustomerName.clear()
        self.plainTextEditNewCustomerName.hide()
        self.pushButtonAddCustomer.hide()
        self.dbx.CreateCustomer(customerNameNew)
        self.UpdateCustomerList()


    # --------------------------------------------------------
    def pushButtonAddProject_Callback(self):
        iSelection = self.listWidgetCustomerList.currentRow()
        if iSelection < 0:
            self.DisplayErrorMsg('No customer selected. Please first select a customer, then add project.')
            return
        customerName = self.listWidgetCustomerList.item(iSelection).text()
        projectNameNew = self.plainTextEditNewProjectName.toPlainText()
        if len(projectNameNew) == 0:
            return
        self.dbx.CreateProject(customerName, projectNameNew)


    # --------------------------------------------------------
    def UpdateCustomerList(self):
        self.listWidgetCustomerList.clear()
        customerList = self.dbx.GetCustomers()
        for ii in range(0, len(customerList)):
            sys.stdout.write('Adding customer %s  ...\n'% customerList[ii])
            self.listWidgetCustomerList.insertItem(ii, customerList[ii])
            self.listWidgetCustomerList.update()


    # --------------------------------------------------------
    def UpdateProjectList(self):
        self.listWidgetProjectList.clear()
        iSelection = self.listWidgetCustomerList.currentRow()
        if iSelection < 0:
            self.DisplayErrorMsg('No customer selected. Please first select a customer, then add project.')
            return
        customerName = self.listWidgetCustomerList.item(iSelection).text()
        projectList = self.dbx.GetProjects(customerName)
        for ii in range(0, len(projectList)):
            sys.stdout.write('Adding customer %s  ...\n'% projectList[ii])
            self.listWidgetProjectList.insertItem(ii, projectList[ii])
            self.listWidgetProjectList.update()


    # ----------------------------------------------------------
    def DisplayErrorMsg(self, errmsg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText(errmsg)

        # setting Message box window title
        msg.setWindowTitle("ERROR")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        return retval
