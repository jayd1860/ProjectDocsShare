import sys
from AutoGenerateNewCustomerName import AutoGenerateNewCustomerName

def ConsoleUI(dbx):
    while 1:
        opstr = sys.stdout.write("Enter operation: \n")
        sys.stdout.write("    1. list customers\n")
        sys.stdout.write("    2. list customers test\n")
        sys.stdout.write("    3. new customer\n")
        sys.stdout.write("    4. new customer test\n")
        opstr = input("    5. exit\n").strip()
        if opstr == '1':
            sys.stdout.write('=============\n')
            sys.stdout.write('Customer List\n')
            sys.stdout.write('=============\n')
            customersExisting = dbx.GetCustomers()
            for ii in range(0, len(customersExisting)):
                sys.stdout.write('    %s\n' % customersExisting[ii])
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

