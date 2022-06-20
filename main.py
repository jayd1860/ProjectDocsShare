import sys
from Utils import strlib
from ProjectDocsShare import ProjectDocsShare

APP_KEY = "3h3ft83fmamys5f"


# -------------------------------------------------------------------------
def AutoGenerateNewCustomerName(dbx, test=False):
    nameNew = 'CustomerName'
    numNew = 1
    if type(test) is str:
        if test == 'Test':
            test = True
        else:
            test = False
    if not test:
        Test = ''
    else:
        Test = 'Test'
    customerList = dbx.GetCustomers(test)
    kk = []
    for ii in range(0, len(customerList)):
        k = strlib.findstr(customerList[ii], 'CustomerName')
        if len(k) > 0:
            kk.append(ii)
    numNew = len(kk)+1
    return nameNew + Test + strlib.num2str(numNew)


# --------------------------------------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) == 0:
        op = 'Create New Customer'
        customerName = ''

    dbx = ProjectDocsShare(APP_KEY)
    customersExisting = dbx.GetCustomers()

    while 1:
        opstr = sys.stdout.write("Enter operation: \n")
        sys.stdout.write("    1. list customers\n")
        sys.stdout.write("    2. list customers test\n")
        sys.stdout.write("    3. new customer\n")
        sys.stdout.write("    4. new customer test\n")
        opstr   =  input("    5. exit\n" ).strip()
        if opstr == '1':
            sys.stdout.write('=============\n')
            sys.stdout.write('Customer List\n')
            sys.stdout.write('=============\n')
            customersExisting = dbx.GetCustomers()
            for ii in range(0, len(customersExisting)):
                sys.stdout.write('    %s\n'% customersExisting[ii])
        elif opstr == '2':
            sys.stdout.write('==================\n')
            sys.stdout.write('Customer List Test\n')
            sys.stdout.write('==================\n')
            customersExisting = dbx.GetCustomers('Test')
            for ii in range(0, len(customersExisting)):
                sys.stdout.write('    %s\n' % customersExisting[ii])
        elif opstr == '3':
            # customerName = input("Enter new customer name: ").strip()
            customerNameNew = AutoGenerateNewCustomerName(dbx)
            dbx.CreateCustomer(customerNameNew)
        elif opstr == '4':
            customerNameNew = AutoGenerateNewCustomerName(dbx, 'Test')
            dbx.CreateCustomer(customerNameNew)
        elif opstr == '5':
            sys.stdout.write('Exiting ...\n')
            break
        sys.stdout.write('\n')

