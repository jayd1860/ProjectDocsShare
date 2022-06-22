from Utils import strlib


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


