import sys
import time
from MainGUI_0 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


##############################################################
class MainGUI(Ui_MainWindow):

    # --------------------------------------------------------
    def __init__(self, parentGui=None, dbx=None):
        Ui_MainWindow.__init__(self)
        self.setupUi(parentGui)

        customersExisting = dbx.GetCustomers()
        self.pushButtonNewCustomer.clicked.connect(self.pushButtonNewCustomer_Callback)
        self.plainTextEditNewCustomer.hide()

        parentGui.setWindowTitle('ProjectDocuShare')
        parentGui.show()

        for ii in range(0, len(customersExisting)):
            sys.stdout.write('Adding customer %s  ...\n'% customersExisting[ii])
            self.listWidgetCustomerList.insertItem(ii, customersExisting[ii])
            time.sleep(.2)



    # --------------------------------------------------------
    def pushButtonNewCustomer_Callback(self):
        if self.pushButtonNewCustomer.isChecked():
            self.plainTextEditNewCustomer.show()
        else:
            self.plainTextEditNewCustomer.hide()

